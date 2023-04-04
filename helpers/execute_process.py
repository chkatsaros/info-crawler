import subprocess
from helpers.loader import Loader

def execute_process(cmd, msg = None, custom_stdout = None):
    if not msg is None: loader = Loader(msg).start()
    try: 
        process = subprocess.Popen(cmd, stdout=custom_stdout)
        process.wait()
        if not msg is None: loader.stop()
    except KeyboardInterrupt:
        process.kill()
        print(f'\nAborting...')
        exit()