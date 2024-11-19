from utils.date_utils import generate_filename_with_timestamp
from utils.file_ops import ensure_directory_exists,concat_dir_and_filename
from config.settings import DATABASE_BACKUP_DIR
from backup.core import take_database_backup

def database_backup():
	ensure_directory_exists(DATABASE_BACKUP_DIR)
	backup_filename = generate_filename_with_timestamp(prefix="pg_backup_daily",endfix="sql")
	backup_file_path = concat_dir_and_filename(DATABASE_BACKUP_DIR,backup_filename)
	take_database_backup(backup_file_path)
	return backup_file_path
