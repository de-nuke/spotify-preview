#!/usr/bin/env bash

if [[ "$0" = "$BASH_SOURCE" ]]; then
    echo "Needs to be run using source: . $0"
    exit 1
fi

if [[ -z "${VIRTUAL_ENV}" ]]; then
  :
else
  deactivate
fi

rm -rf .venv
rm -rf dist
