from django.shortcuts import render
from django.http import JsonResponse
from shop.models import  Product
from shop.utlis import Cart

              
        
def cart(request, product_id):
    cart = Cart(request)

    if Product.objects.filter(id=product_id).exists():
        cart.add(product_id)


    return JsonResponse({"message":  "Savatga qo'shildi", "cart_count": cart.get_count()})

def cart_page(request):
    cart = Cart(request)
    products = cart.get_products()
    data = {
        'path':"Savatcha",
        'cart_count': cart.get_count(),
        'products':products,
        'tot_items': cart.get_count_items()
    }
    return render(request,'shop/cart.html', context=data)



