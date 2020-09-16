from rest_framework import serializers
from .models import Company, Review, Rating
from accounts.models import User

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
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
        fields = ('id', 'review','user_id', 'company_id')
        

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        source = 'user'
    )
    company_id = serializers.PrimaryKeyRelatedField(
        queryset = Company.objects.all(),
        source = 'company'
    )
    class Meta:
        model = Rating
        fields = ('id', 'rating','user_id','company_id')
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields =('id', 'name','domain', 'logo','ratings','reviews')