#!/usr/bin/env bash

set -e
rm -rf dist
mkdir -p dist
(
  ln -s .venv/lib/python3.8/site-packages python;
  zip -r dist/libs.zip python;
  rm python
)
zip dist/code *.py