from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

def update_profile(request):

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            email = profile_form.cleaned_data.get('email')
            password1 = profile_form.cleaned_data.get('password1')
            account = profile_form.save()
            # account = authenticate(email=email, password=password1)
            login(request, account)
            return redirect('/')
        else:
            profile_form = ProfileForm(request.POST)
    else:
        profile_form = ProfileForm()
    return render(request, 'registration/registration.html', {
        'profile_form': profile_form
    })
