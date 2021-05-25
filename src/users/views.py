from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm, SignUpForm, UserEditForm
from .models import user_post_save


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            print(user)
            if user is not None:
                if user.verified and user.created_by_template:
                    login(request, user)
                    return redirect('index')
                elif not user.created_by_template and user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Проверьте вашу почту')
            else:
                return HttpResponse(
                    'Проверьте введённые данные или подтвердите почту'
                )
    else:
        form = LoginForm()
    return render(request, 'login.html', locals())


def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_by_template = True
            user.username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.email = form.cleaned_data['email']
            user.set_password(password)
            user.save()
            return HttpResponse(
                'На вашу почту было выслано собщение с подтверждением'
            )
    return render(request, 'sign_up.html', locals())


def uuid_verify(request, uuid):
    user = get_object_or_404(get_user_model(),
                             verification_uuid=uuid, verified=False)
    user.verified = True
    user.save()
    return redirect('index')


@csrf_exempt
def user_update(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.user != user:
        return HttpResponse('У вас недостаточно прав для этого действия')
    print(request.is_ajax())
    if request.method == 'POST' and request.is_ajax():
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST.get('password'))
            post_save.disconnect(user_post_save, sender=get_user_model())
            user.save()
            login(request, user)
            post_save.connect(user_post_save, sender=get_user_model())
            return JsonResponse({"success": True}, status=200)
        return HttpResponse('Проверьте введённые данные')
    form = UserEditForm()
    return render(request, 'user_edit.html', locals())
