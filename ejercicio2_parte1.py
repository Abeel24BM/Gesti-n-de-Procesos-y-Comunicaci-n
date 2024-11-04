import os

def main():
    pipe_read, pipe_write = os.pipe()
    #Hijo
    pid = os.fork()

    if pid > 0:
        os.close(pipe_read)

        mensaje = "Yoooo soy tu padre!"
        os.write(pipe_write, mensaje.encode())
        os.close(pipe_write)
        os.wait()
        
        #Respuesta del hijo
        pipe_read, pipe_write = os.pipe()  
        pid = os.fork()
        
        if pid == 0:
            os.close(pipe_write)
            mensaje_modificado = os.read(pipe_read, 1024).decode()
            print(f"Padre recibió: {mensaje_modificado}")
            os.close(pipe_read)
            os._exit(0)
    else:
        # Proceso hijo
        os.close(pipe_write)

        # Mensaje del padre
        mensaje = os.read(pipe_read, 1024).decode()
        print(f"Hijo recibió: {mensaje}")

        mensaje_modificado = mensaje.upper()  
        os.close(pipe_read)

        # Respuesta al padre
        pipe_read, pipe_write = os.pipe() 
        os.write(pipe_write, mensaje_modificado.encode()) 
        os.close(pipe_write)
        os._exit(0)

if __name__ == "__main__":
    main()
