from django.urls import path
from .views import category, CategoryCreate, ProductCreate


urlpatterns = [
    path('', category, name='category'),
    path('create/', CategoryCreate.as_view()),
    # path('products/', ProductList.as_view()),
    path('product/create/', ProductCreate.as_view()),
]