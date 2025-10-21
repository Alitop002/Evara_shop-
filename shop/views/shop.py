from django.shortcuts import get_object_or_404, redirect, render
from shop.models import Category, Product
from django.core.paginator import Paginator
from .cart import Cart
from django.db.models import Q


def dahsboard(request):
    categories = Category.objects.all()
    produtcs = Product.objects.all()
    cart = Cart(request)
    data = {
        "categories": categories,
        "produtcs":produtcs,
        "cart_count":cart.get_count()
        }
    return render(request, "shop/index.html", context=data)


def detail(request):
    return render(request, "shop/details.html")

def compare(request):
    data = {'path': 'Compare'}
    return render(request, "shop/compare.html", context=data)


def shop(request):
    products = Product.objects.all()

    q = request.GET.get('q')
    if q:
        products = Product.objects.filter(Q(name__icontains=q) | Q(description__contains=q))

    paginator = Paginator(products, 2)
    cart = Cart(request)
    page = request.GET.get('page')

    page_products = paginator.get_page(page)

   
 

    data = {'path': 'Mahsulotlar', 
            'products': page_products,
            'cart_count':cart.get_count(),
            'count': products.count()
            }
    return render(request, "shop/shop.html", context=data)

def get_product_view_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    category =  get_object_or_404(Category, id=category_id)
    
    data = {
        'path': category.name,
        'products': products 
    }
    return render(request, "shop/category-product.html", context=data)    

   
