from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

# Представлення для відображення списку всіх бронювань
def booking_list(request):
    # Отримуємо всі бронювання з бази даних
    bookings = Booking.objects.all()
    # Відображаємо шаблон зі списком бронювань
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

# Представлення для створення нового бронювання
def booking_create(request):
    # Якщо запит POST, обробляємо дані форми
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Зберігаємо нове бронювання
            form.save()
            return redirect('booking_list')
    else:
        # Якщо GET-запит, створюємо порожню форму
        form = BookingForm()
    # Відображаємо шаблон з формою бронювання
    return render(request, 'booking/booking_form.html', {'form': form})