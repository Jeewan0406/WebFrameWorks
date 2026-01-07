# myfirstproject/urls.py
from django.contrib import admin
from django.urls import path, include # <--- Make sure to add include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')), # <--- This points to your app
]