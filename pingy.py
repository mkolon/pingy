import pandas as pd
import subprocess
import platform

# Load targets file
df = pd.read_csv("targets", header=None, names=["IP", "Label"])

# Determine the ping command flag based on OS
ping_count_flag = "-n" if platform.system().lower() == "windows" else "-c"

# Loop through each target and ping
for index, row in df.iterrows():
    ip = row["IP"]
    label = row["Label"].strip('"')
    try:
        result = subprocess.run(
            ["ping", ping_count_flag, "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        status = "reachable" if result.returncode == 0 else "unreachable"
    except Exception as e:
        status = f"error: {e}"
    print(f"{label} ({ip}): {status}")

