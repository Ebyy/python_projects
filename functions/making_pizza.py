import making_pizza_module

making_pizza_module.make_pizza(16,'pepperoni','onions')
making_pizza_module.make_pizza(12,'chicken','mushrooms','ham')


#A specific function can be imported by issuing the prompt:
#from making_pizza_module import make_pizza instead
#and with this quoting the module and using a dot(.) isn't necessary

from making_pizza_module import make_pizza

make_pizza(14,'sausages','green peppers')

#an alias can even be issued to the function using 'as' and stating an abbreviation

from making_pizza_module import make_pizza as mp

mp(18,'olives')

#An alias can also be given to the module using as

import making_pizza_module as mpm

mpm.make_pizza('12','pepperoni','beef')

#or we can decide to import all functions from a module using (*)
#from module_name import *
#python copies all the functions in the named module into the current program
