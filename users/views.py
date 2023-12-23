from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import RegisterSerializer, UserProfileSerializer


class LoginAPIView(APIView):
    """
    登录成功时返回user的id和token
    """

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = get_object_or_404(User, username=username)
        if user.check_password(password):
            return Response({'user_id': user.id, 'token': user.auth_token.key})
        return Response({'message': '用户名或密码错误'}, status=400)


class RegisterAPIView(APIView):
    def post(self, request):
        """
        注册
        """
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '注册成功'})
        return Response(serializer.errors, status=400)


class UserProfileView(APIView):
    """
    用户信息
    """

    def get(self, request, pk):
        """
        获取用户信息
        """
        profile = get_object_or_404(UserProfile, user=pk)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request, pk):
        """
        更新用户信息。
        """
        profile = get_object_or_404(UserProfile, user=pk)
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
