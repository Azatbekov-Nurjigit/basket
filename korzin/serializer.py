from rest_framework import serializers
from korzin.models import Basket
from rest_framework.exceptions import ValidationError
from abc import ABC, ABCMeta


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ('name', 'price', 'products_price',)



class BasketValidateSerializer(serializers.Serializer, metaclass=ABCMeta):
    name = serializers.CharField(max_length=255, required=True)





