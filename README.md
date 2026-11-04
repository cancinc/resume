# nicking.cv

Professional executive résumé and career website for Nicholas King.

## Source and baseline

- Canonical repository: https://github.com/cancinc/resume
- Public site: https://nicking.cv
- Verified November 3, 2026 (America/New_York): GitHub `main`, the local tracked files, `resumeArchive`, and the live website contain identical HTML and PDF files.
- Baseline commit: `a019a932c1cde9fe778393f069dc643376587d4c`.
- HTML SHA-256: `8edd3250cedca4eab3f2daf916a69622ce9b70806d92007e029cbe080877bc86`.
- PDF SHA-256: `d539c05016bd58a50610020f86e4e54c2107db360865c7f8742ecf33d672efc0`.

The live response identifies Cloudflare. The archive describes GitHub Pages. The origin, deployment project, production branch settings, and preview mechanism have not yet been verified in the hosting account. Identical assets establish source equivalence, not the deployment mechanism.

## Files

- `index.html`: single-page site with embedded styles, JavaScript, and logo images; Google Fonts is an external dependency. No build step.
- `Nicholas_King_Resume.pdf`: downloadable résumé.
- `CNAME`: domain declaration; not proof of the active hosting arrangement.
- `resumeArchive/`: user-supplied Claude handoff and matching source assets. Preserve as historical background; handoff claims require verification.
- `docs/DECISIONS.md`: audit findings and pending decisions.
- `AGENTS.md`: project working instructions.

## Review and deployment

1. Work on a `codex/` development branch. Do not edit or push production directly.
2. Confirm factual content and synchronize website and PDF revisions.
3. Verify the active hosting project, repository connection, production trigger, and preview settings before pushing changes that might deploy.
4. Create a preview using the verified hosting mechanism; review desktop, mobile, keyboard access, links, and PDF download.
5. Record the reviewed commit and rollback baseline.
6. Obtain explicit user approval before merging or deploying anything that publishes to `nicking.cv`.
7. After approval, deploy through the verified mechanism and check live HTML, PDF, and links against the approved revision.

Production deployment commands are intentionally pending hosting verification. Do not follow the archive's direct-to-main procedure.

For local review, run `python3 -m http.server 8000` from this directory and open http://localhost:8000. A local review is not a hosting preview deployment.

GitHub backup status requires a successful commit and push followed by remote verification. Local files alone are not synced.

## Executive profile draft

The proposed redesign is in `preview/index.html`; the production `index.html` and PDF remain unchanged. Review at http://127.0.0.1:8765/preview/ while the local server is running. To restart it, run `python3 -m http.server 8765 --bind 127.0.0.1` from the repository root. The draft can also be opened directly as a local HTML file.

Review priorities: opening positioning; selected impact; shortened C-Path descriptions; FNIH responsibilities still to be supplied; Senior Project Manager dates and Program Manager title discrepancies. The preview download now serves the synchronized, independently reviewed PDF. See `docs/DEPLOYMENT_CHECKS.md` for release readiness and remaining hosting checks.

Build the synchronized PDF and prepare deployment assets with `python scripts/prepare_release.py` after installing `scripts/requirements-pdf.txt`. Deploy only the contents of `output/site` once the hosting workflow and release approval are verified. The root HTML/PDF now match the approved production release. The previous baseline remains recoverable from commit `a019a932c1cde9fe778393f069dc643376587d4c` and branch `production-baseline-2026-11-04`.

## Production release — November 4, 2026

Published https://nicking.cv after explicit approval. Cloudflare Worker `resume` serves only the files from `output/site`; there is no automatic GitHub build connection. Runtime compatibility date `2025-09-27` and flag `nodejs_compat` were preserved. Both live assets were fetched and matched against the approved SHA-256 hashes. See `docs/RELEASE-2026-11-04.md` for version, verification, and rollback details.
