
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from priceapp.forms import FarmerSignUpForm


def login_view(request):
    if request.method == 'POST':
        form =FarmerSignUpForm( request.POST)
        if form.is_valid():
            return redirect('form')
    else:
        form = FarmerSignUpForm()
    return render(request, 'priceapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') 
