from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


print ("Наблюдение началось")
class Observation(FileSystemEventHandler):
    def on_modified(self, event):
        
        with open("file.txt", "r", encoding='utf8') as file:
               print(file.read())
observer = Observer()
observer.schedule(Observation(), path="/home/sasha/pr4")
observer.start()
try:
    while 1:
        pass
except KeyboardInterrupt:
    observer.stop()
    print("Наблюдение было завершено")