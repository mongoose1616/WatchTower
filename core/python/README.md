# `core/python`

## Description

This directory is the initial Python workspace for the WatchTower product repo bootstrap.

## Paths

| Path | Description |
|---|---|
| `core/python/README.md` | Workspace purpose and command quick reference. |
| `core/python/pyproject.toml` | Python project metadata and tool configuration. |
| `core/python/src/watchtower/` | Bootstrap package source. |
| `core/python/tests/` | Bootstrap test coverage. |

## Commands

```sh
cd core/python
python -m watchtower.cli doctor
```

```sh
cd core/python
python -m watchtower.cli doctor --format json
```

```sh
cd core/python
python -m watchtower.cli init
```

```sh
cd core/python
python -m watchtower.cli init --format json
```

```sh
cd core/python
python -m pytest
```

## Notes

- The current bootstrap keeps the workspace dependency-light.
- The first CLI surfaces are `watchtower doctor` and `watchtower init`.
- Local managed workspace state lives under `.watchtower/`.
- Later slices can add richer workflow commands once the product boundary is better defined.
