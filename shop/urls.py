from django.urls import path
from .views import dahsboard,detail,accounts,cart,checkout,compare,login_reg,shop,wishilst,logout_view,get_product_view_category,register_user

urlpatterns = [
    path('', dahsboard, name='dashboard'),
    path('detail/', detail, name='detail'),
    path('profile/', accounts, name='accounts'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('compare/', compare, name='compare'),
    path('login/', login_reg, name='login'),
    path('shop/', shop, name="shop"),
    path('wishlist/',wishilst,name="wishlist"),
    path('logout/', logout_view, name='logout'),
    path('category/<int:category_id>/', get_product_view_category, name='category_prod'),
    path('register/', register_user, name='register'),

]
