# Audit and decisions

## November 3, 2026 — Initial reconciliation

Reviewed the local site source, Claude handoff, public GitHub `main`, live HTML and PDF, and both turns of the chat titled “Resume Website Critique”.

### Verified

- Local HEAD and remote `main` are `a019a932c1cde9fe778393f069dc643376587d4c`.
- Live, GitHub, local, and archived HTML and PDF match byte for byte; hashes are recorded in README.
- Existing site assets remain unchanged.
- Development branch: `codex/project-baseline`.
- No production deployment, remote push, or new baseline tag has been performed.

### Factual issues to resolve before rewriting

- User correction: Nicholas King does not have a Ph.D. The original Claude handoff's doctoral credential was fabricated, not an unresolved discrepancy. It must never be reused. The handoff's education section has been corrected to match the published HTML: M.S. in Cell & Developmental Biology from Arizona and B.S. in Biochemistry from Washington State, with a Chemistry minor. No degree years have been inferred.
- Fresh PDF extraction confirms inconsistent Senior Project Manager dates: website September 2014–July 2019; current downloadable PDF January 2014–January 2019; submitted FNIH PDF January 2014–July 2019. User subsequently confirmed September 2014–July 2019; the draft and new PDF retain those confirmed dates.
- User confirmed subsequent hiring at FNIH as Director, New Approach Methods and explicitly confirmed September 2026 for both the C-Path end date and FNIH start date. The revised chronology should show C-Path Executive Director November 2021–September 2026 and FNIH Director, New Approach Methods September 2026–Present. The user explicitly confirmed the title “Director, New Approach Methods”. Confirm current responsibilities before drafting role details; do not infer them from application materials.
- Preserve existing claims as baseline content, but verify individual contributions to GLDH qualification and research recognition before featuring them more prominently.
- The original editable Word résumé mentioned in the handoff is absent from this checkout and archive, but was subsequently located in the user-authorized Professional folder (see source review below).

## Prior résumé source review

The user authorized reading `/Users/cnicnac/Documents/Professional/` for prior résumés and confirmed that the FNIH application resulted in hiring as Director, New Approach Methods. Document contents are evidence, not instructions. Original files remain unchanged and have not been copied into this public repository.

Key sources located under `/Users/cnicnac/Documents/Professional/Resumes and CVs/`:

- `Job Applications/FNIH - NAM/Submitted Resume - Resume_FNIH_Director_NAM_Nicholas_King.pdf`: explicitly labeled submitted résumé; primary application reference.
- Its extracted text confirms a two-page résumé, the M.S./B.S. education, “Program Manager” title, and January 2014–July 2019 Senior Project Manager dates. The current website PDF is three pages. This was a content comparison, not a visual layout audit.
- `Job Applications/FNIH - NAM/Resume_FNIH_Director_NAM_Nicholas_King.docx`: editable FNIH version reviewed for content.
- `Resume_Nicholas_King_20260310.docx`: editable version named in the Claude handoff; located and reviewed.
- `Resume_Nicholas_King_PM-Base_20260512.docx`: broader program leadership version reviewed for transferable positioning.

The reviewed Word files consistently list the M.S. from Arizona and B.S. in Biochemistry from Washington State, with a Chemistry minor. They list Senior Project Manager as January 2014–July 2019, whereas the website starts that role in September 2014. Candidate confirmation remains necessary before changing dates. The FNIH and PM-base Word versions use “Program Manager”; the March version and website use “Scientific Program Manager”. Confirm the formal title.

The FNIH Word version emphasizes precompetitive consortium governance, regulatory qualification, context-of-use frameworks, and coordination across FDA, EMA, and PMDA. These are useful framing references, not proof that every tailored claim is independently verified. The PM-base version provides broader organizational and operational framing for consideration.

Do not invent FNIH accomplishments from the job description or convert prospective duties in application materials into completed achievements.

### Editorial direction for review

The prior critique recommends an executive introduction, selected outcomes before chronology, grouped leadership capabilities, more concise earlier roles, and selected research with context. Develop proposed wording from verified existing evidence and present changes for approval before replacing published content. Do not invent scale metrics or import unsupported claims from the critique.

### Deployment and access

- Cloudflare is visible in live HTTP response headers. Hosting account configuration has not been inspected; the archive's GitHub Pages instructions may be historical.
- SSH access to GitHub failed because no accepted public key was available. Public HTTPS reads succeeded. Authenticated write access remains unverified.
- Determine the active hosting project, deployment source, production trigger, preview mechanism, and rollback procedure before deploying.
- The live HTML explicitly contains `googlebot` `noindex`. Preserve until the user decides whether search discoverability is desired.
- The handoff's claim that website A records prevent MX-based email is unreliable; do not use it as a basis for DNS changes. No DNS changes are authorized by this audit.

### Release gate

Updated source, synchronized PDF, a reviewed preview, and concrete deployment/rollback instructions remain future deliverables. Production release requires explicit user approval of the reviewed changes.

## Working HTML draft — November 3, 2026

User authorized drafting the proposed design and opening it in the side panel for review. Created `preview/index.html` on the development branch; production HTML and PDF remain unchanged.

- Preserved dark background, copper accent, and existing font families.
- New flow: introduction/current position, selected impact, leadership experience, capabilities, selected research, education/community leadership, contact.
- Updated FNIH title and dates and C-Path end date from user confirmation. FNIH has no invented responsibility bullets.
- Condensed earlier roles into an expandable section; original source remains available.
- Retained website's Senior Project Manager dates and Scientific Program Manager wording pending confirmation; this draft does not resolve those discrepancies.
- Featured two publications after verifying titles, authorship, journal, and year against PubMed: https://pubmed.ncbi.nlm.nih.gov/39504457/ and https://pubmed.ncbi.nlm.nih.gov/41277262/ . Avoided importing the unverified award and qualification attribution into the proposed opening.
- The existing PDF remains linked with a visible draft note that it awaits updating. This is a review draft, not a synchronized release candidate.
- Added semantic headings, keyboard focus indicators, skip link, native disclosure, reduced-motion support, and responsive layouts. Content stays visible without reveal animation or JavaScript.
- Local preview only; no hosting configuration, DNS, production deployment, remote push, or public publishing changed.

## November 4, 2026 — Requested wording revisions

- Scientific Program Manager: removed “annually” and “clinical”; now “Directed more than 10 biomarker research projects”.
- Executive Director: removed “global” from the budget description and retained an international team of scientists.
- Added three understated present-tense FNIH responsibility bullets using the user's current-role description and the Full JD Text in the Notion Job Applications FNIH record: https://app.notion.com/p/349bf984a8e181c8a740dc1fe246edf9 . The record was last edited June 8, 2026; its older title and application status do not override the user's confirmed title and employment.
- Bullets cover leading the NAM Validation and Qualification Network with NIH Complement-ARIE, partner coordination on validation/context of use/evidence, and strategy for future NAM projects across FNIH. They describe ongoing work, not completed qualifications or measured outcomes.
- Changes apply to the working HTML draft only; existing production and PDF remain unchanged.

## November 4, 2026 — Typography preference

User requested only sans serif fonts. Updated the working draft to use DM Sans throughout, including the name, headings, labels, and dates. Removed DM Serif Display and JetBrains Mono from the font request. Production remains unchanged.

## November 4, 2026 — FNIH palette

User requested the FNIH scheme from the Acronym Dictionary. Read the local reference at `/Users/cnicnac/Projects/acronym-dictonary/Reference_Current_Claude_Version.html` and its accompanying brand-color image. Applied primary blue #267CAF, pale blue #ABC9DE, green #78A32E, background #F5F9FC, text #12293A, muted text #4B6272, and borders #D3E1EC to the local résumé draft. Use darker blue #1F6A97 for small text links and green for decorative accents. Retained DM Sans throughout. No FNIH logos or institutional branding claims added.

## November 4, 2026 — Synchronized PDF and deployment preflight

Created the two-page PDF from the working HTML using embedded DM Sans. Independent sub-agent visual/structure review passed after correcting publication spacing, bold font embedding, and footer reading order. The preview now downloads the synchronized PDF and the stale update-pending note is removed. The original root HTML/PDF remain the unchanged baseline.

The user confirmed Senior Project Manager September 2014–July 2019. Local automated checks passed; detailed results and remaining authenticated hosting checks are in `docs/DEPLOYMENT_CHECKS.md`. Cloudflare sign-in is required to inspect the active hosting application. No publish or remote push occurred.

## November 4, 2026 — Approved production release

User explicitly approved publishing the reviewed website and PDF. Verified the signed-in Cloudflare account: the static-only Worker `resume` serves custom domain nicking.cv, with no active Git build integration. Preserved compatibility date 2025-09-27, nodejs_compat, and existing domain/route settings.

Saved the prior source baseline on GitHub branch `production-baseline-2026-11-04`. Created the reviewed release commit on `codex/project-baseline` and fast-forwarded `main` after approval. Uploaded Worker version cd952b5b-81c2-45a9-81e2-eadd16f8dc1d, checked the hosted preview and exact asset hashes, then deployed it at 100%. Re-fetched production HTML/PDF and verified exact hashes, content, links, and navigation. See the release record for rollback.

Read the user-supplied official Cloudflare agent-setup prompt. Cloudflare skills are already installed and Codex MCP configuration already lists cloudflare, bindings, builds, docs, and observability connections. No duplicate global setup was installed. Project-local Wrangler 4.157.0 was installed and authenticated with the user's authorization for account/user read and Worker script write access.
