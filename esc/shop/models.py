from django.db import models

# Create your models here.



class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50,default="")
    sub_category = models.CharField(max_length=50,default="")
    price =models.IntegerField(default=0)
    desc = models.CharField(max_length=120)
    pub_date = models.DateField()
    images = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Register(models.Model):
    cust_id = models.AutoField
    firstname = models.CharField(max_length=100,default="")
    middlename = models.CharField(max_length=100,default="")
    lastname = models.CharField(max_length=100,default="")
    cust_name = models.CharField(max_length=100,default="")
    username = models.CharField(max_length=100,default="")
    mail = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=20,default="")
    address = models.CharField(max_length=100,default="")
    contact = models.IntegerField(default=0)
    cust_create_date = models.DateField()

    def __str__(self):
        return self.firstname
