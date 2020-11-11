from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import ProfileForm, CustomUserCreationForm
from .models import Profile

def update_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        # profile = Profile.objects.get(user=request.user)
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save() 
            return redirect('/')
    else:
        user_form = CustomUserCreationForm()
        # profile = Profile.objects.get(user=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'registration/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
