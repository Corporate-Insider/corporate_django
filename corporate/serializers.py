from rest_framework import serializers
from .models import User, Company, Review

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    review_url = serializers.ModelSerializer.serializer_url_field(view_name='review_detail')

    company = serializers.HyperlinkedRelatedField(
        view_name='company_detail',
        read_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        source = 'user'
    )
    company_id = serializers.PrimaryKeyRelatedField(
        queryset = Company.objects.all(),
        source = 'company'
    )
    class Meta:
        model = Review
        fields = ('id', 'review','rating','rated','review_url','user_id','company', 'company_id')
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
  
    class Meta:
        model = User
        fields = ('id', 'name','email', 'password', 'reviews')


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    url = serializers.ModelSerializer.serializer_url_field(view_name='company_detail')

    class Meta:
        model = Company
        fields =('id', 'name','domain', 'logo','reviews','url')
