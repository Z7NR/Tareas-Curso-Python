
print("¿Que desea hacer? \n", "Presione la tecla correspondiente \n\n", 
      "1-Sumar \n", "2-Restar \n\n", "3-Salir \n")

opcion=int(input(" "))

if opcion == 1:
   
    a = int(input("\nintroduzca primer valor: "))
    b = int(input("introduzca segundo valor: "))

    resultado = abs(a + b)

    print("\n", a, "+", b, "es igual a: ", resultado)

elif opcion == 2:
   
    a = int(input("\nintroduzca primer valor: "))
    b = int(input("introduzca segundo valor: "))

    resultado = abs(a - b)

    print("\n", a, "-", b, "es igual a: ", resultado)

elif opcion == 3:
    print("Adios")

else: 

    print("No es una opción valida. \n", "elija de nuevo")

