from abc import ABC
from rest_framework import serializers
from korzin.models import Basket, History, Product



class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ('id', 'image', 'name', 'color', 'rate', 'price', 'time')


class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = ('id', 'image', 'name', 'color', 'rate', 'price', 'time')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'image', 'name', 'color', 'rate', 'price', 'time')




class PostValidateSerializer(serializers.Serializer, ABC):
    image = serializers.ImageField(required=False, default='No text')
    name = serializers.CharField(min_length=1, max_length=245)
    color = serializers.CharField(min_length=1, max_length=255)
    rate = serializers.IntegerField(min_value=1, max_value=10)
    price = serializers.IntegerField(min_value=1)




