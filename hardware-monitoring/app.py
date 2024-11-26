import logging
import psutil
from config.logging_config import setup_logging
from utils.date_utils import generate_filename_with_timestamp



def get_cpu_usage():
    """
    CPU kullanım yüzdesini döndürür.
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    return {
        "cpu_percent":cpu_percent
    }

def get_ram_usage():
    """
    RAM kullanımını GB ve yüzde cinsinden döndürür.
    """
    memory = psutil.virtual_memory()
    return {
        "total_gb": memory.total / (1024 ** 3),
        "used_gb": memory.used / (1024 ** 3),
        "free_gb": memory.available / (1024 ** 3),
        "percent": memory.percent
    }

def get_disk_usage():
    """
    Disk kullanımını GB ve yüzde cinsinden döndürür.
    """
    disk = psutil.disk_usage('/')
    return {
        "total_gb": disk.total / (1024 ** 3),
        "used_gb": disk.used / (1024 ** 3),
        "free_gb": disk.free / (1024 ** 3),
        "percent": disk.percent
    }

if __name__ == "__main__":
    filename = generate_filename_with_timestamp(prefix="hardware_monitor",endfix="log")
    dir = "/home/eren/Documents/"
    setup_logging(dir,filename)
    cpu = get_cpu_usage()
    ram = get_ram_usage()
    disk = get_disk_usage()
    logging.info(cpu)
    logging.info(ram)
    logging.info(disk)

