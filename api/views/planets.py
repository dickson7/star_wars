from ..models import Planets
from rest_framework import viewsets, permissions
from ..serializers import PlanetsSerializer

class PlanetsViewset(viewsets.ModelViewSet):
    queryset = Planets.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlanetsSerializer