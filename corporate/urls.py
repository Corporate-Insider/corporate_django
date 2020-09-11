from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
import os
from rest_framework_jwt.views import obtain_jwt_token

api_key = os.environ['API_KEY']

urlpatterns = [
    path('companies/', views.CompanyView.as_view(), name='company_list'),
    path('reviews/', views.ReviewView.as_view(), name='review_list'),
    path(f'companies/<int:pk>/{api_key}', views.CompanyDetail.as_view(), name='company_detail'),
    path(f'reviews/<int:pk>/{api_key}', views.ReviewDetail.as_view(), name='review_detail'),
    path('token-auth/', obtain_jwt_token)
]
