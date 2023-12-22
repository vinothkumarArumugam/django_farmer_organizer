from django.shortcuts import render

def form_redirect_view(request):
    return render(request,'priceapp/form.html')
