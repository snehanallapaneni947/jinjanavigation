from django.urls import path
from movie.views import *

app_name='movie'
urlpatterns  = [
    
    path('pushpa/',pushpa,name='pushpa'),
]