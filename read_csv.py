import csv

def read_csv(path):
    #abrimos el archivo
  with open(path, 'r') as csvfile:
      #ejecutamos la lectura para obtener un iterable por columna
      # Separado por comas
    reader = csv.reader(csvfile, delimiter=',')
    #Iteramos manualmente la primera fila para obtener los encabezados
    header = next(reader)
    
    #Generamos la lista donde almacenaremos la info de cada columna que iteremos, como diccionarios
    data = []
    
    #Iteramos cada fila restante del documento, estos seran nuestros "value" de los dicc.
    for row in reader:
        #Generamos un arreglo con una tupla por cada par "encabezado:columna"
      iterable = zip(header, row)
      #Generamos diccionarios por cada lista del arreglo, con una entrada de diccionario por cada tupla (encabezado, columna)
      country_dict = {key: value for key, value in iterable}
       #agregamos cada iteracion en a lista "data"
      data.append(country_dict)
       #Obtenemos el retorno de la función, al nivel de identación de la apertura de la función
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])