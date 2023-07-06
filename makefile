# Makefile

.PHONY:	test

build:
	docker-compose build

test:
	python -m pytest --cov tests

run:
	docker-compose up -e FLASK_RUN_PORT=5000

down:
	docker-compose down
