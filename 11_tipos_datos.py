# Tipos de datos: int, float, 
# Números enteros : sin parte fraccionaria
x = 14
print(x)       #14
print(type(x)) # <class 'int'>
               

# Números flotantes : con parte fraccionaria
# nearly: cerca
nearly_pi = 3.141592653589793238462643383279502884197169399375105820974944
print(nearly_pi)       # 3.141592653589793
print(type(nearly_pi)) # <class 'float'>

# También podemos especificar un float con una fracción
# almost: casi
almost_pi = 22/7
print(almost_pi)       # 3.142857142857143
print(type(almost_pi)) # <class 'float'>

# Redondear a 5 decimales
rounded_pi = round(almost_pi, 5)
print(rounded_pi)       # 3.14286
print(type(rounded_pi)) # <class 'float'>

# Números con un punto decimal Python lo reconoce como datos floats
y_floats = 1.
print(y_floats)       # 1.0
print(type(y_floats)) # <class 'float'>
# Booleanos verdadero
z_one = True
print(z_one)       # True
print(type(z_one)) # <class 'bool'>

# Booleanos False
z_two = False
print(z_two)       # False
print(type(z_two)) # <class 'bool'>

# Representar el valor verdad de una expesión
z_three = (1 < 2)
print(z_three)       # True
print(type(z_three)) # <class 'bool'>

# Representar el valor de falso de una expresión
z_four = (5 < 2)
print(z_four)       # False
print(type(z_four)) # <class 'bool'>

# Cambiar el valor de un booleano usando "not"
# z_four = False, entonces no False se convierte en True
z_five = not z_four
print(z_five)       # True
print(type(z_five)) # <class 'bool'>

# String - "Cadenas"
w = "Hello, Python!"
print(w)       # Hello, Python!
print(type(w)) # <class'str'>

# Obtener la longitud
print(len(w))  # 14

# Tipo especial de String: la cadena vacía
shortest_string = ""
print(type(shortest_string)) # <class'str'>
print(len(shortest_string))  # 0

# Si pones un número entre comillas, tienes un tipo de dato string
my_number = "7.777777"
print(my_number)       # 7.777777
print(type(my_number)) # <class'str'>
print(len(my_number))  # 8

# Convertir String de números a float("7.777777")
# No se puede convertir String de palabras a un float("Hola, Python!")
also_my_number = float(my_number)
print(also_my_number)       # 7.777777
print(type(also_my_number)) # <class'float'>

# Puedes sumar dos números flotantes o enteros
# También puedes sumar dos String
new_string = "abc" + "def"
print(new_string)       # abcdef
print(type(new_string)) # <class 'str'>

# No es posible restar o dividir con dos strings
# Tampoco puedes multiplicar dos cadenas
# Sí puedes multiplicar una cadena por un número entero
new_string = "abc" * 3
print(new_string)       # abcabcabc
print(type(new_string)) # <class'str'>

# No se puede multiplicar un string por un float
# will_not_work: no trabajará
will_not_work = "abc" * 3.
print(will_not_work)

# Traceback (most recent call last):
#  File "/home/pol/Desktop/Kaggle_python/salidas.py", line 3, in <module>
#    will_not_work = "abc" * 3.
#                    ~~~~~~^~~~
# TypeError: can't multiply sequence by non-int of type 'float'



