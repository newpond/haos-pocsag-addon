ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache \
    rtl-sdr \
    multimon-ng \
    mosquitto-clients \
    python3 \
    jq

COPY run.sh /run.sh
COPY parser.py /parser.py

RUN chmod +x /run.sh

CMD [ "/run.sh" ]
