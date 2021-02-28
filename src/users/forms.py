from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
User = get_user_model()

class SignUpForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('email', 'username', 'password')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)


class UserEditForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('email', 'username', 'password')