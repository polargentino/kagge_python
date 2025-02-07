# Conversión booleana
print(bool(1)) # Todos los números se tratan como True excepto 0
# Salida: True
print(bool(0))
# Salida: False
print(bool("asf")) # Todas los string se tratan como True, excepto las vacías
# Salida: True
print(bool(""))
# Salida: False
# Secuencias generalmente vacías(cadenas, listas y otros tipos que aún no hemos visto, como listas y tuplas)
# Son "falsos" y el resto son "verdaderos"

# En python el valor 0 se evalúa como False en el contexto booleano
# if 0: # Condición if no se cumple
#    print(0) # No se ejecuta
# elif "spam": # Cualquier cadena no vacía se evalua como True
#    print("spam") # Se imprime spam
