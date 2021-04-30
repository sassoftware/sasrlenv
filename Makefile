DOCKER_REPO=rl
DOCKER_IMAGE=sasrl-env

all: clean setup docker_pull docker_build

clean:
	rm -rf build

setup:
	mkdir -p build

docker_pull:
	docker pull docker.sas.com/${DOCKER_REPO}/${DOCKER_IMAGE}:latest

docker_build:
	docker build -t docker.sas.com/${DOCKER_REPO}/${DOCKER_IMAGE}:latest -f Dockerfile .

push:
	docker push docker.sas.com/${DOCKER_REPO}/${DOCKER_IMAGE}:latest
