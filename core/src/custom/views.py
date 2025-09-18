from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer

class ItemViewSet(ViewSet):
    def list(self, request):
        item = [
            {"name": "Kurti", "price": "599.0"},
            {"name": "Shirt", "price": 799.0, "color": "blue"},
        ]
        
        serializer = ItemSerializer(item, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)