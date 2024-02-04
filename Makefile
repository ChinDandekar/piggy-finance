# Makefile to make building and running the docker container easier
build: 
	docker build -t piggy-finance-image .

run:
	docker run -p 80:80 -p 8080:8080 piggy-finance-image

kill:
	docker kill $$(docker ps -q)

dev:
	docker-compose up

access_logs:
	rm -rf tmp
	docker cp $$(docker ps -q):/tmp .

access_local_logs:
	rm -rf tmp
	docker cp app-node:/tmp .

access_shell:
	docker exec -it $$(docker ps -q) sh

all: build run