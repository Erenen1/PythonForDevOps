from utils.date_utils import generate_filename_with_timestamp
from utils.file_ops import ensure_directory_exists,concat_dir_and_filename
from config.settings import SYSTEM_BACKUP_DIR,DATABASE_BACKUP_DIR
from backup.core import take_system_backup

def system_backup():
    ensure_directory_exists(SYSTEM_BACKUP_DIR)
    backup_filename = generate_filename_with_timestamp(prefix="system_backup_daily",endfix="tar.gz")
    backup_file_path = concat_dir_and_filename(SYSTEM_BACKUP_DIR,backup_filename)
    take_system_backup(backup_file_path)
    return backup_file_path

