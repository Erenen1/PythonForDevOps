from datetime import datetime

def generate_filename_with_timestamp(prefix="backup",endfix="sql"):
	timestamp = datetime.now().strftime("%Y-%m-%d")
	return f"{prefix}_{timestamp}.{endfix}"