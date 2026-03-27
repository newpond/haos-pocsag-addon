ARG BUILD_FROM
FROM $BUILD_FROM

# Install only what's available
RUN apk add --no-cache \
    rtl-sdr \
    mosquitto-clients \
    python3 \
    jq \
    curl

# Download prebuilt multimon-ng binary (ARM64)
RUN curl -L -o /usr/local/bin/multimon-ng \
    https://github.com/EliasOenal/multimon-ng/releases/download/1.2.0/multimon-ng-linux-arm64 && \
    chmod +x /usr/local/bin/multimon-ng

COPY run.sh /run.sh
COPY parser.py /parser.py

RUN chmod +x /run.sh

CMD [ "/run.sh" ]
