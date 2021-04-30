from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Electricity_bill import views

urlpatterns = [
    path('', views.overview),
    path('admin/', admin.site.urls),
    path('userlist/', views.userlist),
    path('userdetail/<str:pk>/', views.userdetail),
    path('newuser/', views.newuser),
    path('newelec/', views.newelec),
    path('eleclist/', views.eleclist),
    path('updateelec/<str:pk>/', views.updateelec),
    path('readlist/',views.readlist),
    path('newread/', views.newread),
    path('sublist/',views.sublist),
    path('newsub/',views.newsub),
    path('updatesub/',views.updatesub),
    path('bill/',views.bill),
]
