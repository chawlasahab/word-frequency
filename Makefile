install:
	@echo "Installing dependencies..."
	pip install requests

flake:
	@echo "Checking code base using flake8..."
	flake8 --ignore=E501,W503,W605

test:
	@echo "Running unit tests..."
	python3 -m unittest -v WordFrequencyTest.py

run: install test
ifdef pageid
ifdef n
	python3 WordFrequency.py --pageid $(pageid) -n $(n)
endif
endif
ifndef pageid
ifndef n
	python3 WordFrequency.py
endif
endif
