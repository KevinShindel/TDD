from django.contrib import admin
from django.urls import path
from lists.views import home_page, shared_page

urlpatterns = [
    path('', home_page),
    path('lists/shared/', shared_page),
    path('admin/', admin.site.urls),
]
