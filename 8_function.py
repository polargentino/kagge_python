# Defino la función - ejemplo más complejo que el anterior
def get_pay(num_hours):
    # Pago antes de impuestos, basado en recibir $15 por hora
    pay_pretax = num_hours * 15
    # Pago despúes de impuestos, basado en estar en la categoría impositiva del 12%
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax
# Calcular el salario basado en trabajar 40 horas
pay_fulltime = get_pay(40)
print(pay_fulltime) # 528.0
# Calcular el salario basado en trabajar 32 horas     
pay_parttime = get_pay(32)
print(pay_parttime) # 422.4



