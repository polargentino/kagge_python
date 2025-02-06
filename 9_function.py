# Función con múltiples argumentos
# num_hours: núms. de hs. trabajadas en una semana
# hourly_wage: el salario por hora(en $/hora)
# tax_bracket: porcentaje del salario que se elimina para impuestos
def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    # Pre-tax(pago antes de impuestos: 40hs * $24/hora)
    pay_pretax = num_hours * hourly_wage
    # Aftet-tax(pago despúes de impuestos)
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax
# Pago mayor despues de impuestos
higher_pay_aftertax = get_pay_with_more_inputs(40, 24, .22)
print(higher_pay_aftertax) # 748.8000000000001
# Mismo pago fulltime
same_pay_fulltime = get_pay_with_more_inputs(40, 15, .12)
print(same_pay_fulltime) # 528.0