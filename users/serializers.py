from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password= serializers.CharField(required=True, write_only=True)
    class Meta:
        model= User
        fields= ['username','password','confirm_password']    

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create(username=validated_data['username'], password= validated_data['password'])    


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields= ['id', 'user']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model= User
        fields= ['id', 'username', 'profile']


    def update(self, instance, validated_data):
        profile_data= validated_data.pop('profile', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update or create profile related to the user
        if profile_data:
            profile_instance, _ = Profile.objects.update_or_create(user=instance, defaults=profile_data)
            # Update profile instance with nested serializer data
            ProfileSerializer(profile_instance, data=profile_data, partial=True).is_valid(raise_exception=True)
            profile_instance.save()
        return instance



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True,write_only=True)
    new_password = serializers.CharField(required=True,write_only=True)
    confirm_new_password= serializers.CharField(required=True,write_only=True)