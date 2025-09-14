.DEFAULT_GOAL := help

.PHONY: help
help: ## Print Makefile help
	@grep -Eh '^[a-z.A-Z_0-9-]+:.*?## .*$$' ${MAKEFILE_LIST} | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[1;36m%-18s\033[0m %s\n", $$1, $$2}'

IMAGE_NAME     ?= quay.io/danielhoherd/plexdl
NO_CACHE       ?= false
ORG_PREFIX     ?= danielhoherd
GIT_ORIGIN      = $(shell git config --get remote.origin.url)
GIT_BRANCH      = $(shell git rev-parse --abbrev-ref HEAD)
GIT_SHA_SHORT   = $(shell if [ ! -z "`git status --porcelain`" ] ; then echo "DIRTY" ; else git rev-parse --short HEAD ; fi)
BUILD_TIME      = $(shell date '+%s')
BUILD_DATE      = $(shell date '+%F')


.PHONY: all
all: docker-build

.PHONY: docker-build
docker-build: wheel ## Build the Dockerfile found in PWD
	docker build --no-cache="${NO_CACHE}" \
		-t "${IMAGE_NAME}:latest" \
		-t "${IMAGE_NAME}:${BUILD_DATE}" \
		-t "${IMAGE_NAME}:${GIT_BRANCH}" \
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
clean: ## Delete build artifacts
	-rm -rf .venv
	-find . -name '*.pyc' -delete
	-find . -name '__pycache__' -delete
	-rm -rf dist

.PHONY: build
build: ## Build a wheel
	uv build

.PHONY: test
test: ## Run tests
	uv run pytest tests

.PHONY: venv
venv: .venv ## Install dev requirements
.venv:
	uv venv --seed
	uv sync

.PHONY: generate-setup.py
generate-setup.py: wheel ## Generate the setup.py file from pyproject.toml
	tar -xvf dist/*.tar.gz --wildcards --no-anchored '*/setup.py' --strip=1
