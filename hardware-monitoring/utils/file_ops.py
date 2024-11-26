import os
import logging

def concat_dir_and_filename(dir,filename):
    return os.path.join(dir,filename)


def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
        except Exception as e:
            raise