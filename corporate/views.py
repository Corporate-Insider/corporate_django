from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from .models import User, Review, Company
from accounts.serializers import UserSerializer
from .serializers import CompanySerializer, ReviewSerializer

# Create your views here.
@permission_classes((AllowAny, ))
class CompanyView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
@permission_classes((AllowAny, ))
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
@permission_classes((AllowAny, ))
class ReviewView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@permission_classes((AllowAny, ))
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
