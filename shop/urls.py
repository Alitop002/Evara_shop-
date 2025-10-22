from django.urls import path
from shop.views import dahsboard,detail,accounts,cart,compare,login_reg,shop,logout_view,get_product_view_category,register_user,cart_page,wishilst,GetChekoutPageView
urlpatterns = [
    path('', dahsboard, name='dashboard'),
    path('detail/', detail, name='detail'),
    path('profile/', accounts, name='accounts'),
    path('cart/add/<int:product_id>/', cart, name='cart'),
    path('compare/', compare, name='compare'),
    path('login/', login_reg, name='login'),
    path('shop/', shop, name="shop"),
    path('logout/', logout_view, name='logout'),
    path('category/<int:category_id>/', get_product_view_category, name='category_prod'),
    path('register/', register_user, name='register'),
    path('getcart/', cart_page, name='cart_page'),
    path('wishlist/', wishilst, name='wishlist'),

    # Chekout
    path('checkout/', GetChekoutPageView.as_view(), name='checkout')

 



]
