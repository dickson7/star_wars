import json
import requests
from rest_framework.generics import GenericAPIView
from rest_framework import status as codes
from django.http import HttpResponse
from ..models import People, Films, Planets
from rest_framework import viewsets, permissions
from urllib.parse import urlparse


APPLICATION_JSON = "application/json"

class ColletView(GenericAPIView):
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
        
        try:

            url = "https://swapi.dev/api/people/?page=2"
            response = requests.get(url)
            data= json.loads(response.text)
            data = data["results"]
            for people in data:
                id = extract_id(urls=people["url"], endpoint='people', type=1)
                register={
                    "id":id,
                    "name": people["name"],
                    "height": people["height"],
                    "mass": people["mass"],
                    "gender": people["gender"],
                    "homeworld": extract_id(urls=[people["homeworld"]],endpoint='planets'),
                    "films": extract_id(urls=people["films"],endpoint='films'), 
                    "species": extract_id(urls=people["species"], endpoint='species')
                }
                instance = People.objects.filter(id=id).last()
                if not instance:
                    instance = People.objects.create(**register)
                    print(instance.name)
                save_planets(instance.homeworld)
            save_films()
            response={"status":"Done"}
            status = codes.HTTP_200_OK
        except Exception as e:
            response={"details": str(e)}
            status = codes.HTTP_400_BAD_REQUEST
        return HttpResponse(json.dumps(response), APPLICATION_JSON, status=status)


def extract_id(urls, endpoint, type=0):
    count = len(endpoint)
    if type==1 and len(urls)>0:
        parsed = urlparse(urls)
        return parsed.path[count+6:-1]
    else:
        response=[]
        if len(urls) > 0:
            for url in urls:
                parsed = urlparse(url)
                response.append(parsed.path[count+6:-1])
        return f'{response}'
        
            
def save_planets(homeworld):
    try:
        for planet in eval(homeworld):
            try:
                Planets.objects.get(id=planet)
            except Planets.DoesNotExist:
                url = f'https://swapi.dev/api/planets/{planet}/'
                response = requests.get(url)
                data= json.loads(response.text)
                register={
                    "id":extract_id(urls=data["url"], endpoint='planets', type=1),
                    "name":data["name"],
                    "rotation_period":data["rotation_period"],
                    "orbital_period":data["orbital_period"],
                    "diameter":data["diameter"],
                    "climate":data["climate"],
                    "gravity":data["gravity"],
                    "terrain":data["terrain"],
                    "surface_water":data["surface_water"],
                    "population":data["population"],
                    "residents":extract_id(urls=data["residents"], endpoint='residents'),
                    "films":extract_id(urls=data["films"], endpoint='films')
                    }
                instance = Planets.objects.create(**register)
                print(instance.id)
    except Exception as e:
        raise Exception(e)        
            
def save_films():
    
    url = f'https://swapi.dev/api/films/'
    response = requests.get(url)
    if response.status_code ==200:
        data= json.loads(response.text)
        films = data["results"]
        for data in films:
            id = extract_id(urls=data["url"], endpoint='films', type=1)
            register={
                "id":id,
                "name":data["title"],
                "episode_id":data["episode_id"],
                "opening_crawl":data["opening_crawl"],
                "director":data["director"],
                "producer":data["producer"],
                "planets":extract_id(urls=data["planets"], endpoint='planets'),
                }
            instance = Films.objects.filter(id=id).last()
            if not instance:
                instance = Films.objects.create(**register)
                print(instance.id)