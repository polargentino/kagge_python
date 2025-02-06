# Cantidad de spam
spam_amount = 0
print(spam_amount) # 0

# Ordenar, huevo, spam, spam, tocino, y spam(4 porciones más de spam)
spam_amount = spam_amount + 4
if spam_amount > 0:
    # No quiero ningún spam
    print("But I don't want ANY spam") # But I don't want ANY spam
viking_song = "Spam " * spam_amount
print(viking_song) # Spam Spam Spam Spam 
print(type(viking_song)) # <class 'str'>

# El operador //(división del píso), nos da un rsultado que se redondea hacia abajo
print(5//2) # 2

# Gerarquía de operaciones PEMDAS: (Paréntesis, Exponenetes, Multiplicación/División, Suma/REsta)
resultado = -3 + 4 * 2
print(resultado) # Esto imprimirá 5

# Altura del sombrero en cm
hat_height_cm = 25
my_heigth_cm = 190
# Cúanto mido en metros cuando utilizo mi sombrero
# Resultado incorrecto!
total_heigth_meters = hat_height_cm + my_heigth_cm / 100
print("Height in meters =", total_heigth_meters, "?") # Height in meters = 26.9 ?

# Resultado correcto! , Agrego paréntesis.
total_heigth_meters = (hat_height_cm + my_heigth_cm) / 100
print("total_heigth_meters =", total_heigth_meters) # total_heigth_meters = 2.15


# Funciones integradas para trabajar con números
print(min(1, 2, 3)) # 1
print(max(1, 2, 3)) # 3

# abs devuelve el valor absoluto de un argumento
print(abs(32))  # 32
print(abs(-32)) # 32

# Funciones que devuelven sus argumentos al tipo correspondiente
print(float(10)) # 10.0
print(int(3.33)) # 3
# Incluso se pueden invocar mediante strings
print(int('807') + 1) # 808
