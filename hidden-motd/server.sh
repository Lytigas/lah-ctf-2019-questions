#!/usr/bin/env bash


#mknod /tmp/backpipe
#while true ; do ./handler.sh | nc -l -p 1500 ; done
socat TCP4-LISTEN:5556,reuseaddr,fork EXEC:"./handler.sh"
