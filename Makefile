install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
format:
	black *.py

lint:	
	pylint --disable=R,C hello.py
	
test:
	python -m pytest -vv --cov=hello --cov=greeting tests

all: install lint test format
