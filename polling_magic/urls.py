from . import views
from django.urls import path, include
# from .views import AddCommentView

urlpatterns = [
    path('', views.PollList.as_view(), name='home'),
    path('poll/<int:id>/', views.view_poll, name='view_poll'),
    path('accounts/', include('allauth.urls')),
    path('home', views.home),
    # path('poll/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
