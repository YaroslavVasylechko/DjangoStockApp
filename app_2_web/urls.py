from django.urls import  path, include

from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('addfirminfo/', add_firm_info, name='addfirminfo'),
    path('getfirminfo/', get_firm_info, name='getfirminfo'),
]