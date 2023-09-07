from rest_framework import viewsets
from .models import SmallProject, BigProject
from .serializer import SmallProjectSerializer, BigProjectSerializer

class SmallProjectViewSet(viewsets.ModelViewSet):

    queryset=SmallProject.objects.all()
    serializer_class=SmallProjectSerializer

class BigProjectViewSet(viewsets.ModelViewSet):

    queryset=BigProject.objects.all()
    serializer_class=BigProjectSerializer