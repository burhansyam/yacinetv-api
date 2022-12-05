#!/usr/bin/env bash

set -e
set -x

uvicorn --port 80 --host 0.0.0.0 main:app --reload

