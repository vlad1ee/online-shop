from django.contrib import admin
from django.urls import path, include
from categories.views import index_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/v1/', include('api.urls')),
    path('category/', include('categories.urls')),
    path('user/', include('users.urls')),
]
