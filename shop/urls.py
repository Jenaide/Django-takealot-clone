from django.urls import path
from .views.home import Index, shop
#from .views.signup import Signup
#from .views.login import Login , logout
#from .views.cart import Cart
#from .views.checkout import Checkout
#from .views.orders import OrderView
#from .middlewares.auth import  auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('shop', shop , name='shop'),

    #path('signup', Signup.as_view(), name='signup'),
    #path('login', Login.as_view(), name='login'),
    #path('logout', logout , name='logout'),
    #path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    #path('check-out', Checkout.as_view() , name='checkout'),
    #path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]