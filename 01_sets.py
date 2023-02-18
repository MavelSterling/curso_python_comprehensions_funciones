# Sets (conjuntos)

'''
Conjuntos, es una agrupación de elementos que tienen propiedades en común.
    - Se puede modificar
    - No tiene un orden específico
    - No se permiten duplicados
    
 Los sets (conjuntos) comparten la sintaxis con los diccionarios al momento de definirlos 
 ya que usan curly braces {}, lo que los diferencia es que los sets no contienen la estructua de clave-valor.   
    
'''

set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)

set_from_string = set('hoola')
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)


'''
Para crear un set en Python se puede hacer con set() y 
pasando como entrada cualquier tipo iterable, como puede ser una lista. 
Se puede ver como a pesar de pasar elementos duplicados como dos 8 y en un orden determinado, 
al imprimir el set no conserva ese orden y los duplicados se han eliminado.

'''

s = set([5, 4, 6, 8, 8, 1])
print(s)       #{1, 4, 5, 6, 8}
print(type(s)) #<class 'set'>

# Se puede hacer lo mismo haciendo uso de {} y 
# sin usar la palabra set() como se muestra a continuación.

s1 = {5, 4, 6, 8, 8, 1}
print(s1)       #{1, 4, 5, 6, 8}
print(type(s1)) #<class 'set'>