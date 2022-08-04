from django.db import models

class PlayerPicture(models.Model):

    picture_url = models.TextField()
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    # DO I NEED TO PUT THE PLAYER/GAME FOREIGN KEYS IN HERE OR WILL THAT HAPPEN AUTOMATICALLy???