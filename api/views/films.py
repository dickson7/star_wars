from ..models import Films
from rest_framework import viewsets, permissions
from ..serializers import FilmsSerializer

class FilmsViewset(viewsets.ModelViewSet):
    queryset = Films.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FilmsSerializer