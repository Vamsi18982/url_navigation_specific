from django.urls import path
from food.views import *
app_name='food'
urlpatterns = [
    path('biriyani/',biriyani,name='biriyani'),
    path('biriyani_response/',biriyani_response,name='biriyani_response')
]
