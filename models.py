from django.db import models
from django.contrib.auth.models import User




CATEGORY_CHOICES=(
    ('FO','Food'),
    ('ME','Medicine'),
    ('AC','Accesories'),
    ('ES','Essentials'),
      ('DO','Dogs'),
    ('CA','Cats'),
    ('FI','Fishes'),
    ('BI','Birds'),
    ('RO','Rodents'),
    
)


CATEGORY_CHOICES1=(
  
    
)

CATEGORY_CHOICES2=(
    ('DG', 'Dog'),
    ('CT', 'Cat'),
    ('FS', 'Fish'),
    ('BR', 'Bird'),
    ('RD', 'Rodent'),

)

CATEGORY_CHOICES3=(
    ('SP', 'Specialists'),
    ('VE', 'Vet'),
  

)

class Product(models.Model):
    title=models.CharField(max_length=100)
    sellingprice=models.FloatField()
    description=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='product')
    def _str_(self):
        return self.title
    
    
    

class Product2(models.Model):
    title=models.CharField(max_length=100)
    intro=models.TextField(default='')
    groom=models.TextField(default='')
    train=models.TextField(default='')
    nutri=models.TextField(default='')
    category2=models.CharField(choices=CATEGORY_CHOICES2,max_length=2)
    product_image=models.ImageField(upload_to='product2')
    def _str_(self):
        return self.title     


class Product3(models.Model):
    name=models.CharField(max_length=100)
    intro=models.TextField(default='')
    degree=models.TextField(default='')
    email=models.TextField(default='')
    number=models.TextField(default='')
    category3=models.CharField(choices=CATEGORY_CHOICES3,max_length=2)
    product_image=models.ImageField(upload_to='product3')
    def _str_(self):
        return self.title      
    
    
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    mobile=models.IntegerField(default=0)
    address=models.CharField(max_length=200)
    def _str_(self):
        return self.name



class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    @property
    def total_cost(self):
       return self.quantity*self.product.sellingprice

