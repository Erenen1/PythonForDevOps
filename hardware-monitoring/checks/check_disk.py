from config.settings import DISK_PERCENT_TRESHOLD
from hardware_funcs.hardware import get_disk_usage
import logging

def check_disk_usage(disk_percent):
    if disk_percent > DISK_PERCENT_TRESHOLD:
        logging.warning(f"Disk kullanımı kritik seviyede: {disk_percent}%")
        print("ALERT: Disk kullanımı çok yüksek!")
