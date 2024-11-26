from hardware.disk import get_disk_usage
from config.settings import DIR,FILENAME
from config.logging_config import setup_logging
from checks.disk_check import check_disk_usage

if __name__ == "__main__":
    setup_logging(DIR,FILENAME)
    disk_percent = get_disk_usage()
    check_disk_usage(disk_percent)
