def sum_with_range(min, max):
  print(min, max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result = sum_with_range(1, 10)
print(result)
result_2 = sum_with_range(result, result + 10)
print(result_2)


#Funciones con return

'''
def sum_with_range(min, max):
suma=0
for x in range(1,10):
    suma+=x
print(suma)

for x in range(20,101):
    suma+=x
print(suma)
'''
#Sin return
def suma_consecutiva_v1(minimo,maximo):
    print("Resultados sin Return en la función")
    print(minimo,maximo)
    suma=0
    for x in range(minimo,maximo+1 ):
        suma+=x
    print(suma)
 
#Con return
def suma_consecutiva_v2(minimo,maximo):
    print("Resultados con Return en la función")
    print(minimo,maximo)
    suma=0
    for x in range(minimo,maximo+1 ):
        suma+=x
    return suma

suma_consecutiva_v1(1,8)
resultado=suma_consecutiva_v2(1,8)
print(resultado)
