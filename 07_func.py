'''
Funciones

Una función es un grupo de declaraciones relacionadas que realizan una tarea específica.
    Las funciones ayudan a dividir nuestro programa en partes más pequeñas y modulares. 
    A medida que nuestro programa crece más y más, las funciones lo hacen más organizado y manejable.
    Además, evita la repetición y hace que el código sea reutilizable.
'''

print('Hola')

def my_print(text):
  print(text * 2)

my_print('Este es my texto')
my_print('Hola')

a = 10
b = 90

c = a + b

def suma(a, b):
  my_print(a + b)

suma(1 ,5) # 6
suma(10, 4) # 14

#................................................................

print('Hola, Platzinauta') 
#Agregando una funcion print

def greeting(text):
# Aquí se agrega una funcion y su sintaxis.
# Junto con sus parametros en este caso 'text'
  print('This is my print')
  print('This is my print 2')
  print(text)

greeting('parametro')
#  Una manera de llamar a la función
greeting('Texto ejemplo, llamando a la función desde su parametro. ' * 2)
#Aquí otro ejemplo con suma
def suma(a,b):
  print(a + b)
#  se imprime el resultado 
suma(200, 100) 
# llama a la función con parametros

#................................................................

def my_print(text):
  print(text * 4) # veces que repite el texto

my_print('This is my text ')

def operation(a, b):
  print("a: ",a, "b: ",b ,"suma: ",a + b,"Multi: " ,a * b,"Resta: ", a - b)

operation(10,5)
operation(8,12)
operation(20,10)