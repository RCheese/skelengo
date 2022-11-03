import os


def clear_environment(prefix: str):
    for e in os.environ:
        if e.startswith(prefix):
            os.environ.pop(e)
