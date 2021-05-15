from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User

class ride(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default = 1,null=True)
    location = models.TextField(max_length=20)
    destination = models.TextField(max_length=20)
    nop = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    avgspeed = models.IntegerField(validators=[MinValueValidator(30), MaxValueValidator(150)])
    money = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(5000)] ,default= 10)
    acnonac = models.BooleanField(null= True, default= True)
    date = models.DateField()
    
    