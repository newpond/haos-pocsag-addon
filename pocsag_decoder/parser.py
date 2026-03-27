import sys
import json
import re
import time
import subprocess

TOPIC = None
pattern = re.compile(r"POCSAG\d+: Address:\s*(\d+).*?Alpha:\s*(.*)")

cache = {}

def dedup(key, ttl=15):
    now = time.time()
    if key in cache and now - cache[key] < ttl:
        return True
    cache[key] = now
    return False

def publish(payload):
    subprocess.run([
        "mosquitto_pub",
        "-h", "core-mosquitto",
        "-t", TOPIC,
        "-m", json.dumps(payload)
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

for line in sys.stdin:
    m = pattern.search(line)
    if not m:
        continue

    ric, msg = m.group(1), m.group(2).strip()
    key = f"{ric}:{msg}"

    if dedup(key):
        continue

    publish({
        "ric": int(ric),
        "message": msg,
        "ts": int(time.time())
    })
    publish({
        "ric": int(ric),
        "message": msg,
        "ts": int(time.time())
    })    })

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
