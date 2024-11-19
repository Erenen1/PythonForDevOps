import os
import logging

def is_valid_file(file_path):
    return os.path.isfile(file_path)

def is_valid_directory(directory_path):
    return os.path.isdir(directory_path)

def is_dir_exists(directory_path):
    if not os.path.exists(directory_path):
        logging.warning(f"{directory_path} mevcut değil veya geçerli bir dizin değil.")
        return False
    return True