import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./app/data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  '''

'''
MÓDULOS COMO SCRIPTS: NAME y MAIN

Cuando utilizamos name == ‘main’ estamos dando dualidad a cierta función para que sea ejecutada en dos archivos distintos.
Para ello debemos tener en cuenta que su uso esta catalogado de dos maneras:

Se puede ejecutar el archivo como un script.
Importando el codding de un archivo a otro archivo python.

Para Python, es independiente cual de las dos formas estemos utilizando el código, ya que python define una variable especial 
llamada __name__ la cual contiene un string y cuyo resultado dependerá de la forma en como sea usada.
'''


# Si ejecuta el archivo desde el terminal
if __name__ == '__main__':
  run()