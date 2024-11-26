from utils.date_utils import generate_filename_with_timestamp

CPU_PERCENT_TRESHOLD=20
RAM_PERCENT_TRESHOLD=20
DISK_PERCENT_TRESHOLD=90
FILENAME=generate_filename_with_timestamp("hardware_monitoring","log")
DIR= "/home/eren/Documentation"
SMTP_SERVER="smtp.winnerlist.net"
SMTP_PORT=465
SMTP_USERNAME="alerts@winnerlist.net"
SMTP_PASSWORD="winnerlist_alerts_mail_password"
RECIPIENTS=["security@winnerlist.net","it-admin@winnerlist.net"]
