from django.db.models import Count,Q
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from . models import Product,Product2,Customer,Cart,Product3
from . forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@login_required 
def home(request):
    totalitem=0
    if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))   
    return render(request,"app/home.html")

login_required
class CategoryView(View):
    def get(self,request,val):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))   
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())
    

    
login_required
class Category2View(View):
    def get(self,request,val2):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))   
        product=Product2.objects.filter(category2=val2)
        title=Product2.objects.filter(category2=val2).values('title')
        return render(request,"app/category2.html",locals())  
        
        
        
login_required
class Category3View(View):
    def get(self,request,val3):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))   
        product3=Product3.objects.filter(category3=val3)
        name=Product3.objects.filter(category3=val3).values('name')
        return render(request,"app/category3.html",locals())    
    
    
login_required
class ProductDetail(View):
    def get(self,request,pk):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))   
        product=Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals()) 
    
  
    
login_required
class ProductDetail2(View):
    def get(self,request,pk2):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))   
        product=Product2.objects.get(pk=pk2)
        return render(request,"app/productdetail2.html",locals()) 



        
    
login_required
class ProductDetail3(View):
    def get(self,request,pk3):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))   
        product3=Product3.objects.get(pk=pk3)
        return render(request,"app/productdetails3.html",locals()) 
   
login_required
class CategoryTitle(View):
    def get(self,request,val):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))   
        product=Product.objects.filter(title=val)
        title=Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())    
    
    
  
        
login_required
class CategoryTitle2(View):
    def get(self,request,val2):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))   
        product=Product2.objects.filter(title=val2)
        title=Product2.objects.filter(category2=product[0].category2).values('title')
        return render(request,"app/category2.html",locals())    



login_required
class CategoryTitle3(View):
    def get(self,request,val3):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))   
        product3=Product3.objects.filter(name=val3)
        name=Product3.objects.filter(category3=product3[0].category3).values('name')
        return render(request,"app/category3.html",locals())    
        
class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,"app/customerregistration.html",locals())  
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! Registration Successful.")
        else:
            messages.warning(request,"Invalid Inputs")
        return render(request,"app/customerregistration.html",locals())    
    
login_required
class ProfileView(View):
    def get(self,request):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))   
        form=CustomerProfileForm()
        return render(request,"app/profile.html",locals())


    def post(self,request): 
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))   
        form=CustomerProfileForm(request.POST)
        totalitem=0
        
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            address=form.cleaned_data['address']
            email=form.cleaned_data['email']
            mobile=form.cleaned_data['mobile']

            reg=Customer(user=user,name=name,address=address,email=email,mobile=mobile)
            reg.save()
            messages.success(request,"Congratulations! Your details have been saved successfully!")
        else:
            messages.warning(request,"Data Entered Is Invalid!!!")
        return render(request,"app/profile.html",locals())

login_required
def add_to_cart(request):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))   
        user = request.user
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        Cart(user=user,product=product).save()
        return redirect("/cart")

login_required
def show_cart(request):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))   
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.sellingprice
            amount = amount + value
        totalamount = amount
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))

        return render(request, 'app/addtocart.html', locals())




@method_decorator(login_required,name='dispatch')
class checkout(View):
    def get(self,request):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
       
        user=request.user
        customer=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
       
        famount=0
        for p in cart_items:
            value=p.quantity*p.product.sellingprice
            famount=famount+value
        totalamount=famount
        return render(request,'app/checkout.html',locals())


@method_decorator(login_required,name='dispatch')
class summary(View):
    def get(self,request):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
       
        user=request.user
        customer=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
       
        famount=0
        for p in cart_items:
            value=p.quantity*p.product.sellingprice
            famount=famount+value
        totalamount=famount
        return render(request,'app/summary.html',locals())


def plus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value=p.quantity*p.product.sellingprice
            amount=amount+value
        totalamount=amount
        data={'quantity':c.quantity,
                'amount':amount,
                'totalamount':totalamount
        }
        return JsonResponse(data)




def minus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value=p.quantity*p.product.sellingprice
            amount=amount-value
        totalamount=amount
        data={'quantity':c.quantity,
                'amount':amount,
                'totalamount':totalamount
        }
        return JsonResponse(data)



def remove_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value=p.quantity*p.product.sellingprice
            amount=amount+value
        totalamount=amount
        data={
                'amount':amount,
                'totalamount':totalamount
        }
        return JsonResponse(data)

@login_required
def search(request):
    query=request.GET['search']
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    product=Product.objects.filter(Q(title__icontains=query))
    return render(request,"app/search.html",locals())