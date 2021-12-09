.PHONY: format
format:
	pip install black isort mypy
	black *.py
	isort *.py
	mypy --strict *.py
