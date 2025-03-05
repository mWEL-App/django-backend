from django.db import models
from django.conf import settings

# Create your models here.

# Financial Situation 
class FinancialSituation(models.Model):
    User = settings.AUTH_USER_MODEL

    class YES_NO(models.IntegerChoices):
        YES = 1, 'YES'
        NO = 0, 'NO'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='finacial_situation')
    enough_food = models.IntegerField(choices=YES_NO)
    basic_day_living_expenses = models.IntegerField(choices=YES_NO)
    housing_stress = models.IntegerField(choices=YES_NO)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Financial situation of {self.user.username}'

# Physical Health 
class PhysicalHealth(models.Model):
    User = settings.AUTH_USER_MODEL

    class YES_NO(models.IntegerChoices):
        YES = 1, 'YES'
        NO = 0, 'NO'
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='physical_health')
    physica_health_problem  = models.IntegerField(choices=YES_NO)
    family_members_phy_health = models.IntegerField(choices=YES_NO)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Physical health challenges of {self.user.username}'
    