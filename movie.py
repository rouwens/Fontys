from tmdbv3api import TMDb
from tmdbv3api import Movie
import requests


tmdb = TMDb()
tmdb.api_key = '3d5fc567499c5c48967bd3add31ebefe'

#movie = Movie()
#popular = movie.popular()

#search = movie.search('Saving private Ryan')

#for res in search:
    #print(res.id)
    #print(res.title)
    #print(res.overview)
    #print(res.poster_path)
    #print(res.vote_average)

#https://api.themoviedb.org/3/search/person?api_key=3d5fc567499c5c48967bd3add31ebefe&query=bruce+willis

print ("Vul de voornaam in van de acteur/actrice")
voornaam = input()

print ()
print ("Vul de achternaam in van de acteur/actrice")
achternaam = input()


volledig = voornaam + "+" + achternaam
url = "https://api.themoviedb.org/3/search/person?api_key="+tmdb.api_key+"&query="+volledig

actordata = requests.get(url) 
x = actordata.text
#print (x)

idvoor = x.index("id") + 4 
idachter = x.index("known") -2
id = x[idvoor:idachter]

print ()
print ("Het ID van de gevraagde acteur/actrice is: " + id)