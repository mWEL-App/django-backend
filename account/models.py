from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save 
from django.dispatch import receiver  
from django.core.validators import RegexValidator
# Create your models here.

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username



class UserProfile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
    
    class YES_NO(models.TextChoices):
        YES = 'yes', 'Yes'
        NO = 'no', 'No'

    class Education(models.TextChoices):
        NONE = 'none', 'None'
        PRIMARY = 'primary', 'Primary'
        SECONDARY = 'secondary', 'secondary'
        HIGHER = 'higher', 'Higher'
        NON_STABDARD = 'non-Standard-Curriculum', 'Non-Standard-Curriculum'
    

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    marital_status = models.CharField(max_length=20)
    parent = models.CharField(max_length=3, choices=YES_NO.choices)
    household_members = models.IntegerField()
    total_children = models.IntegerField()
    teacher_or_educator = models.TextField(max_length=3, choices=YES_NO.choices)
    employed_business_or_working = models.CharField(max_length=3, choices=YES_NO.choices)
    occupation = models.TextField(blank=True, null=True)
    highest_level_education = models.CharField(max_length=30, choices=Education.choices)
    religion = models.TextField()
    access_to_internet_with_smartphone = models.CharField(max_length=3, choices=YES_NO.choices)
    phonenumber = models.CharField(blank=True, 
                                   null=True, 
                                   default=None,
                                   max_length=20,
                                   validators=[
                                        RegexValidator(
                                            regex=r'^\+?1?\d{9,15}$',  # Example regex for international phone numbers
                                            message="Phone number must be entered in the format: '+256777777777'. Up to 15 digits allowed."
            )
        ]
                                   )
    preffered_contact_method = models.TextField()
    teacher = models.CharField(max_length=3, choices=YES_NO.choices, blank=True, null=True)
    parent_or_caregiver = models.CharField(max_length=3, choices=YES_NO.choices, blank=True, null=True)
    parent_and_teacher = models.CharField(max_length=3, choices=YES_NO.choices, blank=True, null=True)
    neither_parent_or_teacher_over_18 = models.CharField(max_length=3, choices=YES_NO.choices, blank=True, null=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

# @receiver(post_save, sender=CustomUser)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     UserProfile.objects.get_or_create(user=instance)