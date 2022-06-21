build:
	@docker-compose build

up:
	@docker-compose up -d

seed:
	@docker-compose run --rm app seed.py

run:
	@docker-compose run --rm app app.py

sh:
	@docker-compose run --rm --entrypoint sh app