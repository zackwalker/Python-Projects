from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.core.exceptions import ValidationError
from django.contrib.auth import login, authenticate
# #create a custom form and use forms.Form since we dont have to save to database


class ProfileForm(UserCreationForm):

    category_choices = [
        ('couple', 'Couple'),
        ('vendor', 'Vendor'),
        ('wedding_planner', 'Wedding Planner')
    ]

    wedding_category = forms.ChoiceField(
        choices=category_choices, required=True)

    class Meta:
        model = Profile
        fields = ['name_of_event', 'date_of_event','email','username','password1','password2']


        widgets = {
            'name_of_event': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_event': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'wedding_category': forms.Select(attrs={'class': 'form-control'}),
        }


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['email','password']
    
    def clean(self):
        if self.is_valid():
            email =  self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email,password=password):
                raise ValidationError("Invalid Login")