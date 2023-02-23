'''
ESCRIBIR TEXTOS EN PYTHON

Para poder escribir texto en python solo debemos agregar al parámetro open( ) algunas de las siguientes reglas:

Exception	Description
“r”	Lectura: Abre por defecto un archivo para su lectura, genera error si este no existe.
“a”	Agregar: se agregar texto al final del texto.
“w”	Escribir: Sobre escribir cualquier contenido existente en el archivo texto.
“x”	Crear: Crea un archivo en especifico, devuelve un error si este no es valido.
“t”	texto: Valor por defecto, devuelve el resultado como tipo texto.
“b”	Binario: Devuelve el valor de tipo binario (por ejemplo imágenes)


Sintaxis.

Su sintaxis es un simple y fácil de usar, solo es necesario especificar el tipo de parámetro que queremos agregar a nuestro texto.

f = open('./text.txt') o file = open('./text.txt')

'''
f = open('./text.txt', "a")
f.write("nueva linea de texto1\n")
f.write("nueva linea de texto2\n")
f.write("nueva linea de texto3\n")

'''
Ahora y quizas este comando puede ser muy util como muy peligro ya que “w” lo que realiza es eliminar todo el texto y
lo sobre escribir con lo que le vayamos a ingresar por eso es de cuidado!.

'''
f = open('./text.txt', "w")
f.write("Uppps!! hemos sobre escrito el texto con este nuevo\n")
f.close()


with open('./texs.txt', 'w+') as file:
  for line in file:
    print(line)
  file.write('nuevas cosas en este archivo\n')
  file.write('otra linea\n')
  file.write(' mas linea\n')