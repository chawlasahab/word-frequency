install:
	@echo "Installing dependencies..."
	pip install requests

flake:
	@echo "Checking code base using flake8..."
	flake8 --ignore=E501,W503,W605

test:
	@echo "Running unit tests..."
	python3 -m unittest -v WordFrequencyTest.py

run: install flake test
	python3 WordFrequency.py --pageid $(pageid) -n $(n)

default: install flake test
	python3 WordFrequency.py
