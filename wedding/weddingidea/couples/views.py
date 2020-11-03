from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm

def landing_page(request):
    return render(request, 'couples/landPage.html')
    # return HttpResponse("Hello, world. You're at the polls index.")


def registerPage(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _(
                'Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm()
        # profile_form = ProfileForm()
    return render(request, 'couples/register.html', {
        'user_form': user_form,
        # 'profile_form': profile_form
    })
