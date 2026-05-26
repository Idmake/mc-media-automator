import os

def get_invalid_path_index(paths: list[str]):
    for index, path in enumerate(paths):
        if not os.path.exists(path):
            return index

    return -1