from django.urls import path
from .views import *

urlpatterns = [
    path('create_order', create_order, name='create_order'),
    path('created_order', created_order, name='created_order'),
]
