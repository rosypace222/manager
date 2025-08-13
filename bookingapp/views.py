from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from bookingapp.models import Room


# Create your views here.

# Головна сторінка з фільтрацією номерів за параметрами
def main_page(request):
    # Отримуємо всі номери
    rooms = Room.objects.all()

    # Якщо запит GET, отримуємо параметри фільтрації з форми
    if request.method == "GET":
        start_date = request.GET.get('start_date')  # Дата заїзду
        end_date = request.GET.get('end_date')      # Дата виїзду
        quantity = request.GET.get('quantity')      # Кількість осіб
        price_from = request.GET.get('price_from')  # Мінімальна ціна
        price_to = request.GET.get('price_to')      # Максимальна ціна

        # Фільтрація номерів за датами (виключає зайняті)
        if start_date and end_date:
            rooms = Room.objects.exclude(bookings__check_in__lt = end_date, bookings__check_out__gt = start_date)

        # Додатково можна додати фільтрацію за кількістю осіб та ціною
        # ... (не реалізовано)

    # Формуємо контекст для шаблону
    context = {
        'rooms': rooms,
        'start_date': start_date,
        'end_date': end_date,
        'quantity': quantity,
        'price_from': price_from,
        'price_to': price_to
    }

    # Відображаємо головну сторінку з результатами пошуку
    return render(request, template_name="bookingapp/index.html", context=context)

# Відображення списку всіх номерів
def room_list(request):
    # Отримуємо всі номери
    rooms = Room.objects.all()

    context = {
        'rooms': rooms,
    }
    # Відображаємо сторінку зі списком номерів
    return render(request, template_name="bookingapp/room_list.html", context=context)

# Сторінка бронювання номера (доступна лише авторизованим користувачам)
@login_required(login_url='/login/')
def book_room(request):
    # Отримуємо параметри з GET-запиту
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    room_id = request.GET.get('room_id')

    # Отримуємо об'єкт кімнати або 404, якщо не знайдено
    room = get_object_or_404(Room, id=room_id)

    context = {
        'room': room,
        'start_date': start_date,
        'end_date': end_date,
    }
    # Відображаємо сторінку бронювання
    return render(request, template_name="bookingapp/booking.html", context=context)


