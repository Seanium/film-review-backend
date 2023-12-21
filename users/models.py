from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='static/image/avatars/', unique=True)
    # 昵称
    nickname = models.CharField(max_length=255, unique=True)
    # 性别
    gender = models.CharField(max_length=255)
    # 手机号码
    phone = models.CharField(max_length=255)
    # 职业
    occupation = models.CharField(max_length=255)
    # 个性签名
    signature = models.CharField(max_length=255)
    # 年龄
    age = models.PositiveIntegerField()
    # 邮箱
    email = models.EmailField()
    # 地区
    location = models.CharField(max_length=255)
    # 兴趣爱好
    hobby = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
