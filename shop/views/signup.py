from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View

class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')