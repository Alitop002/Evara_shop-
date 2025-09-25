from django.urls import path
from .views import dahsboard,detail,accounts,cart,checkout,compare,login,shop,wishilst

urlpatterns = [
    path('', dahsboard, name='dashboard'),
    path('detail/', detail, name='detail'),
    path('accounts/', accounts, name='accounts'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('compare/', compare, name='compare'),
    path('login/', login, name='login'),
    path('shop/', shop, name="shop"),
    path('wishlist/',wishilst,name="wishlist")

]
