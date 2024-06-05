from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from .forms import UserRegisterForm, UserLoginFrom
from .utils import user_additional_models


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)

                user_additional_models(request)

                messages.success(request, 'You successfully registered!')
                return redirect('home')
            else:
                messages.error(request, 'Registration error.')
        else:
            form = UserRegisterForm()
        return render(request, 'user/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserLoginFrom(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)

                user_additional_models(request)

                messages.success(request, f'Welcome back {str(request.user.username).title()}. You successfully logged in!')
                return redirect('home')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
        else:
            form = UserLoginFrom()
        return render(request, 'user/login.html', {'form': form})


def logout(request):
    logout(request)
    return redirect('login')
