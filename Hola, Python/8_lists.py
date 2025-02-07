# Listas y lo que se puede hacer con ellas; incluye indexación, segmentación y mutación
# Números primos: son aquellos números naturales mayores que 1 que sólo son divisibles por 1 y por sí mismos
primes = [2, 3, 5, 7]

# Podemos poner otros tipos de datos en las listas:
planets = ['Mercury', 'Venus', 'Earth', 'Mart', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Incluso podemos hacer una lista de listas
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (La coma despùes del ùltimo elemento es opcional)
]
# Tambìèn podrìa haber escrito esto en una sòla lìnea de còdigo, pero es difìcil de leer
hands = [['J','Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

# Una lista puede contener una combinaciòn de diferentes tipos de variables
my_favourite_things = [32, 'raindrops on roses', help]

# Indexaciòn
print(planets[0]) # 'Mercury'
print(planets[1]) # 'Venus'
print(planets[-1]) # 'Neptune'
print(planets[-2]) # 'Uranus'

# Slicing(rebanar - corte)
# ¿Cùales son los primeros tres planetas?
print(planets[0:3]) # ['Mercury', 'Venus', 'Earth']

# Los ìndices inicial y final son opcionales
print(planets[:3]) # ['Mercury', 'Venus', 'Earth']

# Si omito el ìndice final se supone que es la longitud de la lista(lo que continua de Earth...)
print(planets[3:]) # ['Mart', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Tambièn podemos usar ìndices negativos al cortar
# Todos los planetas excepto el primero y el ùltimo
print(planets[1:-1]) # ['Venus', 'Earth', 'Mart', 'Jupiter', 'Saturn', 'Uranus']

# Los ùltimos 3 planets
print(planets[-3:])

# Cambiando listas
planets[3] = 'Malacandra'
print(planets) # ['Mercury', 'Venus', 'Earth', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planets[:3] = ['Mur','Vee','Ur']
print(planets) # Eso fue una tonterìa. Devolvamosle sus antiguos nombres
planets[:4] = ['Mercury','Venus','Earth','Mars'] # ['Mur', 'Vee', 'Ur', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Funciones de lista
# Cùantos planetas hay
print(len(planets)) # 8

# Los planetas ordenados en orden alfabètico
print(sorted(planets)) # ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']

# Sum hace lo que se podrìa esperar
primes = [2, 3, 5, 7]
print(sum(primes)) # 17

# Tambièn podemos pasar un argumento de lista ùnica
print(max(primes)) # 7


