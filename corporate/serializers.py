from rest_framework import serializers
from .models import Company, Review
from accounts.models import User

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
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
        fields = ('id', 'review','rating','rated','user_id','company', 'company_id')
        
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields =('id', 'name','domain', 'logo','reviews')
