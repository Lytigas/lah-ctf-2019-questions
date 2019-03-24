FROM python:3.6-alpine
RUN apk update && \
    apk add python3 py3-pip openssl-dev

WORKDIR /opt/inject
RUN mkdir -p /opt/inject

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /opt/inject

EXPOSE 7895

ENTRYPOINT ["/opt/inject/docker-entrypoint.sh"]
