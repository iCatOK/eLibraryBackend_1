from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import models
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('full_name', 'branch', 'status',)

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ('username', 'profile',)

"""
class RegistrationSerializer(models.ModelSerializer):
    username = serializers.CharField(required=True, write_only=True)
    surname = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                ("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'name': self.validated_data.get('name', ''),
            'surname': self.validated_data.get('surname', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])

        user.save()
        return user
"""