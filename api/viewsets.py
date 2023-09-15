from rest_framework import viewsets
from .models import SmallProject, BigProject
from .serializer import SmallProjectSerializer, BigProjectSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission



class ApiAccessPermission(BasePermission):
    """
    Custom permission class to allow unauthenticated access for API calls.
    """

    def has_permission(self, request, view):
        # Verifica si la solicitud proviene de una fuente confiable, como tu aplicación web
        if request.META.get('HTTP_REFERER') and 'tusitio.com' in request.META.get('HTTP_REFERER'):
            return True
        # Si no proviene de tu aplicación web, requiere autenticación
        return request.user and request.user.is_authenticated

class SmallProjectViewSet(viewsets.ModelViewSet):
    queryset = SmallProject.objects.all()
    serializer_class = SmallProjectSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [ApiAccessPermission()]
        return []

class BigProjectViewSet(viewsets.ModelViewSet):
    queryset = BigProject.objects.all()
    serializer_class = BigProjectSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [ApiAccessPermission()]
        return []

