from config.settings import CPU_PERCENT_TRESHOLD
import logging
from hardware.cpu import get_cpu_usage
from services.email_service import EmailService
from services.alert_service import AlertService 
from config.settings import SMTP_SERVER,SMTP_PORT,SMTP_USERNAME,SMTP_PASSWORD,RECIPIENTS 

def check_cpu_usage(cpu_percent):
    if cpu_percent > CPU_PERCENT_TRESHOLD:
        cpu_percent_in_minute =get_cpu_usage(interval=15)
        if cpu_percent_in_minute > CPU_PERCENT_TRESHOLD:
            logging.warning(f"CPU kullanimi kritik seviyede: {cpu_percent_in_minute}%")
            EmailServiceInstance = EmailService(SMTP_SERVER,SMTP_PORT,SMTP_USERNAME,SMTP_PASSWORD)
            AlertServiceInstance = AlertService(EmailServiceInstance,RECIPIENTS)
            AlertServiceInstance.send_alert(
                subject="CPU Usage Alert",
                message="CPU kullanimi %90 uzerine cikt!"
            )