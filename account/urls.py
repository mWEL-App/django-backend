from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('create-profile/', views.CreateUserProfileView.as_view(), name='create_profile'),
    # path('update-profile/', views.UpdateUserProfile, name='update_profile'),

    path('update-profile/<int:pk>/', views.UpdateUserProfileView.as_view(), name='update_profile'),
   
] 