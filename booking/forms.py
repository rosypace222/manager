from django import forms
from .models import Booking

# Форма для створення та редагування бронювання
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        # Поля, які будуть відображатися у формі
        fields = ['user', 'start_time', 'end_time']