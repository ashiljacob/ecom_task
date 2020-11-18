from django.urls import path

from . import views

urlpatterns = [
    path('signup',views.SignUpView.as_view(),name='signup'),
    path("cart",views.cart,name='cart'),
     path('', views.home, name='home'), # new
     path("add_to_cart/<int:id>",views.add_to_cart,name='add_toCart'),
     path('increase-item/<int:id>',views.increaseItem,name='increase_item'),
     path('decrease-item/<int:id>',views.decreaseitem,name='decrease_item'),

]
