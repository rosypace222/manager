from django.contrib import admin
from .models import Booking

# Реєстрація моделі Booking в адміністративній панелі Django
admin.site.register(Booking)