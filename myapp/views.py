from django.shortcuts import render,redirect
from .models import Customer

def indexx(request):
    customers = Customer.objects.all()
    return render(request, "myapp/index.html", context={"customers":customers})


def create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        custom = Customer(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address)
        custom.save()
        return redirect('index')
    
    return render(request, "myapp/create.html")

def delete(request, c_id):
    custom = Customer.objects.get(id=c_id)
    custom.delete()
    return redirect('index')
