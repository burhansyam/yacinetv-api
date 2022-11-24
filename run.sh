#!/usr/bin/env bash

set -e
set -x

uvicorn app:app --port 80  --reload
