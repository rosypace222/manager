from django.contrib import admin

from bookingapp.models import Category, Room, Booking

# Адмін-налаштування для моделі Booking
class BookingAdmin(admin.ModelAdmin):
    # Відображати ці поля у списку бронювань
    list_display = ("id", "client", "room", "check_in", "check_out", "phone", "creation_time")
    # Які поля є посиланнями для переходу до детальної інформації
    list_display_links = ("id", "client", "room", "check_in", "check_out", "phone", "creation_time")

# Адмін-налаштування для моделі Room
class RoomAdmin(admin.ModelAdmin):
    # Відображати ці поля у списку номерів
    list_display = ("id", "numbers", "capacity", "price", "description")
    # Які поля є посиланнями для переходу до детальної інформації
    list_display_links = ("id", "numbers", "capacity", "price")

# Реєстрація моделей у адмін-панелі
admin.site.register(Category)  # Категорії номерів
admin.site.register(Room, RoomAdmin)  # Номери з кастомним адмініструванням
admin.site.register(Booking, BookingAdmin)  # Бронювання з кастомним адмініструванням

