from django.urls import path
from . import views
urlpatterns = [
    path('', views.about, name='about'),
    path('achievements/', views.achievements, name='achievements'),
    path('achievements/<int:pk>/', views.achievement_detail, name='achievement_detail'),
    path('school/', views.school, name='school'),
    path('weather/', views.weather, name='weather'),
]
