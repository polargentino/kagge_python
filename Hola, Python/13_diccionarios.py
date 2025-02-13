# Diccionarios; clave, valor
numbers = {'one':1,'two':2,'three':3}
print(numbers['one']) # 1

# Podemos usar la misma sintaxis para agregar otro par clave-valor
numbers['eleven'] = 11
print(numbers) # {'one': 1, 'two': 2, 'three': 3, 'eleven': 11}
for k in numbers: # k es cada clave(key)
    print("{} = {}".format(k, numbers[k]))
# one = 1
# two = 2
# three = 3
# eleven = 11   

# Comprensiones de diccionarios
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial) # {'Mercury': 'M', 'Venus': 'V', 'Earth': 'E', 'Mars': 'M', 'Jupiter': 'J', 'Saturn': 'S', 'Uranus': 'U', 'Neptune': 'N'}

# El operador "in" nos dice si algo es una clave en el diccionario
print('Saturn' in planet_to_initial) # True

print('Betelgeuse' in planet_to_initial # False
)
# Obtenga todas las iniciales, ordénelas alfabeticamente y coloquélas en una cadena separada por espacios
print(' '.join(sorted(planet_to_initial.values())))
# E J M M N S U V

# Comprensiones de diccionarios
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial) # {'Mercury': 'M', 'Venus': 'V', 'Earth': 'E', 'Mars': 'M', 'Jupiter': 'J', 'Saturn': 'S', 'Uranus': 'U', 'Neptune': 'N'}
# El muy útil método dict.items() nos permite iterar sobre las claves y valores del diccionario simultaneamente
# Un elemento se refiere a un par clave-valor
for planet, initial in planet_to_initial.items(): # planet_to_initial.items(): Este método devuelve una vista de los pares clave-valor del diccionario. Permite iterar sobre las claves y los valores simultáneamente.
# for planet, initial in ...: En cada iteración del bucle:
# planet toma el valor de la clave (el nombre del planeta).
# initial toma el valor asociado a esa clave (la inicial del planeta).
# planet.rjust(10): Ajusta el nombre del planeta a la derecha en un campo de 10 caracteres, rellenando con espacios a la izquierda si es necesario. Esto alinea los nombres de los planetas para una mejor presentación.
# print("{} begins with \"{}\"".format(planet.rjust(10), initial)): Imprime una cadena formateada. {} son marcadores de posición que se reemplazan con planet.rjust(10) y initial respectivamente. El resultado es una frase que indica con qué letra comienza cada planeta.

    print("{} begins with \"{}\"".format(planet.rjust(10), initial))
# Mercury begins with "M"
#     Venus begins with "V"
#     Earth begins with "E"
#      Mars begins with "M"
#   Jupiter begins with "J"
#    Saturn begins with "S"
#    Uranus begins with "U"
#   Neptune begins with "N"

print(help(dict)) # Obtener ayuda sobre el objeto dict