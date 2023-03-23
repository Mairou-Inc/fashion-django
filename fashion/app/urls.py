from django.urls import path, include
from . import viewsets


urlpatterns = [
    path('products/', viewsets.ProductView.as_view()),
]

