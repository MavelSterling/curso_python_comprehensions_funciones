'''
LEER ARCHIVOS DE TEXTO

Para realizar la lectura de un archivo tipo texto en Python debemos utilizar la función open( ), 
esta función nos permite abrir un archivo tipo texto en python.

'''
# imprimir linea a linea del archivo
file = open('./text.txt')

# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# leer el archivo con for iterando linea a linea
for line in file:
  print(line)

file.close() # close the file

# cerrar el archivo una vez se ejecuten ciertas instrucciones con with
with open('./text.txt') as file:
    # leer archivo
  for line in file:
    print(line)