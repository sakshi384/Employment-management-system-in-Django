from django import forms
from .models import trial_details

class Trial_registration(forms.ModelForm):
    class Meta:
        model=trial_details
        # fields=['name','email','location','image','technology','domain','project','blogs','score','placed']
        fields=['name','email','location','technology','domain','project','blogs']