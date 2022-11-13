from django.db import models

# Create your models here.

class inorganic(models.Model):
    id = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=200,default='')
    company=models.CharField(max_length=200,default='')
    qty=models.DecimalField(max_digits=10,decimal_places=2)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
         return self.name