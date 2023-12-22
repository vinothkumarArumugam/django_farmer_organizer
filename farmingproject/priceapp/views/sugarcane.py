from django.shortcuts import render,redirect
from priceapp.models.Sugarcane import SugarcaneModel
from priceapp.forms import SugarcaneForm
from django.views import View

def SugarcaneView(request):
    if request.method == 'POST':
        form=SugarcaneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sugarcaneprice')
    else :
        form=SugarcaneForm()
    return render(request,'priceapp/sugarcane.html',{'form':form})         
def sugarcane_price_view(request):
    sugarcane_price=0
    if SugarcaneModel.get_acres() > 10000000 :
        sugarcane_price=2000
    elif 9000000 < SugarcaneModel.get_acres() and SugarcaneModel.get_acres() <= 9999999 :
        sugarcane_price=2500
    elif 8000000 < SugarcaneModel.get_acres() and SugarcaneModel.get_acres() < 9000000 :
        sugarcane_price=2800
    elif 7000000 < SugarcaneModel.get_acres() and SugarcaneModel.get_acres() < 8000000 :
        sugarcane_price=3000
    else :
        sugarcane_price=2600
    return render (request,'priceapp/index.html',{'sugarcane_price':sugarcane_price})                
   