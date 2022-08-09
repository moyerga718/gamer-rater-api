from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from gamerraterapi.models import Category

class CategoryView(ViewSet):
    """GamerRater category view"""

    def retrieve(self, request, pk):
        """Handle GET requests for a single category
        
        Returns: 
            Response -- JSON serialized category
        """

        try:
            #GET ONE GAME OBJECT THAT MATCHES ID YOU GIVE IT
            category = Category.objects.get(pk=pk)
            #PASS THAT INTO THE GAME SERIALIZER WHICH CONVERTS DB DATA INTO JSON
            serializer = CategorySerializer(category)
            #RETURN SERIALIZED JSON DATA TO CLIENT
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
        Response -- json serialized list of all games
        """

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = Category
        fields = ('id', 'name') 