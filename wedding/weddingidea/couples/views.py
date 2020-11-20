from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

def landing_page(request):
    return render(request, 'couples/landPage.html')

# create a list view of all vendor types

#navbar: vendor list, upcoming events, upcoming actions

# todo/ needed venders remaining list
# vender list - small cards of each vender and a pic/address
# create search tool to find venders
