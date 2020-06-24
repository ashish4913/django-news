"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('about/',views.about),
    
    path('news_details/<str:which_news>/',views.news_details,name='news_details'),
    path('panel/',views.panel,name='panel'),
    path('panel/news/list',views.news_list,name="news_list"),
    path('panel/news/add',views.news_add,name="news_add"),
    path('news_list/<int:pk>/',views.news_delete,name='news_delete'),
    path('panel/login',views.my_login,name='my_login'),
    path('panel/logout',views.my_logout,name='my_logout'),
    path('fullcatnews/<str:getnews>/',views.fullcatnews,name='fullcatnews'),
    path('panel/sitesettings/',views.sitesettings,name='sitesettings')


]
