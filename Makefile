# Makefile to make building and running the docker container easier

build_frontend:
	cd frontend && mv .env .env_local && mv .env_deploy .env && npm run build && mv .env .env_deploy && mv .env_local .env


build_local: 
	docker build -t piggy-finance-image .

build:
	rm nginx.conf
	mv nginx_ec2.conf nginx.conf
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

connect_ec2_frontend:
	ssh -i ~/.ssh/piggy-finance-key.pem -L 3000:localhost:3000 ec2-user@ec2-34-208-152-184.us-west-2.compute.amazonaws.com

connect_ec2_backend:
	ssh -i ~/.ssh/piggy-finance-key.pem -L 8080:localhost:8080 ec2-user@ec2-34-208-152-184.us-west-2.compute.amazonaws.com
connect_ec2_server:
	ssh -i ~/.ssh/piggy-finance-key.pem -L 80:localhost:80 ec2-user@ec2-34-208-152-184.us-west-2.compute.amazonaws.com

start_frontend:
	cd frontend
	npm start

start_backend:
	cd backend
	conda activate piggyEnv
	python manage.py runserver localhost:8080
all: build run