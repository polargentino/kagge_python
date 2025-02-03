# Tipos de datos: int, float, 
# Números enteros : sin parte fraccionaria
x = 14
print(x)
print(type(x))

# Números flotantes : con parte fraccionaria
# nearly: cerca
nearly_pi = 3.141592653589793238462643383279502884197169399375105820974944
print(nearly_pi)
print(type(nearly_pi))

# También podemos especificar un float con una fracción
# almost: casi
almost_pi = 22/7
print(almost_pi)
print(type(almost_pi))

# Redondear a 5 decimales
rounded_pi = round(almost_pi, 5)
print(rounded_pi)
print(type(rounded_pi))

# Números con un punto decimal Python lo reconoce como datos floats
y_floats = 1.
print(y_floats)
print(type(y_floats))

# Booleanos verdadero
z_one = True
print(z_one)
print(type(z_one))

# Booleanos False
z_two = False
print(z_two)
print(type(z_two))

# Representar el valor verdad de una expesión
z_three = (1 < 2)
print(z_three)
print(type(z_three))

# Representar el valor de falso de una expresión
z_four = (5 < 2)
print(z_four)
print(type(z_four))

# Cambiar el valor de un booleano usando "not"
# z_four = False, entonces no False se convierte en True
z_five = not z_four
print(z_five)
print(type(z_five))

# String - "Cadenas"
w = "Hello, Python!"
print(w)
print(type(w))

# Obtener la longitud
print(len(w))

# Tipo especial de String: la cadena vacía
shortest_string = ""
print(type(shortest_string))
print(len(shortest_string))

# Si pones un número entre comillas, tienes un tipo de dato string
my_number = "7.777777"
print(my_number)
print(type(my_number))
print(len(my_number))

# Convertir String de números a float("7.777777")
# No se puede convertir String de palabras a un float("Hola, Python!")
also_my_number = float(my_number)
print(also_my_number)
print(type(also_my_number))

# Puedes sumar dos números flotantes o enteros
# También puedes sumar dos String
new_string = "abc" + "def"
print(new_string)
print(type(new_string))

# No es posible restar o dividir con dos strings
# Tampoco puedes multiplicar dos cadenas
# Sí puedes multiplicar una cadena por un número entero
new_string = "abc" * 3
print(new_string)
print(type(new_string))

# No se puede multiplicar un string por un float
# will_not_work: no trabajará
will_not_work = "abc" * 3.
print(will_not_work)

