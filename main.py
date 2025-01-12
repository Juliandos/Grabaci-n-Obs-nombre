from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class WatchdogHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Archivo o carpeta creado: {event.src_path}")

    def on_deleted(self, event):
        print(f"Archivo o carpeta eliminado: {event.src_path}")

    def on_modified(self, event):
        print(f"Archivo o carpeta modificado: {event.src_path}")

    def on_moved(self, event):
        print(f"Archivo o carpeta movido: {event.src_path} a {event.dest_path}")

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
    folder_to_watch = "/"  # Cambia esto por la ruta de la carpeta que quieres supervisar
    start_monitoring(folder_to_watch)
