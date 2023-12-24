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

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = '电影'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = '电影类型'
        verbose_name_plural = '电影类型'

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

    class Meta:
        verbose_name = '导演'
        verbose_name_plural = '导演'

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

    class Meta:
        verbose_name = '演员'
        verbose_name_plural = '演员'

    def __str__(self):
        return self.name


# 语言
class Language(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = '电影语言'
        verbose_name_plural = '电影语言'

    def __str__(self):
        return self.name


# 出版国家
class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = '制片国家/地区'
        verbose_name_plural = '制片国家/地区'

    def __str__(self):
        return self.name
