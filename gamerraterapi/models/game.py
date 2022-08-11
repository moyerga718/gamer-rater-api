from django.db import models

class Game(models.Model):

    title = models.TextField()
    description = models.TextField()
    designer = models.TextField()
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    duration = models.IntegerField()
    age_recommendation = models.IntegerField()
    categories = models.ManyToManyField("Category", through="GameCategory", related_name="games")

    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = self.ratings.all()

        # Sum all of the ratings for the game
        total_rating = 0
        counter = 0
        for rating in ratings:
            total_rating += rating.rating
            counter += 1
        


        # Calculate the averge and return it.
        # If you don't know how to calculate average, Google it.
        if total_rating == 0:
            avg_rating = 0
        else:
            avg_rating = total_rating / counter

        return avg_rating

        #return the result