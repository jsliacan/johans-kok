VERSION ?= 0.1.0
CONTAINER_MANAGER ?= podman
REGISTRY ?= ghcr.io
IMAGE_NAME ?= jsliacan/johans-kok

.PHONY: build
build:
	${CONTAINER_MANAGER} build -t ${IMAGE_NAME}:${VERSION} .

.PHONY: push # requires login to ghcr.io
push:
	${CONTAINER_MANAGER} push ${IMAGE_NAME}:${VERSION} ${REGISTRY}/${IMAGE_NAME}:${VERSION}

.PHONY: run # requires Stripe secret key in STRIPE_KEY
run:
	# podman secret create --env=true stripe-secret STRIPE_KEY:
	${CONTAINER_MANAGER} run -p 5000:5000 -d --pull=always --rm --secret=stripe-secret,type=env,target=STRIPE_SECRET_KEY --name johan ${REGISTRY}/${IMAGE_NAME}:${VERSION}

