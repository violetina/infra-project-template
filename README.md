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
```

## Main tasks

| Target | Description |
|---|---|
| `make install` | Create venv and install dependencies |
| `make docs-live` | Serve docs locally (port 8000) |
| `make docs-write` | Regenerate docs: target list + Makefile graph |
| `make view_makeflow` | Open the Makefile dependency SVG locally |
| `make docs-confluence-prep` | Expand snippets into `docs_confluence/` |
| `make lint` / `make test` | Lint and test hooks |

Run `make help` for the full list.

## Makefile dependency graph

`make docs-write` generates a dependency graph of all Make targets using
[makefile2graph](https://github.com/lindenb/makefile2graph). Three formats are written:

- `docs/generated/makeflow.mmd` — Mermaid (rendered in the docs site)
- `docs/generated/makeflow.dot` — Graphviz DOT source
- `docs/assets/makeflow.svg` — SVG (requires `graphviz` / `dot` to be installed)

View locally after generating:

```bash
make docs-write       # build graph + target list
make view_makeflow    # open SVG in browser
```

Or browse the interactive Mermaid version in the docs site under **Makefile graph**.

## Repository conventions
- docs/ = authoring source
- docs_confluence/ = generated export tree
- docs/generated/ = generated diagrams/reports
- src/<tool>/docs/ = tool-owned sub-docs

---

See [`Makefile`](Makefile) for all targets, or run `make help`.
