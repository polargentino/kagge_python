# Importando math de la bibliote estándar
import math # Colección de variables definidas por otra persona
print("It`s math! It has type {}".format(type(math)))
# It`s math! It has type <class 'module'>

# Directorio de funciones incorporado
print(dir(math))
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

# Podemos acceder a éstas variables usando la sintaxis de puntos
print("pi to 4 significant digits = {:.4}".format(math.pi))
#  pi to 4 significant digits = 3.142   

print(math.log(32, 2)) # 5.0
# qhelp(math.log) #  Help on built-in function log in module math:

# log(...)
#    log(x, [base=math.e])
#    Return the logarithm of x to the given base.

#    If the base is not specified, returns the natural logarithm (base e) of x.
help(math) 
#  Help on module math:

# NAME
#    math

# MODULE REFERENCE
#    https://docs.python.org/3.7/library/math       

