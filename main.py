import re
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter as tk
from tkinter import simpledialog

class WatchdogHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Archivo o carpeta creado: {event.src_path}")

    def on_deleted(self, event):
        print(f"Archivo o carpeta eliminado: {event.src_path}")

    def on_modified(self, event):
        print(f"Archivo o carpeta modificado: {event.src_path}")
        user_input = prompt_user_input(event.src_path)
        if user_input:
            if validar_nombre_archivo(event.src_path):
                if renombrar_archivo(event.src_path, user_input):
                    print(f"Archivo renombrado: {user_input}")
                else:
                    print("Error al renombrar el archivo.")
            else:
                print("Nombre de archivo inválido.")

def renombrar_archivo(archivo_actual, nuevo_nombre):
    """
    Renombra un archivo o carpeta según el nuevo nombre.
    
    Args:
        archivo_actual (str): Ruta del archivo o carpeta actual.
        nuevo_nombre (str): Nuevo nombre para el archivo o carpeta.
    """
    try:
        directorio,_= os.path.split(archivo_actual)
        nueva_ruta = os.path.join(directorio, nuevo_nombre)
        os.rename(archivo_actual, nueva_ruta)
        return True
    except Exception as e:
        print(f"Error al renombrar el archivo: {e}")

def validar_nombre_archivo(nombre_archivo):
    """
    Valida el nombre de un archivo o carpeta según los requisitos de Windows y Linux/macOS.
    
    Args:
        nombre_archivo (str): Nombre del archivo o carpeta a validar.

    returns:
        bool: Verdadero si el nombre es válido, falso en caso contrario.
    """
    if not nombre_archivo.strip():
        return False, "El nombre está vacío o contiene solo espacios."
    
    if os.name == 'nt':  # Windows
        caracteres_invalidos = r'[<>:"/\\|?*\x00-\x1f]'
        nombres_reservados = {"CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
                            "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"}
    else:  # Linux/macOS
        caracteres_invalidos = r'[/\x00]'
        nombres_reservados = set()

    if re.search(caracteres_invalidos, nombre_archivo):
        return False, f"El nombre contiene caracteres inválidos: {caracteres_invalidos}"

    nombre_sin_ext = os.path.splitext(nombre_archivo)[0]
    if nombre_sin_ext.upper() in nombres_reservados:
        return False, "El nombre es un nombre reservado en Windows."

    if len(nombre_archivo) > 255:
        return False, "El nombre excede los 255 caracteres permitidos."

    return True, "El nombre es válido."

# Función para desplegar el cuadro de texto con tkinter
def prompt_user_input(route):
    # Crear una ventana de tkinter
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    route = route.split('/')[-1]

    user_input = simpledialog.askstring("Input", "Archivo modificado. Ingresa un texto:", initialvalue = route)

    root.destroy()  # Destruir la ventana después de cerrar el cuadro de diálogo
    return user_input

def start_monitoring(folder_to_watch):
    event_handler = WatchdogHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=True)
    observer.start()

    print(f"Supervisando la carpeta: {folder_to_watch}")

    try:
        while True:
            time.sleep(1)  # Mantén el programa en ejecución
    except KeyboardInterrupt:
        print("Deteniendo la supervisión...")
        observer.stop()

    observer.join()

if __name__ == "__main__":
    folder_to_watch = "c:/Users/ASUS/Videos"  # Cambia esto por la ruta de la carpeta que quieres supervisar
    start_monitoring(folder_to_watch)