from django import forms
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(forms.ModelForm):    
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email','password1']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['person2_first_name', 'person2_last_name', 'date_of_event']

        widgets = {
            'person2_first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'person2_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_event': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }
