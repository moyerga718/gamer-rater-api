from django.db import models

class Game(models.Model):

    title = models.TextField()
    description = models.TextField()
    designer = models.TextField()
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    duration = models.IntegerField()
    age_recommendation = models.IntegerField()
    categories = models.ManyToManyField("Category", related_name="games")
    player_reviews = models.ManyToManyField("Player", through="PlayerReview", related_name="games")
    player_pictures = models.ManyToManyField("Player", through="PlayerPicture", related_name="games")
