import json
import requests
from rest_framework.generics import GenericAPIView
from rest_framework import status as codes
from django.http import HttpResponse
from ..models import People, Films, Planets
from rest_framework import viewsets, permissions


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

            url = "https://swapi.dev/api/people/"
            response = requests.get(url)
            data= json.loads(response.text)
            data = data["results"]
            status = codes.HTTP_200_OK
        except Exception as e:
            response["details"] = e
            status = codes.HTTP_400_BAD_REQUEST
        return HttpResponse(json.dumps(response), APPLICATION_JSON, status=status)
    