from ..models import People
from rest_framework import viewsets, permissions
from ..serializers import PeopleSerializer

class PeopleViewset(viewsets.ModelViewSet):
    queryset = People.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PeopleSerializer