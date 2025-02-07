from django.shortcuts import render, redirect
from account.models import CustomUser, UserProfile
from django.urls import reverse

# Create your views here.

def index(request):
    profile_exist = False
    if request.user.is_authenticated:

        user = request.user
        try:
            profile = user.profile
            print("Profile exists ", profile.gender)
            profile_exist = True
        except:
            print("No profile set")
            return redirect(reverse('create_profile'))

    return render(request, 'index.html', {'section':'home', 'profile_exist': profile_exist})