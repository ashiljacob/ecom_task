from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy,reverse
from django.views import generic
from .utils import cartData
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseRedirect

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def home(request):
    data = cartData(request)
    cartItem = data['cartItems']
       
    product = Product.objects.all()
    context = {'products':product,'cartItem':cartItem}
    return render(request,'home.html',context)

def cart(request):
    data = cartData(request)
    cartItem = data['cartItems']
    order    = data['order']
    items    = data['items']
    print(items)
    total = order.get_cart_items * order.get_cart_total

    context = {'items':items,'order':order,'cartItem':cartItem,'total':total}
    return render(request,'cart.html',context)

def add_to_cart(request,id):
    if request.method == "POST":
        customer = request.user.customer
       
        product = Product.objects.get(id=id)
        
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity = orderItem.quantity + 1

        orderItem.save()


        # if orderItem.quantity <= 0:
        #     orderItem.delete()

        return HttpResponseRedirect('/')

    

def cart(request):
    user=request.user
    customer,created = Customer.objects.get_or_create(user=user)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

    context = {
        'items':items,
        'order':order,
        'cartItem':cartItems
    }
    print(items,cartItems,order)
    return render(request,'cart.html',context)

def increaseItem(request,id):
    user= request.user
    item = OrderItem.objects.get(id=id)
    item.quantity += 1
    item.save()
    print(item.quantity)

    return HttpResponseRedirect(reverse("cart"))

def decreaseitem(request,id):
    user= request.user
    item = OrderItem.objects.get(id=id)
    item.quantity -= 1
    item.save()
    if item.quantity <= 0:
        item.delete()
    print(item)

    return HttpResponseRedirect(reverse("cart"))