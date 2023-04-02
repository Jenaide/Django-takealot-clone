from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View

class Checkout (View):
    def get(self, request):
        return render (request, 'checkout.html')