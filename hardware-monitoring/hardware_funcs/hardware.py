import psutil
from config.logging_config import setup_logging
from utils.date_utils import generate_filename_with_timestamp


def get_cpu_usage(interval=1):
    return psutil.cpu_percent(interval=interval)

def get_ram_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent
