from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import RegisterSerializer, UserProfileSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        """
        注册
        """
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 创建user_profile
            user = serializer.instance
            user_profile = UserProfile(user=user)
            user_profile.save()
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
