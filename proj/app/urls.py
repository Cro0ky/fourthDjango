from django.urls import path
from .views import *


urlpatterns = [
    path('main/', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('user/<int:id>/', client, name='client'),
    path('users', clientView, name='clientView')
]
