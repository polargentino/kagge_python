# Organizandolos nombres de las flores en un string de Python
flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

print(type(flowers)) # <class 'str'>
print(flowers)       # pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle

# Organizandolos nombres de las flores en una lista de Python
flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list)) # <class'list'>
print(flowers_list)       # ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold', 'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood', 'globe thistle']
# La lista tiene diez entradas
print(len(flowers_list))  # 10

# Indexación
print("First entry:", flowers_list[0])  # First entry: pink primrose
print("Second entry:", flowers_list[7]) # Second entry: bird of paradise

# La lista tiene una longitud de diez(10), por lo que nos referimos a la entrada final con un 9
print("Last entry:", flowers_list[9])   # Last entry: globe thistle

# Slicing: (Rebanar)
# Para extraer las primeras tres entradas
print("First three entries:" ,flowers_list[:3]) # First three entries: ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells']
# Para extraer las últimas dos entradas
print("Final two entries:" ,flowers_list[-2:])  # Final two entries: ['monkshood', 'globe thistle']

# Eliminar elementos
flowers_list.remove("globe thistle")
print(flowers_list) # ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold', 'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood']

# Agregar elementos
flowers_list.append("snapdragon")
print(flowers_list) # ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold', 'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood', 'snapdragon']

# Las listas no son sòlo para strings
# Venta de libros de tapa dura en la primera semana de abril del año 2000
# hardcover_sales: lista de nùmeros enteros
hardcover_sales = [139, 129, 172, 139, 191, 168, 170]
# Se puede obtener longitud, extraer entradas individuales y ampliar lista
print("Length of the list:" ,len(hardcover_sales)) # Length of the list: 7
print("Entry at index 2:" ,hardcover_sales[2])     # Entry at index 2: 172

# Obtener el nùmero mìnimo y nùmero màximo
print("Minimum:" ,min(hardcover_sales))  # Minimum: 129
print("Maximum:" ,max(hardcover_sales))  # Maximum: 191

# Para agregar cada elemento en la lista use sum().
print("Total book sold in one week:", sum(hardcover_sales)) # Total book sold in one week: 1108

# Promedio de libros vendidos en los primeros cinco dìas
