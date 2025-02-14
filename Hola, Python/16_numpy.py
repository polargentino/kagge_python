import numpy as np  # Importamos numpy con el alias "np"

# randint es una función útil para generar números enteros aleatorios dentro de un rango específico, ideal para simulaciones, juegos, pruebas de código, etc.

# Lanzar 10 dados (valores entre 1 y 6)
rolls = np.random.randint(low=1, high=7, size=10)

# Imprimir los valores generados
print(rolls) # Imprimimos los valores generados
# [5 6 5 4 2 5 5 2 4 6]
# [3 5 4 3 4 2 1 4 3 5]

# type(), ¿Qué es esto?
print(type(rolls)) # <class 'numpy.ndarray'>
# dir(), ¿Qué puedo hacer con esto?
print(dir(rolls)) # ['__abs__', '__add__', '__and__', '__class__', '__contains__', '__delattr__',
# Si quiero la tirada promedio.
print(rolls.mean()) # 4.1
# Convertir la matríz em una lista
print(rolls.tolist()) # [3, 3, 5, 1, 1, 3, 4, 4, 4, 2]
# help() - Cúenteme más sobre esto
# help(rolls.ravel) # Devuelve :
# Help on built-in function ravel:

# ravel(...) method of numpy.ndarray instance
#     a.ravel([order])

#     Return a flattened array.
# Cùentame todo lo que hay que saber sobre numpy.ndarray
# help(rools)
print(rolls.ravel()) # [3 3 5 1 1 3 4 4 4]  Devuelve una matriz aplanada

# 🎲 Ejemplo 1: Un solo número aleatorio entre 1 y 6
num = np.random.randint(1, 7)  # Genera un número entre 1 y 6
print(num)
# 4
# 3

# 🎲 Ejemplo 2: Generar una lista de 6 números aleatorios entre 10 y 20
nums = np.random.randint(10, 21, size=5)
print(nums) # [17 15 13 18 20]


# 🎲 Ejemplo 3: Generar una matriz 3x3 con valores entre 0 y 9
matrix = np.random.randint(0, 10, size=(3,3))
print(matrix)
# [[5 7 1]
# [9 4 8]
# [0 0 3]]

# 🚨 Pero cuidado: El Quini 6 no permite números repetidos
# 📌 Solución correcta sin repeticiones (usando np.random.choice):
# 🔹 np.random.choice(range(46), size=6, replace=False) elige 6 números aleatorios sin repetir, asegurando que cada número esté entre 0 y 45.

nums = np.random.choice(range(46), size=6, replace=False)  # Sin repeticiones
print(nums)
# [23 21 40 26 15  6]
# [16  5 31 43  1 33]
# [ 0 16 40  2 42  3]

