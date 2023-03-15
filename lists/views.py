from django.shortcuts import render, redirect
from django.urls import resolve

from lists.models import Item


def home_page(request):

    if request.method == 'POST':
        Item.objects.create(text=request.POST.get('item_text', ''))
        return redirect('/lists/shared/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})


def shared_page(request):
    items = Item.objects.all()
    return render(request, 'shared.html', {'items': items})


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/shared/')
