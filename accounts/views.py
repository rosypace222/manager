from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Функція для реєстрації нового користувача
def register(request):
    # Якщо форма відправлена (POST)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # Перевіряємо валідність форми
        if form.is_valid():
            user = form.save()  # Створюємо нового користувача
            login(request, user)  # Автоматично входимо після реєстрації
            return redirect('index')  # Перенаправляємо на головну
    else:
        form = UserCreationForm()  # Порожня форма для GET-запиту

    # Відображаємо сторінку реєстрації з формою
    return render(request, 'accounts/register.html', context={
        'form':form,
    })

# Функція для авторизації користувача
def login_view(request):
    # Якщо форма відправлена (POST)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        # Перевіряємо валідність форми
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Аутентифікуємо користувача
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Вхід у систему
                return redirect('index')  # Перенаправлення на головну
    else:
        form = AuthenticationForm()  # Порожня форма для GET-запиту

    # Відображаємо сторінку входу з формою
    return render(request, 'accounts/login.html', context={
        'form':form,
    })

# Функція для виходу користувача з системи
def logout_view(request):
    # Якщо користувач авторизований, виконуємо вихід
    if request.user.is_authenticated:
        logout(request)

    # Перенаправляємо на сторінку входу
    return redirect('login')