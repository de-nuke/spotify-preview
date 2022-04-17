.PHONY: test types static all build

include .env
export $(shell sed 's/=.*//' .env)

all: static types test

static: black flake isort

test:
	./test.sh

types:
	mypy --config-file pyproject.toml .

black:
	black .

flake:
	flake8

isort:
	isort .

build:
	./build.sh