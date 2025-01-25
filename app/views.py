from django.shortcuts import render
from rest_framework import viewsets
from .models import GeeksModel
from .serializers import GeeksModelSerializer

# Create your views here.
class GeeksModelViewSet(viewsets.ModelViewSet):
    queryset = GeeksModel.objects.all()
    serializer_class = GeeksModelSerializer