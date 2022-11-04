from django.urls import path
from .views.search_people import PeopleView

from rest_framework import routers
from .views.planets import PlanetsViewset
from .views.films import FilmsViewset
from .views.people import PeopleViewset
from .views.collet import ColletView

router = routers.DefaultRouter()

router.register('api/planets', PlanetsViewset, 'people')
router.register('api/films', FilmsViewset, 'films')
router.register('api/people', PeopleViewset, 'people')

urlpatterns = [
    path('', PeopleView.as_view()),
    path('api/search_people/', PeopleView.as_view(), name='search'),
    path('api/collet/', ColletView.as_view(), name='collet'),
]

urlpatterns += router.urls