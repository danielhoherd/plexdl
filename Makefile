.DEFAULT_GOAL := help
include *.mk

.PHONY: help
help: ## Print Makefile help
	@grep -Eh '^[a-zA-Z_-]+:.*?## .*$$' ${MAKEFILE_LIST} | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'


IMAGE_NAME        ?= danielhoherd/plexdl
NO_CACHE          ?= false
ORG_PREFIX        ?= danielhoherd
GIT_ORIGIN         = $(shell git config --get remote.origin.url)
GIT_BRANCH         = $(shell git rev-parse --abbrev-ref HEAD)
GIT_SHA_SHORT      = $(shell if [ ! -z "`git status --porcelain`" ] ; then echo "DIRTY" ; else git rev-parse --short HEAD ; fi)
BUILD_TIME         = $(shell date '+%s')


.PHONY: all
all: build

.PHONY: build
build: ## Build the Dockerfile found in PWD
	docker build --no-cache="${NO_CACHE}" \
		-t "${IMAGE_NAME}:latest" \
		-t "${IMAGE_NAME}:${BUILD_TIME}" \
		-t "${IMAGE_NAME}:${GIT_BRANCH}-${GIT_SHA_SHORT}" \
		--label "${ORG_PREFIX}.repo.origin=${GIT_ORIGIN}" \
		--label "${ORG_PREFIX}.repo.branch=${GIT_BRANCH}" \
		--label "${ORG_PREFIX}.repo.commit=${GIT_SHA_SHORT}" \
		--label "${ORG_PREFIX}.build_time=${BUILD_TIME}" \
		.

.PHONY: push
push: ## Push built container to docker hub
	docker images --format="{{.Repository}}:{{.Tag}}" | grep '${IMAGE_NAME}.*DIRTY' | xargs -n1 docker rmi
	docker push ${IMAGE_NAME}

.PHONY: clean
clean: ## Clean build artifacts
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

.PHONY: test
test: ## Run tests
	tox
