from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
import os
from rest_framework_jwt.views import obtain_jwt_token
import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
api_key = env('API_KEY')

urlpatterns = [
    path('companies/', views.CompanyView.as_view(), name='company_list'),
    path('reviews/', views.ReviewView.as_view(), name='review_list'),
    path('ratings/', views.RatingView.as_view(), name='rating_list'),
    path(f'companies/<int:pk>/{api_key}', views.CompanyDetail.as_view(), name='company_detail'),
    path(f'reviews/<int:pk>/{api_key}', views.ReviewDetail.as_view(), name='review_detail'),
    path(f'ratings/<int:pk>/{api_key}', views.RatingDetail.as_view(), name='rating_detail'),
    path('token-auth/', obtain_jwt_token)
]
