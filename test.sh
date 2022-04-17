#!/usr/bin/env bash

if [[ -z "${VIRTUAL_ENV}" ]]; then
  echo "Virtualenv must be activated"
  exit 1
else
  if [ ! -f .env ]
  then
    export $(cat .env | xargs)
    python -m unittest test.py
  else
    python -m unittest test.py
  fi
fi