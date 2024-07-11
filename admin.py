from django.contrib import admin
from . models import Product,Product2,Customer,Cart,Product3

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','sellingprice','category','product_image']
    
    
@admin.register(Product2)
class Product2ModelAdmin(admin.ModelAdmin):
    list_display=['id','title','intro','groom','train','nutri','category2','product_image']
   
@admin.register(Product3)
class Product3ModelAdmin(admin.ModelAdmin):
    list_display=['id','name','intro','degree','email','number','category3','product_image']

  
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','address','email','mobile']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
   list_display=['id','user','products','quantity']
   def products(self,obj):
    link=reverse("admin:app_product_change",args=[obj.product.pk])
    return format_html('<a href="{}">{}</a>',link,obj.product.title)
