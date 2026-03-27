import sys
import json
import subprocess
import re
import time

TOPIC = sys.argv[1]

pattern = re.compile(r"POCSAG\d+: Address:\s*(\d+).*?Alpha:\s*(.*)")

seen_cache = {}
DEDUP = 20

def dup(key):
    now = time.time()
    if key in seen_cache and now - seen_cache[key] < DEDUP:
        return True
    seen_cache[key] = now
    return False

for line in sys.stdin:
    m = pattern.search(line)
    if not m:
        continue

    ric = int(m.group(1))
    msg = m.group(2).strip()

    key = f"{ric}:{msg}"
    if dup(key):
        continue

    payload = json.dumps({
        "ric": ric,
        "message": msg,
        "ts": int(time.time())
    })

    subprocess.run([
        "mosquitto_pub",
        "-h", "core-mosquitto",
        "-t", TOPIC,
        "-m", payload
    ])
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
