from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FinancialSituationForm, PhysicalHealthForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import FinancialSituation, PhysicalHealth

from django.contrib.auth import get_user_model

# Create your views here.
@login_required
def home_living_challenges(request):
    diplay_form = True
    financial_stress = 0
    phy_health_stress = 0
    score = 0
    if request.method == 'POST':
        user = request.user
        UserObject =  get_user_model()

        financial_form = FinancialSituationForm(request.POST)
        physicalhealth_form = PhysicalHealthForm(request.POST)
        
        if financial_form.is_valid() and physicalhealth_form.is_valid():
            #  Financial Situation form
            fs = financial_form.save(commit=False)
            fs.user = UserObject.objects.get(pk=request.user.id)
            fs.save()
            enough_food = fs.enough_food
            basic_day_living_expenses = fs.basic_day_living_expenses
            housing_stress = fs.housing_stress
            total_fs_score = enough_food + basic_day_living_expenses + housing_stress
            if (enough_food == 1 or basic_day_living_expenses == 1 or  housing_stress == 1 or total_fs_score >= 1):
                financial_stress = 1
                
            # Physical Health
            ph = physicalhealth_form.save(commit=False)
            ph.user = UserObject.objects.get(pk=request.user.id)
            ph.save()
            physica_health_problem = ph.physica_health_problem
            family_members_phy_health = ph.family_members_phy_health
            total_ph_score = physica_health_problem + family_members_phy_health
            if (physica_health_problem == 1 or family_members_phy_health ==1 or total_ph_score >= 1 ):
                phy_health_stress = 1

            messages.success(request, 'Home and living challelnges submited')
            diplay_form = False
            score = total_fs_score + total_ph_score
        else:
            messages.error(request, "Error submitting your Home and living challelnges")
    else:
        financial_form = FinancialSituationForm(instance=request.user)
        physicalhealth_form = PhysicalHealthForm(instance=request.user)

    
    return render(request, 'stresstracker/home_and_living_challenges.html', 
                  {'score' : score, 'financial_stress': financial_stress, 
                   'phy_health_stress': phy_health_stress,
                      'display_form': diplay_form ,'financial_form':financial_form,
                   'physicalhealth_form' :physicalhealth_form })

class HomeLivingChallenges(LoginRequiredMixin, CreateView):
    pass;
