from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 


class ride(models.Model):
    email = models.EmailField(default="example@gmail.com")
    location = models.TextField(max_length=20)
    destination = models.TextField(max_length=20)
    nop = models.IntegerFiel(validators=[MinValueValidator(1), MaxValueValidator(10)])
    avgspeed = models.IntegerFiel(validators=[MinValueValidator(30), MaxValueValidator(150)])
    date = models.DateField()
    
    