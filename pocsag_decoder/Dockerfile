ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache \
    rtl-sdr \
    mosquitto-clients \
    python3 \
    jq \
    curl

# Install multimon-ng from Alpine (available on aarch64 in HA base images)
RUN apk add --no-cache multimon-ng || true

COPY run.sh /run.sh
COPY parser.py /parser.py

RUN chmod +x /run.sh

CMD [ "/run.sh" ]
