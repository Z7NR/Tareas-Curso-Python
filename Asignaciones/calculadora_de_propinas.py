"""
Ejercicio 1: Calculadora de Propinas
Contexto: Acabas de cenar en un restaurante y quieres calcular la propina  
Tareas: 
1. Pedir al usuario el total de la cuenta  
2. Preguntar si el servicio fue excelente (15%), bueno (12%) o regular (10%)  
3. Calcular la propina según la calidad del servicio  
4. Preguntar si dividir la cuenta entre N personas  
5. Mostrar:  
   - Total con propina  
   - Propina individual  
   - Total por persona  
"""


print("/" * 57, "\n")
total = int(input("Introduzca monto a pagar:"))

print("\n","/" * 57, "\n")
valo = int(input("¿Cual fue la valoracion sobre el servicio?: \n\n 1-Excelente \n 2-Bueno \n 3-Regular \n\n:"))

print("\n","/" * 57, "\n")
div = int(input("¿Quiere dividir la cuenta? \n\n 0-No \n 1-Si \n\n:"))
boole = bool(div)

if div == True:
    print("\n","/" * 57, "\n")
    pers = int(input("Introduce la cantidad de personas:"))

if valo == 1:
    
    propina = total * 0.15

    print("\n","/" * 57, "\n")
    print("\n El monto asciende a:", abs(propina + total))
    print("\n La propina a pagar es de:", abs(propina))
    while div == True:
    
        print("\n Monto por persona:", abs(total / pers ))
        break
    

elif valo == 2:

    propina = total * 0.12

    print("\n","/" * 57, "\n")
    print("\n El monto asciende a:", abs(propina + total))
    print("\n La propina a pagar es de:", abs(propina))
   
    while div == True:
    
        print("\n Monto por persona:", abs(total / pers ))
        break

elif valo == 3:

    propina = total * 0.10

    print("\n","/" * 57, "\n")
    print("\n El monto asciende a:", abs(propina + total))
    print("\n La propina a pagar es de:", abs(propina))
    
    while div == True:
    
        print("\n Monto por persona:", abs(total / pers ))
        break
else:

    print("\n No es una opcion correcta \n Intente de nuevo")

