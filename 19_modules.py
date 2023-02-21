'''
MODULO
    - Un módulo es un fichero, con extensión *.py y, por tanto, accesible al intérprete de Python y ejecutable por el núcleo de Python. Puede contener:
    - Variables globales, funciones, clases (patrones de objetos) y sentencias ejecutables.
    - La programación de clases no la estudiaremos en este curso introductorio.
    - Un módulo, a su vez, puede importar otros módulos.
'''


import sys
# Ruta en la que se esta ejecutando
print(sys.path) 

# Expresiones regulares
import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
# Buscar todos los números del text.
result = re.findall('[0-9]+', text)
print("Array con los números del texto: ",result)

# Manejo de horas y fechas
import time
timestamp = time.time()
print(timestamp) #hora actual para el computador

# Hora local
local = time.localtime()
# Formato para la hora local
result = time.asctime(local)
print("Fecha y hora: ",result)

# Utilidad para menjar listas
import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
# Diccionario con la frecuencia de los numeros
counter = collections.Counter(numbers)
print(counter)