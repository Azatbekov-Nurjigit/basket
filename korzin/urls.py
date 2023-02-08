from django.urls import path
from korzin.views import  product_list_view, basket_list_view, history_list_view, basket_post_view, basket_delete_view

urlpatterns = [
    path('product_list/', product_list_view),
    path('basket_list/', basket_list_view),
    path('history_list/', history_list_view),
    path('basket_post/', basket_post_view),
    path('basket_delete/', basket_delete_view),
]







