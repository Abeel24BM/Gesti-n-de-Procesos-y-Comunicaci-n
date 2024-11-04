import subprocess
import time

def ejecutar_sincrono():
    print("Ejecutando Notepad de manera síncrona...")
    inicio = time.time()
    #Bloqueo
    proceso = subprocess.Popen("notepad.exe") 
    time.sleep(1)
    
    proceso.terminate() 

    fin = time.time()
    print(f"Tiempo de ejecución síncrona: {fin - inicio:.2f} segundos")

    

def ejecutar_asincrono():
    print("Ejecutando Notepad de manera asíncrona...")
    inicio = time.time()
    #No hay bloqueo
    proceso = subprocess.Popen("notepad.exe")  
    fin = time.time()
    print(f"Tiempo de ejecución asíncrona (tiempo hasta lanzar Notepad): {fin - inicio} segundos")
    
    proceso.wait()
    proceso.terminate()
    print("Notepad ha sido cerrado.")

def mostrar_menu():
    while True:
        print("\nMenú de Ejecución de Programas")
        print("1. Ejecutar Notepad síncronamente")
        print("2. Ejecutar Notepad asíncronamente")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            ejecutar_sincrono()
        elif opcion == '2':
            ejecutar_asincrono()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
