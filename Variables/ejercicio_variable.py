
lastName="Apellido aqui" #colocar tu apellido entre las comillas

"""
treads no tiene memes asi que
twitter >>>> treadzzz
"""

#DECLARACIÓN DE VARIABLES (impuestos)

city="Caracas"
actual_temp=21
have_pets=True
birth_date=2001

print (" Mi ciudad es: ", city, "\n", "Temperatura actual: ", actual_temp, "\n", 
       "Tienes mascotas!", have_pets, "\n", "Fecha de nacimiento: ", birth_date, "\n\n")

animal, animal_age, is_a_mammal= "Gato", 2, True

print("Mi mascota es un: ", animal, "\n", "Su edad es: ", animal_age, " años", "\n", "Es un mamifero: ",
      is_a_mammal, "\n\n")


#EJERCICIOS DE LISTAS


colors=["yellow", "blue", "red", "turquoise", "green"]
prices=[1.22, 1.5, 22.7, 459.21, 0.25]
mix=["Balatro GOTY", 5000000, True, [0,1,1,2,3,5,8,13]]

print("El color es: ", colors[2])
print("El precio es: ", prices[4])
print("El número en la lista anidada es: ", mix[3][1], "\n\n")


#Ejercicios de Tuplas


week_days=("lunes ", "martes ", "miercoles ", "jueves ", "viernes ", "sabado ", "domingo ")
coordinates=(-48.8767, -123.3933)

latitud= coordinates[0]
altitud= coordinates[1]

print("Altitud:", altitud, "\n\n")

#Ejercicios de Diccionarios

book={
    "titulo": "El chico sin color",
    "autor" : "Haruki Murakami",
    "año de publicación": 30,
    "disponible": True
}

students={
    "nombre": "Antonio",
    "edad": 20,
    "carrera": "XXX",
    "materias favoritas":["lengua", "matematicas", "biologia",]

}


print(book["autor"])