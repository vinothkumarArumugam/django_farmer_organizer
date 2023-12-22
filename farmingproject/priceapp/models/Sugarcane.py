from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models import Sum

class SugarcaneModel(models.Model):
    farmer_name=models.CharField(max_length=50)
    farmer_panchayat=models.CharField(max_length=100)
    farmer_district=models.CharField(max_length=100)
    farmer_phone=models.CharField(max_length=10)
    total_acres=models.IntegerField()
    
    def __str__(self):
        return f"Name: {self.farmer_name}, Panchayat: {self.farmer_panchayat}, District: {self.farmer_district}, Phone: {self.farmer_phone}, Acres: {self.total_acres}"
    @staticmethod
    def get_acres():
        total_acres_sum = SugarcaneModel.objects.aggregate(total_acres_sum=Sum('total_acres'))
        return total_acres_sum['total_acres_sum']