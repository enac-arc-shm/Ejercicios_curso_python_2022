#Operaciones numericas
from cmath import sin #Libreria necesaria para operaciones complejas como seno, raiz, etc
import math

#Solicitar numeros y hacer la conversionde str a int 
numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa otro número: "))

#operaciones basicas de python
suma = numero1 + numero2
multiplicacion = numero1 * numero2
reciduo = numero1 % numero2
division_entera = numero1 // numero2
potencia = pow(numero1, numero2)
potencia = numero1 ** numero2

for i in range(numero2):
    potencia *= numero1

#Operacion seno de la libreria math 
seno = sin(numero1)

#impresion de operaciones
print("suma = ", suma, "multiplicacion = ",multiplicacion)
print("potenccia = ", potencia, "reciduo = ",reciduo)
print("division = ", division_entera)