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
from Funciones import write, read, create
import os

print("Ingrese un numero del 1 al 5")
number = input("Numero: ")

#while exit == "1":

match number:

    case "1":
        create()
    case "2":
        write() 
    case "3":
        read() 


