VENV=.venv
PYTHON=${VENV}/bin/python
PIP=${VENV}/bin/pip

.PHONY: help venv install test

help:
	@echo "Available targets: venv, install, test"

venv:
	python3 -m venv ${VENV}
	${PIP} install --upgrade pip

install: venv
	${PIP} install -r requirements.txt

test: install
	${PYTHON} -m pytest -q
