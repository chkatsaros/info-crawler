from pathlib import Path

from helpers.loader import Loader

def delete(artifact):
    file = Path(artifact)
    file.unlink()

def rm_artifacts(items):
    loader = Loader("Removing artifacts created...", "Artifacts removed!").start()
    for item in items:
        delete(item)
    loader.stop()