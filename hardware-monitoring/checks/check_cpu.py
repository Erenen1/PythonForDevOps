from config.settings import CPU_PERCENT_TRESHOLD
import logging
from hardware_funcs.hardware import get_cpu_usage

def check_cpu_usage(cpu_percent):
    if cpu_percent > CPU_PERCENT_TRESHOLD:
        cpu_percent_in_minute =get_cpu_usage(interval=15)
        if cpu_percent_in_minute > CPU_PERCENT_TRESHOLD:
            # mail gönder alert!!!
            print("alert")
            logging.warning("cpu usage is too much")