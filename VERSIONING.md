# Versioning policy

JX Manifesto uses document versions, not application-package semantics. A public version is immutable and must have all five records below:

1. a Git tag named `v{version}`;
2. a GitHub Release with human-readable notes;
3. an entry in `CHANGELOG.md`;
4. permanent English and Persian URLs at `/{locale}/versions/{version}/`;
5. a persistent Zenodo record and DOI.

The unversioned `/{locale}/manifesto/` route is the working text for the next release. It may include accepted but unreleased changes. Citations should use a permanent version URL or a version-specific DOI, not the working route.

## Proposal states

- **Draft** — submitted but not yet ready for a decision.
- **Discussion** — open for evidence, alternatives, translation review, and affected perspectives.
- **Accepted / Rejected** — a documented decision has been made. Accepted work is still unreleased.
- **Released** — included in a Git tag, GitHub Release, changelog entry, permanent bilingual pages and versioned downloads, and a persistent Zenodo record with a DOI.

## Release checklist

- Freeze bilingual manifesto content into a new version snapshot.
- Confirm semantic alignment between English and Persian.
- Generate versioned PDF, Markdown, and plain-text downloads.
- Add the release to the versions index, metadata, sitemap, and changelog.
- Merge the release PR to `main`.
- Create the matching tag and GitHub Release from the merge commit. Never move an existing public-version tag.
- Confirm Zenodo ingestion and record both the version DOI and concept DOI.
