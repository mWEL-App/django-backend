from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('homeandleavingchallenges/', views.home_living_challenges, name="home_living_challenges"),
   
] 