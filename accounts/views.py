from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib import messages

def user_login(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html')
    
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(username = username, password = password)

    if user is None:
        messages.warning(request, "O campos estão inválidos ou o usuario não existe!")
        return redirect("user_login")
    
    login(request, user)
    return redirect("my_courses")
    
def user_register(request):
    if request.method == "GET":
        return render(request, 'accounts/register.html')
    
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    confirm_pass = request.POST.get("confirm_pass")
    role = request.POST.get("profile")

    if password != confirm_pass:
        messages.warning(request, "As senhas não coincidem!")
        return redirect("user_register")
    
    if not User.objects.filter(username = username ).exists():
        
        user = User.objects.create_user(username=username, email=email, password=password)
        profile = Profile.objects.get(user = user)
        profile.role = role
        profile.save()

        return redirect("user_login")
    
    messages.warning(request, "O nome de usuario já está em uso.")
    return redirect("user_register")

def user_logout(request):
    logout(request)
    return redirect("user_login")