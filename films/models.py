from django.db import models


class Film(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    release_date = models.DateField()
    info = models.TextField()
    cover = models.ImageField(upload_to='static/image/covers/', null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='films')
    directors = models.ManyToManyField('Director', related_name='films')
    actors = models.ManyToManyField('Actor', related_name='films')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='films')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='films')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=255)
    # 照片
    photo = models.ImageField(upload_to='static/image/directors/', null=True, blank=True)
    # 出生日期
    birth_date = models.DateField(null=True, blank=True)
    # 出生地
    birth_place = models.CharField(max_length=255, null=True, blank=True)
    # 简介
    info = models.TextField()

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=255)
    # 照片
    photo = models.ImageField(upload_to='static/image/directors/', null=True, blank=True)
    # 出生日期
    birth_date = models.DateField(null=True, blank=True)
    # 出生地
    birth_place = models.CharField(max_length=255, null=True, blank=True)
    # 简介
    info = models.TextField()

    def __str__(self):
        return self.name


# 语言
class Language(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


# 出版国家
class Country(models.Model):
    class Meta:
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
