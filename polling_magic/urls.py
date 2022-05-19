from . import views
from django.urls import path

urlpatterns = [
    path('', views.PollList.as_view(), name='home')
]
