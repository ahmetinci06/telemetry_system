import csv
from datetime import datetime
import os

def log_to_csv(data, filename="telemetry_log.csv"):
    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp"] + list(data.keys()))

        writer.writerow(
            [datetime.now().isoformat()] + list(data.values())
        )
