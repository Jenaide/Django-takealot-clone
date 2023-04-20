from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from shop.models.customer import Customer
from django.views import View
from shop.models.products import Product
from shop.models.orders import Order
from shop.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        context = {
            'orders': orders
        }
        return render(request , 'orders.html'  , context)