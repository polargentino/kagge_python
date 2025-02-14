# Importar con un alias más corto
# import math as mt
# print(mt.pi) # 3.141592653589793

# from math import *
# print(pi, log(32, 2)) # 3.141592653589793 5.0

# from math import *
# from numpy import *
# print(pi, log(32, 2)) # TypeError: return arrays must be of ArrayType

# Un buen compriso es importar sólo las cosas espécificas de cada módulo
# from math import log, pi
# from numpy import asarray

# Submódulos
import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )
# numpy.random is a <class 'module'>
# it contains names such as... ['set_bit_generator', 'set_state', 'shuffle', 'standard_cauchy', 'standard_exponential', 'standard_gamma', 'standard_normal', 'standard_t', 'test', 'triangular', 'uniform', 'vonmises', 'wald', 'weibull', 'zipf']

                                                                             

