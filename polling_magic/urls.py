from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PollList.as_view(), name='home'),
    path('home', views.home),
    path('poll/<int:id>/', views.view_poll, name='view_poll'),
    path('like/<int:id>', views.poll_like, name='poll_like'),
    path('dislike/<int:id>', views.poll_dislike, name='poll_dislike'),
    path('accounts/', include('allauth.urls')),
    path(
        'poll/edit/<int:p_id>/<int:c_id>/',
        views.edit_comment, name='edit_comment'),
    path(
        'poll/delete/<int:p_id>/<int:c_id>/',
        views.delete_comment, name='delete_comment'),
]
