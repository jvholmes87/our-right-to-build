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
- The existing MIT LICENSE has **not** been altered. License choice for documents and creative assets remains an owner decision.

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

## Licensing decision — owner approval required

- **Existing state:** MIT `LICENSE` already on `main`, applying to the original software and repository-authored material unless marked otherwise. Independent `orb-readiness-research` uses its own terms.
- **Option A (recommended for clarity):** MIT for source code and software docs; CC BY 4.0 for selected original non-code research/illustrations **after** rights and source reviews, with precise directories/file notices. Avoid silently applying CC BY to third-party images, official reports or materials of uncertain rights.
- **Option B:** Retain the current MIT baseline across original repository materials, with file-specific exceptions. Simpler management but less tailored to scholarly publishing.
- Neither option conveys rights over third-party materials, government logos, public records or confidential partner data.
- No new license adopted by this PR. Owner selects explicitly before a follow-up licensing change is made.

## Manual verification before closing Issue #3

- [x] Verify issue taxonomy is attached to #1–#4.
- [x] Draft non-deployment CI and publish source for review.
- [ ] Confirm CI run after PR creation and address any failures.
- [ ] Owner selects licensing option and any content-scoped exceptions.
- [ ] Owner approves milestone names/scope; create and verify M0–M3 in GitHub.
- [ ] Configure and verify `main` PR requirements / ruleset and status checks.
- [ ] Confirm whether a Project board is needed; create only after owner selection.
- [ ] Record approved decisions in Drive register and update this record.
- [ ] Owner explicitly approves merge; G3 remains a **separate** release decision.

## Not included

No releases, DNS changes, GitHub Pages enablement, deployment tokens, production analytics, organization formation, certification or fieldwork.
