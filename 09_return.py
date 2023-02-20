def find_volume(length=1, width=1, depth=1):
  return length * width * depth, width, 'hola'

result, width, text = find_volume(width=10)

print(result)
print(width)
print(text)

# Parametros por defecto y retornos multiples

# Sin parametros por defecto
def fin_volume(length,width,depth):
    return length*width*depth

resultado=fin_volume(10,20,30)
print("El resultado es: ",resultado)    

# Con parametros por defecto para todos
def find_volume(length=1,width=1,depth=1):
    return length*width*depth

resultado1=find_volume()
resultado2=find_volume(width=10)
print("Valor por defecto: ",resultado1)    
print("Valor ingresado: ", resultado2)

# Multiples returns, lo devuelve como tupla
def find_volumen(length=1,width=1,depth=1):
    return length*width*depth,width,"hola"
resultado3=find_volumen(width=10)
print(resultado3)
print("Primer elemento del resultado: ",resultado3[0]) #Porque es una tupla
print("tercer elemento del resultado: ", resultado3[2]) #Porque es una tupla


# Alternativa a multiples returns
def find_volumen(length=1,width=1,depth=1):
    return length*width*depth,width,"hola"
resultado4,ancho,texto=find_volumen(width=10)
print(resultado4)
print(texto)
print(ancho)