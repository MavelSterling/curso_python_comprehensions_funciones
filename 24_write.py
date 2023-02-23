'''
ESCRIBIR TEXTOS EN PYTHON

Para poder escribir texto en python solo debemos agregar al parámetro open( ) algunas de las siguientes reglas:

Exception	Description
“a”	Agregar: se agregar texto al final del texto.
“w”	Escribir: Sobre escribir cualquier contenido existente en el archivo texto.

Sintaxis.

Su sintaxis es un simple y fácil de usar, solo es necesario especificar el tipo de parámetro que queremos agregar a nuestro texto.

f = open('./text.txt') o file = open('./text.txt')

'''

with open('./texs.txt', 'w+') as file:
  for line in file:
    print(line)
  file.write('nuevas cosas en este archivo\n')
  file.write('otra linea\n')
  file.write(' mas linea\n')