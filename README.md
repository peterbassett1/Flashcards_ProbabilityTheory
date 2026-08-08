# Probability Theory — Flashcards

A single-file, offline **spaced-repetition flashcard app** for probability
theory — distributions, parameters, common traps, and quick checks. Open
[`index.html`](index.html) in any modern browser — no server, no build step, no
network access required. It is also installable on iOS as a **PWA** (see
[iOS / PWA](#ios--pwa)).

> Sibling project to *Heat Transfer & Fluids*. Unlike that one, this app's
> `index.html` is **hand-written, readable source** — not a minified build
> artifact — so cards and logic can be edited directly. See [Editing](#editing-the-app).

---

## What it is

- **Topic:** probability theory, taught as **recognition + intuition** over
  formula memorization — the approach set out in
  [`probability_flashcard_strategy.md`](probability_flashcard_strategy.md).
- **Mode:** recall only. You read a prompt, decide what fits, flip, and grade
  yourself — nothing that requires working a derivation.
- **Algorithm:** a classic **Leitner box** spaced-repetition system.
- **Persistence:** progress is saved in the browser's `localStorage` on that
  device (see [Data & persistence](#data--persistence)).

## How to run

Just open the file:

- Double-click `index.html`, **or**
- Serve the folder and browse to it (needed for the service worker / PWA):

```bash
python -m http.server 8778
```

Then visit `http://localhost:8778/`. A ready-made launch config lives in
[`.claude/launch.json`](.claude/launch.json). Serving over `http` (not `file://`)
is required to exercise the offline behaviour.

## How to use it

1. Pick one of the five decks — or **All decks** to drill everything due.
2. **Tap the card** — or press **Space** — to flip it.
3. Grade yourself: **Missed it** (`1`) or **Had it** (`2`).
4. Repeat until the due queue is empty. Missed cards cycle back within the
   session; cards you had are scheduled into the future.

Each card wears a coloured **type badge** — Scenario, Intuition, Trap, or
Quick-check — the four card types from the strategy doc.

### The Leitner algorithm

Cards live in one of **5 boxes**. Each box has a review interval, in days:

| Box | 1 | 2 | 3 | 4 | 5 |
|-----|---|---|---|---|---|
| Interval | today | 2 d | 4 d | 8 d | 16 d |

- **Had it** → the card moves **one box to the right** and is scheduled that
  many days into the future.
- **Missed it** → the card drops **all the way back to box 1** and stays due.
- A card is **due** when its scheduled date has arrived. New cards start in box 1,
  due immediately. The home screen shows the due count per deck and a strip
  showing how many cards sit in each box.

(Internally: box→day map `{1:0, 2:2, 3:4, 4:8, 5:16}`, 5 boxes, one day =
`86 400 000` ms, storage key `probdeck:leitner:v1`.)

## The decks

51 cards in five topic decks, allocated per the strategy doc's table.

| Deck (`id`) | Title | Cards | Focus |
|---|---|---|---|
| `discrete-rv` | Discrete RVs | 13 | Binomial, Poisson, Geometric |
| `continuous-rv` | Continuous RVs | 14 | Normal, Exponential, Beta, Uniform |
| `bayesian` | Bayesian | 10 | Priors, posteriors, conjugacy |
| `poisson-process` | Poisson Process | 8 | Counts, gaps, memorylessness |
| `general` | General | 6 | Independence, conditional probability |

The full card content is listed in [CARDS.md](CARDS.md).

## Notation

Card text uses a light markup that renders to real `<sub>` / `<sup>` at display
time:

- **Subscripts** with `_`: `X_i` → X*i*, `λ_1` → λ₁ (Unicode subscripts also work
  literally).
- **Superscripts** with `^`: `e^{−λt}` → e⁻λᵗ. Brace a multi-character run;
  a bare `^x` takes the following alphanumeric run.
- Everything else — Greek letters (λ, μ, σ, α, β), operators (∩, ∪, ≤, →, Σ, √),
  and `≈` — is literal Unicode in the data.

A collapsible **"Symbols & card types"** legend at the bottom of the page explains
the symbols and what each card type trains.

---

## Architecture

Everything the app needs at runtime is inside the one HTML file — no external
requests, so it works fully offline.

| Location | What it is |
|---|---|
| `<head>` → `<style>` | All page CSS: the `:root` theme variables, home/drill/legend styles |
| `<body>` → `<div id="app">` | The app mount point (rendered by plain DOM calls) |
| `<body>` → `<details class="legend">` | The static symbol / card-type legend (plain HTML) |
| `<script id="deck-data" type="application/json">` | The full deck data, inlined so no fetch is needed |
| `<script>` (the app) | ~250 lines of readable vanilla JS — no framework, no build |

Inside the app script:

- **`notate(str, parent)`** — parses the `_` / `^` notation and appends text +
  `<sub>` / `<sup>` nodes. `el(tag, cls, text)` wraps it for convenience.
- **Leitner core** — `loadState` / `saveState` / `grade`, the `INTERVAL` map, and
  `isDue`, all keyed on `localStorage['probdeck:leitner:v1']`.
- **`home()` / `drill()` / `done()`** — the three screens, swapped by clearing and
  re-rendering `#app`.

### Card schema

| Field | Meaning |
|---|---|
| `id` | Unique within its deck (e.g. `d10`, `pp4`) |
| `type` | `scenario` · `intuition` · `trap` · `check` — drives the badge |
| `q` | Prompt text |
| `qs` | A symbol shown large under the text (e.g. `λ`, `μ, σ`) — optional |
| `qeq` | A formula/expression prompt shown above `q` — optional |
| `a` | The answer (always present) |
| `alt` | "Also:" supplementary line — optional |
| `note` | Fine-print intuition under the answer — optional |

## Data & persistence

- Progress is stored under the `localStorage` key **`probdeck:leitner:v1`**, per
  browser, per device.
- **Reset:** use "Reset all progress" in the footer, or clear that key:
  ```js
  localStorage.removeItem('probdeck:leitner:v1')
  ```

## Editing the app

Because the source is hand-written, edits are straightforward:

- **Card content** — edit [`data/decks.json`](data/decks.json) (the source of
  truth), then re-inline it into `index.html`. The runtime copy lives in the
  `<script id="deck-data">` block; replace its contents with the JSON. Keeping the
  two in sync is the only build step, and it's a copy-paste.
- **Styling / theme** — the `:root` variables at the top of the `<style>` block
  (`--accent`, `--ink`, `--page`, the per-type badge colours).
- **Legend** — plain HTML in the `<details class="legend">` block.
- **Icons** — regenerate with [`tools/make-icons.py`](tools/make-icons.py)
  (`python tools/make-icons.py`); it draws the bell-curve glyph from the theme
  colours.

## iOS / PWA

The app is an installable **PWA** ("Add to Home Screen"). This route was chosen
because the target is **personal use on the owner's own iPhone** with **no Mac
available** — a PWA is fully buildable and testable on Windows and needs no Xcode.

**In the repo:**

| File | Purpose |
|---|---|
| [`manifest.json`](manifest.json) | Web-app manifest — name, standalone display, theme `#1c1a2e`, icons. |
| [`sw.js`](sw.js) | Service worker — cache-first, so the app runs offline after the first visit. Bump `CACHE` (`prob-vN`) when app files change. |
| [`icons/`](icons) | App icons (180 apple-touch, 192/512, 512 maskable, 32 favicon), from [`tools/make-icons.py`](tools/make-icons.py). |

All PWA paths are **relative**, so it works whether hosted at a GitHub Pages
subpath (`/repo/`) or a root domain.

**Host, then install:**

1. **Put the folder under git and push to GitHub** (create the repo on
   github.com, then):
   ```bash
   git init
   git add .
   git commit -m "Probability flashcards"
   git branch -M main
   git remote add origin https://github.com/<you>/<repo>.git
   git push -u origin main
   ```
2. **Enable Pages:** repo → **Settings → Pages → Build and deployment → Deploy
   from a branch → `main` / `/ (root)`**. Wait for the green URL
   (`https://<you>.github.io/<repo>/`).
3. **Install on the iPhone:** open that URL in **Safari** → Share → **Add to Home
   Screen**. Launch it once online so the service worker caches it.
4. **Verify:** it opens full-screen (no Safari chrome), the icon looks right, and
   it still works in **Airplane Mode**.

To ship an app change after install, edit files, **bump `CACHE` in `sw.js`**, and
re-push; the SW picks up the new version on next launch.

## Files

```
Flashcards_ProbabilityTheory/
├── index.html                        the app (open this)
├── data/decks.json                   card data — source of truth
├── manifest.json                     PWA manifest
├── sw.js                             offline service worker
├── icons/                            generated app icons
├── tools/make-icons.py               icon generator
├── CARDS.md                          human-readable card list
├── probability_flashcard_strategy.md the design brief behind the deck
└── .claude/launch.json               local dev-server config
```
