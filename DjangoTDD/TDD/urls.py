from django.contrib import admin
from django.urls import path

from lists.views import new_list, view_list, add_item, home_page

urlpatterns = [
    path('', home_page),
    path('lists/new', new_list, name='new_list'),
    path('lists/<int:list_id>/', view_list, name='view_list'),
    path('lists/<int:list_id>/add_item', add_item, name='add_item'),
    path('admin/', admin.site.urls),
]
