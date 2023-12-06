from django.db import models


class Film(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    release_date = models.DateField()
    info = models.TextField()
    cover = models.ImageField(upload_to='static/image/covers/', unique=True)
    tags = models.ManyToManyField('Tag', related_name='films')
    directors = models.ManyToManyField('Director', related_name='films')
    actors = models.ManyToManyField('Actor', related_name='films')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
