# AGENTS.md

## Role
- Treat this file as the repository-wide instruction layer for `WatchTower`.

## Local Rules
- Start with `README.md` before broader scans.
- Keep executable code under `core/python/` for the current bootstrap stage.
- Keep the repo bootstrap bounded: avoid choosing a frontend stack, database, or hosted dependency until a later slice makes that boundary explicit.
- Prefer local-first, inspectable tooling and simple validation.
- Do not assume `WatchTowerPlan` and `WatchTower` share the same source roots; treat this repo as its own implementation target.

## Do
- Keep new files minimal and directly useful.
- Add tests with the same slice when behavior is introduced.

## Do Not
- Do not introduce extra top-level runtimes or parallel language roots in the bootstrap slice.
- Do not reintroduce deleted historical planning notes as active repo guidance.
