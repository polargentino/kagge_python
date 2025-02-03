# Organizandolos nombres de las flores en un string de Python
flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

print(type(flowers))
print(flowers)

# Organizandolos nombres de las flores en una lista de Python
flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(flowers_list)
# La lista tiene diez entradas
print(len(flowers_list))

# Indexación
print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[7])

# La lista tiene una longitud de diez(10), por lo que nos referimos a la entrada final con un 9
print("Last entry:", flowers_list[9])

# Slicing: (Rebanar)
# Para extraer las primeras tres entradas
print("First three entries:" ,flowers_list[:3])
# Para extraer las últimas dos entradas
print("Final two entries:" ,flowers_list[-2:])

# Eliminar elementos
flowers_list.remove("globe thistle")
print(flowers_list)

# Agregar elementos
flowers_list.append("snapdragon")
print(flowers_list)

# Las listas no son sòlo para strings
# Venta de libros de tapa dura en la primera semana de abril del año 2000
# hardcover_sales: lista de nùmeros enteros
hardcover_sales = [139, 129, 172, 139, 191, 168, 170]
# Se puede obtener longitud, extraer entradas individuales y ampliar lista
print("Length of the list:" ,len(hardcover_sales))
print("Entry at index 2:" ,hardcover_sales[2])

# Obtener el nùmero mìnimo y nùmero màximo
print("Minimum:" ,min(hardcover_sales))
print("Maximum:" ,max(hardcover_sales))

# Para agregar cada elemento en la lista use sum().
print("Total book sold in one week:", sum(hardcover_sales))

# Promedio de libros vendidos en los primeros cinco dìas
