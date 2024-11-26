from hardware.cpu import get_cpu_usage
from config.settings import DIR,FILENAME
from config.logging_config import setup_logging
from checks.cpu_check import check_cpu_usage

if __name__ == "__main__":
    setup_logging(DIR,FILENAME)
    cpu_percent = get_cpu_usage(1)
    check_cpu_usage(cpu_percent=cpu_percent)