from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data["phone"]
            password = form.cleaned_data["password"]
            user = authenticate(request, phone=phone, password=password)
            if user:
                login(request, user)
                return redirect("home")  # Замените 'home' на URL вашей главной страницы
            else:
                messages.error(request, "Неверный телефон или пароль")
    else:
        form = LoginForm()
    return render(request, "auth/login.html", {"form": form})


def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.username = form.cleaned_data['phone']
            user.save()
            login(request, user)
            return redirect("home")  # Замените 'home' на URL вашей главной страницы
    else:
        form = RegistrationForm()
    return render(request, "auth/registration.html", {"form": form})


@login_required
def profile_view(request):
    return render(request, "auth/profile.html", {"user": request.user})