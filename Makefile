# Makefile to make building and running the docker container easier
build: 
	docker build -t piggy-finance-container .

run:
	docker run -p 80:80 -p 8000:8000 piggy-finance-container

all: build run