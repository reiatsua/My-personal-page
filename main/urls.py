from django.urls import path
from . import views
urlpatterns = [
    path('', views.about),
    path('achievements/', views.achievements),
    path('achievements/<int:pk>/', views.achievement_detail),
    path('school/', views.school),
]
