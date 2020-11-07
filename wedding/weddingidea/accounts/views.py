from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm, ProfileForm


class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


def update_profile(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save() 
            return redirect('registration:registration')
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()
        print(profile_form)
    return render(request, 'registration/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
