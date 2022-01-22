# El usuario ingresa el límite de datos recopilados 
limit = int(input("Ingresa un número mayor a 3: ?  ")) 
# Muestra los números positivos en múltiplos de 3 
print("Número de multiplos de tres hasta llegar al número", limit, "son: ") 
N_veces = 0
for i in range(3, limit + 1, 3): 
    print(i)
    N_veces = N_veces + 1
print("Se tienen ", N_veces, "multiplos")
