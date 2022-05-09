from django.contrib import admin
from django.urls import path
from polling_magic.views import say_hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', say_hello, name='hello'),
]
