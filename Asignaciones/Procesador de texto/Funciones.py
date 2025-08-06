import os


def create():
    
    try:
       
        bucle = False
        
        while bucle == False:
            print("♠"*50)
            name = input("Nombre de archivo (sin extensión): ")
            ruta = f"./Tareas-Curso-Python/Asignaciones/Procesador de texto/{name}.txt"

            if os.path.exists(ruta): #comprueba si el archivo existe
                exist = True

                if exist == True:

                    print("♠"*50)
                    print(f"El archivo '{name}' ya existe.")
                    print("♠"*50)
                    print("¿Que desea hacer?")
                    print("1- ¿Deseas sobrescribir y, por lo tanto, BORRAR PERMANENTEMENTE el archivo existente?")
                    print("2- ¿Introducir otro nombre para el archivo?")
                    print("3- Finalizar proceso")
                    opcion = input(": ")

                    match opcion:
                        case "1":
                        
                            with open(ruta, "w"):

                                print("♠"*50)
                                print(f"Archivo {name} sobrescrito.") #sobrescribe el archivo

                                return True
                        
                        case "2":    
                                
                            continue
                        
                        case "3":
                            
                            print("♠"*50)
                            print("Operación cancelada.")
                            return
                        
                        case _:
                            
                            print("♠"*50)
                            print("Opción inválida.")
            
            else: 
            
                with open(ruta, "w") as document:
                    print(f"Archivo '{name}.txt' creado correctamente.")
                
                return True


    except FileNotFoundError:
        print("Archivo no encontrado.")

        return False

    except IOError as e:
        print(f"Error de entrada/salida: {e}")

        return False

def write(): 

    try:
       
        content = input("Ingrese el contenido del archivo: ")
        with open("./Tareas-Curso-Python/Asignaciones/Procesador de texto/relatos.txt", "w") as document:
            document.write(content)

        return True

    except FileNotFoundError:
        print("Archivo no encontrado.")
    
        return False

    except IOError as e:
        print(f"Error de entrada/salida: {e}")

        return False

def read(): 

    try:
        print("♦" *30, "\n")
        print("Leyendo archivo...\n")
        print("♦" *30, "\n")

        with open("./Tareas-Curso-Python/Asignaciones/Procesador de texto/relatos.txt", "r") as document:
            print(document.read())

        return True

    except FileNotFoundError:
        print("Archivo no encontrado.")

        return False

    except IOError as e:
        print(f"Error de entrada/salida: {e}")

        return False
    


       