IMAGE=nextgenshop_backend
PORT=8000

build:
	docker build --tag=${IMAGE} .

run:
	docker run --rm \
		-p ${PORT}:8000 \
		${IMAGE}
