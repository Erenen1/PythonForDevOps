import subprocess
import os
import datetime
import logging
from config.settings import POSTGRESQL_USERNAME,POSTGRESQL_HOSTNAME,POSTGRESQL_DATABASE_NAME,POSTGRESQL_PASSWORD,SUDO_PASSWORD
from utils.date_utils import generate_filename_with_timestamp
from utils.file_ops import concat_dir_and_filename
from utils.validation import is_dir_exists, is_valid_directory,is_valid_file

def take_database_backup(backup_file_path):
    try:
        subprocess.run(["pg_dump", "-U", POSTGRESQL_USERNAME, "-h", POSTGRESQL_HOSTNAME, POSTGRESQL_DATABASE_NAME, "-f", backup_file_path],env={"PGPASSWORD":POSTGRESQL_PASSWORD},text=True,check=True)
        print("Yedek alma işlemi başarılı")
        logging.info("Yedek alma işlemi başarılı")
    except subprocess.CalledProcessError as e:
        print(f"Yedek alınırken hata oluştu:: {e.stderr}")
        logging.error(f"Yedek alınırken hata oluştu:: {e.stderr}")
        raise RuntimeError(f"Veritabanı yedekleme hatası:{e.stderr}")
    except Exception as e:
        logging.error(f"Bilinmeyen bir hata oluştu: {str(e)}")
        raise RuntimeError(f"Bilinmeyen hata: {str(e)}")

    
def take_system_backup(backup_dir):
    # command = ["echo","eren","|","sudo","-S","tar","-cpzf",backup_dir,"/etc","/var","/root","/usr/local"]
    command= f"echo {SUDO_PASSWORD} | sudo -S tar -cpzf {backup_dir} /etc /var /root /usr/local"
    try: 
        subprocess.run(command,check=True,shell=True)
        logging.info(f"Sistem yedekleme başarılı: {backup_dir}")
        return backup_dir
    except subprocess.CalledProcessError as e:
        logging.error(f"Yedekleme sırasında hata oluştu: {e.stderr}")
        raise RuntimeError(f"Sistem yedekleme hatası: {e.stderr}")
    except Exception as e:
        logging.error(f"Bilinmeyen bir hata oluştu: {str(e)}")
        raise RuntimeError(f"Bilinmeyen hata: {str(e)}")


def clean_old_backups(backup_dir, days_to_keep=7):

    cutoff_time = datetime.datetime.now() - datetime.timedelta(days=days_to_keep)

    if not is_dir_exists(backup_dir) or not is_valid_directory(backup_dir):
        logging.warning(f"{backup_dir} mevcut değil veya geçerli bir dizin değil.")
        return

    for filename in os.listdir(backup_dir):
        file_path = concat_dir_and_filename(backup_dir,filename)

        if is_valid_file(file_path):
            file_mtime = os.path.getmtime(file_path)
            if file_mtime < cutoff_time:
                try:
                    os.remove(file_path)
                    logging.info(f"Silindi: {file_path}")
                except Exception as e:
                    logging.error(f"Silinirken hata oluştu: {file_path}, {e}")

