from django.db import models
from listings.choices import position_choices

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=50)
    portrait = models.ImageField(upload_to='photo/%Y/%m/%d/')
    phone = models.CharField(max_length=20)
    email= models.CharField(max_length=50)
    hire_date = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=100,choices=position_choices.items(),default='')

    def __str__(self):
        return self.name




