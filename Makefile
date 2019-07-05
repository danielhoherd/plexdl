.DEFAULT_GOAL := help

.PHONY: help
help: ## Print Makefile help
	@grep -Eh '^[a-zA-Z_-]+:.*?## .*$$' ${MAKEFILE_LIST} | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'


IMAGE_NAME     ?= danielhoherd/plexdl
NO_CACHE       ?= false
ORG_PREFIX     ?= danielhoherd
GIT_ORIGIN      = $(shell git config --get remote.origin.url)
GIT_BRANCH      = $(shell git rev-parse --abbrev-ref HEAD)
GIT_SHA_SHORT   = $(shell if [ ! -z "`git status --porcelain`" ] ; then echo "DIRTY" ; else git rev-parse --short HEAD ; fi)
BUILD_TIME      = $(shell date '+%s')


.PHONY: all
all: docker-build

.PHONY: docker-build
docker-build: ## Build the Dockerfile found in PWD
	docker build --no-cache="${NO_CACHE}" \
		-t "${IMAGE_NAME}:latest" \
		-t "${IMAGE_NAME}:${BUILD_TIME}" \
		-t "${IMAGE_NAME}:${GIT_BRANCH}-${GIT_SHA_SHORT}" \
		--label "${ORG_PREFIX}.repo.origin=${GIT_ORIGIN}" \
		--label "${ORG_PREFIX}.repo.branch=${GIT_BRANCH}" \
		--label "${ORG_PREFIX}.repo.commit=${GIT_SHA_SHORT}" \
		--label "${ORG_PREFIX}.build_time=${BUILD_TIME}" \
		.

.PHONY: docker-push
docker-push: ## Push built Docker container to Docker Hub
	docker images --format="{{.Repository}}:{{.Tag}}" | grep '${IMAGE_NAME}.*DIRTY' | xargs -n1 docker rmi
	docker push ${IMAGE_NAME}

.PHONY: clean
clean: ## Clean build artifacts and delete virtualenv
	rm -f .requirements-dev .requirements || true
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	pipenv --rm || true

.PHONY: test
test: ## Run tests
	tox

.PHONY: requirements-dev
requirements-dev: .requirements ## Install dev requirements
.requirements-dev:
	pip3 install --user --upgrade pipenv
	pipenv --three install --dev
	touch .requirements-dev .requirements

.PHONY: requirements
requirements: .requirements ## Install requirements
.requirements:
	pip3 install --user --upgrade pipenv
	pipenv --three install
	touch .requirements
