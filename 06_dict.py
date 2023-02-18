# Dict comprehension con coniciones

import random
countries = ['col', 'mex', 'bol', 'pe']

population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2)

result = { country: population for (country, population) in population_v2.items() if population > 50 }
print(result)

text = 'Hola, soy Nicolas'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)


# Contar las vocales

texto = 'Hola, Platzi'

unico = {c.upper() : texto.count(c) for c in texto if c in {'a', 'e', 'i', 'o', 'u'}}

print(unico)