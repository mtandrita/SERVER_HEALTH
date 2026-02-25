import psutil
import csv
import time
from datetime import datetime

file_path = "../data/system_metrics.csv"

# Write header (only once)
with open(file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "timestamp",
        "cpu_percent",
        "ram_percent",
        "bytes_sent",
        "bytes_received"
    ])

print("Starting metrics collection... Press Ctrl+C to stop.")

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    net = psutil.net_io_counters()

    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            timestamp,
            cpu,
            ram,
            net.bytes_sent,
            net.bytes_recv
        ])

    print(f"[{timestamp}] Data saved")
    time.sleep(5)