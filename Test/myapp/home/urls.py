from django.urls import path
from . import views

urlpatterns =[
    path('home/', views.page),
    path('login/', views.login)
]