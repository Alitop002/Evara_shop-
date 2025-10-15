from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from shop.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


@login_required
def accounts(request):
    data = {'path': 'Profilim'}
    return render(request, "shop/accounts.html", context=data)



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
        
    form = RegisterForm()
    data = {
        'path': 'Register',
        'form': form
    }
    return render(request, "shop/register.html", context=data)