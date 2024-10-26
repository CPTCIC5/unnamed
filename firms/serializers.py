from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Firm,Entity

class CreateFirmSerialzer(serializers.ModelSerializer):
    class Meta:
        model= Firm
        fields= ['name' ,'address' ,'contact_number' ,'email' ,'website_url']

class FirmSerializer(serializers.ModelSerializer):
    root_user = UserSerializer()
    members = UserSerializer(many=True)  # Ensure this is correct for your use case
    class Meta:
        model = Firm
        fields = ['id', 'root_user', 'name', 'address', 'contact_number', 'email', 'website_url', 'members', 'created_at']



class CreateEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model= Entity
        fields= ['firm', 'name', 'industry_type', 'entity_type', 'gstin', 'pan_number','city', 'zipcode']

class EntitySerializer(serializers.ModelSerializer):
    firm= FirmSerializer()

    class Meta:
        model= Entity
        fields= ['id','firm', 'name', 'industry_type', 'entity_type', 'gstin', 'pan_number','city', 'zipcode', 'created_at']
