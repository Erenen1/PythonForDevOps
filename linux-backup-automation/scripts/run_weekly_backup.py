from utils.date_utils import generate_filename_with_timestamp
from config.logging_config import setup_logging
from config.settings import LOG_DIR_WEEKLY,AWS_BUCKET_NAME
from backup.system_backup import system_backup
from services.aws_s3 import upload_to_s3
from backup.core import clean_old_backups

if __name__ == "__main__":
        log_filename = generate_filename_with_timestamp(prefix="weekly_backup",endfix="log")
        setup_logging(LOG_DIR_WEEKLY,log_filename)
        
        backup_path = system_backup()
        print()
        clean_old_backups(backup_path, days_to_keep=28)
        upload_to_s3(backup_path,AWS_BUCKET_NAME)

        
