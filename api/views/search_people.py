import json
from rest_framework.generics import GenericAPIView
from rest_framework import status as codes
from django.http import HttpResponse
from ..models import People, Films, Planets
from rest_framework import viewsets, permissions


APPLICATION_JSON = "application/json"

class PeopleView(GenericAPIView):
    """Class that allows to consult all star wars characters.

     Methods availables : GET
    """
    
    permission_classes = [permissions.IsAuthenticated,]
    
    def get(self, request, *args, **kwargs):
        """GET method that performs the data query. If the parament name is sent, 
        the query is performed by the name of the character. 
        Otherwise it returns all the characters. 

        Args:
            request: param name

        Returns:
            dict: Response star wars characters
        """
        params = {key: value for key, value in request.GET.items()}
        response = []
        try:
            if "name" in params:
                people = People.objects.filter(name=params["name"])
            else:
                people = People.objects.all()
                
            for person in people:
                response.append({
                    "id":person.id,
                    "name":person.name,
                    "height":person.height,
                    "mass":person.mass,
                    "gender":person.gender,
                    "homeworld":person.homeworld,
                    "species":person.species,
                    "films": search_films(person.films)
                })
            status = codes.HTTP_200_OK
        except Exception as e:
            response = {"details":  str(e)}
            status = codes.HTTP_400_BAD_REQUEST
        return HttpResponse(json.dumps(response), APPLICATION_JSON, status=status)
    
    
def search_films(films):
    """function that performs the search for movies related to the character

    Args:
        films (str): id of films

    Returns:
        list: details flims
    """
    response =[]
    for film in eval(films):
        search = Films.objects.filter(id=film)
        if search:
            response.append({
                "film":film,
                "details":{
                    "title": search[0].name,
                    "opening_crawl": search[0].opening_crawl,
                    "director": search[0].director,
                    "producer": search[0].producer,
                    "planets":search_planets(search[0].planets)
                    }
            })
    return response

def search_planets(planets):
    """function that performs the search for movies related to the character

    Args:
        planets (str): list with id planets

    Returns:
        list: name of planets
    """
    response = []
    for planet in eval(planets):
        search = Planets.objects.filter(id=planet)
        if search:
            response.append(search[0].name)
    return response