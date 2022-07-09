from django.db import models

# Create your models here.
class Quote(models.Model):
    company_name = models.CharField(max_length=200, null=True, blank=True)

