# æmeth website

English and Japanese pages for æmeth (Aemeth), the project brand behind zkFMI,
published with GitHub Pages.

## Develop

```sh
python3 build.py
python3 -m http.server 8000 --directory public
```

English is at `/`, Japanese at `/ja/`. Fonts (Fraunces, Inter, JetBrains Mono)
are self-hosted under `static/fonts/`; nothing is fetched from a third party at
runtime, there is no tracking and no form. The only script is `static/site.js`,
which drives the letter demo in the "name" section.

`WORDMARK=Æmeth python3 build.py` builds the capital-ligature variant of the
wordmark, hero glyph and favicon. The default is the lowercase `æmeth`.

## Layout

- `build.py` — bilingual copy and the page template, including the inline SVG
  flow diagram.
- `static/style.css` — the one stylesheet. Warm paper, ink, one brick-red letter.
- `static/site.js` — letter demo only.
- `static/og.png` — social card, rendered from `brand/og.html` at 1200×630.
- `brand/*.path` — glyph outlines (Fraunces æ / Æ, upright and italic) used for
  the hero mark and favicon so they render identically everywhere.
- `public/` — build output, not committed.

## Publish

Push the reviewed source to `main`. GitHub Actions builds `public/` and deploys
it to Pages. The served `version.txt` contains the source commit. Set the
repository variable `SITE_URL` to `https://aemeth.fi` once the custom domain is
bound and serves HTTPS; until then the canonical URL is
`https://zkfmi.github.io/aemeth`.

Requested domain: `aemeth.fi` (Marcaria). Domain registration, DNS, Pages
domain binding and HTTPS certificate readiness are separate states. Do not
claim the custom domain is live based only on a successful workflow.

## Content ownership

æmeth is the project brand; zkFMI is the technology stack; Aethel is the
payment-stream receivables application. Technical claims and the headline
measurements are reproduced from zkfmi.com with their date, and research status
and limits stay explicit. No unverified affiliations or financing offers are
published. No contact email is configured at the user's request.

## Review

Check both languages on desktop and a narrow viewport, exercise navigation,
the letter demo and outbound links, and compare the served `version.txt` with
the deployed commit. Build success is a development check, not acceptance
evidence.
