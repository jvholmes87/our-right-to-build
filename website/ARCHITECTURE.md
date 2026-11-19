# Proposed website architecture — OurRightToBuild.org

**Domain status:** a preferred domain, not confirmed registered, owned or pointed to this repository. **Release state:** local static starter only; no production host, API, tracking, payment, signup or contact form.

## Information architecture

- `/` — mission, proposed-status disclosure, three workstreams, evidence policy and links.
- `/research/` — Value Pool 0, methods, limitations, verified publications and independent research repository.
- `/new-orleans-east/` — concept and readiness analysis, not a site acquisition or City project.
- `/futurism/` — New Orleans Futurism design principles, performance criteria and concepts.
- `/visualizations/` — verified diagrams and clearly labeled illustrative models.
- `/publications/` — citations, versioned outputs and claims notes.
- `/about/` — mission, leadership, governance status, contacts with consent-safe outreach.

**Implementation phase A:** static accessible pages with sourced copy, generated from vetted content. **Phase B:** optional interactive visualizations only when prototypes validate usability and licenses. **Phase C:** optional contact/collaboration features after privacy, security and operational review.

## Tech decision

Initial baseline: framework-free HTML/CSS in `website/` to avoid premature dependencies. Evaluate Eleventy/Astro or another static site generator only when scale or publishing workflow justifies it. Avoid coupling research data or content approval to the visual implementation.

## Quality gates

- Semantic headings, keyboard navigation, visible focus, contrast, responsive narrow/mobile widths, accessible alt text/captions.
- No claims of incorporation, fiscal sponsorship, agency partnership, City approval, site control, certification or field-study outcomes.
- Content reviewed against the ORB source register, with dated claims and source links.
- No cookies/analytics, unsafe external scripts, forms or data storage introduced without approval.
- Manual local preview and link checks first; deployment only under [release gates](../docs/RELEASE_GATES.md).

This document is an architecture proposal, not evidence of a registered domain or running website.

---

**Content licensing:** Original non-code prose in this document is designated **CC BY 4.0 International**, subject to the exclusions and attribution terms in [ORB Content Licensing](../CONTENT_LICENSE.md). External sources, hyperlinks, and third-party assets are not relicensed. The legal code is at https://creativecommons.org/licenses/by/4.0/legalcode .
