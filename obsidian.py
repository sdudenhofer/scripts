from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import git 

class watchFile:
    folder_location = "/home/sethd/Documents/obsidian/Personal"    

    def __init__(self):
        self.observer = Observer()
    
    def run(self):
        handler = Handler()
        self.observer.schedule(handler, self.folder_location, recursive=True)
        self.observer.start()
        return self.folder_location
        try:
            while True:
                time.sleep(30)
        except KeyboardInterrupt:
            self.observer.stop()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        repo = git.Repo(self.folder_location)
        existing_branch = repo.heads('main')
        origin = repo.remote(name="origin")
        if event.is_directory:
            return
        if event.event_type == "created":
            repo.index.add(event.src_path)
        elif event.event_type == "modified":
            repo.index.add(event.src_path)
        repo.index.commit(f"file {event.src_path} modified")
        origin.push()


if __name__ == "__main__":
    watch = watchFile()
    watch.run()