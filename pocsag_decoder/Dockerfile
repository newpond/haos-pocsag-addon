ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache \
    rtl-sdr \
    multimon-ng \
    mosquitto-clients \
    python3 \
    jq

COPY rootfs/ /
RUN chmod a+x /etc/services.d/*/run
