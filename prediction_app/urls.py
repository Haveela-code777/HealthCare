from ast import pattern
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',HomeView,name='home'),
    path('heart_ml/',heartmlview,name='heart_ml'),
    path('heart_ann/',heartannview,name='heart_ann'),
    path('api/heart_ml/',HeartMachineLearningAPIView.as_view()),
    path('api/heart_ann/',HeartANNAPIView.as_view()),
]
