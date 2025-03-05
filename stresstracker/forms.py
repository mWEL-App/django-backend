from django import forms
from django.contrib.auth.models import User
from .models import FinancialSituation, PhysicalHealth

#      Financial Situation 
class FinancialSituationForm(forms.ModelForm):

    class Meta:
        model = FinancialSituation
        fields = ("enough_food", "basic_day_living_expenses", "housing_stress")
        labels = {
            "enough_food": "Not having enough food to eat in house because of lack of resource to buy food", 
            "basic_day_living_expenses": "Basic day-to-day living expenses", 
            "housing_stress": "Housing stress"
        }
        widgets = {
            
        }


# Physical Health 
class PhysicalHealthForm(forms.ModelForm):

    class Meta:
        model = PhysicalHealth
        fields = ("physica_health_problem", "family_members_phy_health")
        labels = {
            "physica_health_problem" :  "physica_health_problem",
            "family_members_phy_health" : "family_members_phy_health",
        }