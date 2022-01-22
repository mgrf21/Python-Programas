# Lafunción se llama “dibujo”,dibuja un rectángulo y las variables(parámetros)que solicita son el ancho y el alto de la figura 
def dibujo(width,height):# se utiliza una estructura de control.ifwidth <10or height <10:print("Error: La figura es muy pequeña o muy grande.")quit()# Dibujala parte superior de la figura 
   print("*"*width)# Dibujalos lados,en este caso se utiliza un bucle para el valor del alto de la figura 
   for i in range(height -2):
       print("*"+" "*(width -2)+"*")# Dibujala parte inferior 
       print("*"*width)
dibujo(5,5)
dibujo(10,10)