from django.shortcuts import redirect, render,get_object_or_404
from shop.models import Category,Product
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import RegisterForm, LoginForm




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
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request,user)
                return redirect('dashboard')
            
    form = LoginForm()
        
    data = {'path': 'Login',
            'form': form
            }
    return render(request, "shop/login-register.html", context=data)

def shop(request):
    products = Product.objects.all()
    paginator = Paginator(products, 2)

    page = request.GET.get('page')

    page_products = paginator.get_page(page)


    data = {'path': 'Mahsulotlar',
            'products': page_products
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


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User(first_name=first_name, last_name=last_name, username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect('login')
        
        
    form = RegisterForm()
    data = {
        'path': 'Register',
        'form': form
    }
    return render(request, "shop/register.html", context=data)
        