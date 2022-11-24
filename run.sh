#!/usr/bin/env bash

set -e
set -x

uvicorn YacineTV:app --reload
