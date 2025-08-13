import os, re
import pyfiglet

def create():
    """
    Crea un archivo de texto en la ruta "./Asignaciones/Procesador de texto/"
    Pide el nombre del archivo al usuario y lo crea.
    Si el archivo existe, pregunta al usuario si desea sobrescribirlo.

    Returns:
        bool: True si el archivo se creó correctamente. False si no lo hizo.
    """
    try:
        while True:
            os.system("cls") 
            ascii_art = pyfiglet.figlet_format("Crear archivo", font="slant")
            print(ascii_art)
            print("♠"*50)
            name = input("Nombre de archivo (sin extensión): ")
            if not re.match(r"^[\w-]+$", name): #Solo permite, letras, numeros, "_" y "-". Impide espacios, dejar en blanco y caracteres especiales.
                print("Por favor, limitese a escribir el nombre del archivo sin incluir '.txt' o algún otro tipo de extensión " \
                "y sin dejar en blanco")
                continue
            ruta = f"./Asignaciones/Procesador de texto/{name}.txt"

            if os.path.exists(ruta): #comprueba si el archivo existe
                    os.system("cls") 
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
                with open(ruta, "w"):
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
        while True:
            os.system("cls") 
            ascii_art = pyfiglet.figlet_format("Escribir en archivo", font="slant")
            print(ascii_art)
            print("♠"*50)
            name = input("Nombre de archivo (sin extensión): ")
            if not re.match(r"^[\w-]+$", name):
                print("Por favor, limitese a escribir el nombre del archivo sin incluir '.txt' o algún otro tipo de extensión " \
                "y sin dejar en blanco")
                continue
            ruta = f"./Asignaciones/Procesador de texto/{name}.txt"

            if os.path.exists(ruta): #comprueba si el archivo existe
                    os.system("cls") 
                    content = input("Ingrese el contenido del archivo: ")
                    with open(ruta, "a") as document:
                        document.write("\n\n" + content)
                    return True
            else:
                print("♠"*50)
                print(f"El archivo '{name}' no existe.")
                print("♠"*50)
                print("¿Que desea hacer?")
                print("1- ¿Deseas crear el archivo desde cero Y escribir en él?")
                print("2- Finalizar proceso")
                opcion = input(": ")

                match opcion:
                        
                    case "1":
                        content = input("Ingrese el contenido del archivo: ")
                        with open(ruta, "a") as document:
                            document.write(content)
                        print("♠" * 50)
                        print(f"El archivo '{name}' se ha creado y se ha escrito en él.")
                        return True
                        
                        
                    case "2":
                        print("♠"*50)
                        print("Operación cancelada.")
                        return True
                        
                    case _:
                        print("♠"*50)
                        print("Opción inválida.")
            
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return False

    except IOError as e:
        print(f"Error de entrada/salida: {e}")
        return False

def read(): 
    try:
        
        while True:
            os.system("cls") 
            ascii_art = pyfiglet.figlet_format("Leer archivo", font="slant")
            print(ascii_art)
            print("♠"*50)
            name = input("Nombre de archivo (sin extensión): ")
            if not re.match(r"^[\w-]+$", name):
                print("Por favor, limitese a escribir el nombre del archivo sin incluir '.txt' o algún otro tipo de extensión " \
                "y sin dejar en blanco")
                continue
            ruta = f"./Asignaciones/Procesador de texto/{name}.txt"

            if os.path.exists(ruta): #comprueba si el archivo existe
                os.system("cls") 
                
                with open(ruta, "r") as document:
                    print("♦" *30, "\n")
                    print("Leyendo archivo...\n")
                    print("♦" *30, "\n")
                    print(document.read())
                    input("\nPresione Enter para volver al menú...")
                    return True
                

            
            else: 
                print(f"El archivo {name} no existe.")
                print("¿Que desea hacer?")
                print("1- Introducir el nombre de nuevo")
                print("2- Finalizar proceso")
                opcion=input(": ")

                match opcion:
                        
                    case "1":    
                        continue
                        
                    case "2":
                        print("♠"*50)
                        print("Operación cancelada.")
                        return
                        
                    case _:
                        print("♠"*50)
                        print("Opción inválida.")

    except FileNotFoundError:
        print("Archivo no encontrado.")

        return False

    except IOError as e:
        print(f"Error de entrada/salida: {e}")

        return False
    
def erased():
    try:
       
        while True:
            os.system("cls") 
            ascii_art = pyfiglet.figlet_format("Borrar archivo", font="slant")
            print(ascii_art)
            print("♠"*50)
            name = input("Nombre de archivo (sin extensión): ")
            if not re.match(r"^[\w-]+$", name):
                print("Por favor, limitese a escribir el nombre del archivo sin incluir '.txt' o algún otro tipo de extensión " \
                "y sin dejar en blanco")
                continue
            ruta = f"./Asignaciones/Procesador de texto/{name}.txt"

            print(f"\n¿Estas seguro de querer borrar el archivo {name}? No podra ser recuperado despues")
            print("1- Continuar / 2- Colocar otro nombre / 3- Salir del programa")  
            decision=input(": ")

            if decision == "1":
                if os.path.exists(ruta): #comprueba si el archivo existe
                    os.remove(ruta)
                    print(f"Archivo {name} ha sido borrado satisfactoriamente")
                    input("\nPresione Enter para volver al menú...")
                    return True
                else: 
                        print(f"El archivo {name} no existe.")
                        print("¿Que desea hacer?")
                        print("1- Introducir el nombre de nuevo")
                        print("2- Finalizar proceso")
                        opcion=input(": ")

                        match opcion:
                                
                            case "1":    
                                continue
                                
                            case "2":
                                print("♠"*50)
                                print("Operación cancelada.")
                                return
                                
                            case _:
                                print("♠"*50)
                                print("Opción inválida.")
            elif decision == "2":
                return False
            elif decision == "3":
                exit()
            else:
                print("Opción inválida")

    except FileNotFoundError:
        print("Archivo no encontrado.")

        return False

    except IOError as e:
        print(f"Error de entrada/salida: {e}")

        return False
    
def line_count():
    try:
        
        while True:
            os.system("cls") 
            ascii_art = pyfiglet.figlet_format("Conteo de lineas", font="slant")
            print(ascii_art)
            print("♠"*50)
            name = input("Nombre de archivo (sin extensión): ")
            if not re.match(r"^[\w-]+$", name):
                print("Por favor, limitese a escribir el nombre del archivo sin incluir '.txt' o algún otro tipo de extensión " \
                "y sin dejar en blanco")
                continue
            ruta = f"./Asignaciones/Procesador de texto/{name}.txt"

            if os.path.exists(ruta): #comprueba si el archivo existe
                os.system("cls") 
                
                with open(ruta, "r") as document:
                    print("♦" *30, "\n")
                    print("Analizando archivo...\n")
                    print("♦" *30, "\n")
                    lineas = document.readlines()

                    cantidad = len(lineas)
                    print(f"El archivo tiene {cantidad-2} líneas")
                    input("\nPresione Enter para volver al menú...")
                return True
                

            
            else: 
                print(f"El archivo {name} no existe.")
                print("¿Que desea hacer?")
                print("1- Introducir el nombre de nuevo")
                print("2- Finalizar proceso")
                opcion=input(": ")

                match opcion:
                        
                    case "1":    
                        continue
                        
                    case "2":
                        print("♠"*50)
                        print("Operación cancelada.")
                        return
                        
                    case _:
                        print("♠"*50)
                        print("Opción inválida.")

    except FileNotFoundError:
        print("Archivo no encontrado.")

        return False

    except IOError as e:
        print(f"Error de entrada/salida: {e}")

        return False

def search_word():
    try:
        
        while True:
            os.system("cls") 
            ascii_art = pyfiglet.figlet_format("Busqueda de palabra", font="slant")
            print(ascii_art)
            print("♠"*50)
            name = input("Nombre de archivo (sin extensión): ")
            if not re.match(r"^[\w-]+$", name):
                print("Por favor, limitese a escribir el nombre del archivo sin incluir '.txt' o algún otro tipo de extensión " \
                "y sin dejar en blanco")
                continue
            ruta = f"./Asignaciones/Procesador de texto/{name}.txt"

            if os.path.exists(ruta): #comprueba si el archivo existe
                os.system("cls") 
                
                with open(ruta, "r") as document:
                    print("¿Que palabra desea buscar?")
                    palabra = input(": ")
                    os.system("cls")
                    print("♦" *30, "\n")
                    print("Analizando archivo...\n")
                    print("♦" *30, "\n")
                    
                    find = False

                    for linea in document:
                        linea_limpia = linea.strip()

                        if palabra.lower() in linea_limpia.lower():
                            print(f"La palabra {palabra} se encuentra en la siguiente linea: {linea_limpia}") #imprime la linea en la que se encuentra la palabra 
                            find = True
                    
                    if not find:
                        print(f'La palabra "{palabra}" no se encontró en el archivo.')
                    
                    input("\nPresione Enter para volver al menú...")
                    return True
                

            
            else: 
                print(f"El archivo {name} no existe.")
                print("¿Que desea hacer?")
                print("1- Introducir el nombre de nuevo")
                print("2- Finalizar proceso")
                opcion=input(": ")

                match opcion:
                        
                    case "1":    
                        continue
                        
                    case "2":
                        print("♠"*50)
                        print("Operación cancelada.")
                        return
                        
                    case _:
                        print("♠"*50)
                        print("Opción inválida.")

    except FileNotFoundError:
        print("Archivo no encontrado.")

        return False

    except IOError as e:
        print(f"Error de entrada/salida: {e}")

        return False

def word_counter():
    
    try:
        
        while True:
            os.system("cls") 
            ascii_art = pyfiglet.figlet_format("Contador palabras", font="slant")
            print(ascii_art)
            print("♠"*50)
            name = input("Nombre de archivo (sin extensión): ")
            if not re.match(r"^[\w-]+$", name):
                print("Por favor, limitese a escribir el nombre del archivo sin incluir '.txt' o algún otro tipo de extensión " \
                "y sin dejar en blanco")
                continue
            ruta = f"./Asignaciones/Procesador de texto/{name}.txt"

            if os.path.exists(ruta): #comprueba si el archivo existe
                os.system("cls") 
                
                
                with open(ruta, "r") as document:
                    print("¿Que palabra desea buscar?")
                    palabra = input(": ")
                    os.system("cls")
                    print("♦" *30, "\n")
                    print("Analizando archivo...\n")
                    print("♦" *30, "\n")

                    find = False
                    count = 0

                    for linea in document:
                        linea_limpia = linea.strip()

                        if palabra.lower() in linea_limpia.lower():
                            count += linea_limpia.lower().count(palabra.lower())
                            find = True
                
                    if find:
                        print(f'La palabra "{palabra}" apareció {count} veces en el archivo.')
                    else:
                        print(f'La palabra "{palabra}" no se encontró en el archivo.')
       

                    input("\nPresione Enter para volver al menú...")
                    return True
                

            
            else: 
                print(f"El archivo {name} no existe.")
                print("¿Que desea hacer?")
                print("1- Introducir el nombre de nuevo")
                print("2- Finalizar proceso")
                opcion=input(": ")

                match opcion:
                        
                    case "1":    
                        continue
                        
                    case "2":
                        print("♠"*50)
                        print("Operación cancelada.")
                        return
                        
                    case _:
                        print("♠"*50)
                        print("Opción inválida.")

    except FileNotFoundError:
        print("Archivo no encontrado.")

        return False

    except IOError as e:
        print(f"Error de entrada/salida: {e}")

        return False

def copy():
    try:
        while True:
            os.system("cls") 
            ascii_art = pyfiglet.figlet_format("Copiar archivo", font="slant")
            print(ascii_art)
            print("♠" * 50)

            origen_name = input("Nombre del archivo origen (sin extensión): ")
            if not re.match(r"^[\w-]+$", origen_name):
                print("Por favor, escriba solo el nombre del archivo sin '.txt', sin espacios y sin dejar en blanco.")
                continue
            ruta_origen = f"./Asignaciones/Procesador de texto/{origen_name}.txt"

            if not os.path.exists(ruta_origen):
                print(f"El archivo {origen_name} no existe.")
                continue

            with open(ruta_origen, "r") as origen:
                contenido = origen.read()

            destino_name = input("Nombre del archivo destino (sin extensión): ")
            if not re.match(r"^[\w-]+$", destino_name):
                print("Por favor, escriba solo el nombre del archivo sin '.txt', sin espacios y sin dejar en blanco.")
                continue
            ruta_destino = f"./Asignaciones/Procesador de texto/{destino_name}.txt"

            with open(ruta_destino, "w") as destino:
                destino.write(contenido)

            print(f"\nArchivo copiado con éxito a: {ruta_destino}")
            break

    except FileNotFoundError:
        print("Archivo no encontrado.")
        return False

    except IOError as e:
        print(f"Error de entrada/salida: {e}")
        return False


# not re.match(r"^[\w-]+$", name): Solo permite, letras, numeros, "_" y "-". Impide espacios, dejar en blanco y caracteres especiales.
#def create(): #Función para crear un archivo de texto
#def write(): Funcion para escribir en el archivo de texto
#def read(): Funcion para leer el contenido en el archivo de texto
#def erased(): Funcion para borrar el archivo de texto
#os.path.exists(ruta): #comprueba si el archivo existe
#pyfiglet permite colocar letras tipo ascii