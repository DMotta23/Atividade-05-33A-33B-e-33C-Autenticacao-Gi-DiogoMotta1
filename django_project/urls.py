"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appDiogo import views

urlpatterns = [
    path('', views.home, name="home"),
    path('porcoes', views.create_porcoes),
    path('porcoes/update/<id>', views.update_porcoes),
    path('porcoes/delete/<id>', views.delete_porcoes),
    path('pratos', views.create_pratos),
    path('pratos/update/<id>', views.update_pratos),
    path('pratos/delete/<id>', views.delete_pratos),
    path('utensilios', views.create_utensilios),
    path('utensilios/update/<id>', views.update_utensilios),
    path('utensilios/delete/<id>', views.delete_utensilios), 
    path('admin/', admin.site.urls),
]
