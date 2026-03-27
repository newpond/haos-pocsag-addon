#!/usr/bin/with-contenv bash

FREQ=$(jq -r ".frequency" /data/options.json)
GAIN=$(jq -r ".gain" /data/options.json)
TOPIC=$(jq -r ".mqtt_topic" /data/options.json)
BAUD=$(jq -r ".baud" /data/options.json)

rtl_fm -f ${FREQ}M -M fm -s 22050 -g ${GAIN} | \
multimon-ng -t raw -a ${BAUD} - | \
python3 /parser.py "${TOPIC}"
