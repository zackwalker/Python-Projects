from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import ProfileForm, CustomUserCreationForm

def update_profile(request):
    if request.method == 'POST':
<<<<<<< HEAD
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save() 
            return redirect('registration:registration')
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileForm(request.POST)
        print(profile_form)
=======
        profile = Profile.objects.get(user=request.user)
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save() 
            return redirect('/')
    else:
        user_form = CustomUserCreationForm()
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
>>>>>>> a1cc382631312f64c6dd56057d48ea35206c7fa9
    return render(request, 'registration/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
