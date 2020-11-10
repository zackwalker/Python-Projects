from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.core.exceptions import ValidationError

#create a custom form and use forms.Form since we dont have to save to database
class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4,
                               max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Enter email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class meta: 
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            # 'person2_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'date_of_event': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    #ensures the username doesnt already exist
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    # ensures email isnt already used
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    # makes sure that the passwords match
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    #saves the data to be part of the User model
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['person2_first_name', 'person2_last_name', 'date_of_event','email']

    class meta: 
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            # 'person2_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'date_of_event': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

