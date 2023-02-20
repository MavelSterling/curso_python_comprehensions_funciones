# lista items con diccionarios
items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

# Ahora una lista de los precios con map
prices = list(map(lambda item: item['price'], items))
print("Lista de diccionarios: ",items)
print("Precio de los diccionarios: ",prices)

def add_taxes(item):
  item['taxes'] = item['price'] * .19 # agregar el atributo del impuesto 19%
  return item

new_items = list(map(add_taxes, items))
print(new_items)
print(items)