# Función de una sucesión geométrica 
def sumGeometric(a,r,n):# Si el radio tiene un valor de uno 
   if r ==1:
       return a * n 
   # Calcula la suma geométrica cuando el radio es diferente de uno 
   s = a*(1-r **n)/(1-r)
   #regresa el valor de s 
   return s
Resultado = sumGeometric(2,2,2)
print("Resultado = ",Resultado)