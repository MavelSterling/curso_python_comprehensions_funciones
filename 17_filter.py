'''
Python’s filter()es una función incorporada que le permite procesar un iterable y 
    extraer aquellos elementos que satisfacen una condición dada. 
    Este proceso se conoce comúnmente como una operación de filtrado.
    
Con filter(), puede aplicar una función de filtrado a un iterable y producir un 
    iterable nuevo con los elementos que satisfacen la condición en cuestión. 
    En Python, filter()es una de las herramientas que puedes usar para la programación funcional .

'''
numbers = [1,2,3,4,5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)
print(numbers)