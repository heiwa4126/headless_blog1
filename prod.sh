#!/bin/sh
cd $(dirname $0) ; . .venv/bin/activate
cd src
FASTAPI_ENV=production uvicorn main:app
