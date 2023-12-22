from django.contrib import admin
from priceapp.models.Turmeric import TurmericModel
from priceapp.models.Flower import FlowerModel
from priceapp.models.Sugarcane import SugarcaneModel
from priceapp.models.farmer import FarmerModel

class TurmericModelAdmin(admin.ModelAdmin):
    list_display = ('farmer_name', 'farmer_panchayat', 'farmer_district', 'farmer_phone', 'total_acres')


class SugarcaneModelAdmin(admin.ModelAdmin):
    list_display = ('farmer_name', 'farmer_panchayat', 'farmer_district', 'farmer_phone', 'total_acres')

class FlowerModelAdmin(admin.ModelAdmin):
    list_display = ('farmer_name', 'farmer_panchayat', 'farmer_district', 'farmer_phone', 'total_acres')

class FarmerModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')
    

admin.site.register(TurmericModel, TurmericModelAdmin)
admin.site.register(SugarcaneModel,SugarcaneModelAdmin)
admin.site.register(FlowerModel,FlowerModelAdmin)
admin.site.register(FarmerModel,FarmerModelAdmin)


# Register your models here.
