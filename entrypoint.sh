#!/bin/bash

echo "Starting Celery worker & beat"
celery -A redis_jokes worker -B -l INFO

tail -f /dev/null
