from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Product

class ProductViewSet(ViewSet):
    def list(self, request):
        products = list(Product.objects.all().values('id', 'title', 'uuid'))  # use a different variable name
        print("products are",products)
        return Response(products, status=status.HTTP_202_ACCEPTED)


    def retrive(self, request, pk):
        pass

    def create(self, request):
        pass

    def update(self, request, pk):
        pass

    def partial_update(self, request, pk):
        pass

    def destroy(self, request, pk):
        pass
