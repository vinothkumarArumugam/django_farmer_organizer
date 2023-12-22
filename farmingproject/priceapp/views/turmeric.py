from django.shortcuts import render,redirect
from priceapp.models.Turmeric import TurmericModel
from priceapp.forms import TurmericForm
from django.views import View


def TurmericView(request):
    if request.method == 'POST':
        form=TurmericForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('turmericprice')
    else :
        form=TurmericForm()
    return render(request,'priceapp/turmeric.html',{'form':form}) 

    
def turmeric_price_view(request):
    turmeric_price=0
    if TurmericModel.get_acres() >= 770000 :
        turmeric_price=10000
    elif 600000 <= TurmericModel.get_acres() and TurmericModel.get_acres() <= 700000 :
        turmeric_price=15000
    elif 700000 < TurmericModel.get_acres() and TurmericModel.get_acres() < 769999 :  
        turmeric_price=12000
    else:
        turmeric_price=13000
    return render(request,'priceapp/index.html',{'turmeric_price':turmeric_price})          
                     
    
