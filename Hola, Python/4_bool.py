# Booleanos
x = True
print(x) # True
print(type(x)) # <class 'bool'>

# Puede alguien de la edad indicada postularse para presidente de los EE.UU?
def can_run_for_president(age):
    # La constiución de EE.UU dice que debes tener al menos 35 años
    return age >= 35
print("Can a 19-year-old run for president?", can_run_for_president(19)) # Can a 19-year-old run for president? False
print("Can a 45-year-old run for president?", can_run_for_president(45)) # Can a 45-year-old run for president? True

# Comparaciones frecuentes que funcionan
#3.0 == 3 # True
# Pero a veces pueden ser complicados
#'3' == 3 # False

# Podemos comparar si un número es impar comprobando que el módulo con 2 devuelve 1
def is_odd(n):
    return(n % 2) == 1
print("Is 100 odd?", is_odd(100)) # Is 100 odd? False
print("Is -1 odd?", is_odd(-1)) # Is -1 odd? True












