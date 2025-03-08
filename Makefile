.PHONY: run
run:
	python manage.py runserver

.PHONY: test
test:
	docker compose exec web-app pytest

.PHONY: up
up:
	docker compose -f docker-compose.yml up

.PHONY: build
build:
	docker compose -f docker-compose.yml up --build

.PHONY: down
down:
	docker compose -f docker-compose.yml down
