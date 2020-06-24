from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('panel/news/catnewsadd',views.addcatnews,name="catnewsadd"),
   path('panel/news/news_list',views.news_list,name="news_list")
 


]
