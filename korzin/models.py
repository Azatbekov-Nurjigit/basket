from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=100)

class Size(models.Model):
    name = models.IntegerField(max_length=100)

class Bet(models.Model):
    name = models.CharField(max_length=255)
    color = models.ManyToManyField(Color, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.FloatField()

class History(models.Model):
    name = models.CharField(max_length=245)
    color = models.ManyToManyField(Color, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE,
                                 null=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.FloatField()

class Shoe(models.Model):
    name = models.CharField(max_length=265)
    color = models.ManyToManyField(Color, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.FloatField()





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