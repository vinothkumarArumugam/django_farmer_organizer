from django import forms
from priceapp.models.Turmeric import TurmericModel
from priceapp.models.Sugarcane import SugarcaneModel
from priceapp.models.Flower import FlowerModel

from priceapp.models.farmer import FarmerModel




class TurmericForm(forms.ModelForm):
    class Meta:
        model=TurmericModel
        fields=['farmer_name','farmer_panchayat','farmer_district','farmer_phone','total_acres']

class SugarcaneForm(forms.ModelForm):
    class Meta:
        model=SugarcaneModel
        fields=['farmer_name','farmer_panchayat','farmer_district','farmer_phone','total_acres']

class FlowerForm(forms.ModelForm):
    class Meta:
        model=FlowerModel
        fields=['farmer_name','farmer_panchayat','farmer_district','farmer_phone','total_acres']  


class FarmerSignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)







