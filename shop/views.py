from django.shortcuts import redirect, render,get_object_or_404
from shop.models import Category,Product
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def dahsboard(request):
    categories = Category.objects.all()
    produtcs = Product.objects.all()
    data = {
        "categories": categories,
        "produtcs":produtcs
        }
    return render(request, "shop/index.html", context=data)


def detail(request):
    return render(request, "shop/details.html")

@login_required
def accounts(request):
    data = {'path': 'Profilim'}
    return render(request, "shop/accounts.html", context=data)

def cart(request):
    return render(request, "shop/cart.html")

def checkout(request):
    return render(request, "shop/checkout.html")

def compare(request):
    data = {'path': 'Compare'}
    return render(request, "shop/compare.html", context=data)

def login_reg(request):
    data = {'path': 'Login'}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
    return render(request, "shop/login-register.html", context=data)

def shop(request):
    products = Product.objects.all()

    data = {'path': 'Mahsulotlar',
            'products':products
            }
    return render(request, "shop/shop.html", context=data)

def wishilst(request):
    return render(request, "shop/wishlist.html")

def logout_view(request):
    logout(request)
    return redirect('dashboard')

def get_product_view_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    category =  get_object_or_404(Category, id=category_id)
    
    data = {
        'path': category.name,
        'products': products 
    }
    return render(request, "shop/category-product.html", context=data)    