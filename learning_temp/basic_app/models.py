from django.db import models
from phone_field import PhoneField
# Create your models here.

CHOICES=[('M','Male'),('F','Female')]
class User(models.Model):
    Name=models.CharField(max_length=64)
    Bdate=models.DateField(auto_now=False,null=True,blank=True)
    Gender=models.CharField(max_length=1,choices=CHOICES)
    Email=models.EmailField(unique=True)
    Contact=PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return self.Name
