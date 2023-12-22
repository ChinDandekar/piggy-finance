# Makefile to make building and running the docker container easier
build: 
	docker build -t piggy-finance-image .

run:
	docker run -p 80:80 -p 8080:8080 piggy-finance-image

kill:
	docker kill $(docker ps -q)

all: build run