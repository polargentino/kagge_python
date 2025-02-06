# Condicionales : if, elif, else 
def inspect(x):
    if x == 0: # Pregunto por el valor de x
        print(x, "is zero")
    elif x > 0: # Verifiquemos esta nueva condición
        print(x, "is positive")
    elif x < 0: # Verifiquemos esta nueva condición
        print(x, "is negative")
    else: # Entonces
        print(x, "is unlike anything I've ever seen...") # No se parece a nada que haya visto...
inspect(0)
inspect(-15)


# Otro ejemplo
def f(x):
    if x > 0:
        # Sólo se imprime cuando x es positivo
        print("Only printed when x is positive; x =", x)
        # También sólo se imprime cuando x es positivo
        print("Also only printed when x is positive; x =", x)
    # Siempre impreso, independientemente del valor de x
    print("Always printed, regardless of x's value; x =", x)

f(1)
f(0)


