from django import forms
from django.contrib.auth.models import User
# from .models import Profile
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField, SplitPhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, UserProfile

from crispy_forms.helper import FormHelper


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")


class UserProfileCreationForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            "date_of_birth", "gender", "marital_status", "parent", "household_members", 
            "total_children" , "teacher_or_educator" , "employed_business_or_working", "occupation",
            "highest_level_education", "religion", "access_to_internet_with_smartphone",
            "phonenumber" , "preffered_contact_method", "teacher", "parent_or_caregiver" ,
            "parent_and_teacher", "neither_parent_or_teacher_over_18"
        )
        widgets = {
            'date_of_birth': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date', 'max': datetime.now().date()}),
            
        }
    

class UserProfileEditForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            "date_of_birth", "gender", "marital_status", "parent", "household_members", 
            "total_children" , "teacher_or_educator" , "employed_business_or_working", "occupation",
            "highest_level_education", "religion", "access_to_internet_with_smartphone",
            "phonenumber" , "preffered_contact_method", "teacher", "parent_or_caregiver" ,
            "parent_and_teacher", "neither_parent_or_teacher_over_18"
        )
        widgets = {
            'date_of_birth': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date', 'max': datetime.now().date()}),
            
        }
    
