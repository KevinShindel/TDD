
from django.shortcuts import render


# def home_page(request):
#     from django.http import HttpResponse
#     return HttpResponse('<html><title>To-Do lists</title></html>')

def home_page(request):
    return render(request, 'home.html')
