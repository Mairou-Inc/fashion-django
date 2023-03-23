from django.db.models.query import QuerySet
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import *
from rest_framework import status, generics
from datetime import datetime
from django.db.models import  Q


class ProductView(generics.ListAPIView):
    """Отдает продукцию"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
