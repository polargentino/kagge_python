# Cadenas y diccionarios
x = 'Pluto is a planet'
y = "Pluto is a planet"
print(x == y) # True

# Comillas dobles y simples
print("Pluto's a planet") # Pluto's a planet
print('My dog is name "Pluto"') # My dog is name "Pluto"

# Python se confunde
# print('Pluto's a planet!') # SyntaxError: invalid syntax

# Solución: "escapando" la comilla simple con una barra invertida \
print('Pluto\'s a planet!') # Pluto's a planet!

# Ejemplos de "|" tabla
print('What\'s up?') # What's up?
print("That's \"coll\"") # That's "coll"
print("Look, a mountain: /\\") # Look, a mountain: /\
print("1\n2 3") # 1
                # 2 3

# \n representa el caràcter de nueva lìnea
hello = "hello\nworld"
print(hello) # hello
             # world

# Comillas triples (""")
triplequoted = """hello
world"""
print(triplequoted) # hello
                    # world
print(triplequoted == hello) # True

# Palabra clave "end"
print("hello") # hello
print("world") # world
print("hello", end='') 
print("pluto", end='') # hellopluto

# Los string's son secuencias, casi todo lo que podemos hacer con listas, también lo podemos hacer con una cadena
# Indexaciòn
planet = 'Pluto'
print(planet[0]) # P
print(type(planet[0])) # <class 'str'>
print(repr(planet[0])) # 'P'

# Slicing
print(planet[-3:]) # uto
print(repr(planet[-3:])) # 'uto'

# Cùanto mide este string?
print(len(planet)) # 5

# Sí, incluso podemos recorrelo
# Definir la variable
planet = 'Pluto'

# Usar la list comprehension para recorrer y modificar cada carácter
result = [char + '! ' for char in planet]

# Imprimir el resultado
print(result) # ['P! ', 'l! ', 'u! ', 't! ', 'o! ']

# A diferencia de las listas los string son inmutables
# planet = 'Pluto'
# planet[0] = 'B'  # Intentamos cambiar el primer carácter a 'B'
# TypeError: 'str' object does not support item assignment

# Còmo puedo modificar uun string?
planet = 'Pluto'

# Crear un nuevo string reemplazando el primer carácter
new_planet = 'B' + planet[1:] # Toma todos los caracteres desde el índice 1 hasta el final(luto)
print(new_planet)  # Resultado: 'Bluto'

# 📋 Diferencias con listas (mutables)
my_list = ['P', 'l', 'u', 't', 'o']
my_list[0] = 'B'  # Cambiamos el primer elemento a 'B'

print(my_list)  # Resultado: ['B', 'l', 'u', 't', 'o']

# Mètodos de cadena

claim = "Pluto is a planet!" # claim:afirmar
print(claim.upper()) # PLUTO IS A PLANET!

print(claim.lower()) # pluto is a planet!

claim = "Pluto is a planet!" # claim:afirmar

print(claim.index('plan'))  # 11
print(claim.find('plan'))  # Resultado: 11 - Devuelve -1 si no encuentra la subcadena (en lugar de lanzar un error). En este caso:

# P  l  u  t  o     i  s     a     p  l  a  n  e  t  !
# 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
print(claim.startswith(planet)) # True

# Si planet tuviera un valor diferente, como "Mars", el resultado sería False 
planet = "Mars"
print(claim.startswith(planet))  # Resultado: False

# False porquè le falta el signo de admiraciòn
print(claim.endswith('planet'))

# Cómo psar de cadenas a listas
claim = "Pluto is a planet!"
words = claim.split()
print(words) # ['Pluto', 'is', 'a', 'planet!']

# En ocaciones, querrás dividir por algo que no sean espacios en blanco
# Definir la cadena con la fecha
datestr = '1956-01-31'
# Dividir la cadena en partes usando el guión '-'
year, month, day = datestr.split('-')
# Imprimir los resultados
print("year:",year) # year: 1956
print("month:", month) # month: 01
print("day:",day) # day: 31
print([year,month,day]) # ['1956', '01', '31']

# Definir la cadena con la fecha
datestr = '1956/01/31'
# Dividir la cadena en partes usando el guión '/'
year, month, day = datestr.split('/')
# Imprimir los resultados
print("year:",year) # year: 1956
print("month:", month) # month: 01
print("day:",day) # day: 31
print([year,month,day]) # ['1956', '01', '31']

# str.join() nos lleva en la otra direcciòn, uniendo una lista de cadenas en una cadena larga
month = '05'
day = '07'
year = '1981'
# Usamos '/' como separador
result = '/'.join([month, day, year])
print(result) # 05/07/1981

print('-'.join(['Python', 'es', 'genial']))  # Python-es-genial
print(' '.join(['Aprendiendo', 'Python']))  # Aprendiendo Python
print('🔥'.join(['Hack', 'The', 'Box']))  # Hack🔥The🔥Box

# Construyendo cadenas con .format()
# Python  nos permite concatenar cadenas con el operador +
planet = 'Venus'
print(planet + ', we miss you!')  # Venus, we miss you!

# Si queremos incluir cualquier objeto que no sea un string, debemos llamar a str()
number = 5
message = "The number is " + str(number) + "!"
print(message)  # The number is 5!

# El mètodo .format() es otra forma de concatenar cadenas
# position = 9 
# planet + ", you'll always be the " + str(position) + "th planet to me."
# Versión con concatenación
# print(planet + ", you'll always be the " + str(position) + "th planet to me.") # Venus, you'll always be the 9th planet to me.
# Versión con .format()
# print("{} , you'll always be the {}th planet to me.".format(planet, position)) # Venus, you'll always be the 9th planet to me.

position = 9
planet = "Pluto"
print("{}, you'll always be the {}th planet to me.".format(planet, position))
# Pluto, you'll always be the 9th planet to me.

# Alternativa moderna
print(f"{planet}, you'll always be the {position}th planet to me.")

# Ejemplo con formato de decimal:
# Los {} actúan como marcador de posición.
# El : indica que viene una especificación de formato.
# El .2 define la cantidad de decimales a mostrar.
# La f significa "fixed-point" (punto fijo), es decir, formato para números decimales.
print("Valor de PI: {:.2f}".format(3.141592))
# Resultado: "Valor de PI: 3.14"

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
planet = "Pluto"  # Variable faltante

# Versión corregida con formato científico y decimales precisos
mensaje = (
    "{} weighs about {:.2e} kilograms ({:.3%} of Earth's mass). "
    "It is home to {:,} Plutonians."
).format(
    planet,                # Nombre del planeta
    pluto_mass,            # Masa en notación científica con 2 decimales
    pluto_mass/earth_mass, # Porcentaje con 3 decimales
    population             # Población con separadores de miles
)

print(mensaje) # Pluto weighs about 1.30e+22 kilograms (0.218% of Earth's mass). It is home to 52,910,390 Plutonians.
#Formato científico para masa ({:.2e}):
# {:.2e}: Notación científica con 2 decimales.
# Original: 1.303e22 → Formateado: 1.30e+22.
# Porcentaje preciso ({:.3%}):
# pluto_mass/earth_mass = 0.002182 → 0.218% (3 decimales redondeados).
# Separadores de miles ({:,}):
# 52910390 → 52,910,390.


numero = 12345.6789
print("{:.2e}".format(numero))  # Output: 1.23e+04
# El e en {:.2e} es una clave de formato que activa la notación científica, heredada de convenciones matemáticas y estándares de programación. Es esencial para representar números extremadamente grandes o pequeños de manera legible. 🚀

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)
# La variable s contiene una cadena multilínea, que se define usando tres comillas dobles ("""). Esto permite que la cadena ocupe varias líneas sin necesidad de usar caracteres de nueva línea (\n).
# Dentro de la cadena, hay marcadores de posición {0} y {1}. Estos son utilizados para insertar valores en la cadena.
# {0} se refiere al primer argumento que se pasa al método format(), y {1} se refiere al segundo argumento.
# El método format() se utiliza para reemplazar los marcadores de posición en la cadena con los valores que se le pasan como argumentos.
# En este caso, se pasan dos argumentos: 'planet' y 'dwarf planet'.
# Por lo tanto, {0} se reemplazará por 'planet' y {1} se reemplazará por 'dwarf planet'.
# Salidas: 
# Pluto's a planet.
# No, it's a dwarf planet.
# planet!
# dwarf planet!

