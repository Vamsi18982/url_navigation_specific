from django.urls import path
from drinks.views import *
app_name='drinks'
urlpatterns = [
    path('cocacola/',cocacola,name='cocacola'),
    path('cocacola_response/',cocacola_response,name='cocacola_response')
]
