# **Linux Backup and Cloud Storage Automation**

This Python project is designed to automate the backup of Linux systems and store the backups securely in the cloud using AWS S3. It provides a robust and scalable solution for both system and database backups, offering options for daily and weekly schedules. The project is lightweight, modular, and configurable to meet your specific backup needs.

---

## **Features and Skills Gained**

### **Features**
- Automates **system backups** (e.g., `/etc`, `/var/www`, `/root`).
- Automates **database backups** using tools like `pg_dump`.
- Uploads backups to **AWS S3** with support for storage class configurations (e.g., `STANDARD_IA`).
- Cleans up old backups to save storage space.
- Fully configurable paths and settings via `config/settings.py`.
- Cron job support for **daily** and **weekly** backup schedules.

### **Skills Gained**
- Mastery of **Python subprocess module** for executing system commands.
- Understanding of AWS services (S3) and the **boto3** library.
- Configuration management using `settings.py`.
- Designing Python projects with modularity and scalability in mind.
- Creating and scheduling **cron jobs** for automation.
- Managing **storage classes** in AWS S3 (e.g., `STANDARD`, `STANDARD_IA`).
- Logging and error handling in Python scripts.

---

## **How to Use This Project**

### **Setup Instructions**
1. **Clone the Repository:**
   ```bash
    git clone https://github.com/your-repo/linux-backup-automation.git
    cd linux-backup-automation
   ```
2. **Set Up a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Configure AWS CLI**
    ```bash
    aws configure
    ```
    provide the following:
    - **Access Key ID:** Your AWS Access Key ID.
    - **Default region:** Your AWS Secret Access Key.
    - **Default region:** ``(us-east-1)``.
    - **Output format:** Leave as default (``json``).
5. **Edit Configuration in** `config/settings.py`
    ```python
    DATABASE_BACKUP_DIR_DAILY = "/path/to/daily/database/backups"
    SYSTEM_BACKUP_DIR_WEEKLY = "/path/to/weekly/system/backups"

    AWS_BUCKET_NAME = "your-s3-bucket-name"
    AWS_REGION = "your-aws-region"

    POSTGRESQL_USERNAME = "your-db-username"
    POSTGRESQL_HOSTNAME = "your-db-hostname"
    POSTGRESQL_DATABASE_NAME = "your-db-name"
    POSTGRESQL_PASSWORD = "your-db-password"
    ```
6. **Run the Scripts:**
    - For daily backups(e.g., database):
        ```bash
        python3 scripts/run_daily_backup.py
        ```
    - For Weekly backups(e.g., system)
        ```bash
        python3 scripts/run_weekly_backup.py
        ```
## Why `STANDARD_IA`?
The``STANDARD_IA`` (Infrequent Access) storage class was chosen for its cost-efficiency and reliability.

### **Pros:**
- **Cost-Effective:** Lower storage costs compared to `STANDARD`.
- **Fast Access:** Similar access speeds to `STANDARD`.
### **Cons:**
- **Retrieval Costs:** Higher cost per GB for data retrieval.
- **Minimum Storage Duration:** Requires objects to be stored for at least 30 days.
### **Usage Goals:**
- Best suited for backups that are not accessed frequently but need fast retrieval during recovery scenarios.
## Scheduling with Cron Jobs
To automate the scripts, set up the following cron jobs:
1. **Edit Cron Jobs:**
    ```bash
    crontab -e
    ```
2. **Add the Following Entries::**
- **Daily Backup (run_daily_backup.py):** Runs every day at 2:00 AM.
    ```bash
    0 2 * * * /path/to/venv/bin/python3 /path/to/scripts/run_daily_backup.py
    ```
- **Weekly Backup (run_weekly_backup.py):** Runs every Sunday at 3:00 AM.
    ```bash
    0 3 * * 0 /path/to/venv/bin/python3 /path/to/scripts/run_weekly_backup.py
    ```
3. **Verify Cron Jobs:**
    ```bash
    crontab -l
    ```
## Daily and Weekly Backup Details
### Daily Backup
- Takes a **PostgreSQL database dump** using ``pg_dump``.
- Compresses the dump and uploads it to S3 under the ``STANDARD_IA`` storage class.
### Weekly Backup
- Creates a complete backup of critical system directories (``/etc``, ``/var/www``, ``/root``, ``/usr/local``).
- Compresses the backup and uploads it to S3 under the ``STANDARD_IA`` storage class.
## Local Installation Summary
1. Clone the repo and set up a virtual environment.
2. Install dependencies using ``pip install -r requirements.txt``.
3. Configure AWS CLI with ``aws configure``.
4. Edit ``config/settings.py`` for your environment.
