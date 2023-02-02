from django.db import models

# Create your models here.

class vaibhav(models.Model):
    name=models.CharField( max_length=20,)
    email=models.EmailField(max_length=20,)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField(max_length=20)
    desc=models.CharField(max_length=20)


    def __str__(self):
        return self.name