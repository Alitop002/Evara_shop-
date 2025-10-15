from django.shortcuts import render
from django.template.context_processors import request






def wishilst(request):
    return render(request, "shop/wishlist.html")
    
