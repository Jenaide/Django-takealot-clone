from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from shop.models.customer import Customer
from django.views import  View
from shop.models.products import Product

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(ids)
        print(products)
        context = {
            'products': products
        }
        return render(request , 'cart.html', context)