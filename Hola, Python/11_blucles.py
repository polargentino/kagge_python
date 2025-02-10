# Bucles "for" , "while" y listas por comprensiòn
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # Imprime todo en la misma lìnea
# Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune                                                                                              

# Podemos iterar sobre los elementos de una tupla
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product) # 360

# Recorrer cada carácter de una cadena
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# Imprime todas las letras mayúsculas en s, una a la vez
for char in s:
    if char.isupper():
        print(char, end='')  # HELLO  

# Rango "range()", función que devuelve una secuencia de números
for i in range(5):
    print("Doing important work. i=", i)
# Doing important work. i= 0
# Doing important work. i= 1
# Doing important work. i= 2
# Doing important work. i= 3
# Doing important work. i= 4

# Bucles "while"; se itera hasta que se cumple una condición
i = 0
while i < 10:
    print(i, end='') # 0123456789
    i += 1 # Incrementa el valor de i en 1

# Lista por comprensión
squares = [n**2 for n in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Asì es como hariamos los mismo sin una lista por comprensiòn
squares = []
for n in range(10):
    squares.append(n**2)
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Tambièn podemos agregar una condiciòn "if"
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets) # ['Venus', 'Earth', 'Mars']

# Ejemplo de filtrado con una condiciòn y aplicaciòn de alguna transformaciòn a la variable del bucle
# str.upper() devuelve una versiòn en mayùscula de un String
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets) # ['VENUS!', 'EARTH!', 'MARS!']

loud_short_planets = [
    planet.upper() + '!'  # 1. Expresión que se evalúa
    for planet in planets  # 2. Bucle for que itera sobre la lista 'planets'
    if len(planet) < 6   # 3. Condición que se aplica a cada elemento
    ]
print(loud_short_planets) # ['VENUS!', 'EARTH!', 'MARS!']

# ¿Què crees que evaluarà la siguinte expresiòn?
loud_short_planets = [32 for planet in planets]
print(loud_short_planets)  # [32, 32, 32, 32, 32, 32, 32, 32]

# Opción 1 - Considerando el Zen de Python ("La legibilidad cuenta" y "Explicito es mejor que implícito"), me inclino por la Opción 1.  Aunque es un poco más larga, es la más clara y fácil de entender, especialmente para principiantes.  La claridad es fundamental para el mantenimiento del código y la colaboración.


# def count_negatives(nums):
    #"""Devuelve el nùmero de nùmeros negativos en la lista dada.
    
#    >>> count_negatives([5, -1, -2, 0, 3])
    #2
    #"""
#    n_negative = 0
#    for num in nums:
#        if num < 0:
#            n_negative = n_negative + 1
#    return n_negative

# ---------------------------------------------------------------------
# Opción 2 -Aquì hay una soluciòn usando una lista de comprensiòn - La opción 2, aunque concisa, implica la creación de una lista intermedia, lo cual es menos eficiente y menos explicito.


# def count_negatives(nums):
#    return len([num for num in nums if num < 0])
# ----------------------------------------------------------------------

# Opción 3 - La opción 3, si bien elegante, es menos legible a primera vista. Requiere un conocimiento específico de cómo Python trata los valores booleanos en contextos numéricos.
# def count_negatives(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
#    return sum([num < 0 for num in nums])
# ------------------------------------------------------------------------
# La opción 1 es la más explicita. Describe paso a paso el proceso de contar números negativos(Gemini)
def count_negatives(nums):
    """
    Cuenta el número de números negativos en la lista dada.

    Args:
        nums: Una lista de números.

    Returns:
        El número de números negativos en la lista.

    Ejemplo:
        >>> count_negatives([5, -1, -2, 0, 3])
        2
    """
    n_negative = 0  # Inicializa el contador de números negativos
    for num in nums:  # Itera sobre cada número en la lista
        if num < 0:  # Verifica si el número es negativo
            n_negative = n_negative + 1  # Incrementa el contador si es negativo
    return n_negative  # Devuelve el número total de negativos

# Puedes probar la función con una lista de ejemplo
numeros = [5, -1, -2, 0, 3, -4, -5, 10]
cantidad_negativos = count_negatives(numeros)
print(f"La lista {numeros} tiene {cantidad_negativos} números negativos.")


