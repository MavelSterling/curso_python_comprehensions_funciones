'''
errores de sintaxis y excepciones.

Errores de sintaxis: son errores que ocurren cuando el código no sigue las reglas de sintaxis de Python. 
    Por ejemplo, si olvidamos colocar dos puntos al final de una línea de código que define un bloque, obtendremos un error de sintaxis.
    
Excepciones: son errores que ocurren durante la ejecución del código. 
    Por ejemplo, podríamos obtener una excepción al intentar dividir un número entero por cero o al intentar acceder a un índice de una lista que no existe.

Podemos utilizar la sentencia try-except para manejar las excepciones y evitar que el programa se bloquee. 
    Por ejemplo:
        La palabra clave assert se utiliza para verificar si una condición es verdadera. Si la condición es verdadera, assert no hace nada y el programa continúa ejecutándose normalmente. Si la condición es falsa, assert genera una excepción AssertionError y detiene la ejecución del programa.
        -La declaración raise se utiliza para lanzar una excepción. A menudo se utiliza junto con las declaraciones try y except para manejar las excepciones que pueden ocurrir en su código.

Algunas excepciones comunes en Python son:

    - TypeError: ocurre cuando se intenta realizar una operación con objetos de tipos incorrectos.
    - NameError: ocurre cuando se hace referencia a una variable que no ha sido definida.
    - IndexError: ocurre cuando se intenta acceder a un índice de una lista que no existe.
    - ValueError: ocurre cuando se intenta realizar una operación con un valor inapropiado.
    - KeyError: ocurre cuando se intenta acceder a un diccionario con una clave que no existe.
    - ZeroDivisionError: ocurre cuando se intenta dividir un número entero por cero.

'''

# print(0 / 0)
# print(result)
print('Hola')

suma = lambda x,y: x + y
assert suma(2,2) == 4

print('Hola 2')

age = 10
if age < 18:
  raise Exception('No se permiten menores de edad')

print('Hola 2')