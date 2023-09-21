from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class movies(models.Model):
    title=models.CharField(max_length=50,null=False)
    film_director=models.CharField(max_length=100,null=False)
    actors=models.CharField(max_length=50,null=False) 
    kind_of_movies=models.CharField(max_length=100,null=False)
    qualification=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)],null=False)
    release_year=models.DateField()
    
class series(models.Model):
    title=models.CharField(max_length=50,null=False)
    film_director=models.CharField(max_length=100,null=False)
    actors=models.CharField(max_length=50,null=False) 
    kind_of_series=models.CharField(max_length=100,null=False)
    qualification=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)],null=False)
    release_year=models.DateField()
    seasons=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(15)],null=False)
    episode=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(20)],null=False)
    
    
    
# Create your models here.
