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
python -m watchtower.cli work start --slug first_slice --title "First Slice"
```

```sh
cd core/python
python -m watchtower.cli work start --slug first_slice --title "First Slice" --format json
```

```sh
cd core/python
python -m watchtower.cli work list
```

```sh
cd core/python
python -m watchtower.cli work list --format json
```

```sh
cd core/python
python -m watchtower.cli work show --slug first_slice
```

```sh
cd core/python
python -m watchtower.cli work show --slug first_slice --format json
```

```sh
cd core/python
python -m watchtower.cli work complete --slug first_slice --summary "Closed after validation"
```

```sh
cd core/python
python -m watchtower.cli work complete --slug first_slice --format json
```

```sh
cd core/python
python -m pytest
```

## Notes

- The current bootstrap keeps the workspace dependency-light.
- The current CLI surfaces are `watchtower doctor`, `watchtower init`, `watchtower work start`, `watchtower work list`, `watchtower work show`, and `watchtower work complete`.
- Local managed workspace state lives under `.watchtower/`.
- Later slices can add richer workflow commands once the product boundary is better defined.
