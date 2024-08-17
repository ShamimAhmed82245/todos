from django.db import models

# Create your models here.
class Husband(models.Model):
    name = models.CharField(max_length=50)

class Wife(models.Model):
    name = models.CharField(max_length=50)
    husband = models.OneToOneField(Husband,on_delete=models.CASCADE)