# Cambiando valores booleanos
# Es_ciudadano_nacido_naturalmente
def can_run_for_president(age, is_natural_born_citizen):
   
    """¿Alguien de la edad y el estatus de ciudadanía indicados puede postularse para presidente en los EE. UU.?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    # La Constitución de los EE. UU. dice que debes ser ciudadano nato *y* tener al menos 35 años
    return is_natural_born_citizen and (age >= 35)

# Imprimiendo los resultados
print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))

# True or True and False
# Orden de evaluación de operadores lógicos
# True and False = False(and requiere que ambos sean True)
# True or False = True(or si al menos un de los operadores es True)
resultado = True or (True and False) # Paréntesis para evitar confuciones
print(resultado)


# Define una variable que es True o False dependiendo de varias condiciones relacionadas con el clima y la preparación de la persona
# Lógica para determinar si una persona está preparada para el clima:
# prepared_for_weather = (
#     have_umbrella 
#     or ((rain_level < 5) and have_hood) 
#     or (not (rain_level > 0 and is_workday))
# )
# 
# Desglose:
# - Estás preparado si tienes un paraguas.
# - Si llueve menos de 5 y tienes capucha, estás preparado.
# - Si no es un día laboral o no está lloviendo, no necesitas preparación.




