# AGENTS.md

## Role
- Treat this file as the repository-wide instruction layer for `WatchTower`.

## Local Rules
- Start with `README.md` before broader scans.
- Keep executable code under `core/python/` for the current bootstrap stage.
- Keep the repo bootstrap bounded: avoid choosing a frontend stack, database, or hosted dependency until a later slice makes that boundary explicit.
- Prefer local-first, inspectable tooling and simple validation.
- Do not assume `WatchTowerPlan` and `WatchTower` share the same source roots; treat this repo as its own implementation target.
- Base WatchTower development on `/home/j/WatchTowerPlan/requirements.md` and `/home/j/WatchTowerPlan/decisions.md`; do not invent product behavior that conflicts with those captured requirements and decisions.
- Treat the current `watchtower work ...` command family as a bootstrap-stage downstream surface. Keep the `work item` concept unless planning changes it, but do not assume the exact CLI namespace or UX is a permanent contract yet.

## Do
- Keep new files minimal and directly useful.
- Add tests with the same slice when behavior is introduced.
- Use `/home/j/WatchTowerPlan/requirements.md` and `/home/j/WatchTowerPlan/decisions.md` as the current implementation boundary and planning rationale for new slices.

## Do Not
- Do not introduce extra top-level runtimes or parallel language roots in the bootstrap slice.
- Do not reintroduce deleted historical planning notes as active repo guidance.
