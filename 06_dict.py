# Dict comprehension con coniciones


#Crear un dict comprehension con una lista
import random
countries = ['col', 'mex', 'bol', 'pe']

population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2)

# crear un dict comprehension con una condicion
# paises con poblacion mayor a 50 - es aleatorio
result = { country: population for (country, population) in population_v2.items() if population > 50 }
print(result)

text = 'Hola, soy Nicolas'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)


#dict comprehension de las vocales de una oracion
text = 'Hola nuevo mundo'
unique = { c: c.upper() for c in text if c in 'aeiou'}
print(unique)

# Contar las vocales

texto = 'Hola, Platzi'

unico = {c.upper() : texto.count(c) for c in texto if c in {'a', 'e', 'i', 'o', 'u'}}

print(unico)