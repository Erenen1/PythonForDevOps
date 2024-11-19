import shutil


def make_archive(output_dir,type,input_dir):
    archive_path = output_dir
    if "." in output_dir:
        output_dir = output_dir.split(".")[0]

    try:
            shutil.make_archive(output_dir,type,input_dir)
    except:
            print("hata olustu")

make_archive("/home/eren/PythonForDevOps/backup_script/requirements.tar.gz")