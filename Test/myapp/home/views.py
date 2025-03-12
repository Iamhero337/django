from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page(request):
    return HttpResponse('<h1>Home Page</h1>')
def login(request):
    return render(request, 'login.html')