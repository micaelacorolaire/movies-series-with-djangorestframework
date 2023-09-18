from rest_framework import serializers
from .models import movies,series

class serializermovies(serializers.ModelSerializer):
    class Meta:
        model=movies
        fields=['title','film_director','actors','kind_of_movies','qualification','release_year']
        
class serializerseries(serializers.ModelSerializer):
    class Meta:
         model=series
         fields=['title','film_director','actors','kind_of_series','qualification','release_year','seasons','episode']
    