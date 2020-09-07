from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
import os
from rest_framework_jwt.views import obtain_jwt_token

api_key = os.environ['API_KEY']

urlpatterns = [
    # path(f'users/key={api_key}', views.UserView.as_view(), name='user_list'),
    path('companies/', views.CompanyView.as_view(), name='company_list'),
    path('reviews/', views.ReviewView.as_view(), name='review_list'),
    # path(f'users/<int:pk>/key={api_key}', views.UserDetail.as_view(), name='user_detail'),
    path('companies/<int:pk>', views.CompanyDetail.as_view(), name='company_detail'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
    path('token-auth/', obtain_jwt_token)
]
