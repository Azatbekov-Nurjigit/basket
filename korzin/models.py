from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=1)
    color = models.CharField(max_length=500)
    price = models.FloatField()
    time = models.DateTimeField()


class Basket(models.Model):
    name = models.CharField(max_length=265)
    image = models.ImageField(null=True, blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=1)
    color = models.CharField(max_length=500)
    price = models.FloatField()
    time = models.DateTimeField()


class History(models.Model):
    name = models.CharField(max_length=260)
    image = models.ImageField(null=True, blank=True)
    rate = models.PositiveIntegerField(null=True, default=0)
    color = models.CharField(max_length=500)
    price = models.FloatField()
    time = models.DateTimeField()





# Главная страница
# • детальный обзор продукта
# • категория
# • поиск
#
# Регистрация
# • регистрация
# • авторизация
# • выход
# • смена пароля
#
# Админпанель
#
# Личный кабинет
# • личные данные
# • контакты
# • история заказов
# • корзина

# Доставка
# • способ оплаты
# • статусы заказа