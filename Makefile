.PHONY: format
format:
	pip install black isort
	black *.py
	isort *.py
