import os
import logging

def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
            logging.info(f"Dizin oluşturuldu: {directory_path}")
        except Exception as e:
            logging.error(f"Dizin oluşturulurken hata oluştu: {e}")
            raise
    logging.info(f"Dizin mevcut: {directory_path}")


def concat_dir_and_filename(dir,filename):
	return os.path.join(dir,filename)
