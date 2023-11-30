from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('info/', info, name='info'),
    path('contacts/', contacts, name='contacts'),
    path('registrate/', registrate, name='registrate'),
]
