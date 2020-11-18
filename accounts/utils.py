from .models import *

def cartData(request):
    if request.user.is_authenticated:
        print(request.user)
        customer, created = Customer.objects.get_or_create(user=request.user)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cartItems = "No Items"
        order = 0
        items = []

    return {'cartItems':cartItems,'order':order,'items':items}