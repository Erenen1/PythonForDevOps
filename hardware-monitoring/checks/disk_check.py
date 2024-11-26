from config.settings import DISK_PERCENT_TRESHOLD
from hardware.disk import get_disk_usage
import logging
from services.email_service import EmailService
from services.alert_service import AlertService 
from config.settings import SMTP_SERVER,SMTP_PORT,SMTP_USERNAME,SMTP_PASSWORD,RECIPIENTS 

def check_disk_usage(disk_percent):
    if disk_percent > DISK_PERCENT_TRESHOLD:
        logging.warning(f"Disk kullanimi kritik seviyede: {disk_percent}%")
        print("ALERT: Disk kullanimi çok yüksek!")
        EmailServiceInstance = EmailService(SMTP_SERVER,SMTP_PORT,SMTP_USERNAME,SMTP_PASSWORD)
        AlertServiceInstance = AlertService(EmailServiceInstance,RECIPIENTS)
        AlertServiceInstance.send_alert(
            subject="DISK Usage Alert",
            message="DISK kullanimi %90 uzerine cikt!"
        )