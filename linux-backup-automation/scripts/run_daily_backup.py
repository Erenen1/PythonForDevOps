from backup.db_backup import database_backup
from config.logging_config import setup_logging
from utils.date_utils import generate_filename_with_timestamp
from config.settings import LOG_DIR_DAILY
from backup.core import clean_old_backups

if __name__ == "__main__":
        log_filename = generate_filename_with_timestamp(prefix="daily_backup",endfix="log")
        setup_logging(LOG_DIR_DAILY,log_filename)
        backup_path = database_backup()
        clean_old_backups(backup_path)
