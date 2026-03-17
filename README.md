# WatchTower

WatchTower is the operator-facing implementation target that consumes the governed core and planning substrate prepared in `WatchTowerPlan`.

## Current State

This repository is in bootstrap mode. The current slice establishes:

- root repo guidance
- one Python workspace under `core/python/`
- one minimal `watchtower doctor` CLI command
- one smoke test proving the bootstrap entrypoint works

## Start Here

- Read `AGENTS.md` for repo-wide working instructions.
- Read `core/python/README.md` for workspace commands and layout.

## Scope of This Bootstrap

This slice does not define the full product surface. It creates the first executable workspace so later WatchTower implementation work can land in a real repo instead of a blank shell.
