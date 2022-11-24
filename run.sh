#!/usr/bin/env bash

set -e
set -x

uvicorn main:app --reload
