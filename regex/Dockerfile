FROM python:3.6-alpine
RUN apk update && \
    apk add python3 py3-pip openssl-dev

WORKDIR /opt/regexer
RUN mkdir -p /opt/regexer

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /opt/regexer

VOLUME ["/opt/regexer"]

RUN for d in CTFd/plugins/*; do \
      if [ -f "$d/requirements.txt" ]; then \
        pip install -r $d/requirements.txt; \
      fi; \
    done;


EXPOSE 8796

ENTRYPOINT ["/opt/regexer/docker-entrypoint.sh"]
