# Enunciado:
# Pide al usuario 5 números enteros:
# 1. Clasifica cada número en:
#    -"Pequeño" si es menor que 10.
#    -"Mediano" si está entre 10 y 50.
#    -"Grande" si es mayor que 50.
#    -"Cero" si es 0.
# 2. Al final, muestra cuántos números hubo en cada categoría.

""""
i = 0



while i < 5:

    if i <= 5:
        
        i +=1
        num = int(input("Ingrese 5 veces numeros enteros: "))

        if num < 10 and num >= 1:
            
            print(num, " es pequeño")

        elif num >= 10 and num < 51:
        
            print(num, " es mediano")

        elif num >= 51:

            print(num, " es grande")

        elif num ==0:

            print(num, " es igual a Cero")
    
    else:
            
        break
"""

"""""
numeros = []
peq = []
med = []
gra = []
i = 0


for i in range(5):
        numero = int(input(f"Ingresa el numero #{i+1}: "))
        numeros.append(numero)

        
        i +=1
        
        if numero < 10 and numero >= 1:
            
            print(numero, " es pequeño")

        elif numero >= 10 and numero < 51:
        
            print(numero, " es mediano")

        elif numero >= 51:

            print(numero, " es grande")

        elif numero == 0:

            print(numero, " es igual a Cero")
    
        else:
            
            break
"""
array = []
peq = []
med = []
gra = []
i = 0


for i in range(5):
        numero = int(input(f"Ingresa el numero #{i+1}: "))
        array.append(numero)


for numero in array:
    if numero < 10 and numero >= 1:

        print(numero, " es pequeño")

    elif numero >= 10 and numero < 51:
        
            print(numero, " es mediano")

    elif numero >= 51:

            print(numero, " es grande")

    elif numero == 0:

            print(numero, " es igual a Cero")
    
    else:
            
            break      
