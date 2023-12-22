from priceapp.forms import FarmerSignUpForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login 
from priceapp.models.farmer import FarmerModel


def signup(request):
    if request.method == 'POST':
        form = FarmerSignUpForm(request.POST)
        if form.is_valid():
            FarmerModel.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

    
            return redirect('login')
    else:
        form = FarmerSignUpForm()
    return render(request, 'priceapp/signup.html', {'form': form})

