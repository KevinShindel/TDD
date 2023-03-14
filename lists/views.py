from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        text = request.POST.get('item_text', '')
        Item.objects.create(text=text)
        return redirect('/lists/shared/')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})


def shared_page(request):
    items = Item.objects.all()
    return render(request, 'shared.html', {'items': items})
