from django.shortcuts import render
from .models import Product

def index_html(request):
    product = Product.objects.all()
    return render(request, 'myapp/index.html', context={'products': product})
    
def create_html(request):
    name = request.GET.get('name')
    description = request.GET.get('description')
    amout = request.GET.get('amout')
    price = request.GET.get('price')
    if name and description and amout and price:
        product =Product(name=name, description=description, amout=amout, price=price)
        product.save()
        return render(request, 'myapp/create.html', context={'message': "Product yaratildi"})
    
    else: 
        return render(request, 'myapp/create.html', context={'message': "Create bo‘lmadi, barcha maydonlarni yuboring"})
    
def detail_html(request, pro_id):
    pro_id = int(pro_id)
    pro = Product.objects.get(id=pro_id)
    
    return render(request, "myapp/detail.html", context={'pro':pro})

def delete_html(request, pro_id):
    try:
        pro = Product.objects.get(id=pro_id)
        pro.delete()
        return render(request, 'myapp/delete.html', context={'message': 'Product Deleted ✔'})
    except Product.DoesNotExist:
        return render(request, 'myapp/delete.html', context={'message': '❌ Bu ID bilan product topilmadi'})
