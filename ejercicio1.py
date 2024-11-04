import psutil

# Función para listar procesos que contienen una palabra clave en su nombre.
def listar_procesos(palabra_clave):
    procesos_encontrados = []
    
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            # Comprobacion de la palabra clave con el nombre del proceso. Si existe se almacena
            if palabra_clave.lower() in proc.info['name'].lower():
                procesos_encontrados.append({
                    'name': proc.info['name'],
                    'pid': proc.info['pid'],   
                    'memory': proc.info['memory_info'].rss 
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Manejador de excepciones:
            # NoSuchProcess: Si el proceso ya no existe.
            # AccessDenied: No tenemos permisos para acceder.
            # ZombieProcess: Se termina de ejecutar y no se vuelve a iniciar.
            pass


    if procesos_encontrados:
        for proceso in procesos_encontrados:
            print(f"Nombre: {proceso['name']}, PID: {proceso['pid']}, Memoria: {proceso['memory']} bytes")
    else:
        print(f"No se encontraron procesos con la palabra clave '{palabra_clave}'.")

# Función para finalizar un proceso por su nombre.
def finalizar_proceso(nombre_proceso):
    try:
        for proc in psutil.process_iter(['name', 'pid']):
            #Buscamos el proceso por su nombre
            if nombre_proceso.lower() in proc.info['name'].lower():
                proc.terminate()
                proc.wait()
                print(f"Proceso {proc.info['name']} con PID {proc.info['pid']} finalizado.")
                return
        print(f"No se encontró ningún proceso con el nombre '{nombre_proceso}'.")
    except psutil.NoSuchProcess:
        print("El proceso ya no existe.")
    except psutil.AccessDenied:
        print("No tienes permisos para finalizar este proceso.") 
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Función para mostrar el menú interactivo al usuario.
def mostrar_menu():
    while True:
        print("\nMenú de Gestión de Procesos")
        print("1. Listar procesos activos")
        print("2. Finalizar un proceso")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            palabra_clave = input("Introduce la palabra clave para buscar procesos: ")
            listar_procesos(palabra_clave)
        elif opcion == '2':
            nombre_proceso = input("Introduce el nombre del proceso que quieres finalizar: ")
            finalizar_proceso(nombre_proceso)
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.") 


if __name__ == "__main__":
    mostrar_menu()
