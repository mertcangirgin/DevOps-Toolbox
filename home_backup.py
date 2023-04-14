import os
import datetime
import tarfile

# Step 1: Get server name
server_name = os.uname().nodename

# Step 2: Compress /home directory to specified directory on NAS server
backup_dir = "/path/to/backup/dir/"
backup_filename = f"{server_name}_{datetime.datetime.today().strftime('%Y-%m-%d')}.tar.gz"
backup_path = os.path.join(backup_dir, backup_filename)

with tarfile.open(backup_path, "w:gz") as tar:
    tar.add("/home")

# Step 3: Write server name, date, and result to home_backup.log file
log_path = "/path/to/log/file/home_backup.log"
with open(log_path, "a") as log_file:
    log_file.write(f"{server_name}\t{datetime.datetime.today().strftime('%Y-%m-%d')}\tSuccess\n")

# Step 4: Set up cron job to run this script every Sunday at 01:00
# Add the following line to your crontab file (run 'crontab -e' to edit it):
# 0 1 * * 0 /usr/bin/python3 /path/to/script.py
