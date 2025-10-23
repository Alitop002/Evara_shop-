from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from shop.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import View
from shop.utlis import Cart
from shop.models import Order
from django.contrib import messages


class ProfileUserView(LoginRequiredMixin,View):
    def get(self, request):
        cart = Cart(request)
        orders = Order.objects.filter(user=request.user) 
        data = {
            'path': 'Profilim',
            'cart_count':cart.get_count(),
            'orders':orders
            }

        return render(request, "shop/accounts.html", context=data)
    
    def post(self, request):
        user = request.user
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if first_name and last_name:
            user.first_name = first_name 
            user.last_name = last_name
            print(first_name,last_name)
            user.save()
            messages.success(request, "Profil ma'llumotlari yangilandi")
        return redirect("accounts")
    

class ChangePassword(View):
    def post(self, request):
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        conf_password = request.POST.get('conf_password')
        user = request.user
        if user.check_password(old_password) and new_password==conf_password:
            user.set_password(new_password)
            user.save()

        return redirect('login')


class LoginUserView(View):
    def get(self, request):
        form = LoginForm()
        
        data = {'path': 'Login',
                'form': form
                }
        return render(request, "shop/login-register.html", context=data)
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request,user)
                return redirect('dashboard')
        data = {
            'path': 'Login',
            'form': form
            }
        return render(request, "shop/login-register.html", context=data)

        
  

def logout_view(request):
    logout(request)
    return redirect('dashboard')

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
