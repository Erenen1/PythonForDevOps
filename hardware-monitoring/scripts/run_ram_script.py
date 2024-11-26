from hardware.ram import get_ram_usage
from config.settings import DIR,FILENAME
from config.logging_config import setup_logging
from checks.ram_check import check_ram_usage

if __name__ == "__main__":
    setup_logging(DIR,FILENAME)
    ram_percent = get_ram_usage()
    check_ram_usage(ram_percent)
