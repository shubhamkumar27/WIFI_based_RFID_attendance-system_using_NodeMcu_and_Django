"""iot_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path('home/', views.index , name = 'index'),
    path('anujnjbxhabnajnxnixtry/', views.index1 , name = 'index1'),
    path('aujnjmciejidwwwenixasi/', views.manage1 , name = 'manage1'),
    path('aujnjmciejidncjeiuwcni/', views.details1 , name = 'details1'),
    path('process/', views.process, name = 'process'),
    path('users/', views.details, name = 'details'),
    path('manage/', views.manage , name = 'manage'),
    path('cardselect/', views.card , name = 'card'),
    path('cardedit/', views.edit , name = 'cardedit'),
    path('searchuser/', views.search , name = 'search'),
]
