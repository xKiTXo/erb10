from django.db import models
from chefs.models import Chef

# Create your models here.
class Listing(models.Model):
    chef = models.ForeignKey(Chef,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    district=models.CharField(max_length=50)
    cuisine_choices=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    specialty=models.IntegerField()
    room_type=models.CharField(max_length=50)
    has_wifi=models.BooleanField(default=True)
    has_delivery=models.BooleanField(default=True)
    rating=models.FloatField(default=0.0)
    opening_hours=models.TimeField()
    price=models.IntegerField()
    promo_badge_text=models.CharField(max_length=100,blank=True,null=True)
    accepts_reservations=models.CharField(max_length=100,blank=True,null=True)
    ambiance_note=models.CharField(max_length=100,blank=True)
    contact_number=models.CharField(max_length=20,blank=True)
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published = models.BooleanField(default=True)
    list_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['-list_date']
        indexes=[models.Index(fields=['list_date'])]

    def __str__(self):
        return self.title


