# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

Generated from `violetina/infra-project-template`.

Recommended generation command, so the project root lands in your home directory:

```bash
cookiecutter https://github.com/{{ cookiecutter.github_org }}/infra-project-template.git --checkout devel --output-dir ~
cd ~/{{ cookiecutter.project_slug }}
```

## Quick start

```bash
make help
make install
make docs-write
make docs-live
```

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

## Description

###  {{ cookiecutter.workflow_type }}

 {{ cookiecutter.description }}

---

