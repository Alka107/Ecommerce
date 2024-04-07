from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from .forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages
from .models import Customer, Cart
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_protect



def home(request):
    return render(request, "app/home.html")

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

class CategoryView(View):
    def get(self,request, val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())
    
class CategoryTitle(View):
    def get(self, request,val):
        product=Product.objects.filter(title=val)
        title=Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html",locals())


class ProductDetail(View):
    def get(self, request, pk):
        product=Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html", locals())

class CustomerRegistrationView(View):
    def get(self, request):
        form= CustomerRegistrationForm()
        return render(request, "app/customerregistration.html", locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congrulation! User Register Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, "app/customerregistration.html", locals())
    

class ProfileView(View):
    def get(self, request):
        form=CustomerProfileForm()
        return render(request, "app/profile.html", locals())
    
    def post(self, request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg=Customer(user=user, name=name, locality=locality, mobile=mobile, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile save Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, "app/profile.html", locals())

def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', locals())


class updateAddress(View):
    def get(Self,request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
#automatically field in update box
        return render(request, 'app/updateAddress.html' , locals())
 
    def post(self, request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name= form.cleaned_data['name']
            add.locality= form.cleaned_data['locality']
            add.city= form.cleaned_data['city']
            add.mobile= form.cleaned_data['mobile']
            add.state= form.cleaned_data['state']
            add.zipcode= form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Congrulations! Profile Update Successfullt")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect('address')
class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
      
        logout(request)
        
        return HttpResponseRedirect(reverse('login'))  # Change 'login' to your actual login URL name

    def post(self, request, *args, **kwargs):
       
        pass
 
        

def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('product_id')
    product=Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

def show_cart(request):
    totalitem=0
    wishlist=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        wishlist=len(Wishlist.objects.filter(user=request.user))
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.quantity * p.product.discounted_price
        amount+=value
    totalamount=amount+50        #50 is the shipping charge 
    return render(request, 'app/addtocart.html',locals())









