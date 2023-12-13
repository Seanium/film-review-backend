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

    def __str__(self):
        return self.user.username + ' - ' + self.film.name + ' - ' + str(self.time)


class ReviewLike(models.Model):
    """
    用户对短评的点赞
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

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

    def __str__(self):
        return self.user.username + ' - ' + self.review.content + ' - ' + str(self.time)


class Article(models.Model):
    """
    用户对电影的长评
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + self.film.name + ' - ' + str(self.time)


class ArticleLike(models.Model):
    """
    用户对长评的点赞
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

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

    def __str__(self):
        return self.user.username + ' - ' + self.article.content + ' - ' + str(self.time)
