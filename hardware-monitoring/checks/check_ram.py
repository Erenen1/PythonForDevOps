from config.settings import RAM_PERCENT_TRESHOLD
from hardware_funcs.hardware import get_ram_usage
import logging
import time

def check_ram_usage(ram_percent):
    print(ram_percent)
    if ram_percent > RAM_PERCENT_TRESHOLD:
        time.sleep(15)
        ram_percent_in_minute = get_ram_usage()
        if ram_percent_in_minute > RAM_PERCENT_TRESHOLD:
            print("alert")
