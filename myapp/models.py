from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=201)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Customer(models.Model):
    first_name = models.CharField(max_length=153)
    last_name = models.CharField(max_length=202)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=202)

    def __str__(self):
        return self.first_name

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_date = models.DateTimeField(auto_now_add=True)
    
