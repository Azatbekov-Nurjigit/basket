from abc import ABC
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from korzin.models import Bet, History, Shoe, Color, Size

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = 'name color size image description price'.split()

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = '__all__'


class PostValidateSerializer(serializers.Serializer, type(ABC)):
    __metaclass__ = ABC
    name = serializers.CharField(min_length=1, max_length=245)
    color = serializers.CharField(min_length=1, max_length=255)
    size = serializers.IntegerField(min_value=1)
    description = serializers.CharField(required=False, default='No text')

    def validate_size(self, size):
        try:
            Size.objects.get(id=size)
        except size.DoesNotExist:
            raise ValidationError('size not found!')
        return size

    def validate_color(self, tags):  # [1,2]
        filtered_tags = Color.objects.filter(id__in=tags)
        if len(tags) != len(filtered_tags):
            raise ValidationError('color not found!')
        return tags

