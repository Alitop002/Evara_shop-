from django.shortcuts import redirect, render
from django.views.generic import View
from shop.views import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from shop.models.order import Order, OrderItem

class GetChekoutPageView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        products = cart.get_products()
        data = {
            'path': 'Chekout',
            'cart_count': cart.get_count(),
            'products':products
        }
        return render(request, "shop/checkout.html", context=data)
    def post(self, request):
        user = request.user
        cart = Cart(request)
        products = cart.get_products()
        address = request.POST.get('address', 'mavjud emas')
        additional = request.POST.get('additional', 'mavjud emas')

        items = []

        for product in products['products']:
            item,created = OrderItem.objects.get_or_create(
                product=product['data'],
                quantity=product['quantity'],
                total_price=product['total']
            )
            items.append(item)

        order=Order(user=user, address=address, additional=additional)
        order.save()
        order.items.add(*items)
        cart.clear()



        return redirect('dashboard')