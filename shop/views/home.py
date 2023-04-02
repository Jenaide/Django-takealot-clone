from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View


class Index (View) :
    def get(self, request):
        return render(request, 'home.html')