from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=200)
    height = models.CharField(max_length=20)
    mass = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    homeworld = models.TextField()
    films = models.TextField()
    species = models.TextField()
    

class Films(models.Model):
    name = models.CharField(max_length=255)
    episode_id = models.CharField(max_length=10)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    planets = models.CharField(max_length=100)


class Planets(models.Model):
    name = models.CharField(max_length=100, null=True)
    rotation_period = models.CharField(max_length=30, null=True)
    orbital_period = models.CharField(max_length=30, null=True)
    diameter = models.CharField(max_length=30, null=True)
    climate = models.CharField(max_length=30, null=True)
    gravity = models.CharField(max_length=30, null=True)
    terrain = models.CharField(max_length=200, null=True)
    surface_water = models.CharField(max_length=30, null=True)
    population = models.CharField(max_length=30, null=True)
    residents = models.CharField(max_length=30, null=True)
    films = models.TextField()
    
    
