#!/usr/bin/env bash

read -r -d '' MOTD << EOM
CONNECT 300

Welcome to LOSALTOSHACKS server.

The server is connected via a wire made from a coat hanger.
Please be patient, and do not brute-force.

EOM
echo "$MOTD"
echo -n "user: "
read line
echo -n "password: "
read line
echo "Account Unavailable"
echo -e "E\bs\ba\bp\be\bC\bh\ba\br\bs\bH\bi\bd\b3\bT\b3\bX\b7\b "
echo "Goodbye."
