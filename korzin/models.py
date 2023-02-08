from django.db import models


class Basket(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10000, decimal_places=1, related_name='baskets')

    @property
    def products_price(self):
        lists = [basket.price for basket in self.baskets.all()]
        return sum(lists) if len(lists) != 0 else "error"



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