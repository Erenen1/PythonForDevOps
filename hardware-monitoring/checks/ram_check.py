from config.settings import RAM_PERCENT_TRESHOLD
from hardware.ram import get_ram_usage
import logging
import time
from services.email_service import EmailService
from services.alert_service import AlertService 
from config.settings import SMTP_SERVER,SMTP_PORT,SMTP_USERNAME,SMTP_PASSWORD,RECIPIENTS 


def check_ram_usage(ram_percent):
    print(ram_percent)
    if ram_percent > RAM_PERCENT_TRESHOLD:
        time.sleep(15)
        ram_percent_in_minute = get_ram_usage()
        if ram_percent_in_minute > RAM_PERCENT_TRESHOLD:
            logging.warning(f"RAM kullanimi kritik seviyede: {ram_percent}%")
            print("ALERT: RAM kullanimi çok yüksek!")
            EmailServiceInstance = EmailService(SMTP_SERVER,SMTP_PORT,SMTP_USERNAME,SMTP_PASSWORD)
            AlertServiceInstance = AlertService(EmailServiceInstance,RECIPIENTS)
            AlertServiceInstance.send_alert(
                subject="RAM Usage Alert",
                message="RAM kullanimi %90 uzerine cikt!"
            )