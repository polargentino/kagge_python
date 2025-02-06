# Crear variables
num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60
# Calcular el número de segundos en cuatro años
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs) # 126144000

# Actualización para incluir años bisiestos
days_per_year = 365.25
# Calcular el número de segundos en cuatro años
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs) # 126230400.0

