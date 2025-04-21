#!/bin/bash
export PORT=10000
exec gunicorn app:app --bind 0.0.0.0:$PORT --timeout 300
