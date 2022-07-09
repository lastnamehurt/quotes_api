from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    estimated_distance = models.CharField(max_length=200, blank=True, null=True)
    container_type = models.CharField(max_length=200, blank=True, null=True)
    is_legal_weight = models.BooleanField(default=True)
    is_hazmat = models.BooleanField(default=False)
    additional_details = models.TextField(default="")
    # total = models.CharField(max_length=200, null=True, blank=True)
    total = MoneyField(decimal_places=2,
                       default=0,
                       default_currency='USD',
                       max_digits=25,
                       )
    # url = models.URLField(null=True, blank=True, verbose_name="API URL")
