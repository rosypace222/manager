from django.db import models

# Модель для зберігання інформації про бронювання
class Booking(models.Model):
    # Ім'я користувача, який зробив бронювання
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # Дата та час початку бронювання
    start_time = models.DateTimeField()
    # Дата та час завершення бронювання
    end_time = models.DateTimeField()
    # Дата створення запису про бронювання
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Повертає рядкове представлення бронювання
        return f"{self.user} - {self.start_time} до {self.end_time}"