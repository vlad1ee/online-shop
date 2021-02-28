from django.shortcuts import render
from django.views import generic
from .models import Category, Product


class CategoryCreate(generic.CreateView):
    model = Category
    fields = ('name', 'parent')
    template_name = 'category_form.html'
    success_url = '/'

def index_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', locals())


def category(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', locals())


class ProductCreate(generic.CreateView):
    model = Product
    fields = ('__all__')
    template_name = 'product_create.html'
    success_url = '/'


# class ProductList(generic.ListView):
#     model = Product
#     template_name = 'product_list.html'
#     context_object_name = 'products'
