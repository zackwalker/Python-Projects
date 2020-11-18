from django.shortcuts import render, redirect
from .forms import ProfileForm, AccountAuthenticationForm
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

def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('/')
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                return redirect('/')
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'accounts/login.html', context)
