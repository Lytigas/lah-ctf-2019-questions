FROM alpine
RUN apk update && \
    apk add socat bash

WORKDIR /opt/motd
RUN mkdir -p /opt/motd

COPY . /opt/motd

EXPOSE 5556

ENTRYPOINT ["/opt/motd/server.sh"]
