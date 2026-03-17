# WatchTower

WatchTower is the operator-facing implementation target that consumes the governed core and planning substrate prepared in `WatchTowerPlan`.

## Current State

This repository is in bootstrap mode. The current slice establishes:

- root repo guidance
- one Python workspace under `core/python/`
- one local `.watchtower/workspace.json` manifest path
- one local `.watchtower/work_items/` record path
- `watchtower doctor`, `watchtower status`, `watchtower init`, `watchtower work start`, `watchtower work list`, `watchtower work show`, `watchtower work note`, and `watchtower work complete` CLI commands
- CLI smoke tests proving bootstrap, initialized workspace, work-item start, work-item inspection, and work-item completion states work

## Start Here

- Read `AGENTS.md` for repo-wide working instructions.
- Read `core/python/README.md` for workspace commands and layout.

## Scope of This Bootstrap

This slice does not define the full product surface. It creates the first executable workspace so later WatchTower implementation work can land in a real repo instead of a blank shell.
