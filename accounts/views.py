from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm




def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'],email=cd['email'],password=cd['password'])
            user.name = cd['name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/user_register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Account logged successfully', 'success')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password', 'error')
    else:
        form = UserLoginForm()

    return render(request, 'accounts/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'User logged successfully', 'success')
    return redirect('home')