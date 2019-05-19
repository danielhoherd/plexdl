.PHONY: install-hooks
install-hooks: ## Install git hooks
	command -v pre-commit || { \
		pip3 install --user --upgrade pre-commit || \
		pip install --user --upgrade pre-commit || \
		pip install --upgrade pre-commit ; \
	} && \
	pre-commit install -f --install-hooks ;
