# infra-project-template

Starter template for infra-focused repositories with:

- Python utility code
- MkDocs + Material
- monorepo-style sub-docs
- generated docs
- Confluence export flow
- Makefile-driven tasks

## Quick start

```bash
make install
make docs-write
make docs-live
````

## Main tasks
```bash
make install - create venv and install dependencies
make docs - build docs locally
make docs-live - serve docs locally
make docs-write - regenerate generated docs
make docs-confluence-prep - expand snippets into docs_confluence/
make docs-confluence-publish - publish Confluence docs
```
## Repository conventions
- docs/ = authoring source
- docs_confluence/ = generated export tree
- docs/generated/ = generated diagrams/reports
- src/<tool>/docs/ = tool-owned sub-docs

---

## `Makefile`

```makefile
SHELL := /bin/bash
VENV ?= .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
MKDOCS := $(VENV)/bin/mkdocs

.DEFAULT_GOAL := help

help: ## Show available targets
	@grep -E '^[a-zA-Z0-9_.-]+:.*?## ' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%-28s %s\n", $$1, $$2}'

venv: ## Create virtual environment
	python3 -m venv $(VENV)

install: venv ## Install dependencies
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

docs: ## Build MkDocs site
	$(MKDOCS) build

docs-live: ## Serve MkDocs locally
	$(MKDOCS) serve

docs-write: ## Regenerate generated docs
	@mkdir -p docs/generated
	@printf "# Generated Makefile targets\n\n" > docs/makefile-targets.md
	@printf "```text\n" >> docs/makefile-targets.md
	@$(MAKE) help >> docs/makefile-targets.md
	@printf "```\n" >> docs/makefile-targets.md
	@printf "flowchart TD\n  A[Project] --> B[Make targets]\n" > docs/generated/makeflow.mmd

docs-confluence-prep: ## Generate Confluence-friendly docs tree
	$(PYTHON) tools/snippet_expander.py

docs-confluence-publish: docs-confluence-prep ## Publish Confluence docs
	$(MKDOCS) build -f mkdocs-confluence.yml

lint: ## Run lint checks
	@echo "Add ruff/yamllint/markdownlint here"

format: ## Run formatters
	@echo "Add ruff format / prettier here"

test: ## Run tests
	@echo "Add pytest here"

clean: ## Remove build artifacts
	rm -rf site .pytest_cache .mypy_cache docs_confluence
	find . -type d -name __pycache__ -prune -exec rm -rf {} +

