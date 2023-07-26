#!/bin/sh
cd $(dirname $0) ; .venv/bin/activate
cd src
uvicorn main:app --reload
