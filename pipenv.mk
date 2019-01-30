.PHONY: pipenv-clean
pipenv-clean: ## Destroy pipenv virtual environment
	pipenv --rm || true
	rm -f Pipfile.lock || true

.PHONY: pipenv
pipenv: Pipfile.lock ## Initialize pipenv virtual environment
Pipfile.lock:
	pip3 install --user --upgrade pipenv || \
	pip install --user --upgrade pipenv
	pipenv --three
	pipenv install
