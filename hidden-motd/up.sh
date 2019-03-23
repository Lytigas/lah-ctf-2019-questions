#!/usr/bin/env sh
docker build -t motd .
docker stop motd_instance
docker container rm motd_instance
if [ $# -eq 0 ]; then
    docker run -p '5556:5556' --name motd_instance -d motd
else
    docker run -p '5556:5556' --name motd_instance motd
fi
