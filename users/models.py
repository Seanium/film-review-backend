from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='static/image/avatars/', null=True, blank=True,
                               default='static/image/avatars/default.jpg')
    # 昵称
    nickname = models.CharField(max_length=255, null=True, blank=True, default='')
    # 性别
    gender = models.CharField(max_length=255, null=True, blank=True, default='')
    # 手机号码
    phone = models.CharField(max_length=255, null=True, blank=True, default='')
    # 职业
    occupation = models.CharField(max_length=255, null=True, blank=True, default='')
    # 个性签名
    signature = models.CharField(max_length=255, null=True, blank=True, default='')
    # 年龄
    age = models.PositiveIntegerField(null=True, blank=True, default=0)
    # 邮箱
    email = models.EmailField(null=True, blank=True, default='')
    # 地区
    location = models.CharField(max_length=255, null=True, blank=True, default='')
    # 兴趣爱好
    hobby = models.CharField(max_length=255, null=True, blank=True, default='')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.user.username
