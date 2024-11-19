import logging
from utils.file_ops import concat_dir_and_filename, ensure_directory_exists

def setup_logging(log_dir,log_filename):
    
    ensure_directory_exists(log_dir)

    log_file_path = concat_dir_and_filename(log_dir,log_filename)

    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Logging baslatildi.")