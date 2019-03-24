#!/usr/bin/env sh
docker build -t inject .
docker stop inject_instance
docker container rm inject_instance
if [ $# -eq 0 ]; then
    docker run -p '7895:7895' --name inject_instance -d inject
else
    docker run -p '7895:7895' --name inject_instance inject
fi
