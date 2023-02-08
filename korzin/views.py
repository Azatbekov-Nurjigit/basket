from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from korzin.serializer import BasketSerializer, HistorySerializer, ProductSerializer, PostValidateSerializer
from korzin.models import Bet, Shoe, History


def product_list_view(request):
    if request.method == 'GET':
        post = Shoe.objects.all().order_by('name')
        serializer = ProductSerializer(post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def basket_post_view(request):
    if request.method == 'POST':
        serializer = PostValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = request.data.get('name')
        color = request.data.get('color')
        size = request.data.get('size')
        image = request.data.get('image')
        description = request.data.get('description')
        price = request.data.get('price')
        basket = Bet.objects.create(name=name, color=color, size=size, image=image, time=description, price=price)
        history = History.objects.create(name=name, color=color, size=size, image=image, time=description, price=price)
        basket.save()
        history.save()

        return Response(data={'basket': BasketSerializer(basket).data,
                              'history': HistorySerializer(history).data})


def basket_list_view(request):
    if request.method == 'GET':
        post = Bet.objects.order_by('-data')
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
        post = Bet.objects.get(id=kwargs['id'])
    except Bet.DoesNotExist:
        return Response(data='error', status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
