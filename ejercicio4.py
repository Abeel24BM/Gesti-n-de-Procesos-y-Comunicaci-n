import subprocess
import pyperclip
import time
import os

def descargar_archivo_ftp(servidor, usuario, contrasena, archivo):
    try:
        # Comando para FTP, el archivo es descargado y guardado en el directorio actual
        ftp_command = f"open {servidor}\n{usuario}\n{contrasena}\nget {archivo}\nbye\n"
        # Ejecutamos el comando FTp
        proceso_ftp = subprocess.Popen(['ftp', '-n'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = proceso_ftp.communicate(ftp_command)

        #Comprobacion
        if proceso_ftp.returncode == 0:
            print(f"Archivo '{archivo}' descargado exitosamente.")
            return True
        else:
            print(f"Error al descargar el archivo: {stderr}")
            return False
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return False

def copiar_al_portapapeles(archivo):
    try:
        with open(archivo, 'r') as f:
            contenido = f.read()
            pyperclip.copy(contenido)
            print("Contenido copiado al portapapeles.")
    except Exception as e:
        print(f"No se pudo copiar el contenido al portapapeles: {e}")

def verificar_portapapeles(copia_anterior):
    while True:
        time.sleep(2)
        nuevo_contenido = pyperclip.paste()
        if nuevo_contenido != copia_anterior:
            print("El contenido del portapapeles ha cambiado.")
            copia_anterior = nuevo_contenido

def main():
    #https://test.rebex.net/
    servidor_ftp = "ftp.dlptest.com"
    usuario_ftp = "dlpuser@dlptest.com"
    contrasena_ftp = "fLDScD4Ynth0p4OJ6bW6qCxjh"
    archivo_a_descargar = "text.txt"

    #Descargamos el archivo
    if descargar_archivo_ftp(servidor_ftp, usuario_ftp, contrasena_ftp, archivo_a_descargar):
        copiar_al_portapapeles(archivo_a_descargar)
        contenido_inicial = pyperclip.paste()
        verificar_portapapeles(contenido_inicial)

if __name__ == "__main__":
    main()
