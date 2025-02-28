.PHONY: help
.DEFAULT_GOAL := help

SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c

GIT_ROOT  := $(shell git rev-parse --show-toplevel)
GIT_COMMIT = $(shell git rev-parse HEAD)
GIT_SHA    = $(shell git rev-parse --short HEAD)
GIT_TAG    = $(shell git describe --tags --abbrev=0 --exact-match 2>/dev/null || echo "canary")
GIT_DIRTY  = $(shell test -n "`git status --porcelain`" && echo "dirty" || echo "clean")
DOCKER_VERSION ?= git-${GIT_SHA}

DOCS_ROOT := $(GIT_ROOT)/docs

##@ General
help: ## Show this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage: \033[36m\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-25s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

info: ## Show info
	@echo "Version:           ${VERSION}"
	@echo "Git Tag:           ${GIT_TAG}"
	@echo "Git Commit:        ${GIT_COMMIT}"
	@echo "Git Tree State:    ${GIT_DIRTY}"
	@echo "Docker Version:    ${DOCKER_VERSION}"


python-virtualenv-init: ## Initialize a Python 3 virtualenv in the current directory
ifeq ("$(wildcard .venv)", "")
	@python3 -m venv .venv
else
	@echo "Skipping virtual environment creation since .venv directory already exists."
endif

python-virtualenv-remove: ## Remove Python 3 virtualenv in the current directory
	@rm -rf .venv


##@ Development
format:
	@ruff format

lint: ## Run linting
	@poetry run isort

check-types:  ## Run type check
	@poetry run mypy

coverage:
	@echo "test"

test:  ## Run tests
	@poetry run pytest

ci: lint test check-types check-dependencies ## Run all checks (test, lint, check-types, check-dependencies)
.PHONY: ci lint test check-types check-dependencies

##@ Security
checkov: ## Run Checkov
	@checkov --directory .

check-dependencies:  ## Run security checks on dependencies
	@poetry run pip-audit

##@ Documentation
docs:
	@mkdocs serve

helm-docs:
	@helm-docs --chart-search-root charts

#include Makefile.include