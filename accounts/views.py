from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request,'accounts/home.html')

def register(request):
    if request.user.is_authenticated:
        homeurl = reverse('home')
        return HttpResponseRedirect(homeurl)
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/account/register/')
        else:
            form = RegisterForm()
        return render(request,'accounts/register.html',{'form':form})