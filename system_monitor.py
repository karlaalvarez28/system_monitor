import requests
from datetime import datetime

# This is a simple system monitor that checks the status of a website.
# Added a fake URL for demonstration purposes of the 'DOWN' alert.
systems_to_monitor = [
    "https://www.google.com",
    "https://workspace.amer.dsv.com/logon/LogonPoint/tmindex.html", 
    "https://example.com/nonexistent"
]

print("-- System Monitor ---")
print("Starting system monitor...")
print("Pinging systems... ")

# We open a text file in 'append' mode ('a'). 
# This means it won't delete previous logs, it will just add new lines at the bottom.
with open("system_monitor_log.txt", mode="a", encoding="utf-8") as log_file:
    
    for url in systems_to_monitor:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                log_message = f"[{timestamp}] [UP] {url} is running correctly."
            else:
                log_message = f"[{timestamp}] [WARNING] {url} is DOWN (Status Code: {response.status_code})"
        except requests.exceptions.RequestException as error:
            log_message = f"[{timestamp}] [DOWN] Critical failure reaching {url}"

        print(log_message)
        log_file.write(log_message + "\n")

print("System monitor completed.")  