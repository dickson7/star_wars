from ..models import Planets
from rest_framework import viewsets, permissions
from ..serializers import PlanetsSerializer

class PlanetsViewset(viewsets.ModelViewSet):
    queryset = Planets.objects.all()
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = PlanetsSerializer