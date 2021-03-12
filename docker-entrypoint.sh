#!/bin/bash
. "${VENV}"/.venv/bin/activate

if [ -z "${PORT}" ] ; then PORT=8080; fi

if [ -z "${HOST}" ] ; then HOST=0.0.0.0; fi

uvicorn main:app --port=${PORT} --host=${HOST} --reload
