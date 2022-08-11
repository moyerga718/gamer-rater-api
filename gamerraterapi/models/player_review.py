from django.db import models

class PlayerReview(models.Model):

    rating = models.IntegerField()
    review = models.TextField()
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="ratings")

    # DO I NEED TO PUT PLAYER / GAME IDS IN HERE OR WILL THAT BE ADDED AUTOMATICALLY???