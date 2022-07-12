from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):
    """
    A Contact is any "Person," "Company," or "Broker" who completes a ContactUs Form
    """
    name = models.CharField(max_length=200, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    message = models.TextField(null=True, blank=True, default="")