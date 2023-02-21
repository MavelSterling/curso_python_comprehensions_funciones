'''
PAQUETES

Los paquetes son las carpetas que contienen varios módulos y cada uno con una función distinta.

Para ello debe tener siempre un archivo de nombre __init__.py (por lo general esta vacio, ya que así es compatible con programas python versiones anteriores a la 3), con esto le estamos indicado a python que esto se trata de un paquete y no de una carpeta.

Para acceder a los módulos de los paquetes podemos utilizar estas opciones:
    import nombrecarpeta.nombremodulo
    from nombrecarpeta import nombremodulo
    from nombrecarpeta.nombremodulo import 
'''

'''
from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())

'''

import pkg
print(pkg.URL)
print(pkg.mod_1.func_1())

# mod_2.py
import pkg.mod_2 as mod_2

print(mod_2.func_3())
print(mod_2.func_4())