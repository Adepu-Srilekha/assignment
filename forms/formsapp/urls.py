from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.contact,name='contact'),
    path('snippet', views.Snippet_detail, name='contact')

]