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
import package.mod_2 as mod_2

print(mod_2.func_3())
print(mod_2.func_4())