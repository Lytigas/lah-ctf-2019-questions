#!/bin/sh
set -eo pipefail

WORKERS=${WORKERS:-1}
WORKER_CLASS=${WORKER_CLASS:-gthread}
ACCESS_LOG=${ACCESS_LOG:--}
ERROR_LOG=${ERROR_LOG:--}

# Start CTFd
echo "Starting brainfucker"
exec gunicorn 'brainfuck_server:app' \
    --bind "0.0.0.0:9183" \
    --workers $WORKERS \
    --worker-class "$WORKER_CLASS" \
    --access-logfile "$ACCESS_LOG" \
    --error-logfile "$ERROR_LOG"
