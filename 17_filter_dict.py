'''
FILTER
La función filter(), devuelve un valor que esta siendo iterado de la cual su resultado será el valor que se esta buscando en el filter

SINTAXIS
_filter (function, iterable_

Valores.
filter: Una función que se ejecutara para cada elemento iterable
iterable: Lo que se va a filtrar.

'''

#------- Filter con diccionarios ----------
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

# obtener una lista con los diccionarios de los equipo locales que hayan ganado

print(matches)
print(len(matches))

new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))

print("Lista de equipos que ganaron: ",new_list)
print("Cantidad de elementos de la lista: ",len(new_list)) # numero de elementos de la lista

print(matches)
print("Cantidad de elementos de la lista: ", len(matches))