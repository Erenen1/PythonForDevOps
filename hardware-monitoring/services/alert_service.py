class AlertService:
    def __init__(self, email_service, alert_recipients):
        self.email_service = email_service
        self.alert_recipients = alert_recipients

    def send_alert(self, subject, message):
        for recipient in self.alert_recipients:
            self.email_service.send_email(subject, message, recipient)
