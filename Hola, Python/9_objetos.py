# Objetos
# imag(representa su parte imaginaria)
x = 12
# x es un nùmero real, por lo que su parte imaginaria es 0
print(x.imag) # 0
# Aquì te explicamos como hacer un nùmero complejo, en caso de que alguna vez hayas sentido curiosidad
c = 12 + 3j
print(c.imag) # 3.0

 # Los nùmeros tienen un mètodo llamado bit_length
print(x.bit_length())

# Listar Métodos
# Podemos poner otros tipos de datos en las listas:
planets = ['Mercury', 'Venus', 'Earth', 'Mart', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Plutón es un planeta, bendita sea
# list.append(), modifica una lista agregando un elemento al final
planets.append('Pluto')
print(planets)

# list.pop(), elimina y devuelve el último elemento de una lista
planets.pop()
print(planets)

# Listas de Búsqueda
# Podemos obtener su índice con el método .index()
indice_de_la_tierra = planets.index('Venus')  # Guardamos el valor retornado en una variable
print(indice_de_la_tierra)  # Imprimimos el valor de la variable
print(planets)  # Imprimimos la lista para verificar que no ha cambiado

# Es la tierra un planeta?
esta_en_la_lista = "Earth" in planets  # Guardamos el valor booleano en una variable
print(esta_en_la_lista)  # Imprimimos el valor de la variable

# Es Calbefraques un planta
esta_en_la_lista = "Calbefraques" in planets
print(esta_en_la_lista)
help(planets) # Nos informará sobre todos los métodos de la lista

