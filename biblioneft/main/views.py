import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, BookForm
from django.contrib import messages
from .models import Book


def index(request):
    books = Book.objects.exclude(image_book__isnull=True).exclude(image_book__exact='')
    return render(request, 'main/index.html', {'books': books})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data["phone"]
            password = form.cleaned_data["password"]
            user = authenticate(request, phone=phone, password=password)
            if user:
                login(request, user)
                return redirect("profile")  # Замените 'home' на URL вашей главной страницы
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
            return redirect("profile")  # Замените 'home' на URL вашей главной страницы
    else:
        form = RegistrationForm()
    return render(request, "auth/registration.html", {"form": form})


@login_required
def profile_view(request):
    """
    Отображает профиль пользователя и форму добавления книги.
    """
    form = BookForm()  # Пустая форма для добавления книги
    return render(request, "auth/profile.html", {"user": request.user, 'form': form})


@login_required
def add_book_view(request):
    """
    Обрабатывает добавление новой книги.
    """
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)  # Важно:  request.FILES для обработки файлов!
        if form.is_valid():
            book = form.save(commit=False)  # Сначала создаем объект, но не сохраняем в БД

            # Создаем папку для книги
            book_folder = generate_book_folder(book.title, book.author)  # вызов функции для формирования названия папки
            book.image_book.field.upload_to = os.path.join('book', book_folder)
            book.file_book.field.upload_to = os.path.join('book', book_folder)

            book.added_by = request.user  # Устанавливаем текущего пользователя как автора
            book.save()  # Теперь сохраняем объект в БД
            return redirect('profile')  # Перенаправляем на страницу профиля (или список книг)
        else:
            # Если форма не валидна, возвращаем ее обратно в шаблон с ошибками.
            return render(request, "auth/profile.html", {"user": request.user, 'form': form})
    else:
        # Если это GET-запрос, возвращаем пустую форму (это не должно происходить, т.к. форма на странице профиля).
        return redirect('profile')  # или raise Http404("Method not allowed")


def generate_book_folder(title, author):
    """
    Генерирует имя папки для книги на основе названия и автора.
    Очищает название и автора от недопустимых символов и объединяет их.
    """
    title = "".join(x for x in title if x.isalnum())  # Удаляем не-буквенно-цифровые символы
    author = "".join(x for x in author if x.isalnum())
    return f"{title}_{author}"

# def add_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')  # Перенаправляем на страницу со списком книг
#     else:
#         form = BookForm()
#
#     return render(request, 'auth/profile.html', {'form': form})


def chit_zal(request):
    return render(request, 'pages/chit-zal.html')


def office(request):
    return render(request, 'pages/office.html')


def lecktoriy(request):
    return render(request, 'pages/lecktoriy.html')


def cafe(request):
    return render(request, 'pages/cafe.html')


def book_list(request):
    books = Book.objects.exclude(image_book__isnull=True).exclude(image_book__exact='')
    return render(request, 'pages/book_list.html', {'books': books})