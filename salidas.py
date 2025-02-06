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
