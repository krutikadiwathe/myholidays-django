from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path("package", views.package, name='package'),
    path("team", views.team, name='team'),
    path("contact", views.contact, name='contact'),
    path("student",views.student, name='student'),
    path("family",views.family, name='family'),
    path("senior",views.senior, name='senior'),
]