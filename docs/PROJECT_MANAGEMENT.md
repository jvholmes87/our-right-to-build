# ORB initial project-management conventions

**Status: proposed operations for owner review.** GitHub issues track public implementation tasks; the [Drive Change and Progress Register](https://docs.google.com/spreadsheets/d/1fsWe2buAgQtcD2d-XKzdXNRufc5JL-ocWCpcoBoj8gs/edit) is the historical decision/evidence record. Do not silently overwrite older decision history.

## Issue taxonomy

- Area: `area:website`, `area:research`, `area:visualization`, `area:governance`, `area:brand`
- Priority: `priority:P0`, `priority:P1`, `priority:P2`
- Gate: `gate:owner-review`, `gate:evidence-review`, `gate:partner-review`
- State: `status:blocked`, `status:ready-for-review`

Labels in the taxonomy were applied to Issues #1–#4 and verified on 2026-11-15. Existing labels remain available for future issues; some taxonomy labels are unused. Milestone administration and ruleset configuration are pending, as documented in [Issue #3 governance review](ISSUE_3_GOVERNANCE_REVIEW.md). Open a focused issue per deliverable, with source links, scope, acceptance criteria and review gate.

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

No duplicate PRs; inspect existing work before opening a new one. The proposed non-deployment CI for Issue #3 is in `.github/workflows/governance-checks.yml` on its review branch. Passing CI does not constitute approval to merge or deploy; GitHub branch rulesets and hosting settings must be verified independently.

## License verification gate

Before merging a PR that adds a non-code visual, report or document, verify whether it is original ORB-owned content or a third-party/source artifact and update the [explicit licensing and rights register](../CONTENT_LICENSE.md). A CC BY 4.0 notice for one file does not automatically apply to new files in its folder. Unverified assets remain excluded from the CC BY grant.

---

**Content licensing:** Original non-code prose in this document is designated **CC BY 4.0 International**, subject to the exclusions and attribution terms in [ORB Content Licensing](../CONTENT_LICENSE.md). External sources, hyperlinks, and third-party assets are not relicensed. The legal code is at https://creativecommons.org/licenses/by/4.0/legalcode .
