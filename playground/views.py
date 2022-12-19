from django.shortcuts import render
from django.db.models import Q, F
from store.models import *


# Create your views here.

def sayHello(request):

    #Q objects allow OR comparisons
    #queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))

    #F objects allow for Reference Comparisons
    #queryset = Product.objects.filter(inventory = F('unit_price'))

    #Sorting data: order_by (gives a queryset), other eg; earliest, latest, etc, return items or objects
    #queryset = Product.objects.order_by('unit_price')

    #Splicing
    #queryset = Product.objects.all()[:5]

    #Selecting particular fields to query using the "values" (dictionary) or "values_list" (tuples)
    #queryset=Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    #Selecting particular fields using the "only". Returns instances instead of dictionaries like 'values'. "Defers" is the opposite of "only"
    queryset = Product.objects.only('id', 'title')    

    return render(request, "hello.html", {"name": "Richard", "products": list(queryset)})