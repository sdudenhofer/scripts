from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import git 

class watchFile:
    folder_location = "/home/sethd/Documents/obsidian/Personal"    
    repo = git.Repo(folder_location)
    existing_branch = repo.heads('main')
    origin = repo.remote(name="origin")


    def __init__(self):
        self.observer = Observer()
    
    def run(self):
        handler = Handler()
        self.observer.schedule(handler, self.folder_location, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(30)
        except KeyboardInterrupt:
            self.observer.stop()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):

        if event.is_directory:
            return
        if event.event_type == "created":
            print(f"Created: {event.src_path}")
        elif event.event_type == "modified":
            print(f"Modified: {event.src_path}")


if __name__ == "__main__":
    watch = watchFile()
    watch.run()