VENV=.venv
PYTHON=${VENV}/bin/python
PIP=${VENV}/bin/pip

.PHONY: help venv install install-dev lint format format-check typecheck test clean

help:
	@echo "Available targets: venv, install, install-dev, lint, format, format-check, typecheck, test, clean"

venv:
	python3 -m venv ${VENV}
	${PIP} install --upgrade pip

install: venv
	${PIP} install -r requirements.txt

install-dev: venv
	${PIP} install -r requirements-dev.txt

lint: install-dev
	${PYTHON} -m ruff check src tests

format: install-dev
	${PYTHON} -m black src tests

format-check: install-dev
	${PYTHON} -m black --check src tests

typecheck: install-dev
	${PYTHON} -m mypy src

test: install-dev
	${PYTHON} -m pytest -q

clean:
	rm -rf ${VENV} .pytest_cache .mypy_cache
