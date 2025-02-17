.PHONY: run
run:
	python manage.py runserver

.PHONY: test
test:
	docker compose exec web-app pytest

.PHONY: build
up-build:
	docker compose -f docker-compose.yml up --build

.PHONY: down
down:
	docker compose -f docker-compose.yml down
