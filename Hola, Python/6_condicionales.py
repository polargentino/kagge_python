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
inspect(0) # 0 is zero
inspect(-15) # -15 is negative


# Otro ejemplo
def f(x):
    if x > 0:
        # Sólo se imprime cuando x es positivo
        print("Only printed when x is positive; x =", x) # Only printed when x is positive; x = 1
        # También sólo se imprime cuando x es positivo
        print("Also only printed when x is positive; x =", x) # Also only printed when x is positive; x = 1
    # Siempre impreso, independientemente del valor de x
    print("Always printed, regardless of x's value; x =", x) # Always printed, regardless of x's value; x = 1
                                                             # Always printed, regardless of x's value; x = 0

f(1)
f(0)


