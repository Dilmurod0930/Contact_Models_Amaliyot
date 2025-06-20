from django.urls import path
from  .views import base, contact_lst

urlpatterns = [
    path('#', base,name='base'),
    path('', contact_lst, name='contact_list'),
]