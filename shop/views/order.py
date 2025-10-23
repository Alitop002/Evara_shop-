from django.shortcuts import redirect, render
from django.views.generic import View
from shop.views import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from shop.models.order import Order, OrderItem
from shop.telegram import send_message
from asgiref.sync import async_to_sync

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
        order_text = self.get_order_text(items,user, address, additional, order)
        async_to_sync(send_message)(order_text)
        return redirect('dashboard')
    
    def get_order_text(self, items, user, address, additional, order):
        order_text = f"🛍️ Yangi buyurtma!\n\n"
        order_text += f"👤 Foydalanuvchi: {user.username}\n"
        order_text += f"📧 Email: {user.email if user.email else 'Mavjud emas'}\n"
        order_text += f"🏠 Manzil: {address}\n"
        order_text += f"📝 Qo‘shimcha ma’lumot: {additional}\n"
        order_text += f"🕒 Sana: {order.created_at.strftime('%Y-%m-%d %H:%M')}\n"
        order_text += f"📦 Holat: {order.get_status_display()}\n\n"
        order_text += f"🧾 Buyurtma tarkibi:\n"

        total_sum = 0
        for item in items:
            p = item.product
            line = f"— {p.name} | Soni: {item.quantity} | Narx: ${item.total_price}\n"
            order_text += line
            total_sum += item.total_price

        order_text += f"\n💰 Umumiy summa: ${total_sum}"
        return order_text
