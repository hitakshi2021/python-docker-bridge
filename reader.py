import time
import os

file_path = "/shared_data/logs.txt"
print("Reader started... Waiting for data...")

while True:
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            lines = f.readlines()
            if lines:
                print(f"Reader sees latest -> {lines[-1].strip()}", flush=True)
    else:
        print("File not created yet...", flush=True)
        
    time.sleep(5)