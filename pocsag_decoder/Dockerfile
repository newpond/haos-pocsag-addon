ARG BUILD_FROM
FROM $BUILD_FROM

# Install dependencies
RUN apk add --no-cache \
    rtl-sdr \
    rtl-sdr-dev \
    mosquitto-clients \
    python3 \
    jq \
    git \
    build-base \
    cmake

# Build multimon-ng from source
RUN git clone https://github.com/EliasOenal/multimon-ng /tmp/multimon-ng && \
    cd /tmp/multimon-ng && \
    mkdir build && cd build && \
    cmake .. && \
    make && \
    make install && \
    rm -rf /tmp/multimon-ng

COPY run.sh /run.sh
COPY parser.py /parser.py

RUN chmod +x /run.sh

CMD [ "/run.sh" ]
