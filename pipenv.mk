.PHONY: pipenv-clean
pipenv-clean: ## Destroy pipenv virtual environment
	pipenv --rm || true
	rm -f Pipfile.lock || true
	rm -f .requirements || true

.PHONY: pipenv
pipenv: .requirements ## Initialize pipenv virtual environment
.requirements:
	pip3 install --user --upgrade pipenv
	pipenv --three
	pipenv install
	touch .requirements
