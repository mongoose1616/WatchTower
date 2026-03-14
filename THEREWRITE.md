# THEREWRITE: WatchTowerPlan Rewrite Program

## Summary
This rewrite should happen, but it should not be framed as a rescue or a greenfield replacement. The live `WatchTowerPlan` repository is already healthy and structurally capable. The case for the rewrite is second-order structural simplification: reduce maintenance fan-out, repeated orchestration patterns, hotspot concentration, and parallel restatement of the same relationships without reopening accepted authority boundaries or destabilizing already-hardened surfaces.

As of March 14, 2026 local time, with the traced rewrite package and coordination surfaces refreshed at `2026-03-14T05:41:11Z`, the validated live state is:

- `watchtower-core doctor --format json`: `status: ok`, with 60 commands, 48 schemas, 55 validators, 64 standards, 31 workflows, 62 initiatives, 211 tasks, and 62 traces loaded.
- `watchtower-core validate all`: 1,227/1,227 targets passed.
- `watchtower-core query authority --domain planning --format json`: five active question-specific planning authorities already exist:
  - `coordination_index`
  - `planning_catalog`
  - `initiative_index`
  - `task_index`
  - `traceability_index`
- `watchtower-core query coordination --format json`: the repo is currently in `active_work`, with one actionable rewrite task, `task.structural_rewrite_program.phase3_command_companion_source_surface_normalization_review.008`, and that task is the explicit Phase 3 command-companion outcome-review gate after the closed Phase 3 entry review and first bounded Phase 3 slice.
- `watchtower-core query planning --trace-id trace.structural_rewrite_program --format json`: the rewrite now exists as a traced repo-native package with an active PRD, an active feature design, four implementation plans, an expanded acceptance contract, four migration records, four validation-evidence artifacts, and eight traced rewrite tasks with only the Phase 3 outcome-review task still open.
- `watchtower-core sync command-index --format json`: `status: ok`, with 60 command-index entries and no rewrite needed.
- `python -m pytest tests/unit/test_command_index_sync.py`: 4/4 tests passed for the new command-companion drift guard.

That baseline matters. The rewrite must prove net simplification over a working system. It does not get to assume the repo is broken or that all older-looking surfaces are accidental debt.

Phase 0 and Phase 1 are complete in repo-native surfaces, the Phase 2 entry review is complete, the first bounded Phase 2 slice has landed, the pilot outcome review has closed cleanly, the Phase 3 entry review is complete, and the first bounded Phase 3 slice has landed. Broader Phase 3 rollout and every later phase still require explicit checkpoint packages, durable slice-control records, and re-review at the checkpoints named later in this program.

---

## Evidence Basis
This program was refreshed again against the following sources on March 14, 2026 local time and the resulting repo-native checkpoint artifacts recorded on March 14, 2026 UTC:

- Live repo checks:
  - `watchtower-core doctor --format json`
  - `watchtower-core validate all`
  - `watchtower-core query authority --domain planning --format json`
  - `watchtower-core query coordination --format json`
  - `watchtower-core query planning --trace-id trace.structural_rewrite_program --format json`
  - `watchtower-core sync command-index --format json`
  - `python -m pytest tests/unit/test_command_index_sync.py`
- Foundations and standards:
  - `repository_scope.md`
  - `engineering_design_principles.md`
  - `repository_standards_posture.md`
  - `engineering_stack_direction.md`
  - `product_direction.md`
  - `customer_story.md`
  - `status_tracking_standard.md`
  - `task_tracking_standard.md`
- Accepted planning and runtime direction:
  - `planning_authority_unification.md`
  - `planning_authority_unification_direction.md`
  - `machine_first_coordination_surface.md`
  - `command_documentation_and_lookup.md`
  - `core_export_ready_architecture.md`
  - `planning_authoring_hotspot_regression_hardening.md`
  - `repo_local_hotspot_modularity_hardening.md`
  - `summary_surface_retirement.md`
  - `summary_surface_retirement_direction.md`
- Current compatibility and history signals:
  - `compatibility_contract.v1.schema.json`
  - `core_python_workspace_compatibility.v1.json`
  - deprecated planning records with `authority: historical`
- Repo-native rewrite execution package:
  - `docs/standards/governance/rewrite_surface_classification_standard.md`
  - `docs/standards/governance/rewrite_execution_control_standard.md`
  - `docs/planning/prds/structural_rewrite_program.md`
  - `docs/planning/design/features/structural_rewrite_program.md`
  - `docs/planning/design/implementation/structural_rewrite_program.md`
  - `docs/planning/design/implementation/structural_rewrite_artifact_role_registry_pilot.md`
  - `docs/planning/design/implementation/structural_rewrite_phase3_command_authority_entry.md`
  - `docs/planning/design/implementation/structural_rewrite_phase3_command_companion_source_surface_normalization.md`
  - `core/control_plane/contracts/acceptance/structural_rewrite_program_acceptance.v1.json`
  - `core/control_plane/ledgers/migrations/structural_rewrite_program_phase0_phase1_ready.v1.json`
  - `core/control_plane/ledgers/migrations/structural_rewrite_artifact_role_registry_pilot.v1.json`
  - `core/control_plane/ledgers/migrations/structural_rewrite_phase3_command_companion_source_surface_normalization_ready.v1.json`
  - `core/control_plane/ledgers/migrations/structural_rewrite_phase3_command_companion_source_surface_normalization.v1.json`
  - `core/control_plane/ledgers/validation_evidence/structural_rewrite_program_phase0_phase1_baseline.v1.json`
  - `core/control_plane/ledgers/validation_evidence/structural_rewrite_artifact_role_registry_pilot.v1.json`
  - `core/control_plane/ledgers/validation_evidence/structural_rewrite_phase3_command_companion_source_surface_normalization_ready.v1.json`
  - `core/control_plane/ledgers/validation_evidence/structural_rewrite_phase3_command_companion_source_surface_normalization.v1.json`
  - `docs/planning/tasks/closed/review_structural_rewrite_program_phase2_entry_package.md`
  - `docs/planning/tasks/closed/implement_structural_rewrite_artifact_role_registry_pilot.md`
  - `docs/planning/tasks/closed/review_structural_rewrite_artifact_role_registry_pilot_outcome.md`
  - `docs/planning/tasks/closed/review_structural_rewrite_phase3_entry_package.md`
  - `docs/planning/tasks/closed/implement_structural_rewrite_phase3_command_companion_source_surface_normalization.md`
  - `docs/planning/tasks/open/review_structural_rewrite_phase3_command_companion_source_surface_normalization_outcome.md`

This document is therefore execution-oriented. It replaces the earlier draft framing and does not rely on the stale "deliverable note" assumption that the file still needed to be created later.

It also does not outrank the repo-native rewrite package it cites. As the trace advances, the PRD, feature design, implementation plans, acceptance contract, migration records, validation evidence, and active task surfaces need to stay synchronized to the live checkpoint; when supporting narrative surfaces lag, the live queries plus the current controlling checkpoint artifacts take precedence until those supporting surfaces are refreshed.

---

## Current Execution Checkpoint

The rewrite is no longer at a generic pre-execution planning state. It has already completed the preparatory phases that this program originally gated.

- Phase 0 is complete: the live baseline and hotspot inventory were refreshed, the four-axis classification guidance was published, the public planning-authority parity boundary was fixed, the rewrite slice-control package model was published, and the pilot family was chosen.
- Phase 1 is complete for the currently published critical-surface scope: critical public planning, command-boundary, compatibility, and historical-retention candidate surfaces were classified; consumer maps and retention reasons were recorded; and no-go conditions, rollback expectations, and Phase 2 entry conditions were published.
- The Phase 2 entry-review gate is closed and recorded in `docs/planning/tasks/closed/review_structural_rewrite_program_phase2_entry_package.md`.
- The only accepted Phase 2 pilot family is artifact-role metadata.
- The first artifact-role slice is now complete as a small dedicated registry with its own checkpoint document, migration record, validation evidence, and explicit approval outcome.
- The Phase 3 entry review is closed and recorded in `docs/planning/tasks/closed/review_structural_rewrite_phase3_entry_package.md`.
- The first bounded Phase 3 slice is now complete as command companion source-surface normalization, with its own checkpoint document, migration record, validation evidence, and closed implementation task.
- The slice-specific validation surfaces are already green: `watchtower-core sync command-index --format json` reports `status: ok` with 60 entries and no write, and `python -m pytest tests/unit/test_command_index_sync.py` passes 4/4 tests against the new fail-closed guard.
- The active hard stop is now the Phase 3 outcome-review task `docs/planning/tasks/open/review_structural_rewrite_phase3_command_companion_source_surface_normalization_outcome.md`.
- The current question is no longer whether Phase 3 may begin. The current question is whether the bounded command-companion slice held cleanly enough that broader rewrite work remains blocked or may proceed to one new bounded checkpoint.

The earlier execution-accuracy guardrail about first-slice classification sufficiency no longer blocks the current checkpoint. The closed Phase 3 entry review recorded that no additional command-adjacent workflow, route, or compatibility classification addendum was required for the first slice because it stayed inside already-classified command companion surfaces. That resolution is bounded to this slice only. Later workflow, route, sync, validator, projection, history, or compatibility work still needs its own family-specific classification or parity package before implementation.

One narrower trace-coherence gap still remains. The supporting feature design currently carries stale `209`-task / `1219`-validation / open-entry-review current-state narration, and the repo-native PRD still uses broader Phase 1 requirement wording than this document's narrowed critical-surface framing. Those supporting lines do not change the live checkpoint. Until they are refreshed or explicitly relabeled as historical checkpoint context, they must not be read as authorization to touch untouched workflow, route, sync, validator, projection, history, or compatibility families.

That is the state this program should describe going forward. It should no longer read as if the repo still needs a Phase 0 authorization decision.

---

## 1. Rewrite Thesis

### Why the rewrite is still justified
The repository has succeeded at building explicit governance, machine-readable authority, deterministic validation, and clear repo-local boundaries. That success also created a second-order cost:

- too many surfaces restate nearby relationships in slightly different ways
- several families still rely on repeated orchestration patterns
- the remaining hotspots are concentrated in high-context repo-local services
- adding or changing one capability still tends to move multiple companion layers together

The rewrite is justified because the repo is now mature enough that structural simplification will compound across every future change.

### What problem is actually being solved
The rewrite is not primarily about runtime speed or correctness rescue. The dominant problems are:

- authority fan-out
- repeated family mechanics
- hand-wired derivation paths
- hotspot concentration
- excessive change cost for bounded repo-local evolution

### Rewrite framing
The correct framing is:

- preserve the validated repository foundations
- preserve accepted public authority contracts
- simplify internal machinery behind those contracts
- tighten authored-versus-derived boundaries
- reduce ongoing maintenance cost without widening repository scope

---

## 2. Goals, Non-Goals, and Rewrite Invariants

### Goals
- Reduce internal complexity, maintenance fan-out, and repeated family mechanics.
- Keep one explicit authority answer per important question.
- Preserve the top-level repository shape and operating model.
- Make derived and compatibility surfaces more obviously derived or compatibility-scoped.
- Extend registry- and descriptor-driven internals only where authored truth is explicit.
- Shrink remaining repo-local hotspots into narrower helper-backed seams.
- Produce a cleaner active baseline after the rewrite without breaking history lookup, trace context, or start-here navigation.
- Fold durable standing policy into standards, schemas, registries, and canonical control-plane surfaces where appropriate.

### Non-goals
- Do not turn `WatchTowerPlan` into the operator-facing WatchTower product.
- Do not replace local Markdown and JSON authority with a database or hosted backend.
- Do not collapse the repo into code-only authority with docs added later.
- Do not flatten `repo_ops` into reusable core.
- Do not reopen accepted public planning-boundary decisions just because an internal graph exists.
- Do not replace the current parser and command registry with a second durable command-existence authority unless a separate accepted decision explicitly authorizes that change.
- Do not introduce a broad new generic planning-authoring framework for the sake of architectural purity.
- Do not treat every old-looking compatibility or historical surface as a retirement candidate by default.

### Rewrite invariants
The following must hold through every phase:

- `docs/`, `workflows/`, `core/control_plane/`, and `core/python/` remain the top-level strata.
- `core/control_plane/` remains the canonical machine-readable authority layer.
- `core/python/` remains the runtime and tooling layer, not the authored policy layer.
- `repo_ops` remains the explicit home of repo-local semantics.
- root entrypoints remain thin
- generated outputs remain deterministic, local-first, inspectable, and diffable
- route-first and index-first retrieval remain preferred over broad scans
- human-readable and machine-readable durable artifacts remain paired where practical
- compatibility surfaces remain bounded, explicit, and reviewable

### Public-contract invariants
Unless a separate accepted decision explicitly changes them, the rewrite preserves:

- `coordination_index` as the current-state machine start-here surface
- `planning_catalog` as the deep trace-linked planning read model
- `initiative_index` as the compact initiative-family view
- `task_index` as the task execution and dependency view
- `traceability_index` as the durable trace-linked join
- `query authority --domain planning` as the canonical machine lookup for those planning questions
- the current CLI command names and parser family structure

---

## 3. Baseline Constraints Already In Force

The rewrite is not free to ignore accepted repo direction that already landed.

### Coordination start-here is already governed
The current repo has already accepted and implemented a machine-first coordination start-here model. `coordination_index` and `coordination_tracking.md` are not optional convenience byproducts. They are the default current-state entry surfaces. The rewrite may simplify how they are built, but it must not casually replace their role.

### Planning public authorities already exist
The planning authority unification work already added a canonical planning catalog and a machine authority map while explicitly keeping the current family views available as narrower projections or compatibility surfaces. The rewrite therefore preserves a working public-authority split. It does not invent one from scratch.

### Command authority is already partly registry-backed
The current CLI already uses a typed command-group registry and parser construction flow. Command presence and hierarchy are not purely ad hoc. The rewrite should extend and normalize this model. It should not describe command authority as if nothing meaningful exists yet.

### Hotspot remediation already has accepted boundaries
The live repo direction for planning and task authoring hotspots favors helper extraction and stable service entrypoints around `PlanningScaffoldService` and `TaskLifecycleService`. The rewrite should honor that accepted direction unless new evidence justifies a superseding decision.

### History and compatibility already have repo-native models
The repo already uses:

- `open/` and `closed/` placement for tasks
- `status: deprecated` for governed artifacts retained temporarily
- `authority: historical` for planning records that remain queryable context rather than live authority
- compatibility contracts with `supported`, `transitional`, and `deprecated` support levels

The rewrite should extend those models before inventing a generic replacement taxonomy.

---

## 4. Surface Classification Model

The earlier draft overloaded words such as `archive`, `archived`, `retired`, and `historical`. That is no longer acceptable for execution planning. Every significant surface must be classified on four independent axes.

### 4.1 Classification axes

| Axis | Allowed or Expected Values | Purpose |
|---|---|---|
| Lifecycle status | `draft`, `active`, `deprecated` | Governed artifact lifecycle only. This stays aligned with `status_tracking_standard.md`. |
| Authority role | authored authority, canonical machine answer, discovery index, generated projection, historical record, compatibility surface | Clarifies what the surface means in the repo model. |
| Storage or placement class | active family location, family-native closed or historical location, compatibility namespace or marker, deleted after proof, future standardized history store | Separates file placement from lifecycle status. |
| Compatibility support level | `supported`, `transitional`, `deprecated`, or `n/a` | Declares whether the surface is an intentional live boundary or only a migration aid. |

### 4.2 Non-negotiable rules
- Do not use `archived` as a governed lifecycle status unless a later standards-and-schema program explicitly changes the status vocabulary.
- Do not assume a new repository-wide archive directory or archive taxonomy exists today.
- Treat "archive" only as informal shorthand for possible future storage treatment, not as current executable policy.
- No surface may move, retire, or be deleted until all four axes are classified for that surface family.

### 4.3 History-state model for this rewrite
For this program, historical cleanup can mean one of four things:

| Action | Meaning | Typical Current Repo Pattern |
|---|---|---|
| Keep active | Surface remains current and live | active index, active standard, active command doc |
| Keep as historical in place | Surface stays in the family, but is explicitly no longer current authority | `status: deprecated` plus `authority: historical` on planning records |
| Relocate through an existing family-native mechanism | Surface moves using an already-governed pattern | task move from `open/` to `closed/` |
| Delete after proof | Surface is removed only after consumer rewrites and validation prove it is no longer needed | summary-surface retirement style cleanup |

Any future "history store" or true archive area is a separate gated standards question, not a default assumption of this rewrite.

---

## 5. Target Architecture

## 5.1 Top-level shape
Keep the current top-level shape:

- `docs/` remains the human-readable authority layer.
- `workflows/` remains the procedural authority layer.
- `core/control_plane/` remains the canonical machine-readable authority layer.
- `core/python/` remains the runtime, validation, query, sync, and helper tooling layer.

That shape is already correct.

## 5.2 Authority model
Use a stricter authority model inside the same public repository shape:

- authored authority stays explicit
- canonical machine answers stay explicit
- discovery indexes stay narrow and question-oriented
- generated projections stay visibly derived
- compatibility surfaces stay explicitly classified

The rewrite must improve role clarity, not create hidden authority.

## 5.3 Planning model
The rewrite may introduce a normalized internal planning graph, but only as a runtime implementation detail unless a separate accepted decision explicitly authorizes a new public artifact family.

### Public planning authorities to preserve

| Question | Public authority surface | Rewrite treatment |
|---|---|---|
| What is the current planning state and next action? | `coordination_index` and `query coordination` | Preserve the contract; simplify internals only. |
| What is the full trace-linked planning context for one initiative? | `planning_catalog` and `query planning` | Preserve the contract; simplify internals only. |
| What is the compact initiative-family view? | `initiative_index` and `query initiatives` | Preserve the contract. |
| What is the authoritative task execution state and dependency graph? | `task_index` and `query tasks` | Preserve the contract. |
| What is the durable trace-linked join and initiative outcome state? | `traceability_index` and `query trace` | Preserve the contract. |

### Internal planning-graph rule
The internal graph:

- may be a runtime assembly over existing governed inputs
- may feed shared projection logic
- may reduce bespoke builder duplication
- may not become a shadow public planning-family reset by accident

If the internal graph ever needs to become a new governed public artifact family, that requires a separate accepted planning-boundary decision.

## 5.4 Descriptor-authority matrix
Descriptor expansion is only sound when authored truth versus derived output is explicit. The rewrite therefore uses the following matrix.

| Concern | Current authoritative source | Rewrite move | Derived outputs | Guardrail |
|---|---|---|---|---|
| Command presence and hierarchy | CLI registry plus parser tree | Extend and normalize, do not replace casually | command index, command doc structural metadata, source-surface links | No second durable command-existence truth without explicit superseding decision. |
| Command companion metadata | command docs, registry metadata, generated command index | Tighten derivation and reconciliation | command-page sections, command lookup records | Human docs remain semantic companions; machine lookup remains routing-oriented. |
| Projection family configuration | governed planning and control-plane artifact families | Add bounded projection descriptors where they reduce hand-wiring | coordination, task, initiative, and planning projection internals | Public planning questions remain unchanged. |
| Sync family selection | existing sync registries or enumerations | Normalize into governed specs where beneficial | sync orchestration and family discovery | Do not create duplicate sync truth in both code constants and governed metadata long-term. |
| Validator selection and document semantics dispatch | governed standards, schemas, registries, and explicit rules | Move selection logic toward governed rule registries | validator dispatch and doc-family selection | Python consumes authored rules; it does not silently become the source of truth. |
| Artifact-role classification | new governed control-plane metadata | Publish and validate role classification | inventory, reconciliation, migration ledger views | Role metadata must stay small, explicit, and reviewable. |
| Internal planning graph | existing indexes, planning docs, and trace-linked records | Introduce as private runtime composition | shared projection engine inputs | Not a new public artifact family by default. |

## 5.5 Runtime decomposition direction
The runtime should become a thinner consumer of governed authority and a cleaner repo-local orchestration layer, but it should extend accepted boundaries rather than restart them.

Target direction:

- keep `repo_ops` explicit
- keep CLI entrypoints thin
- preserve stable service entrypoints where recent accepted designs say to preserve them
- extract helper-backed collaborators where responsibility concentration remains high
- let shared projection and selection services reduce duplication only after parity contracts exist

---

## 6. Capability Preservation Matrix

| Current capability or surface | Target disposition | Rewrite treatment |
|---|---|---|
| `query coordination` | Preserve | Keep as the current-state start-here machine query. |
| `docs/planning/coordination_tracking.md` | Preserve | Keep as the compact human current-state byproduct. |
| `query planning` and `planning_catalog` | Preserve | Keep as the canonical deep planning read model. |
| `query initiatives` and `initiative_index` | Preserve | Keep as the compact initiative-family view. |
| `query tasks` and `task_index` | Preserve | Keep as the authoritative task execution view. |
| `query trace` and `traceability_index` | Preserve | Keep as the durable trace join. |
| `query authority` and the authority map | Preserve | Keep as the canonical machine route to planning authority questions. |
| CLI command family names | Preserve | Command names stay stable unless a replacement is explicitly versioned and parity-backed. |
| CLI parser family structure | Preserve and normalize | Extend the current registry-backed parser model rather than replacing it wholesale. |
| command docs under `docs/commands/` | Preserve | Human-readable semantic companion layer remains required. |
| `command_index` | Preserve | Lookup surface remains machine-readable and routing-oriented. |
| workflow modules and `ROUTING_TABLE.md` | Preserve | Procedural and routing authority remain authored. |
| `route_index` and workflow metadata | Preserve and reconcile | Keep derived and discoverable, with tighter duplication control. |
| schema catalog, validator registry, and examples | Preserve | Keep fail-closed governed artifact families intact. |
| document semantics validation | Preserve and refactor | Keep guarantees; normalize selection logic only where authored rules are explicit. |
| task lifecycle commands | Preserve and refactor | Keep dry-run/write parity, path repair, and same-change refresh guarantees. |
| planning scaffold and bootstrap commands | Preserve and refactor | Keep capability; decompose hotspot responsibilities around stable entrypoints. |
| compatibility wrappers or marker surfaces | Mixed | Classify by support level before any retirement decision. |
| closed tasks and deprecated or historical planning docs | Preserve via repo-native history model | Do not blanket-relocate; use family-native history handling first. |
| redundant one-off summary or migration artifacts | Mixed | Retire only through bounded consumer-mapped cleanup slices. |

---

## 7. History, Retirement, and Compatibility Policy

## 7.1 Current repo-native history model to preserve
The repo already has usable historical-state mechanisms:

- Tasks move between `docs/planning/tasks/open/` and `docs/planning/tasks/closed/`.
- Planning artifacts can remain in place with `status: deprecated`.
- Planning artifacts can declare `authority: historical` when they are durable context rather than live authority.
- Compatibility contracts already support `supported`, `transitional`, and `deprecated` support levels.
- Bounded retirement can delete a redundant surface after direct dependency rewrites, as demonstrated by the summary-surface retirement pattern.

The rewrite uses these models as the default starting point.

## 7.2 What this rewrite will and will not assume
This rewrite assumes:

- some live surfaces are redundant enough to retire after proof
- some historical planning records should remain queryable context
- some compatibility surfaces are temporary and should be removed later
- some compatibility surfaces are intentional and should remain

This rewrite does not assume:

- a global archive directory already exists
- all closed tasks or old planning docs should move somewhere else
- "archive" is a current lifecycle status
- every compatibility surface should disappear by the end

## 7.3 History-action decision matrix

| Surface condition | Preferred action | Required proof |
|---|---|---|
| Still answers a live authority question | Keep active | authority-map parity and current consumers confirmed |
| No longer live authority but still needed for rationale or lineage | Keep as historical in place | `deprecated` or equivalent lifecycle treatment, plus explicit historical role where applicable |
| Family already has a governed historical placement model | Use that family-native move | placement rule validation and reference repair |
| Redundant one-off surface with no active authority role | Delete after bounded dependency rewrite | consumer map, broken-link validation, and migration ledger entry |
| Compatibility surface still supports live discoverability or boundary clarity | Keep with explicit support level and retention reason | compatibility classification completed |
| Compatibility surface is transitional only and replacement is proven | Retire | support level is `transitional` or `deprecated`, active consumers gone, rollback path recorded |

## 7.4 Required gates before any historical relocation or retirement
- a family-specific consumer map exists
- route-first and index-first discoverability impacts are documented
- authority-map implications are checked where planning or governance routing is affected
- traceability and governed-reference repair is planned in the same change
- the migration ledger records the intended action
- rollback instructions exist for that family slice

## 7.5 Durable policy absorption rule
When a historical planning chain contains durable standing policy, the rewrite should promote that policy into:

- standards
- governed registries
- schemas and examples
- canonical docs or authority maps

Only after that promotion is complete may the original planning chain be reclassified, retained as historical, or retired.

---

## 8. Standards and Governance Prerequisites

The broad prerequisite no-go that originally blocked the rewrite has been cleared. Phase 0 and Phase 1 published the required repo-native guidance and control surfaces, the Phase 2 entry review recorded an explicit approval outcome, the first bounded artifact-role metadata slice landed, the pilot outcome review closed cleanly, the Phase 3 entry review closed cleanly, and the first bounded Phase 3 slice landed. The remaining no-go is now narrower: broader Phase 3 or later work stays blocked until the Phase 3 command-companion outcome-review task records an explicit pass or block outcome and, if it passes, hands the trace to a new bounded checkpoint rather than implied rollout.

### Published prerequisite and checkpoint surfaces
- refreshed baseline evidence and hotspot inventory in the traced rewrite implementation package
- four-axis classification and retention guidance in `rewrite_surface_classification_standard.md`
- rewrite execution-control guidance, parity boundary, and checkpoint workflow in `rewrite_execution_control_standard.md`
- critical-surface classification, history and compatibility consumer maps, support-level classification, and rollback expectations in `docs/planning/design/implementation/structural_rewrite_program.md`
- the planning public-authority parity contract in `core/control_plane/contracts/acceptance/structural_rewrite_program_acceptance.v1.json`
- the completed Phase 0 and Phase 1 transition record in `core/control_plane/ledgers/migrations/structural_rewrite_program_phase0_phase1_ready.v1.json`
- the completed Phase 0 and Phase 1 validation evidence in `core/control_plane/ledgers/validation_evidence/structural_rewrite_program_phase0_phase1_baseline.v1.json`
- the closed Phase 2 entry-review task in `docs/planning/tasks/closed/review_structural_rewrite_program_phase2_entry_package.md`
- the dedicated first-slice checkpoint document in `docs/planning/design/implementation/structural_rewrite_artifact_role_registry_pilot.md`
- the dedicated first-slice transition record in `core/control_plane/ledgers/migrations/structural_rewrite_artifact_role_registry_pilot.v1.json`
- the dedicated first-slice validation evidence in `core/control_plane/ledgers/validation_evidence/structural_rewrite_artifact_role_registry_pilot.v1.json`
- the closed pilot outcome review task in `docs/planning/tasks/closed/review_structural_rewrite_artifact_role_registry_pilot_outcome.md`
- the Phase 3 entry package in `docs/planning/design/implementation/structural_rewrite_phase3_command_authority_entry.md`
- the closed Phase 3 entry-review task in `docs/planning/tasks/closed/review_structural_rewrite_phase3_entry_package.md`
- the Phase 3 slice plan in `docs/planning/design/implementation/structural_rewrite_phase3_command_companion_source_surface_normalization.md`
- the Phase 3 entry transition record in `core/control_plane/ledgers/migrations/structural_rewrite_phase3_command_companion_source_surface_normalization_ready.v1.json`
- the Phase 3 entry validation evidence in `core/control_plane/ledgers/validation_evidence/structural_rewrite_phase3_command_companion_source_surface_normalization_ready.v1.json`
- the Phase 3 slice transition record in `core/control_plane/ledgers/migrations/structural_rewrite_phase3_command_companion_source_surface_normalization.v1.json`
- the Phase 3 slice validation evidence in `core/control_plane/ledgers/validation_evidence/structural_rewrite_phase3_command_companion_source_surface_normalization.v1.json`
- the closed Phase 3 implementation task in `docs/planning/tasks/closed/implement_structural_rewrite_phase3_command_companion_source_surface_normalization.md`
- the current Phase 3 outcome-review task in `docs/planning/tasks/open/review_structural_rewrite_phase3_command_companion_source_surface_normalization_outcome.md`

### Remaining post-slice controls
- an explicit pass or block outcome in `docs/planning/tasks/open/review_structural_rewrite_phase3_command_companion_source_surface_normalization_outcome.md`
- confirmation that the root command page plus the bounded `doctor`, `sync`, and `validate` command docs still agree with the command-index implementation paths
- confirmation that the new command-index sync guard and direct unit coverage fail closed on future source-surface drift without acting as a second command-authority source
- confirmation that `registry.py` plus `parser.py` remain the only accepted command-authority source and that public planning parity remains unchanged
- if the review passes, identification of the next explicit bounded checkpoint rather than implied broader Phase 3 or later rollout
- continued confirmation that later-touched families outside the current published critical-surface scope get their own classification or parity package before implementation

### Possible later standards work
- a more specific descriptor-authority standard, if the existing rewrite execution-control standard proves too coarse during later descriptor slices
- a more explicit compatibility lifecycle or support-level extension, if Phase 7 needs tighter standing policy than the current compatibility model already provides
- a more explicit history-placement extension, if later family-specific cleanup reveals a durable rule that cannot stay in the current rewrite governance surfaces

Prefer extending current standards where practical. Avoid creating new standards just to rename existing concepts or to restate guidance already carried by the published rewrite standards.

### Separate gated question
If the repo eventually needs a true cross-family archive storage model, that is a separate standards-and-schema initiative. It is not assumed by this rewrite program.

### Intended homes for prerequisite guidance and control surfaces
To avoid ad hoc execution sprawl, the rewrite should place its durable guidance and control surfaces in the existing repo-native homes:

- normative guidance belongs under `docs/standards/`, preferably as extensions to existing standards when practical
- human-readable phase plans, checkpoints, and phase-entry reviews belong under `docs/planning/design/implementation/`
- machine-readable slice transition records belong under `core/control_plane/ledgers/migrations/`
- machine-readable parity and validation evidence pointers belong under `core/control_plane/ledgers/validation_evidence/`

The rewrite should not invent a separate free-floating review or ledger area unless the existing planning and control-plane families prove inadequate during Phase 0.

---

## 9. Phased Rewrite Plan

## Phase 0: Baseline Refresh and Governance Freeze
### Objective
Refresh current-state evidence, freeze rewrite guardrails, and publish the classification and parity framework the later phases must obey.

### Current status
Completed. The baseline refresh, hotspot refresh, parity boundary, classification standard, execution-control standard, and pilot-family selection are already recorded in the repo-native rewrite package.

### In scope
- March 13, 2026 baseline snapshot or later refreshes of the same shape
- hotspot inventory refresh against the live repo, with any older hotspot examples treated only as historical review signals until the current source tree is re-counted
- public planning-authority parity contract
- artifact-role and four-axis classification publication
- pilot-family selection
- rewrite slice-control record format and checkpoint workflow

### Explicitly not yet allowed
- runtime behavior changes
- historical relocation
- compatibility retirement

### Exit criteria
- current-state baseline is published
- hotspot inventory reflects the live repo rather than older generalizations
- the four-axis classification model is accepted
- one Phase 2 pilot family is fixed, justified, and bounded
- the rewrite slice-control record format and checkpoint workflow are published
- no-go conditions are explicit

## Phase 1: Surface Classification and Consumer Mapping
### Objective
Classify important surfaces and map the real consumers of any candidate history cleanup or compatibility retirement work.

### Current status
Completed for the approved critical-surface gate scope. The currently published package covers public planning authorities, command-boundary surfaces, compatibility surfaces, and one historical-retention chain. Broader family-by-family workflow or route and validator, sync, or projection classification should be treated as later phase-entry work before those families are touched.

The broader Phase 1 wording still present in `req.structural_rewrite_program.004` should therefore be interpreted through this narrower published gate scope, not as blanket evidence that untouched workflow, route, sync, validator, projection, history, or compatibility families are already classified. Before any successor checkpoint touches one of those families, either that broader wording needs to be narrowed to the published scope or the exact family-specific classification or parity addendum for the new slice needs to be published.

### In scope
- critical public planning surface classification
- command and command-doc surface classification
- compatibility surface classification
- historical-retention candidate classification
- consumer maps for history-candidate and compatibility surfaces
- retention reasons for intentionally live compatibility markers or wrappers

### Explicitly not yet allowed
- deleting or moving surfaces
- broad descriptor rollout

### Exit criteria
- every critical surface in the approved Phase 1 gate scope has four-axis classification
- every candidate cleanup surface has a consumer map
- every compatibility surface has an initial support-level classification
- no unresolved public-authority ambiguity remains
- any later-touched family that falls outside the current Phase 1 gate scope gets its own phase-entry classification package before implementation

## Phase 2: Descriptor and Derivation Pilot
### Objective
Prove one low-blast-radius descriptor-backed family and its derivation direction before broad rollout.

### Current status
Completed for one bounded slice. The Phase 2 entry-review gate is closed, the only accepted pilot family is artifact-role metadata, the first slice is now published as a small dedicated registry with its own checkpoint package, and the pilot outcome review is closed. No additional Phase 2 rollout is currently authorized; the rewrite is now paused at the Phase 3 command-companion outcome-review gate rather than reopened for broader descriptor rollout.

### In scope
- artifact-role metadata family
- one additive read-only metadata slice with clear authored truth
- parity checks between current behavior and the pilot's descriptive metadata package
- the first slice's dedicated checkpoint document, migration record, and validation evidence

### Current pilot declaration
- The pilot family is fixed to artifact-role metadata only.
- The first slice lands as a small dedicated registry, not additive metadata inside an existing governed family.
- The first slice should stay read-only and additive: it may classify and expose roles, but it may not drive live query routing, sync selection, validator dispatch, or command authority in the same change.
- The first slice should prove deterministic derivation, reviewable storage, bounded consumers, and rollback clarity before any broader descriptor rollout is considered.

### Explicitly not yet allowed
- broad descriptor expansion across multiple unrelated families
- sync target selection, validator-selection rules, or command presence and hierarchy as the first pilot family
- command authority replacement
- planning-graph rollout
- turning artifact-role metadata into live selection logic without a new bounded checkpoint package
- treating the completed pilot slice as standing authorization for broader descriptor rollout or Phase 3 implementation

### Exit criteria
- one pilot family is live and validated
- authored-versus-derived direction is explicit
- rollback for the pilot family is documented
- the repo is not carrying unbounded dual truth after the pilot
- the pilot's first slice remains additive and does not quietly widen into command, planning, sync, or validator authority changes

## Phase 3: Command Authority Normalization
### Objective
Extend and normalize the existing registry-backed command authority so command docs, command index, parser metadata, and source-surface metadata stop drifting.

### Current status
Entered and completed for one bounded companion-only slice. The Phase 3 entry review is closed, the approved first slice was command companion source-surface normalization, the root command page plus `23` bounded `doctor`, `sync`, and `validate` command docs now align with the parser-owned or family-owned implementation paths already published in `command_index`, and the current hard stop is `docs/planning/tasks/open/review_structural_rewrite_phase3_command_companion_source_surface_normalization_outcome.md`. No broader Phase 3 rollout is currently authorized.

### In scope
- command registry metadata tightening
- parser-backed introspection normalization
- command index generation alignment
- command-doc structural metadata derivation
- source-surface metadata reconciliation

### Non-negotiable guardrail
During this phase, the current CLI registry and parser tree remain the machine authority for command presence and hierarchy unless a separate accepted decision explicitly changes that boundary.

### Bounded first-slice outcome
- The root command page's primary `## Source Surface` entry plus the bounded `doctor`, `sync`, and `validate` command docs now point at the parser-owned or family-owned implementation paths already published in `core/control_plane/indexes/commands/command_index.v1.json`.
- `core/python/src/watchtower_core/repo_ops/sync/command_index.py` now fails closed when a companion command doc's `Command` table or primary `## Source Surface` entry drifts from the registry-backed implementation path.
- `core/python/tests/unit/test_command_index_sync.py` now covers that guard directly.
- The slice stayed companion-only: command presence, hierarchy, flags, outputs, and public planning-authority answers did not change.

### Migration strategy
- treat command-index `implementation_path` values as the parity oracle for companion command docs when the index is already derived from the live registry-backed parser tree
- reconcile only bounded command-doc source-surface metadata to those existing family-owned paths
- add only the narrowest fail-closed drift guard needed to catch doc-index disagreement without becoming a second command-authority source
- stop after each bounded slice with an explicit outcome review before any broader command-authority work begins

### Current checkpoint
Phase 3 entry is already closed in `docs/planning/tasks/closed/review_structural_rewrite_phase3_entry_package.md`. The current hard stop is `docs/planning/tasks/open/review_structural_rewrite_phase3_command_companion_source_surface_normalization_outcome.md`. That review must confirm docs-plus-index parity held, confirm the new drift guard remains companion-only, and either keep broader rewrite work blocked or hand off to one new explicit bounded checkpoint. The closed Phase 3 entry review already recorded that no additional command-adjacent workflow, route, or compatibility classification addendum was needed for this first slice because it stayed inside already-classified command companion surfaces. That resolution does not pre-clear later command, workflow, route, sync, validator, or projection work.

### Exit criteria
- no drift between registry, parser tree, command index, and command docs
- command existence and hierarchy remain explicit
- no second durable command-existence authority has been introduced by accident

## Phase 4: Shared Projection Engine and Internal Planning Graph
### Objective
Reduce duplicated projection mechanics by introducing one internal planning graph and one shared projection engine behind the existing planning-family contracts.

### In scope
- graph assembly from existing governed inputs
- shared projection framework for coordination, planning, initiative, task, and adjacent human byproducts
- projection dependency ordering and cache behavior
- parity and intentional-improvement review for projection outputs

### Non-negotiable guardrails
- the internal graph is a private runtime detail in this phase
- public planning question boundaries do not change
- the five current planning authorities remain the machine contract
- `query authority --domain planning` must still resolve those same question-specific public answers
- artifact-role metadata from Phase 2 may not silently become a public planning-boundary change or an unreviewed projection-authority source

### Migration strategy
Dual-run the new projection engine against:

- `coordination_index`
- `planning_catalog`
- `initiative_index`
- `task_index`
- selected human planning byproducts

### Phase-entry checkpoint
Do not enter this phase until the Phase 3 command-companion outcome review has closed cleanly and a dedicated Phase 4 re-review confirms that the internal graph remains a private runtime detail, the five planning authorities remain the public contract, and the planned projection slices have explicit rollback boundaries. If the outcome review instead identifies more bounded command-companion or command-index work, that work remains Phase 3 and must use a new explicit Phase 3 checkpoint rather than being relabeled as Phase 4. If sync, validator, or projection family classification needs more detail than the Phase 1 gate package published, that family-specific classification must be published as part of the Phase 4 entry package before implementation.

### Exit criteria
- shadow outputs match or intentionally improve with documented approval
- public planning boundaries are unchanged
- no new public planning artifact family has been introduced accidentally

## Phase 5: Hotspot Decomposition
### Objective
Decompose remaining repo-local hotspots with bounded helper extraction and collaborator seams instead of broad service-contract or meta-framework redesign.

### Current hotspot anchors
Use the live hotspot cluster, not older shorthand, when planning this phase. At the current checkpoint the largest rewrite-relevant Python files include `initiative_index.py`, `document_semantics.py`, `task_lifecycle.py`, `workflow_index.py`, `planning_scaffold_specs.py`, `loader.py`, `planning_projection_serialization.py`, `planning_documents.py`, `planning_bootstrap_support.py`, `github_task_sync_support.py`, and adjacent coordination or validation models. Do not treat the earlier `planning_scaffolds.py` framing as sufficient without a fresh recount at execution time.

### Mandatory workstream A: planning scaffolding and bootstrap seams
- keep `PlanningScaffoldService` as the stable orchestration entrypoint
- extract scaffold-kind specs, rendering helpers, bootstrap artifact builders, and planning-surface refresh helpers
- preserve current CLI contracts and planning artifact shapes

### Mandatory workstream B: task lifecycle, companion-path repair, and validation seams
- keep `TaskLifecycleService` as the stable task mutation entrypoint
- extract companion-path repair into dedicated helper-backed collaborators
- narrow validation and document-family dispatch seams only where authored rules are explicit
- preserve dry-run/write behavior, task placement rules, and same-change repair guarantees

### Explicitly not allowed
- a new reflection-heavy generic planning framework
- architecture-purity rewrites that move or rename stable service entrypoints without need
- public command or payload changes unless separately versioned

### Exit criteria
- hotspot services are thinner and easier to review
- stable entrypoints remain stable
- helper extraction has reduced responsibility concentration without creating hidden behavior changes

## Phase 6: Standards Absorption and Family-Specific History Cleanup
### Objective
Absorb durable policy into standing authority and perform bounded history cleanup using repo-native patterns and consumer-mapped slices.

### In scope
- promoting standing rules from planning chains into standards or canonical machine-readable surfaces
- bounded retirement of redundant one-off surfaces
- reclassification of planning records as historical where appropriate
- family-native historical placement where already governed
- navigation and discoverability refresh for the smaller active baseline

### Explicitly not assumed
- a new global archive area
- blanket relocation of all closed tasks, PRDs, designs, decisions, or traces

### Migration strategy
Operate in bounded slices modeled after the summary-surface retirement pattern:

1. classify one direct dependency chain
2. rewrite surviving consumers
3. repair references
4. rebuild derived surfaces
5. validate
6. only then reclassify, move through an existing family-native mechanism, or delete

### Expected repo-native tools for this phase
- `closed/` placement for terminal tasks
- `status: deprecated` where temporary retention is needed
- `authority: historical` for durable but non-current planning context
- deletion after proof for redundant one-off surfaces

### Phase-entry checkpoint
Do not enter this phase until history-state and retention guidance is published, family-specific consumer maps exist for the targeted slices, and a dedicated Phase 6 re-review confirms the touched surfaces are using repo-native history handling rather than a speculative cross-family archive model.

### Exit criteria
- durable policy has moved into standing authority where needed
- the active baseline is smaller and clearer
- historical context remains discoverable where policy requires it
- no query, link, or traceability path has been orphaned

## Phase 7: Compatibility Retirement and Retained-Boundary Hardening
### Objective
Retire only transitional compatibility debt while explicitly documenting the supported compatibility boundaries that remain intentional.

### In scope
- compatibility support-level confirmation
- retirement of transitional or deprecated shims with proven replacements
- retention reasons for compatibility surfaces that remain live on purpose
- closeout of stale migration-only compatibility metadata

### Non-negotiable guardrail
Do not treat all compatibility surfaces as temporary leftovers. Some exist for import stability, discoverability, path continuity, or explicit boundary clarity and may remain supported.

### Phase-entry checkpoint
Do not enter this phase until every touched compatibility surface has an explicit support-level classification, retention reason, and active-consumer check, and a dedicated Phase 7 re-review confirms the retirement targets are genuinely transitional.

### Exit criteria
- every compatibility surface has an explicit support level
- transitional shims with proven replacements are retired
- intentionally retained compatibility boundaries have explicit rationale and, where appropriate, an expected horizon

## Phase 8: Rewrite Closeout
### Objective
Accept the rewrite as the new baseline only after parity, validation, and migration ledgers prove the simplification is real.

### In scope
- final parity signoff
- validate-all and targeted regression reruns
- migration ledger closeout
- final standards and README cleanup
- explicit disposition review for rewrite-specific standards

### Exit criteria
- no temporary rewrite scaffolding remains active without ownership
- validation is green
- the final baseline is simpler without weakened authority or discoverability
- each rewrite-specific standard is explicitly classified as standing authority, absorbed into broader standards, or retired after rewrite closeout

---

## 10. Migration, Acceptance, and Rollback

## 10.1 General cutover rules
- Never replace a public authority surface before its replacement has run in shadow mode.
- Never change a public planning question boundary without an explicit accepted decision.
- Never retire a projection until parity or approved intentional improvement is documented.
- Never reclassify or move historical material until durable policy has been promoted where necessary.
- Never delete a compatibility surface until active consumers are gone and the migration ledger records proof.

## 10.2 Rewrite slice-control records
Each Phase 2 through Phase 8 slice should publish a durable human and machine control pair before cutover:

- a machine-readable slice transition record under `core/control_plane/ledgers/migrations/` that records the old and new builder or authority source, related paths, and the bounded transition summary supported by the live migration-record schema
- a companion human checkpoint document under `docs/planning/design/implementation/` that records the shadow-mode window, parity result, approved intentional improvements, rollback procedure, approval outcome, and any rollback trigger details that do not belong in the current migration-record schema

When parity or validation evidence is produced separately, the slice transition record and checkpoint document should point to the matching records under `core/control_plane/ledgers/validation_evidence/`.

This pair is the default durable control surface for rewrite execution. Do not rely on transient review notes or commit messages as the only record of slice approval.

No successor checkpoint is implementation-ready unless its package also makes the touched slice's authored truth, derived outputs, current consumers, parity method, and rollback path explicit enough to review without inference.

## 10.3 Public planning parity contract
The rewrite is not acceptable unless all of the following remain true:

- `query authority --domain planning` still resolves the same five planning questions
- route-first and index-first discoverability still point users to the right planning entry surfaces
- `coordination_index` remains the current-state start-here answer
- `planning_catalog` remains the deep planning answer
- `initiative_index`, `task_index`, and `traceability_index` remain explicit answers to their current questions

## 10.4 History and compatibility proof obligations
Before any history cleanup or compatibility retirement:

- consumer maps must be complete for the touched slice
- broken-link validation must pass
- repository-path, planning, and traceability surfaces must reconcile
- human and machine discoverability for the touched boundary must still work
- retained compatibility surfaces must have explicit rationale

## 10.5 Family-level rollback requirement
Each rewrite slice needs a rollback plan that answers:

- what old path remains available
- what cutover flag or fallback exists
- how to restore the previous builder or metadata source
- how to reverse any file moves or reclassification for the current slice

## 10.6 Required validation scenarios
- `watchtower-core doctor --format json`
- `watchtower-core validate all`
- command discovery parity across top-level and representative leaf commands
- command index, command docs, parser metadata, and source-surface reconciliation
- planning-authority parity via `query authority`
- route-first and index-first discoverability checks
- coordination, planning, initiative, task, and trace query parity
- task create, update, and transition behavior including path-repair cases
- planning scaffold and bootstrap dry-run and write parity
- mixed active and historical planning projection cases
- compatibility behavior before and after transitional-surface retirement

## 10.7 Mandatory phase-entry re-review checkpoints
Phase 2, Phase 3, Phase 4, Phase 6, and Phase 7 require explicit phase-entry re-review before implementation begins for those phases. Phase 3 also now requires a post-slice outcome review before any additional Phase 3 or later-phase work proceeds.

- Phase 2 re-review confirmed that the pilot family, derivation direction, and authored-truth boundary were fixed and low blast radius.
- Phase 3 entry review already confirmed the bounded command-authority slice, parser and registry authority boundary, companion family classification sufficiency, and rollback package expectations before the first Phase 3 slice began.
- Phase 3 outcome review must confirm docs-plus-index parity held, the new drift guard remains companion-only, and any next work is framed as a new bounded checkpoint instead of implied broader rollout. A passing review without a named successor checkpoint is still a no-go for further implementation.
- Before any successor checkpoint touches a family outside the already-classified command companion set, either the broader PRD Phase 1 wording must be narrowed to the published gate scope or the exact family-specific classification or parity addendum for that slice must be published.
- Before implementation begins under any successor checkpoint, refresh or explicitly relabel stale supporting current-state narration in the feature design and adjacent repo-native rewrite package surfaces so the trace tells one checkpoint story.
- Phase 4 re-review confirms the internal planning graph remains private by default and the touched projection slices have bounded rollback.
- Phase 6 re-review confirms history handling uses published repo-native guidance, complete consumer maps, and explicit discoverability proof obligations.
- Phase 7 re-review confirms each retirement target is truly transitional and not an intentionally retained compatibility boundary.

## 10.8 Current controlling checkpoint
At the moment this document is updated, the controlling rewrite checkpoint is the Phase 3 command-companion outcome-review package already published in the live repo:

- `docs/planning/design/implementation/structural_rewrite_program.md`
- `docs/planning/design/implementation/structural_rewrite_artifact_role_registry_pilot.md`
- `docs/planning/design/implementation/structural_rewrite_phase3_command_authority_entry.md`
- `docs/planning/design/implementation/structural_rewrite_phase3_command_companion_source_surface_normalization.md`
- `core/control_plane/contracts/acceptance/structural_rewrite_program_acceptance.v1.json`
- `core/control_plane/ledgers/migrations/structural_rewrite_program_phase0_phase1_ready.v1.json`
- `core/control_plane/ledgers/migrations/structural_rewrite_artifact_role_registry_pilot.v1.json`
- `core/control_plane/ledgers/migrations/structural_rewrite_phase3_command_companion_source_surface_normalization_ready.v1.json`
- `core/control_plane/ledgers/migrations/structural_rewrite_phase3_command_companion_source_surface_normalization.v1.json`
- `core/control_plane/ledgers/validation_evidence/structural_rewrite_program_phase0_phase1_baseline.v1.json`
- `core/control_plane/ledgers/validation_evidence/structural_rewrite_artifact_role_registry_pilot.v1.json`
- `core/control_plane/ledgers/validation_evidence/structural_rewrite_phase3_command_companion_source_surface_normalization_ready.v1.json`
- `core/control_plane/ledgers/validation_evidence/structural_rewrite_phase3_command_companion_source_surface_normalization.v1.json`
- `docs/planning/tasks/closed/review_structural_rewrite_program_phase2_entry_package.md`
- `docs/planning/tasks/closed/implement_structural_rewrite_artifact_role_registry_pilot.md`
- `docs/planning/tasks/closed/review_structural_rewrite_artifact_role_registry_pilot_outcome.md`
- `docs/planning/tasks/closed/review_structural_rewrite_phase3_entry_package.md`
- `docs/planning/tasks/closed/implement_structural_rewrite_phase3_command_companion_source_surface_normalization.md`
- `docs/planning/tasks/open/review_structural_rewrite_phase3_command_companion_source_surface_normalization_outcome.md`

The Phase 2 entry-review approval, first bounded Phase 2 slice, pilot outcome review, Phase 3 entry review, and first bounded Phase 3 slice have already been recorded. The current hard stop is the open Phase 3 command-companion outcome-review task. No broader Phase 3 rollout or later phase should begin until that task records an explicit pass or block outcome, and no successful first slice should be treated as standing authorization for broader rollout.

A positive outcome review must do more than say the landed slice looks clean. It must record whether broader rewrite work remains blocked or may proceed and, if it may proceed, it must name the next bounded checkpoint rather than implying automatic Phase 3 or Phase 4 continuation. A positive review that does not name and package that successor checkpoint is still not approval to continue implementation. The closed Phase 3 entry review already answered the first-slice classification sufficiency question. Any later family outside the already-classified command companion surfaces still needs its own classification or parity package before implementation.

---

## 11. Risk Analysis

### Duplicate-authority risk
Risk: descriptor work creates a second durable truth source instead of reducing duplication.
Mitigation: every descriptor family must declare authored truth, derived outputs, and fallback behavior before rollout.

### Public-boundary churn risk
Risk: an internal planning graph gradually becomes a public planning-model reset.
Mitigation: keep the graph private by default and require an explicit accepted decision for any public-boundary change.

### Command-authority drift risk
Risk: command descriptors or metadata layers drift from the live parser and registry model.
Mitigation: treat the current registry and parser tree as authoritative during normalization unless explicitly superseded.

### History-taxonomy risk
Risk: vague archive language introduces an ungoverned storage or lifecycle model.
Mitigation: use the four-axis classification model and repo-native history patterns first.

### Over-broad cleanup risk
Risk: family cleanup becomes a wholesale history rewrite.
Mitigation: use direct dependency chains, consumer maps, and summary-retirement-style bounded slices.

### Compatibility overreach risk
Risk: intentionally useful compatibility boundaries are deleted because they look transitional.
Mitigation: classify support levels and retention reasons before retirement decisions.

### Hotspot over-engineering risk
Risk: hotspot cleanup turns into a meta-framework redesign.
Mitigation: prefer helper extraction and stable service entrypoints unless new evidence demands more.

### Pilot-scope expansion risk
Risk: the artifact-role metadata pilot starts driving live query, sync, validator, or command behavior before the first slice has proved its read-only additive value.
Mitigation: keep the first slice classification-only, require explicit parity evidence, and treat any live selection behavior as later-slice work that needs a new checkpoint package.

### Checkpoint-escalation risk
Risk: a clean first Phase 3 slice is mistaken for standing approval to continue into broader Phase 3 or later-phase work without a new checkpoint.
Mitigation: require the open outcome review to nominate the next bounded checkpoint explicitly or keep the rewrite blocked.

### Scope-evidence mismatch risk
Risk: broad “phase complete” wording causes later implementers to assume families were fully classified when the published package only covered the approved critical-surface gate scope.
Mitigation: keep the Phase 1 wording aligned with the evidence package, treat the closed Phase 3 entry review as first-slice classification sufficiency only, and require family-specific classification in later phase-entry packages before touching workflow, route, sync, validator, or projection families.

### Supporting-trace drift risk
Risk: live coordination and checkpoint state diverge from stale current-state narration in supporting repo-native rewrite documents, leaving implementers with competing stories about what gate is open and what groundwork is already complete.
Mitigation: treat live coordination and planning queries plus the current controlling checkpoint artifacts as higher authority, and refresh or explicitly relabel stale PRD or feature-design narration before any successor checkpoint begins implementation.

### Migration half-finished risk
Risk: both old and new systems remain live indefinitely.
Mitigation: require pilot closeout, family-level rollback, explicit cutover, and rewrite closeout ownership.

### Discoverability regression risk
Risk: route-first or index-first navigation gets weaker after cleanup.
Mitigation: treat discoverability parity as a first-class acceptance gate.

### False urgency risk
Risk: the rewrite adopts emergency framing and over-rotates despite the repo already being green.
Mitigation: keep current-state evidence and acceptance criteria visible at the top of the program.

---

## 12. Recommended Order of Execution

### Current position: Phase 3 outcome review
Reason:

- Phase 0 and Phase 1 are complete in repo-native surfaces
- the Phase 2 entry review is complete, the first bounded slice is live, and the pilot outcome review is closed
- the Phase 3 entry review is complete, the first bounded Phase 3 slice is live, and the only authorized next move is the explicit outcome review on that slice

### Immediate next step: close the bounded Phase 3 outcome review
Reason:

- the current hard stop is `docs/planning/tasks/open/review_structural_rewrite_phase3_command_companion_source_surface_normalization_outcome.md`
- the review must confirm docs-plus-index parity, fail-closed drift-guard behavior, and unchanged command-authority and public-planning boundaries
- even a positive result may only hand off to a new bounded checkpoint rather than implied broader Phase 3 continuation
- if the review passes, refresh the stale feature-design current-state narration and either narrow the broader PRD Phase 1 wording or publish the family-specific addendum required for the named successor checkpoint before new implementation begins

### Next checkpoint after review: decide explicitly, do not assume Phase 4
Reason:

- a valid outcome may be another bounded Phase 3 checkpoint, an explicit hold, or a separately packaged later-phase entry review
- the landed command-companion slice does not authorize broader command-authority, workflow, route, compatibility, or projection rollout by itself

### Likely later sequence, if separately approved
- Phase 4: shared projection mechanics can remove duplicated work, but only after the outcome review says the command-authority and companion-surface boundary is stable enough to move on.
- Phase 5: planning and task hotspots are still real, and accepted direction says to decompose them through bounded helper extraction rather than framework replacement.
- Phase 6: historical cleanup is only safe after standards absorption, consumer mapping, and public-surface stabilization.
- Phase 7: compatibility retirement is a closeout move for transitional shims, not an early speculative cleanup mechanism.
- Phase 8: final acceptance should happen only after the simplified baseline is proven and the migration ledger can close cleanly.

---

## Defaults Chosen
- The rewrite stays in the current repository rather than creating a separate replacement repo.
- Foundations are binding; older internal implementation assumptions are not.
- Public planning questions and current command names stay stable unless a replacement is explicitly versioned and decision-backed.
- The rewrite is successful only if it preserves current authority clarity and validation breadth while making future changes cheaper.
