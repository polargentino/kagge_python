# Tuplas
t = (1, 2, 3)
# t = 1, 2, 3 (equivalente a lo anterior)
print(t)

# No se pueden modificar(son inmutables)
#t[0] = 100

#Traceback (most recent call last):
#  File "/home/pol/Desktop/Kaggle_python/Hola, Python/10_tuples.py", line 7, in <module>
#    t[0] = 100
#    ~^^^
#TypeError: 'tuple' object does not support item assignment

# El mètodo as_integer_ratio(), devuelv un numerador y un denominador en forma de tupla
x = 0.125
numerador, denominador = x.as_integer_ratio()
print(f"El número {x} es igual a la fracción {numerador}/{denominador}")
                                     

x = 0.125
resultado = x.as_integer_ratio()
print(resultado)  # Imprime la tupla (1, 8)

# Estos mùltiples valores de retorno se pueden asignar individualmente de la sig. manera
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

# Intercambiar dos variable
a = 1
b = 0
a, b = b, a
print(a, b)
print(b ,a)
