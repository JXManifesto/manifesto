# Contributing to JX Manifesto

JX is an open, versioned professional manifesto. Contributions may improve wording, challenge a principle, add a translation, or document evidence from a real newsroom.

You do not need to know Git. Start from the contribution page and choose the focused form that matches your proposal:

- Wording change: quote the current passage, propose replacement text, and explain the improvement.
- Principle proposal: connect the proposal to a concrete newsroom decision or workflow.
- Translation: include the source, target language and locale, proposed translation, and terminology notes.
- Case study: describe context, workflow, friction, intervention, and observed outcome without exposing confidential information.

## Review states

1. **Draft** — a proposal is submitted with enough context to review; maintainers may ask for missing scope or evidence.
2. **Discussion** — contributors and affected practitioners compare evidence, alternatives, and trade-offs.
3. **Accepted / Rejected** — maintainers record a decision and its rationale. Accepted proposals remain unreleased until they are assigned to a version.
4. **Released** — an accepted change appears in a tagged GitHub Release, the changelog, and an immutable version URL.

There is no guarantee that a proposal will be accepted. Decisions should favor clarity, evidence, applicability across newsroom contexts, and semantic alignment between languages.

## Pull requests

Use a pull request for a precise, reviewable change. Keep unrelated changes separate. For user-facing text:

- preserve meaning across English and Persian;
- use the correct document language and direction;
- isolate embedded left-to-right terms such as `JX`, `GitHub`, and license identifiers;
- explain terminology choices that do not have a direct equivalent;
- avoid including confidential newsroom information.

This is a content-only repository and does not use npm. Before opening a pull
request:

```bash
jq empty .zenodo.json
python -c 'import yaml; yaml.safe_load(open("CITATION.cff", encoding="utf-8"))'
git diff --check -- . ':(exclude)en/manifesto.md' ':(exclude)fa/manifesto.md'
```

For a release import, also compare the English and Persian snapshot files with
the permanent downloads published by JXManifesto.org. Trailing double spaces in
the Markdown editions are intentional hard line breaks and may be reported by
`git diff --check`; do not remove them from an immutable snapshot.

## فارسی

برای مشارکت لازم نیست با Git یا برنامه‌نویسی آشنا باشید. از صفحه «مشارکت» یکی از چهار مسیر اصلاح متن، نقد یا پیشنهاد اصل، ترجمه، یا ثبت تجربه تحریریه را انتخاب کنید.

وضعیت پیشنهادها به‌ترتیب «پیش‌نویس»، «گفت‌وگو»، «پذیرفته/ردشده» و «منتشرشده» است. پذیرفته‌شدن به‌تنهایی به معنی انتشار نیست؛ تغییر تنها زمانی منتشرشده محسوب می‌شود که در یک تگ، GitHub Release، تاریخچه تغییرات و URL دائمی نسخه ثبت شود. تغییرهای فارسی و انگلیسی باید از نظر معنا هم‌راستا بمانند و اصطلاح‌های چپ‌به‌راست در متن فارسی به‌درستی ایزوله شوند.

See [VERSIONING.md](VERSIONING.md) for the release and permanence policy.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
