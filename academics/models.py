from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    id= models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=50, unique=True, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null = False, blank = False)
    updated_at = models.DateTimeField(auto_now=True, null = False, blank = False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.email
    
class client(models.Model):
    id_client = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    identification = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null = False, blank = False)
    updated_at = models.DateTimeField(auto_now=True, null = False, blank = False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.name

class product(models.Model):
    id_product = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    abrebiation = models.CharField(max_length=5, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    price = models.IntegerField(blank= False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null = False, blank = False)
    updated_at = models.DateTimeField(auto_now=True, null = False, blank = False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class order(models.Model):   
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    id_product = models.ForeignKey(product, on_delete=models.CASCADE, blank=False, null=False)
    id_client = models.ForeignKey(client, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return self.name
    
    
class sale(models.Model):
    id_sale = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    id_product = models.ForeignKey(product, on_delete=models.CASCADE, blank=False, null=False)
    cant = models.IntegerField(blank=False, null=False)
    total = models.IntegerField(blank=False, null=False)
    def __str__(self):
        return self.total
    



    

    