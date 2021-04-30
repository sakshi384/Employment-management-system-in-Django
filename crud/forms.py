from django.core import validators
from  django import forms
from .models import emp_details
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class employeeRegistration(forms.ModelForm):

    class Meta:
        model = emp_details
        fields = ['name','email','location','technology','domain','project','blogs','score','placed']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'technology': forms.TextInput(attrs={'class': 'form-control'}),
            'domain': forms.TextInput(attrs={'class': 'form-control'}),
            'project': forms.TextInput(attrs={'class': 'form-control'}),
            'blogs': forms.TextInput(attrs={'class': 'form-control'}),
            'score': forms.TextInput(attrs={'class': 'form-control'}),
            'placed': forms.CheckboxInput,
        }


# Create your forms here.
