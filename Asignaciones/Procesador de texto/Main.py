"""
1- Lectura básica: Crea un programa que lea un archivo datos.txt 
( y lo cree si no exista, con su contenido) y muestre su contenido por pantalla.

2- Conteo de líneas: Escribe un programa que cuente el número de líneas en un archivo poema.txt. 
(pista: deben usar el método .readlines y len() )

3- Búsqueda simple: crea un archivo "notas.txt ", Lee el archivo notas.txt e imprime todas las líneas 
que contengan la palabra "importante". (pista, deben usar condicionales y el método strip() )

4- Copiador de archivos: Crea un programa que copie el contenido de origen.txt en un nuevo archivo 
copia.txt.

5-Contador de palabras: Cuenta cuántas veces aparece la palabra "Python" en un archivo creado por
ustedes llamado documento.txt.( Pista: Deben usar condicionales, el método split() y el método count()




"""
from Funciones import write, read, create, erased, line_count, search_word, word_counter, copy
import os
import pyfiglet

while True:

    os.system("cls")
    ascii_art = pyfiglet.figlet_format("Menu", font="slant")
    print(ascii_art)
    print("\n¿Que desea hacer?")
    print("1- Crear archivo de texto")
    print("2- Escribir en un archivo de texto")
    print("3- Leer contenido del archivo de texto")
    print("4- Borrar archivo de texto")
    print("5- Contador de lineas")
    print("6- Buscador de palabra")
    print("7- Contador de palabra")
    print("8- Copiar contenido de un archivo de texto a otro")
    print("Ingrese 0 para salir")
    number = input("\nNumero: ")



    match number:

        case "1":
                create()
        case "2":
                write() 
        case "3":
                read() 
        case "4":
                erased()
        case "5":
                line_count()

        case "6":
                search_word()

        case "7":
                word_counter()

        case "8":
                copy()

        case "0":
                os.system("cls")
                ascii_art = pyfiglet.figlet_format("Saliendo del programa... Gracias por usarme :)", font="slant")
                print(ascii_art)
                input("\nPresione enter para salir...")
                os.system("cls") 
                break

        case _:
            os.system("cls") 
            print("♠"*50)
            print("Opción inválida.")
            input("\nPresione enter para salir...")
            os.system("cls") 
