# Makefile

.PHONY:	test

test:
	python -m pytest --cov tests

build:
	docker-compose build

run:
	docker-compose up -e FLASK_RUN_PORT=5000

down:
	docker-compose down

run:
	python proxy_server.py