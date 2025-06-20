from django.urls import path
from  .views import base, contact_lst, contact_detail

urlpatterns = [
    path('#', base,name='base'),
    path('', contact_lst, name='contact_list'),
    path('contact/<int:id>',contact_detail, name='contact_detail'),
]