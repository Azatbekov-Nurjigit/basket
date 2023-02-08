from korzin.serializer import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from korzin.models import Basket
from django.db import transaction


@api_view(['GET', 'POST'])
def basket_list_view(request):
    if request.method == 'GET':
        directs = Basket.objects.all()
        serializer = BasketSerializer(directs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BasketSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        name = serializer.validated_data.get("name")
        price = serializer.validated_data.get("price")
        directs = Basket.objects.create(name=name, price=price)
        directs.save()
        return Response(data={'products': BasketSerializer(directs).data})







@api_view(['GET', 'DELETE', 'PUT'])
def basket_detail_view(request, **kwargs):
    try:
        directs = Basket.objects.get(id=kwargs['id'])
    except Basket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Post not found!'})
    if request.method == 'GET':
        serializer = BasketSerializer(directs, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        directs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = BasketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get("name")
        price = serializer.validated_data.get("price")
        directs = Basket.objects.create(name=name, price=price)
        directs.save()
        return Response(data={'post': BasketSerializer(directs).data})


