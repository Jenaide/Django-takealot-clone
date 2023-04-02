from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View

class Orders (View):
    def get(self, request):
        return render (request, 'orders.html')