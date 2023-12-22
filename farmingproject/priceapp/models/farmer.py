from django.db import models

class FarmerModel(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.username}{self.password}'


