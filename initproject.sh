#!/usr/bin/env bash

if [[ "$0" = "$BASH_SOURCE" ]]; then
    echo "Needs to be run using source: . $0"
    exit 1
fi

rm -rf .venv
sudo apt install python3-venv
python -m venv .venv
alias activate=". .venv/bin/activate"
activate
pip -V
pip install -r requirements.txt
echo "ACCESS_CONTROL_ALLOW_HEADERS=Content-Type" >> .env
echo "ACCESS_CONTROL_ALLOW_METHODS=OPTIONS,GET" >> .env
echo "ACCESS_CONTROL_ALLOW_ORIGIN=*" >> .env
deactivate