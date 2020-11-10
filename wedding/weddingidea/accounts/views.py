from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import ProfileForm, CustomUserCreationForm

def update_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        user_form = CustomUserCreationForm(request.POST)
<<<<<<< HEAD
        profile_form = ProfileForm(request.POST, instance=profile)
=======
<<<<<<< HEAD
        profile_form = ProfileForm(request.POST)
=======
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
>>>>>>> bda3eed06045d724e6ee441676371eb0c4d0e9ad
>>>>>>> eb20b60ede3cf6438a5be5220dd047fff0dd73e5
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save() 
            return redirect('registration:registration')
    else:
        user_form = CustomUserCreationForm()
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
    return render(request, 'registration/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
<<<<<<< HEAD

=======
>>>>>>> bda3eed06045d724e6ee441676371eb0c4d0e9ad
