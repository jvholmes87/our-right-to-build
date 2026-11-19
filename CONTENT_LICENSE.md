# ORB content licensing and rights register

**Status: owner-approved licensing policy (Option A), proposed implementation on PR #6.**
**Decision date:** 2026-11-15. **Owner:** Jason V. Holmes.
**Effective in this repository's current version only after PR merge.** Prior MIT permission grants for historical versions are not revoked.

## License boundaries

- **MIT:** original executable software, website HTML/CSS/JavaScript and software-specific documentation/configuration, as described in [LICENSE](LICENSE).
- **CC BY 4.0 International:** only the **original non-code prose** of the specific documents listed in the table below. The formal license is published by Creative Commons at https://creativecommons.org/licenses/by/4.0/legalcode . Attribution and indication of changes are required.
- **Not automatically covered:** all other repository prose, unreviewed research reports, acquired images, photographs, fonts, maps, datasets, logos, trademarks, vendor tool names, official publications, citations, research in separate repositories, and partner-produced work. These require their own rights determination and notices.

## Explicit CC BY 4.0 designations

| Repository path | Covered portion | Rights/provenance basis | Status |
|---|---|---|---|
| `docs/PROJECT_MANAGEMENT.md` | Original ORB project-management prose; not linked source documents | Created for this repository on founding PR #5; reviewed for obvious third-party reproduction | Proposed designation, owner approved license choice; merge and final review pending |
| `docs/RELEASE_GATES.md` | Original ORB approval-gate wording; not external standards quoted or linked | Created for this repository on founding PR #5 | Proposed designation, owner approved license choice; merge and final review pending |
| `docs/ISSUE_3_GOVERNANCE_REVIEW.md` | Original summary and implementation checklist; not linked material | Created for Issue #3 on draft PR #6 | Proposed designation, owner approved license choice; merge and final review pending |
| `website/ARCHITECTURE.md` | Original proposed information architecture and implementation commentary | Created for this repository on founding PR #5 | Proposed designation, owner approved license choice; merge and final review pending |

These entries do not relicense external facts, third-party works, trademarks, federal/municipal publications, or hyperlinks. A hyperlink alone is not a claim of license ownership.

**Attribution:** `© 2026 Jason V. Holmes. "Our Right to Build (ORB)" — [document title], [commit or version], CC BY 4.0 International, https://creativecommons.org/licenses/by/4.0/ . Indicate if modified.`

**Scope caution:** Because licensing and provenance are distinct from research-validity review, CC BY 4.0 licensing does not imply a claim has been verified, endorsed, or adopted. Source IDs, evidence grades and uncertainty controls remain mandatory.

## Deferred and excluded pending review

| Material | Current licensing treatment | Next review |
|---|---|---|
| README and original research/explanatory prose in other files | Not designated CC BY 4.0 by this manifest; existing rights/license for versions remain subject to file-level interpretation | Determine which authored prose and embedded third-party materials may be separated and designated |
| `visualizations/TOOL_REGISTER.md` | Repo-authored list/reference text; external repositories and names remain third-party | Check attribution, tool versions and license terms; only independently created commentary could later be designated |
| `brand/` and proposed ORB graphics | No brand graphics have been licensed in this PR | Inventory originals, fonts, trademarks and permissions |
| `visualizations/` images or models | No image/model grant; no finished images are designated | Establish asset manifest, authorship, sources, third-party rights, and per-asset approvals |
| Material in `jvholmes87/orb-readiness-research` | Governed by that independent repository's licenses, not this manifest | Separate review and separate approval; do not copy without permissions |
| Source folders and linked Google Drive artifacts | No licensing grant by linking | Determine ownership/rights independently before import |

## Contribution and change-control procedure

1. Specify **exact file and content scope**; avoid broad directory-level license claims.
2. Verify creator, copyright holder, coauthors, sources and whether any third-party components appear. Record uncertainty.
3. Record a chosen license and attribution/changes requirement in this manifest.
4. Obtain explicit owner approval for each expanded designation, then review a PR, preserve a change log, and merge only under G2.
5. Defer site publishing, domain changes or release to a separate G3 approval.

This register is administrative guidance, not legal advice or proof of third-party ownership.
