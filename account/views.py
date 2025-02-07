from django.shortcuts import render

from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserCreationForm, UserProfileCreationForm, UserProfileEditForm
from django.contrib import messages

# Create your views here.

@login_required
def profile(request):
    profile_exist = True
    return render(request, 'account/profile.html', {'section':'profile', 'profile_exist':profile_exist})

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CreateUserProfileView(LoginRequiredMixin, CreateView):
    template_name = "account/create_profile.html"
    form_class = UserProfileCreationForm
    success_url = "/account/profile/"

    def form_valid(self, form):
        instance = form.instance
        instance.user =self.request.user
        messages.add_message(self.request, messages.INFO, 'Profile successfully Created.')
        return super().form_valid(form)


class UpdateUserProfileView(LoginRequiredMixin,  UpdateView):
    model = UserProfile
    template_name = "account/update_profile.html"
    form_class = UserProfileEditForm
    success_url = "/account/profile/"
    profile_exist = True
    extra_content = {'profile_exist': profile_exist}

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, 'Profile successfully Updated.')
        return super().form_valid(form)


# @login_required
# def UpdateUserProfile(request):
#     if request == 'POST':
#         profile_form = UserProfileEditForm(data = request.POST)
#         if profile_form.is_valid():
#             profile_form.save()
#             messages.success(request, 'Profile updated successfully')
#         else:
#             messages.error(request, 'Error updating your profile')
    
#     else:
#         profile_form = UserProfileEditForm(instance=request.user.profile)

#     return render(request, 'account/update_profile.html', {'profile_form':profile_form})