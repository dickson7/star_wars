import json
from rest_framework.views import APIView
from rest_framework import status as codes
from django.http import HttpResponse
from ..models import People



APPLICATION_JSON = "application/json"

class PeopleView(APIView):
    
    def get(self, request, *args, **kwargs):
        params = {key: value for key, value in request.GET.items()}
        response = []
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
                "films":[{
                    "film":"2",
                    "details":{
                        "title": "A New Hope",
                        "opening_crawl": "It is a period of civil war.\r\nRebel spaceships",
                        "director": "George Lucas",
                        "producer": "Gary Kurtz, Rick McCallum"
                    }
                },
                    {
                    "film":"3",
                    "details":{
                        "title": "A New Hope",
                        "opening_crawl": "It is a period of civil war.\r\nRebel spaceships",
                        "director": "George Lucas",
                        "producer": "Gary Kurtz, Rick McCallum"
                    }
                }
                ],
            })
        
        status = codes.HTTP_200_OK
        return HttpResponse(json.dumps(response), APPLICATION_JSON, status=status)