'''

Funciones de set:

  - add(): Añade un elemento.
  - update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.
  - discard(): Elimina un elemento y si ya existe no lanza ningún error.
  - remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
  - pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.
  - clear(): Elimina todo el contenido del conjunto.
  
  
'''


set_countries = {'col', 'mex', 'bol'}

size = len(set_countries) # Tamaño del conjunto
print(size)

print('col' in set_countries) # Consulta si col esta en el conjunto
print('pe' in set_countries) # Consulta si pe esta en el conjunto

# add - agregar pe al conjunto
set_countries.add('pe')
print(set_countries)

# Volver a agregar al elemento - Solo se agrega una vez en el conjunto
set_countries.add('pe')
print(set_countries)

# update - Actualizar el conjunto 
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# remove - Quitar a col del conjunto
set_countries.remove('col')
print(set_countries)

set_countries.remove('ar')
set_countries.discard('arg')
print(set_countries)

# Agregar arg al conjunto
set_countries.add('arg')
print(set_countries)

# Limpiar el conjunto
set_countries.clear()
print(set_countries)
print(len(set_countries))