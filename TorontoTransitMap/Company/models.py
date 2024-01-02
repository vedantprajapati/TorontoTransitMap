from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True,null=True)
    
    def __str__(self):
        return self.name