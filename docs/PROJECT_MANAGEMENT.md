# ORB initial project-management conventions

**Status: proposed operations for owner review.** GitHub issues track public implementation tasks; the [Drive Change and Progress Register](https://docs.google.com/spreadsheets/d/1fsWe2buAgQtcD2d-XKzdXNRufc5JL-ocWCpcoBoj8gs/edit) is the historical decision/evidence record. Do not silently overwrite older decision history.

## Issue taxonomy

- Area: `area:website`, `area:research`, `area:visualization`, `area:governance`, `area:brand`
- Priority: `priority:P0`, `priority:P1`, `priority:P2`
- Gate: `gate:owner-review`, `gate:evidence-review`, `gate:partner-review`
- State: `status:blocked`, `status:ready-for-review`

Labels should be added when repository label management is available; do not claim they already exist. Open a focused issue per deliverable, with source links, scope, acceptance criteria and review gate.

## Proposed milestones (not created in GitHub until supported)

- **M0: Foundation and evidence governance** — initial docs, license, repository conventions, review controls.
- **M1: Website concept and content approval** — accessible static architecture, copy, responsive checks, owner-approved brand.
- **M2: Research visualization pilots** — source-linked V009, V001 and V002 pilot assets.
- **M3: Release readiness** — rights/claims/security/accessibility/performance signoffs, domain verification, explicit deployment approval.

Do not place calendar deadlines on these milestones before the owner agrees to a schedule.

## Definition of done

A task is complete only when code/docs are committed to a review branch, tests and evidence checks are documented, source/rights review is complete, reviewer concerns are resolved, and the owner approves the relevant gate. **An open PR is not a deployment authorization.**

## Pull request workflow

`issue → scoped branch → changes + tests → draft PR → evidence/security/content review → explicit owner approval → merge → separate release/deployment approval`.

No duplicate PRs; inspect existing work before opening a new one. No automatic merge or deployment is configured by this scaffold.
