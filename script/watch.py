import datetime
import subprocess
import sys
import time
import traceback
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

assert __name__ == "__main__"

cwd = Path.cwd()
content = cwd / "content"
build = cwd / "script" / "build.py"
build_args = sys.argv[1:]


last_build = datetime.datetime(1818, 5, 5)
build_requested = True


class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        global build_requested
        build_requested = True


observer = Observer()
observer.schedule(Handler(), str(content), recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)

        if build_requested:
            print()
            try:
                args = ["python", str(build), *build_args]
                print(">", " ".join(args))
                subprocess.run(args)
            except:
                traceback.print_exc()
            print()
            build_requested = False

except KeyboardInterrupt:
    observer.stop()
observer.join()
