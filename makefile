# Makefile

.PHONY:	test

build:
	docker-compose build

test:
	python -m pytest --cov tests

run:
	docker-compose up 

down:
	docker-compose down
