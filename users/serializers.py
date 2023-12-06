from rest_framework import serializers
from django.contrib.auth.models import User

from users.models import UserProfile


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('user', 'avatar')

    def update(self, instance, validated_data):
        # 只允许更新 avatar 字段
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance
