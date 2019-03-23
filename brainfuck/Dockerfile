FROM python:3.6-alpine
RUN apk update && \
    apk add python3 py3-pip openssl-dev

WORKDIR /opt/brainfuck
RUN mkdir -p /opt/brainfuck

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /opt/brainfuck

EXPOSE 9183

ENTRYPOINT ["/opt/brainfuck/docker-entrypoint.sh"]
