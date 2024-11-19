FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV AWS_ACCESS_KEY_ID="Your access key id"
ENV AWS_SECRET_ACCESS_KEY="Your secret access key"
ENV AWS_REGION="Your aws region"

RUN mkdir -p /home/eren/backups/database /home/eren/backups/system

CMD ["python", "scripts/run_daily_backup.py"]
