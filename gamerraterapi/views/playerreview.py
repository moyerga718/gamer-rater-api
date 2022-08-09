from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from gamerraterapi.models import Game
from gamerraterapi.models import Player
from gamerraterapi.models import PlayerReview



class PlayerReviewView(ViewSet):
    """GamerRater game view"""

    def retrieve(self, request, pk):
        """Handle GET requests for a single review
        
        Returns: 
            Response -- JSON serialized review
        """

        try:
            #GET ONE GAME OBJECT THAT MATCHES ID YOU GIVE IT
            review = PlayerReview.objects.get(pk=pk)
            #PASS THAT INTO THE GAME SERIALIZER WHICH CONVERTS DB DATA INTO JSON
            serializer = PlayerReviewSerializer(review)
            #RETURN SERIALIZED JSON DATA TO CLIENT
            return Response(serializer.data)
        except PlayerReview.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all reviews

        Returns:
            Response -- json serialized list of all reviews
        """

        reviews = PlayerReview.objects.all()

        game = request.query_params.get('game', None)
        if game is not None:
            reviews = reviews.filter(game_id=game)

        serializer = PlayerReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests for a new game entry.
        """

        game = Game.objects.get(pk=request.data["game_id"])
        player = Player.objects.get(user=request.auth.user)

        review = PlayerReview.objects.create(
            rating=request.data["rating"],
            review=request.data["review"],
            game=game,
            player=player
        )

        serializer = PlayerReviewSerializer(review)
        return Response(serializer.data)

class PlayerReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews
    """
    class Meta:
        model = PlayerReview
        fields = ('id', 'rating', 'review', 'game', 'player')
        depth = 2