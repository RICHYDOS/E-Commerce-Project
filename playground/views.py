from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def calculate():
    x=1
    y=2
    return x
def sayHello(request):
    x=calculate()
    y=2
    return render(request, "hello.html", {"name": "Richard", "x": x})