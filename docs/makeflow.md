# Makefile dependency graph

The graph below is generated automatically from the `Makefile` by `make docs-write`.
It shows how Make targets depend on each other — useful for understanding what a target
pulls in before you run it.

## Regenerating

```bash
make docs-write       # regenerates graph + target list (requires graphviz for SVG)
make view_makeflow    # open the SVG locally in a browser
```

`docs-write` writes three artefacts:

| File | Format | Use |
|---|---|---|
| `docs/generated/makeflow.mmd` | Mermaid | rendered below in this page |
| `docs/generated/makeflow.dot` | Graphviz DOT | source for the SVG |
| `docs/assets/makeflow.svg` | SVG | static embed, downloadable |

## Interactive graph

```mermaid
--8<-- "generated/makeflow.mmd"
```

## Static SVG

Useful when copying docs or viewing offline.

![Makefile dependency graph](assets/makeflow.svg)
