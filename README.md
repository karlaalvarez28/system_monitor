# System Health Monitor

## Overview
In global IT operations, system availability is critical. Waiting for end-users to report an outage creates delays. 

This Python automation script acts as a monitoring tool. It checks the health and availability of platforms (such as Google, Citrix Workspace, and a fake site) and generates a timestamped log to track uptime and detect failures.

## Business Value
* **Automated Health Checks:** Replaces manual portal testing with an automated script.
* **Proactive Alerting Mindset:** Identifies connection timeouts and non-200 HTTP status codes instantly.
* **Historical Logging:** Automatically generates a persistent log file (`.txt`) with precise timestamps, essential for audit trails.

## Technologies Used
* **Python 3.x:** Programming language.
* **`requests` library:** Utilized to send HTTP GET requests and handle connection timeouts.
* **`datetime` module:** Timestamps every automated check for accurate historical tracking.
* **Exception Handling (`try/except`):** Ensures the script continues monitoring even if a target server completely drops the connection.

## How to Run It
1. Clone this repository to your local machine.
2. Ensure you have Python installed along with the requests library (`pip install requests`).
3. Run the script using the terminal:
   system_monitor.py
