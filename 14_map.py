'''
MAP( )
La función map() ejecuta una función especifica para cada elemento en un iterable y 
el elemento se envía a la función como un parámetro.

Sintaxis.
    map(function, iterable[, iterable1, iterable2,..., iterableN])
    
map() recorre los elementos de una entrada iterable (o iterables) y 
devuelve un iterador que resulta de aplicar una función de transformación a cada elemento en la entrada iterable original.

Nota: el primer argumento para map()es un objeto de función , lo que significa que debe pasar una función sin llamarla. 
Es decir, sin usar un par de paréntesis.
    
'''

numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:
  numbers_v2.append(i * 2)

numbers_v3 = list(map(lambda i: i * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)