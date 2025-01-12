from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import tkinter as tk
from tkinter import simpledialog

class WatchdogHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Archivo o carpeta creado: {event.src_path}")
        user_input = prompt_user_input()
        if user_input:
            print(f"Texto ingresado: {user_input}")

    def on_deleted(self, event):
        print(f"Archivo o carpeta eliminado: {event.src_path}")

    def on_modified(self, event):
        print(f"Archivo o carpeta modificado: {event.src_path}")

    def on_moved(self, event):
        print(f"Archivo o carpeta movido: {event.src_path} a {event.dest_path}")

# Función para desplegar el cuadro de texto con tkinter
def prompt_user_input():
    # Crear una ventana de tkinter
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Mostrar un cuadro de diálogo para que el usuario ingrese texto
    user_input = simpledialog.askstring("Input", "Archivo modificado. Ingresa un texto:")

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