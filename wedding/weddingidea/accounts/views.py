from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import ProfileForm, CustomUserCreationForm
from .models import Profile
from django.contrib.auth.decorators import login_required

def update_profile(request):

    if request.method == 'POST':
        profile = get_object_or_404(Profile, user=request.user)
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, instance=profile)
        # if user_form.is_valid():
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            return redirect('/')
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'registration/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
