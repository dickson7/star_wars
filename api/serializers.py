from rest_framework import serializers
from .models import People, Planets, Films


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('id','name','height','mass','gender','homeworld','films','species')
   
        
class PlanetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planets
        fields = ('id','name','rotation_period','orbital_period','diameter','climate','gravity','terrain','surface_water','population','residents','films')
     
        
class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = ('id','name','episode_id','opening_crawl','director','producer','planets')
      