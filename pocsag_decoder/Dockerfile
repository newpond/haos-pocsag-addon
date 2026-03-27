ARG BUILD_FROM
FROM ghcr.io/home-assistant/aarch64-base-debian:latest

RUN apk add --no-cache \
    rtl-sdr \
    multimon-ng \
    mosquitto-clients \
    python3 \
    jq

COPY rootfs/ /
RUN chmod a+x /etc/services.d/*/run
