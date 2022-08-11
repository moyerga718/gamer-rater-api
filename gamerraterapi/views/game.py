from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from gamerraterapi.models import Game
from gamerraterapi.models import Category

class GameView(ViewSet):
    """GamerRater game view"""

    def retrieve(self, request, pk):
        """Handle GET requests for a single game
        
        Returns: 
            Response -- JSON serialized game
        """

        try:
            #GET ONE GAME OBJECT THAT MATCHES ID YOU GIVE IT
            game = Game.objects.get(pk=pk)
            #PASS THAT INTO THE GAME SERIALIZER WHICH CONVERTS DB DATA INTO JSON
            serializer = GameSerializer(game)
            #RETURN SERIALIZED JSON DATA TO CLIENT
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- json serialized list of all games
        """

        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests for a new game entry.
        """
        game = Game.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            designer=request.data["designer"],
            year_released=request.data["year_released"],
            number_of_players=request.data["number_of_players"],
            duration=request.data["duration"],
            age_recommendation=request.data["age_recommendation"]
        )

        game.categories.add(request.data["category_id"])
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a game
    
        Returns:
            Response -- Empty body with 204 status code
        """
    
        game = Game.objects.get(pk=pk)
        game.title = request.data["title"]
        game.description = request.data["description"]
        game.designer = request.data["designer"]
        game.year_released = request.data["year_released"]
        game.number_of_players = request.data["number_of_players"]
        game.duration = request.data["duration"]
        game.age_recommendation = request.data["age_recommendation"]
    
        game.categories.clear()
        game.categories.add(request.data["category_id"])
        game.save()
    
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'designer', 'year_released', 'number_of_players', 'duration', 'age_recommendation', 'categories', 'average_rating')
        depth = 1
