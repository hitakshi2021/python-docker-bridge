import time
import os
from datetime import datetime

user = os.getenv("UERNAME" ,"Hitakshi")
file_path = "/shared_data/logs.txt"

print(f"writer started for : {user}...")

count = 1
while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{timestamp}] message #{count} from {user}\n"

    with open(file_path, "a") as f:
        f.write(message)

    print(f"written : {message.strip()}", flush=True)
    count = count + 1
    time.sleep(5) 
