from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View

class Cart (View):
    def get(self, request):
        return render (request, 'cart.html')