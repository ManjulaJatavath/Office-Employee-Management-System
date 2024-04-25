# views.py
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')  
        password = request.POST.get('pass1')
        confirm_password = request.POST.get('pass2')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('/authapp/signup/')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('/authapp/signup/')
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        messages.success(request, "User created successfully and logged in")
        return redirect('/')
    
    return render(request, 'signup.html')
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')  # Redirect to the homepage or any other page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('index')  # Redirect to the login page after logout
