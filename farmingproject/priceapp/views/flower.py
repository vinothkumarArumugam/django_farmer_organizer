from django.shortcuts import render,redirect
from priceapp.models.Flower import FlowerModel
from priceapp.forms import FlowerForm
from django.views import View


def FlowerView (request):
    if request.method == 'POST':
        form=FlowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flowerprice')
    else:
        form=FlowerForm()
    return render(request,'priceapp/flower.html',{'form':form})

    
def flower_price_view(request):
    flower_price=0
    if FlowerModel.get_acres() >=14000 :
        flower_price=50
    elif 10000 < FlowerModel.get_acres() and FlowerModel.get_acres() < 14000 :
        flower_price=100
    elif 7000 < FlowerModel.get_acres() and FlowerModel.get_acres() < 10000 :
        flower_price=150
    else :
        flower_price=80
    return render (request,'priceapp/index.html',{'flower_price':flower_price})                      