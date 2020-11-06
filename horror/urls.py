from django.urls import path
from . import views

urlpatterns = [
    path('', views.hot_post, name="hot_post"),
    path('about', views.about, name="about"),
    path('<str:id>/', views.nosleep, name="nosleep")
]
