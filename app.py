from src.get_files import FixDownload
from time import sleep
from src.event_handler import Handler
from pathlib import Path
from watchdog.observers import Observer

if __name__ == "__main__":
    FixDownload()
    path = str(Path.home() / "Downloads")
    my_handler = Handler()
    observer = Observer()
    observer.schedule(my_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
