import psutil

def get_ram_usage():
    memory = psutil.virtual_memory()
    return memory.percent
