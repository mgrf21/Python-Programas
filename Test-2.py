# Este ejemplo ilustra el utilizar mismo programa con terminación "py"
import numpy as np
print("Ejemplo de prueba 2")
arr= np.array([100,2.7,8.333,4, 0.5])
print(arr)
print(type(arr))
x= 1 #inicializando variables
y= 0
for i in range (6): # haciendo las iteracción y detectando valores
    x = x + 1
    print("La suma va en ",x)
    if x==4:
        print ("numero detectado")
        y = 1
    print ("y= ", y)
print("El resultado es: ",x)
w = input ("ingresa tu color favorito; ? ")
tuedad = int(input("ingresa tu edad: ? "))
tupeso = float(input("Cual es tu peso: ? "))
# Imprimiendo los datos

print("tu color favorito es: ",w)
print("Tu edad registrada es: ", tuedad)
print("Tu peso registrado es: ", tupeso)