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
        fields = (
            'user', 'avatar', 'nickname', 'gender', 'phone', 'occupation', 'signature', 'age', 'email', 'location',
            'hobby')

    def update(self, instance, validated_data):
        # 只允许更新 avatar 及之后的字段
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.occupation = validated_data.get('occupation', instance.occupation)
        instance.signature = validated_data.get('signature', instance.signature)
        instance.age = validated_data.get('age', instance.age)
        instance.email = validated_data.get('email', instance.email)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance
