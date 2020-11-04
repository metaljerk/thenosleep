from django.urls import path
from . import views

urlpatterns = [
    path('', views.horror, name="horror"),
    path('about', views.about, name="about"),
    path('/<str:id>/', views.nosleep, name="nosleep")
]
