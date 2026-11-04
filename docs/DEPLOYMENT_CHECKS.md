# Release readiness — November 4, 2026

## Result

Local PDF and release checks PASS. Production deployment readiness is NOT YET VERIFIED because authenticated hosting configuration is unavailable. No production publish, GitHub push, merge, or DNS change was performed.

## PDF review

The user-requested independent sub-agent reviewed both rendered pages and the final PDF structure. PASS: two readable pages; no clipping, overlap, orphaned headings, or split roles; embedded DM Sans regular/bold; selectable text in logical order; six valid URI targets; correct document metadata. All 10 experience bullets match the website. No doctoral claim, annual project count, or global-budget wording remains.

Source: `preview/index.html`. PDF: `output/pdf/Nicholas_King_Resume.pdf`. The preview's download now serves the reviewed PDF rather than the old production PDF. The PDF includes all roles, capabilities, education, community service, and selected publications; selected-impact copy is not repeated as a separate PDF section.

User confirmed Senior Project Manager September 2014–July 2019. Retained the draft's “Scientific Program Manager” wording, which the user has used in revision requests; older application versions say “Program Manager”, so formal historical title remains worth confirming before publication.

## Local checks passed

- Two-page PDF, all experience bullets synchronized, current title and September 2026 transition dates present.
- Confirmed Senior Project Manager dates present.
- Sans serif typography throughout.
- Internal section links and relative PDF download resolve.
- Preview PDF responds HTTP 200 and its hash matches the reviewed output.
- Deployment directory contains exactly `index.html` and `Nicholas_King_Resume.pdf`; no handoff, archive, development notes, source resumes, or screenshots.
- `git diff --check` passed.
- Exact content hashes are in `output/release-checks.json`.

## Remote checks completed

- Remote GitHub `main` remains `a019a932c1cde9fe778393f069dc643376587d4c`.
- Live HTML/PDF still match the original baseline files byte for byte.
- DNS nameservers are Cloudflare. HTTPS retrieval works and response headers identify Cloudflare.
- Public GitHub deployment history records historical `github-pages` deployments. This does not establish the active origin or production deployment trigger.
- GitHub CLI has no authenticated session. The earlier SSH read failed. Public HTTPS repository reads work.
- No Cloudflare credential environment variables or local Wrangler login configuration were found in the standard checked locations.
- Cloudflare dashboard in the in-app browser redirects to sign-in; account/project details cannot yet be inspected.

## Remaining hosting checks

After signing in to the Cloudflare dashboard, identify the application or proxied origin serving nicking.cv. Inspect custom-domain mapping, active deployment, connected repository, production branch, build/output settings, preview configuration, and rollback controls. Do not assume Pages, Workers, or GitHub Pages solely from the historical handoff.

If Git-integrated, confirm that only the intended deployment directory is served and determine whether pushes or merges trigger production. If manually uploaded, confirm the upload target and preview environment. Do not upload the entire repository.

Review a hosted preview of the prepared files before production approval. Preserve the existing noindex behavior pending a separate search-visibility decision; the current release candidate retains noindex/nofollow.

## Build and review

Create a Python environment and install `scripts/requirements-pdf.txt`. From the repository root run:

```sh
python scripts/prepare_release.py
```

The builder obtains DM Sans from Google Fonts' official repository on first run and caches static instances under ignored `tmp/pdfs`. It generates page images there for review. Whenever content/layout changes, repeat visual review of both pages before release. Build output is local until committed and pushed; no GitHub backup is claimed.

## Production and rollback — pending approval

1. Finish account-level checks and record the actual application and deployment ID.
2. Back up the verified baseline through the canonical repository and record the rollback deployment. Baseline commit is listed above.
3. Commit the reviewed source/PDF changes to the development branch and push through an authenticated method, after confirming deployment triggers.
4. Review the hosted preview, then obtain explicit approval for production.
5. Publish only the reviewed HTML/PDF using the verified mechanism.
6. Fetch production HTML/PDF, compare hashes to the approved release, and verify navigation, contact, downloads, and mobile rendering.
7. If verification fails, restore the recorded prior deployment or redeploy the baseline assets through the same verified hosting mechanism.

Exact deployment/rollback commands remain pending identification of the active host; inventing them now could target the wrong application.
