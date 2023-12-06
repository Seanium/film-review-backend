from django.db import models
from rest_framework.authtoken.admin import User
from films.models import Film
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + self.film.name + ' - ' + str(self.time)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + self.film.name + ' - ' + str(self.time)
