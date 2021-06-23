#!/bin/sh
source /opt/detail-cpu-memory/venv/bin/activate
cd /opt/detail-cpu-memory/
uvicorn main:app --host 42.114.245.120 --port 1998

