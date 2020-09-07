from django.urls import path
from .views import current_user, UserCreate, UserView
import os
api_key = os.environ['API_KEY']

urlpatterns = [
    path('current_user/', current_user),
    path('create_user/', UserCreate.as_view()),
    path(f'users/{api_key}', UserView.as_view()),
]