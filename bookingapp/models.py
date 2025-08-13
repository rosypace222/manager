from django.contrib.auth.models import User
from django.db import models

from booking import settings

# Модель для категорій номерів (наприклад, люкс, стандарт)
class Category(models.Model):
    # Назва категорії (наприклад, "Люкс", "Стандарт")
    title = models.CharField(max_length=100)

    def __str__(self):
        # Повертає назву категорії для відображення у списках
        return  self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ["title"]

# Модель для готельних номерів
class Room(models.Model):
    # Номер кімнати (наприклад, 101)
    numbers = models.IntegerField(verbose_name="Номер")
    # Кількість осіб, які можуть проживати у номері
    capacity = models.IntegerField(verbose_name="Місткість")
    # Опис кімнати (зручності, особливості)
    description = models.TextField(verbose_name="Опис")
    # Категорія кімнати (зв'язок з моделлю Category)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='rooms', verbose_name="Категорія" )
    # Вартість проживання за добу
    price = models.IntegerField(verbose_name="Ціна")
    # Зображення кімнати
    image = models.ImageField(verbose_name="Зображення", upload_to='rooms', null=True)

    def __str__(self):
        # Повертає номер кімнати для відображення у списках
        return f'{self.numbers}'

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номери'
        ordering = ["numbers"]

# Модель для бронювання номерів
class Booking(models.Model):
    # Користувач, який здійснив бронювання
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', verbose_name="Клієнт")
    # Заброньований номер (зв'язок з Room)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings', verbose_name="Номер")

    # Дата та час заїзду
    check_in = models.DateTimeField(verbose_name="Дата заїзду")
    # Дата та час виїзду
    check_out = models.DateTimeField(verbose_name="Дата виїзду")

    # Контактний телефон клієнта
    phone = models.CharField(max_length=14)
    # Дата та час створення бронювання (автоматично)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Повертає інформацію про бронювання для відображення у списках
        return f'{self.client} -  номер {self.room}'

    class Meta:
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'
        ordering = ["creation_time"]

