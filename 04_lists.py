'''
numbers = []
for element in range(1, 11):
  numbers.append(element * 2)

print(numbers)

numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)
'''
numbers = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers.append(i * 2)

print(numbers)

numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)


# for

days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
newlist = []

for i in days:
  if "a" in i:
    newlist.append(i)

print(newlist) #["martes", "sabado"]


# List Comprehesion

days1 = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

newlist1 = [i for i in days1 if "a" in i]

print(newlist1) # ["martes", "sabado"]


#Listas por comprension 

'''
Vamos a definir una lista, pero
de manera mas sencilla

Sintaxis:

[element for element in iterable]
Elemento    Ciclo donde se extraen elementos
            de cualquier iterable
'''

numeros=[]
for element in range(1,11): 
    numeros.append(element)
print(numeros)

numers_v2=[element for element in range(1,11)]
print(numers_v2)

# [element for element in iterafle if contiditon]
numeros_v3=[]
for i in range (1,11):
    if i%2==0:
        numeros_v3.append(i*2)
print(numeros_v3)

numeros_v4=[i*2 for i in range(1,11) if i%2==0]
print(numeros_v4)