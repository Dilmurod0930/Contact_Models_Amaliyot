from django.shortcuts import render

from .models import Contacts


# Create your views here.

def base(request):
    return render(request, 'contact/base.html')

def  contact_lst(request):
    contacts = Contacts.objects.all()
    context = {'contacts': contacts}
    return render(request, 'contact/list.html', context = context)