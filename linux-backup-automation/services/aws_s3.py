import boto3
import logging

s3_client = boto3.client("s3")

def upload_to_s3(file_path:str,bucket_name:str,s3_object_name=None):
	if s3_object_name is None:
		s3_object_name = file_path.split("/")[-1]

	s3_client = boto3.client("s3")

	try:
		s3_client.upload_file(file_path,bucket_name,s3_object_name,ExtraArgs={"StorageClass":"STANDARD_IA"})
		logging.info(f"Dosya başarıyla yüklendi: {file_path} -> s3://{bucket_name}/{s3_object_name}")
		return True
	except FileNotFoundError:
		logging.error(f"Dosya bulunamadı: {file_path}")
		return False
	except Exception as e:
		logging.error(f"S3'e yüklenirken hata oluştu: {e}")
		return False
