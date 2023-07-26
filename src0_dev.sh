#!/bin/sh
cd $(dirname $0) ; .venv/bin/activate
cd src0
uvicorn main:app --reload
