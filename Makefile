# LOCAL DJANGO

migrate:
	python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver

createsuperuser:
	python3 manage.py createsuperuser

runserver:
	python3 manage.py runserver


# DOCKER

migrate-docker:
	python3 manage.py makemigrations --no-input
	python3 manage.py migrate --no-input
	python3 manage.py collectstatic --no-input
	python3 manage.py runserver 0.0.0.0:8000

build:
	docker-compose -f local.yml up --build -d --remove-orphans --force-recreate

up:
	docker-compose -f local.yml up -d

down:
	docker-compose -f local.yml down

show_logs:
	docker-compose -f local.yml logs

docer-migrate:
	docker-compose -f local.yml run --rm web python3 manage.py makemigrations & docker-compose -f local.yml run --rm api python3 manage.py migrate

collectstatic:
	docker-compose -f local.yml run --rm web python3 manage.py collectstatic --no-input --clear

docker-createsuperuser:
	docker-compose -f local.yml run --rm web python3 manage.py createsuperuser

down-v:
	docker-compose -f local.yml down -v

volume:
	docker-volume inspect myhall_local_mysql_data
