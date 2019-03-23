#!/usr/bin/env sh
docker build -t regexer .
docker stop regexer_instance
docker container rm regexer_instance
if [ $# -eq 0 ]; then
    docker run -p '8796:8796' --name regexer_instance -d regexer
else
    docker run -p '8796:8796' --name regexer_instance regexer
fi
