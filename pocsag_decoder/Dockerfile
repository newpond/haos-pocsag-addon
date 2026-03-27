FROM ghcr.io/home-assistant/aarch64-base:latest

RUN apk add --no-cache \
    rtl-sdr \
    multimon-ng \
    mosquitto-clients \
    python3 \
    py3-pip \
    jq

COPY run.sh /run.sh
COPY parser.py /parser.py

RUN chmod +x /run.sh

CMD [ "/run.sh" ]
