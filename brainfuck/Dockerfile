FROM python:3.6-alpine
RUN apk update && \
    apk add python3 py3-pip openssl-dev

WORKDIR /opt/brainfuck
RUN mkdir -p /opt/brainfuck

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /opt/brainfuck

VOLUME ["/opt/brainfuck"]

RUN for d in CTFd/plugins/*; do \
      if [ -f "$d/requirements.txt" ]; then \
        pip install -r $d/requirements.txt; \
      fi; \
    done;


EXPOSE 9183

ENTRYPOINT ["/opt/brainfuck/docker-entrypoint.sh"]
