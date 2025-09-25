from rest_framework import serializers
from .models import ProductOffer,Lead

class ProductOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOffer
        fields = "__all__"
        
        
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"
        
class LeadUploadSerializer(serializers.Serializer):
    csv_file = serializers.FileField()
    
class ScoringResultSerializer(serializers.Serializer):
    name = serializers.CharField()
    role = serializers.CharField()
    company = serializers.CharField()
    industry = serializers.CharField()
    location = serializers.CharField()
    intent = serializers.CharField()
    score = serializers.IntegerField()
    reasoning = serializers.CharField()