from django.contrib import admin
from django.urls import path
from lists.views import home_page, shared_page, new_list

urlpatterns = [
    path('', home_page, name='home'),
    path('lists/shared/', shared_page, name='shared'),
    path('lists/new', new_list, name='new_list'),
    path('admin/', admin.site.urls),
]
