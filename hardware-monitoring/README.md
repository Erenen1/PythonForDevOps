
# Hardware Monitoring Script

This project provides a Python-based hardware monitoring system that checks the CPU, RAM, and disk usage. If any of these resources exceed a predefined threshold for a specific duration, an alert is triggered, and a notification email is sent.

---

## Features

- **CPU Monitoring**: Sends an alert if the CPU usage exceeds 80% for 1 minute.
- **RAM Monitoring**: Sends an alert if RAM usage crosses the threshold for 1 minute.
- **Disk Monitoring**: Monitors disk usage and alerts if space usage exceeds the set threshold for 5 minutes.
- **Email Notification**: Alerts are sent to the configured email address.

---

## Project Structure

- `checks/`: Contains scripts for resource checks (CPU, RAM, disk).
- `config/`: Configuration files for thresholds and email settings.
- `hardware/`: Core logic for interacting with system hardware.
- `scripts/`: Cronjob-ready scripts to execute periodic checks.
- `services/`: Handles alerting and email notification services.
- `utils/`: Helper functions and reusable utilities.

---

## Prerequisites

- Python 3.x installed on your system.
- Email server credentials for notifications.
- Virtual environment activated for running the scripts.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Erenen1/PythonForDevOps.git
   cd hardware-monitoring
   ```

2. Set up the virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Configure thresholds and email settings in `config/`.

---

## Usage

### Setting up Cron Jobs

1. **CPU Monitoring**:
   - Runs every minute:
     ```bash
     * * * * * /path/to/python /path/to/hardware-monitoring/checks/run_cpu_script.py
     ```

2. **RAM Monitoring**:
   - Runs every minute:
     ```bash
     * * * * * /path/to/python /path/to/hardware-monitoring/checks/run_ram_script.py
     ```

3. **Disk Monitoring**:
   - Runs every 5 minutes:
     ```bash
     */5 * * * * /path/to/python /path/to/hardware-monitoring/checks/run_disk_script.py
     ```

### Running the Scripts Manually

You can also run any of the scripts directly:
```bash
python3 -m scripts.run_cpu_script
python3 -m scripts.run_ram_script
python3 -m scripts.run_disk_script
```

---

## Configuration

- **Thresholds**:
  Update the threshold values for CPU, RAM, and DISK in the `config/` folder.

- **Email Settings**:
  Configure the sender's email credentials and the recipient's email address in `config/settings`.