.DEFAULT_GOAL := help
include *.mk

.PHONY: help
help: ## Print Makefile help.
	@grep -Eh '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

.PHONY: test
test:
	tox
