import os

def main():
    pipe_read, pipe_write = os.pipe()

    # Hijo
    pid = os.fork()

    if pid > 0:
        #Padre que lee el archivo y se lo manda al hijo
        os.close(pipe_read) 

        # Leer el archivo y se lo envia al hijo
        with open('ejercicio2_part2.txt', 'r') as archivo:
            contenido = archivo.read()
            os.write(pipe_write, contenido.encode())  
        os.close(pipe_write)
        os.wait()
        
        # Se crea una nueva pipe para recibir la respuesta
        pipe_read, pipe_write = os.pipe()
        pid = os.fork()

        if pid == 0:
            os.close(pipe_write)
            respuesta = os.read(pipe_read, 1024).decode()
            print(f"Padre recibió: {respuesta}")
            os.close(pipe_read)
            os._exit(0)

    else:
        # Proceso hijo
        os.close(pipe_write)

        # Mensaje del padre (archivo)
        contenido = os.read(pipe_read, 1024).decode()
        os.close(pipe_read)

        lineas = contenido.count('\n') + 1
        palabras = len(contenido.split())
        
        resultado = f"{lineas} líneas, {palabras} palabras"

        # Respuesta al padre
        pipe_read, pipe_write = os.pipe() 
        os.write(pipe_write, resultado.encode())
        os.close(pipe_write)
        os._exit(0)

if __name__ == "__main__":
    main()
