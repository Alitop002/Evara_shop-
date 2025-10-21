from django.shortcuts import render
from django.views.generic import View
from shop.views import Cart

class GetChekoutPageView(View):
    def get(self, request):
        cart = Cart(request)
        data = {
            'path': 'Chekout',
            'cart_count': cart.get_count()
        }
        return render(request, "shop/chekout.html", context=data)
