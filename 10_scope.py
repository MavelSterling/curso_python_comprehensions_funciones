'''
SCOPE
    Scope o Alcance, es cuando una variable solo esta disponible desde donde fue construida y 
    para ello existen dos ambitos, el local y el global.
    
Scope Local
    Cuando una variable es construida dentro de una función pertenece al ámbito local de esa función y 
    solo se puede usar dentro de esa función.
'''

def incrementar():
  x = 150
  print(x)

incrementar()


'''
Scope Global
    A diferencia del Scope Local, el Scope Global esta creada en la parte externa de la función y 
    esta puede ser utilizada tanto de manera global como local.

'''
y = 150
def incrementar_2():
  print(y)

print(y)


'''
Ahora si se tiene dos variables una global y la otra local con el mismo nombre de variable,
Python lo que hará es tomar los dos variables por separado siendo una de tipo global (fuera de la función) y la otra de tipo local (dentro de la función)
'''
y = 150
def incrementar_2():
  y = 300
  print(y)

incrementar_2()
print(y)

'''
Truco
Si dentro de una variable global que fue creada esta dentro de un ámbito local, podemos utilizar global para que la variable se vuelva de ámbito global dentro de la función.
'''

def incrementar_3():
  global x
  x = 250
  
incrementar_3()
print(x)



price = 100 # global
# result = 200

def increment():
  price = 200
  result = price + 10
  print(result)
  return result

print(price)
price_2 = increment()
print(price_2)
# print(result)
