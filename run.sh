#!/usr/bin/env bash

set -e
set -x

uvicorn YacineTV:app --port 80  --reload
