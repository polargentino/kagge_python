# funciones integradas - Menor diferencia
def least_diference(a, b, c):
    # Docstring: cadena de documentación
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min( diff1, diff2, diff3)

# Python permite comas finales en las listas de argumentos. ¿Qué tan lindo es eso?
print(
    least_diference(1, 10, 100), # min(9, 90, 99) = 9
    least_diference(1, 10, 10),  # min(9, 0, 9) = 0
    least_diference(5, 6, 7)     # min(1, 1, 2) = 1
    ) # Salida: 9 0 1

# Qué pasaría si no incluimos la palabra clave return?
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)
    
print(
    least_difference(1, 10, 100), 
    least_difference(1, 10, 10),  
    least_difference(5, 6, 7),    
) # Salida: None None None

# Otro ejemplo
mystery = print()
print(mystery) # None

# Argumentos predeterminados
print(1, 2, 3, sep=' < ') # 1 < 2 < 3

# Agregar argumentos opcionales con valores predeterminados
def greet(who="Colin"):
    print("Hello,", who) # Hello, Colin
    
greet()
greet(who="Kaggle") # Hello, Kaggle
# (En este caso, no necesitamos especificar el nombre del argumento porque no es ambiguo).
greet("world") # Hello, world

# Funciones aplicadas a funciones
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),         # 5
    squared_call(mult_by_five, 1), # 25
    sep='\n', # '\n' is the newline character - it starts a new line
)

# Argmax - Funciones de orden superior
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?', 
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
) # Salida: 
  # Which number is biggest?
  # 100
  # Which number is the biggest modulo 5?
  # 14