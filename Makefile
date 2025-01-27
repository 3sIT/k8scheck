#
# k8scheck
#

PKG_NAME    := $(shell python setup.py --name)
PKG_VERSION := $(shell python setup.py --version)


.PHONY: clean
clean:  ## Clean up build artifacts
	rm -rf build/ dist/ *.egg-info htmlcov/ .coverage* .pytest_cache/ \
		k8scheck/__pycache__ tests/__pycache__

.PHONY: deps
deps:  ## Update the frozen pip dependencies (requirements.txt)
	tox -e deps

.PHONY: docs
docs:  ## Build the k8scheck docs locally
	tox -e docs

.PHONY: example-tests
example-tests:  ## Run the example tests using k8scheck
	tox -e examples

.PHONY: fmt
fmt:  ## Run formatting checks on the project source code
	pre-commit run --all-files

.PHONY: github-tag
github-tag:  ## Create and push a tag with the current version
	git tag -a ${PKG_VERSION} -m "${PKG_NAME} version ${PKG_VERSION}"
	git push -u origin ${PKG_VERSION}

.PHONY: lint
lint:  ## Run linting checks on the project source code (isort, flake8, twine)
	tox -e lint

.PHONY: test
test:  ## Run the project unit tests
	tox

.PHONY: version
version:  ## Print the version of the project
	@echo "${PKG_VERSION}"

.PHONY: help
help:  ## Print Make usage information
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

.DEFAULT_GOAL := help

# Targets for Jenkins CI

.PHONY: unit-test pypi-release

unit-test:
	tox -e py38

pypi-release:
	tox -e publish
