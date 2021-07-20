from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout


def index(request):
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'app1/index.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'app1/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You are successfully registered.')
            return redirect('index')
        else:
            messages.error(request, 'Registration failed.')
    else:
        form = UserRegisterForm()
    return render(request, 'app1/register.html', {"form": form})
