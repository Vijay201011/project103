import sys
import os
import shutil
import time
import random 

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/prasn/Downloads"
to_dir = "C:/Users/prasn/Documents"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"hey,{event.src_path} has been created")

    def on_deleted(self,event):
        print(f"hey, someone deleted {event.src_path}")

# Initialize Event Handler Class
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


while True:
    time.sleep(2)
    print("running...")

    