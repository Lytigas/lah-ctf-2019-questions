#!/usr/bin/env sh
docker build -t brainfuck .
docker stop brainfuck_instance
docker container rm brainfuck_instance
if [ $# -eq 0 ]; then
    docker run -p '9183:9183' --name brainfuck_instance -d brainfuck
else
    docker run -p '9183:9183' --name brainfuck_instance brainfuck
fi
