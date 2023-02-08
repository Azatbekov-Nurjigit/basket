from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from korzin.serializer import BasketSerializer, HistorySerializer, ProductSerializer, PostValidateSerializer
from korzin.models import Basket, Product, History


def product_list_view(request):
    if request.method == 'GET':
        post = Product.objects.all().order_by('name')
        serializer = ProductSerializer(post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def basket_post_view(request):
    if request.method == 'POST':
        serializer = PostValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image = serializer.validated_data.get('image')
        name = serializer.validated_data.get('name')
        color = serializer.validated_data.get('color')
        rate = serializer.validated_data.get('rate')
        price = serializer.validated_data.get('price')
        time = serializer.validated_data.get('time')
        basket = Basket.objects.create(image=image, name=name, color=color, rate=rate, price=price, time=time)
        history = History.objects.create(image=image, name=name, color=color, rate=rate, price=price, time=time)
        basket.save()
        history.save()

        return Response(data={'basket': BasketSerializer(basket).data,
                              'history': HistorySerializer(history).data})


def basket_list_view(request):
    if request.method == 'GET':
        post = Basket.objects.order_by('-data')
        serializer = BasketSerializer(post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


def history_list_view(request):
    if request.method == 'GET':
        post = History.objects.order_by('-data')
        serializer = HistorySerializer(post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def basket_delete_view(request, **kwargs):
    try:
        post = Basket.objects.get(id=kwargs['id'])
    except Basket.DoesNotExist:
        return Response(data='error', status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






