from django.urls import path
from . import views


urlpatterns = [
    path('', views.result),
    path('result/', views.result, name="result"),
    path('resultpage/<str:pk>/', views.resultpage, name="resultpage"),
]