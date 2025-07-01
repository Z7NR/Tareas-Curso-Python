#Función simple:
#Crea una función saludar() que imprima "¡Hola, bienvenido al curso!"
'''''
def saludar():
    print("¡Hola, bienvenido al curso")

saludar()
'''''

#Función con parámetros:
#Crea una función area_rectangulo(largo, ancho) que calcule y retorne el área de un rectángulo.

''''
def area_rectangulo(alt, anc):
    area_rectangulo = alt * anc
    return area_rectangulo
    
val1 = int(input("introduzca altura:"))
val2 = int(input("introduzca ancho:"))

val3 = area_rectangulo(val1, val2)

print(f" el areá del rectangulo es: {val3} cm²")
'''
''''
#Función con condicional:
#Crea una función es_par(numero) que retorne True si el número es par y False si es impar.


def es_par(num):

    if num % 2 == 0:
        return (True)
    else:
        return (False)    
        
    
val = int(input("Introduce un numero: "))

resul = es_par(val)

print(f" es: {resul}")

'''
""""
#Lambda básica:

#Crea una lambda que eleve un número al cuadrado. Pruébala con el número 5.

potencia = lambda num1: num1 ** 2

num1= int(input(f"numero: "))

print(potencia(num1))
"""

#Lambda con condicionales:
#Crea una lambda que reciba un número y retorne:

#"Positivo" si es mayor que 0.

#"Negativo" si es menor que 0.

#"Cero" si es igual a 0.

def condicional(num):

    if num > 0:
        return ("Positivo")
    
    elif num < 0:
        return ("Negativo")
   
    else:
        return ("Cero")    
        
    
val = int(input("Introduce un numero: "))

resul = condicional(val)

print(f" es: {resul}")

