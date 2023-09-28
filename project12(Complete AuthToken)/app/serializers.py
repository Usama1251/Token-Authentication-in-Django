from rest_framework import serializers
from django.contrib.auth.models import User


class SignupSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError("Username Already exists!")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(username= validated_data['username'], password=validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data


class SigninSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

class HomeSerializers(serializers.Serializer):
    model: User
