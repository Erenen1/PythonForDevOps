import smtplib
from email.mime.text import MIMEText
import logging
from email.mime.multipart import MIMEMultipart

class EmailService:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, subject, body, to_email):
        try:
            msg = MIMEMultipart()
            msg["From"] = self.username
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.username, self.password)
                server.sendmail(self.username, to_email, msg.as_string())

            print(f"E-posta başarıyla gönderildi: {to_email}")
            logging.info(f"E-posta başarıyla gönderildi: {to_email}")
        except Exception as e:
            print(f"E-posta gönderim hatası: {e}")
            logging.warning(f"E-posta gönderim hatası: {e}")

