# Issue #3 — Governance implementation and owner decision record

**Status: review pending | 2026-11-15 | Scope: governance controls only**

Tracking: [Issue #3](https://github.com/jvholmes87/our-right-to-build/issues/3). This record supplements, not replaces, the canonical [ORB Change and Progress Register](https://docs.google.com/spreadsheets/d/1fsWe2buAgQtcD2d-XKzdXNRufc5JL-ocWCpcoBoj8gs/edit).

## Verified and performed

- Repo owner linked account: `jvholmes87`; repository `our-right-to-build`.
- Public repository has initial ORB files from merged PR #5.
- Applied these issue labels using GitHub's issue endpoint (GitHub returned labels on the issues):
  - #1 Website: `area:website`, `priority:P0`, `gate:owner-review`
  - #2 Research visuals: `area:visualization`, `area:research`, `priority:P1`, `gate:evidence-review`
  - #3 Governance: `area:governance`, `priority:P0`, `gate:owner-review`
  - #4 Deferred site concept: `area:brand`, `priority:P2`, `gate:partner-review`, `status:blocked`
- Proposed a pull-request-only **non-deployment** check that validates required governance files, homepage semantics and local URL targets. It does **not** verify facts, third-party licenses, accessibility compliance, or operational security.
- **Licensing update (2026-11-15):** owner approved Option A: MIT for original software and CC BY 4.0 for expressly designated original non-code content, subject to rights review. This branch proposes amendments to the MIT scope notice, an explicit [content license manifest](../CONTENT_LICENSE.md), and citation guidance. No merge has been authorized; unrelated third-party assets are excluded.

## Proposed milestone configuration

These are documented milestone names, **not yet created in GitHub** because milestone administration is not provided by the connected GitHub actions.

| Milestone | Scope | Suggested issues | Gate |
|---|---|---|---|
| M0 — Foundation and evidence governance | License decision, issue labels, protections and CI | #3 | G1/G2 |
| M1 — Website concept and content approval | Content, responsiveness, branding, domain verification | #1 | G1/G2, later G3 |
| M2 — Research visualization pilots | V009 asset inventory, V001 and V002 evidence-led prototypes | #2 | G1/G2 |
| M3 — Release readiness | Rights, content, accessibility, privacy, security, performance, DNS and hosting | #1, future release checklist | G3 |

No dates or automatic releases should be set without owner approval. M0 should not be marked complete until owner licensing choice and repository settings are verified.

## Recommended branch/ruleset settings (manual admin action needed)

On GitHub repository **Settings → Rules → Rulesets** or **Branches → Add branch protection rule** for `main`:

1. Require pull requests before merging and require conversations to be resolved.
2. Prefer at least one independent approval when a distinct reviewer is available. Because this is a solo-owner repository, do **not** assert that self-review counts as an independent approval; ensure the rule does not make ordinary maintenance impossible.
3. After the proposed workflow has run successfully on a PR, require its exact check name: `Foundation and website safety checks`; do not guess a status-check name before it exists.
4. Disable force pushes and branch deletion; preserve maintainer emergency recovery with an auditable exception policy if required.
5. Review ruleset applicability and GitHub plan support; **do not claim protection is active until verified**.
6. Keep GitHub Pages, third-party hosting, Actions deployment permissions and domain records unchanged absent G3 approval.

A workflow running successfully is only a technical gate, not merge or deployment authorization.

## Licensing decision — owner approved Option A; scope still under PR review

- **Existing state:** MIT `LICENSE` already on `main`, applying to the original software and repository-authored material unless marked otherwise. Independent `orb-readiness-research` uses its own terms.
- **Approved Option A (2026-11-15):** MIT for original source code and software docs; CC BY 4.0 only for the explicitly enumerated original prose documents in [CONTENT_LICENSE.md](../CONTENT_LICENSE.md). Further research/illustration assets require separate affirmative rights review and a manifest update; none are silently relicensed.
- **Unselected Option B:** Keep a single MIT baseline with exceptions. Not adopted by the owner.
- Neither option conveys rights over third-party materials, government logos, public records or confidential partner data.
- The decision is documented in this draft PR and the ORB change register; its file changes do **not** become part of `main` until the owner approves and merges PR #6. Existing grants covering older versions remain unaffected.

## Manual verification before closing Issue #3

- [x] Verify issue taxonomy is attached to #1–#4.
- [x] Draft non-deployment CI and publish source for review.
- [x] Initial PR CI run succeeded; recheck the workflow after licensing changes.
- [x] Owner selected Option A (2026-11-15).
- [ ] Owner reviews proposed CC BY 4.0 per-file rights inventory and approves PR #6 changes.
- [ ] Owner approves milestone names/scope; create and verify M0–M3 in GitHub.
- [ ] Configure and verify `main` PR requirements / ruleset and status checks.
- [ ] Confirm whether a Project board is needed; create only after owner selection.
- [ ] Record approved decisions in Drive register and update this record.
- [ ] Owner explicitly approves merge; G3 remains a **separate** release decision.

## Not included

No releases, DNS changes, GitHub Pages enablement, deployment tokens, production analytics, organization formation, certification or fieldwork.
