from django.db import models
from rest_framework.authtoken.admin import User
from films.models import Film
from django.core.validators import MaxValueValidator, MinValueValidator


class Favorite(models.Model):
    """
    用户对电影的收藏
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '收藏电影'
        verbose_name_plural = '收藏电影'

    def __str__(self):
        return self.user.username + ' - ' + self.film.name + ' - ' + str(self.time)


class Review(models.Model):
    """
    用户对电影的短评
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    time = models.DateTimeField(auto_now_add=True)
    # 看过与否，分为0,1两个等级，0表示未看过，1表示已看过
    watched = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])

    class Meta:
        verbose_name = '短影评'
        verbose_name_plural = '短影评'

    def __str__(self):
        return self.user.username + ' - ' + self.film.name + ' - ' + str(self.time)


class ReviewLike(models.Model):
    """
    用户对短评的点赞
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '点赞短影评'
        verbose_name_plural = '点赞短影评'

    def __str__(self):
        return self.user.username + ' - ' + self.review.content + ' - ' + str(self.time)


class ReviewComment(models.Model):
    """
    用户对短评的评论
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '评论短影评'
        verbose_name_plural = '评论短影评'

    def __str__(self):
        return self.user.username + ' - ' + self.review.content + ' - ' + str(self.time)


class Article(models.Model):
    """
    用户对电影的长评
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # 剧透提醒，分为0,1,2三个等级，0表示无剧透，1表示轻度剧透，2表示重度剧透
    spoiler = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
    # 隐私设置，分为0,1两个等级，0表示仅自己可见，1表示所有人可见
    privacy = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    # 是否原创，分为0,1两个等级，0表示有参考，1表示原创
    original = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    # 标题
    title = models.CharField(max_length=255)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '长影评'
        verbose_name_plural = '长影评'

    def __str__(self):
        return self.user.username + ' - ' + self.film.name + ' - ' + str(self.time)


class ArticleLike(models.Model):
    """
    用户对长评的点赞
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '点赞长影评'
        verbose_name_plural = '点赞长影评'

    def __str__(self):
        return self.user.username + ' - ' + self.article.content + ' - ' + str(self.time)


class ArticleComment(models.Model):
    """
    用户对长评的评论
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '评论长影评'
        verbose_name_plural = '评论长影评'

    def __str__(self):
        return self.user.username + ' - ' + self.article.content + ' - ' + str(self.time)
