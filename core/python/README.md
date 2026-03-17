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
python -m watchtower.cli status
```

```sh
cd core/python
python -m watchtower.cli status --format json
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
python -m watchtower.cli work begin --slug first_slice
```

```sh
cd core/python
python -m watchtower.cli work begin --slug first_slice --format json
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
python -m watchtower.cli work next
```

```sh
cd core/python
python -m watchtower.cli work next --format json
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
python -m watchtower.cli work note --slug first_slice --message "Resume from the last validated checkpoint"
```

```sh
cd core/python
python -m watchtower.cli work note --slug first_slice --message "Resume from the last validated checkpoint" --format json
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
- The current CLI surfaces are `watchtower doctor`, `watchtower status`, `watchtower init`, `watchtower work start`, `watchtower work begin`, `watchtower work list`, `watchtower work next`, `watchtower work show`, `watchtower work note`, and `watchtower work complete`.
- The current `watchtower work ...` surface is a bootstrap-stage local work-item contract derived from `/home/j/WatchTowerPlan/requirements.md` and `/home/j/WatchTowerPlan/decisions.md`; treat the work-item concept as intentional, but the exact CLI shape as provisional until a later slice stabilizes it.
- Local managed workspace state lives under `.watchtower/`.
- New WatchTower behavior should remain aligned to `/home/j/WatchTowerPlan/requirements.md` and `/home/j/WatchTowerPlan/decisions.md`.
- Later slices can add richer workflow commands once the product boundary is better defined.
