from django import http
from website.api.serialization.product_serializer import ProductSerializer
from website.models import Products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def product_list(request):
    print("Product list API called")
    serialized = ProductSerializer(Products.objects.all(), many=True)
    return Response(serialized.data)