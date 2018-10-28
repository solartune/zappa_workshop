up:
	docker-compose up -d

build:
	docker-compose build

cmd:
	docker-compose exec app $(CMD)