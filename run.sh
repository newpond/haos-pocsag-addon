#!/usr/bin/with-contenv bash

FREQ=$(jq --raw-output ".frequency" /data/options.json)
GAIN=$(jq --raw-output ".gain" /data/options.json)
MQTT=$(jq --raw-output ".mqtt_host" /data/options.json)
TOPIC=$(jq --raw-output ".mqtt_topic" /data/options.json)
BAUD=$(jq --raw-output ".baud" /data/options.json)

echo "Starting POCSAG decoder..."
echo "Frequency: ${FREQ} MHz | Gain: ${GAIN} | Baud: ${BAUD}"

rtl_fm -f ${FREQ}M -M fm -s 22050 -g ${GAIN} | \
multimon-ng -t raw -a ${BAUD} - | \
python3 /parser.py "${MQTT}" "${TOPIC}"
