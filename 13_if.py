# Declaraciones "if"
def evaluate_temp(temp):
    # Establecer un mensaje inicial
    message = 'Normal temperature.'
    # Actualizar el valor del mensaje sólo si la temp. es superior a 38°C
    if temp > 38:
        message = "Fever!"
    return message

print(evaluate_temp(37)) # Normal temperature
# (sólo escribimos un print, aqui escribimos dos para que al ajecutar Python nos muestre los dos mensajes)
print(evaluate_temp(39)) # Fever! 

# El código debajo de "if" se ejecuta si la declaración es True
# El código debajo de "else" se ejecuta si la declaración es False
def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message
print(evaluate_temp_with_else(37)) # Normal temperature.

# Declaraciones "if"..."elif"..."else"
def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message
print(evaluate_temp_with_elif(34)) # Low temperature.

# Declaraciones condicionales para realizar diferentes cálculos
# Pago de impuestos según lo que gana
# taxes: impuestos, earnings: ganacias, tax_owed: impuesto adeudado
def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = .25 * earnings
    else:
        tax_owed = .30 * earnings
    return tax_owed
ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)
print(ana_taxes) # 2250.0
print(bob_taxes) # 4500.0

# Acepta un número como entrada y suma 3 si es < 10
# En caso contrario suma 8 si la entrada es > 10
def add_three_or_eight(number):
    if number < 10:
        result = number + 3
    else:
        result = number + 8
    return result
print(add_three_or_eight(12)) # 20
print(add_three_or_eight(5))  # 8

# Multiples declaraciones "elif"
def get_dose(weight):
    # La dosis es de 1.25 ml para cualquier persona que pese menos de 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.25
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # La dosis es de 10 ml para cualquier persona que pese 21.2 kg o más
    else:
        dose = 10
    return dose
print(get_dose(12)) # 5



