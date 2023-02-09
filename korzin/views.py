from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from korzin.serializer import BasketSerializer, HistorySerializer, ProductSerializer, PostValidateSerializer, ColorSerializer
from korzin.models import Bet, Shoe, History, Color

@api_view(['GET'])
def color_list_view(request):
    if request.method == 'GET':
        post = Color.objects.all()
        serializer = ColorSerializer(post, many=True)
        return Response(data=serializer.data)

@api_view(['GET'])
def product_list_view(request):
    if request.method == 'GET':
        post = Shoe.objects.all()
        serializer = ProductSerializer(post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

        # data = {
        #     'serializer': serializer
        # }
        # return render(request, 'products/create.html', context=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def basket_list_view(request):
    if request.method == 'GET':
        post = Bet.objects.all()
        serializer = BasketSerializer(post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)




@api_view(['GET'])

def history_list_view(request):
    if request.method == 'GET':
        post = History.objects.all()
        serializer = HistorySerializer(post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

# order_by('-data')


@api_view(['POST'])
def basket_post_view(request):
    if request.method == 'POST':
        serializer = PostValidateSerializer(data=request.POST)
        serializer.is_valid()
        name = serializer.validated_data.get('name'),
        color = serializer.validated_data.set('color'),
        size = serializer.validated_data.get('size'),
        image = serializer.validated_data.get('image'),
        description = serializer.validated_data.get('description'),
        price = serializer.validated_data.get('price')

        basket = Bet.objects.create(name=name, color=color, size=size, image=image, time=description, price=price)
        history = History.objects.create(name=name, color=color, size=size, image=image, time=description, price=price)
        basket.save()
        history.save()
        print(request.data)
        return Response(data={'OK'})
        # return redirect('/basket_list/')
    else:
        data = {
            'error': 'error'
        }
        return render(request, 'ERROR/eror.html', context=data)


@api_view(['DELETE'])
def basket_delete_view(request, **kwargs):
    try:
        post = Bet.objects.get(id=kwargs['id'])
    except Bet.DoesNotExist:
        return Response(data='error', status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
