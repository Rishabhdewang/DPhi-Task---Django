from django.db import models

# Create your models here.
class Plant(models.Model):
    plantId = models.AutoField
    pName = models.CharField(max_length=50)
    pDescription = models.CharField(max_length=250)
    pPrice = models.CharField(max_length=50)
    pStock = models.CharField(max_length=50)
    PImage = models.ImageField(upload_to ='task/images',blank= True,null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.pName


class User(models.Model):
    userId = models.AutoField
    name = models.CharField(max_length=50,default="Anonymous")
    email = models.EmailField(max_length=254,unique=True)
    password = models.EmailField(max_length=12)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Nursery(models.Model):
    nurseryId = models.AutoField
    name = models.CharField(max_length=50,default="Anonymous")
    email = models.EmailField(max_length=254,unique=True)
    password = models.EmailField(max_length=12)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name