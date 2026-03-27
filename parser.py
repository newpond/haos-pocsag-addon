import sys
import json
import subprocess
import re
import time

MQTT_HOST = sys.argv[1]
TOPIC = sys.argv[2]

pattern = re.compile(r"POCSAG\d+: Address:\s*(\d+).*?Alpha:\s*(.*)")

last_messages = {}
DEDUP_SECONDS = 30

def is_duplicate(ric, msg):
    key = f"{ric}:{msg}"
    now = time.time()

    if key in last_messages:
        if now - last_messages[key] < DEDUP_SECONDS:
            return True

    last_messages[key] = now
    return False

for line in sys.stdin:
    match = pattern.search(line)
    if match:
        ric = int(match.group(1))
        msg = match.group(2).strip()

        if not msg:
            continue

        if is_duplicate(ric, msg):
            continue

        payload = json.dumps({
            "ric": ric,
            "message": msg,
            "timestamp": int(time.time())
        })

        subprocess.run([
            "mosquitto_pub",
            "-h", MQTT_HOST,
            "-t", TOPIC,
            "-m", payload
        ])
