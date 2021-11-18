from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view()),
    path("formmaker", views.FormMake.as_view()),
    path('navbar', views.navbar, name='navbar'),
    path('nav', views.navbar1, name='nav'),
    path('nav11', views.navbar2, name='nav11')
]
