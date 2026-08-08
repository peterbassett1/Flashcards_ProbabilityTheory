# Card list

51 cards across 5 decks. Card **types**: **S** = Scenario recognition ·
**I** = Intuition anchor · **T** = Common trap · **Q** = Quick-check.
The source of truth is [`data/decks.json`](data/decks.json) (also inlined into
[`index.html`](index.html)); this file is a human-readable mirror.

Notation in the data: `_` = subscript, `^` = superscript, `{…}` groups a run
(e.g. `e^{−λt}` → e⁻λᵗ). Everything else is literal Unicode.

---

## Discrete RVs — Binomial · Poisson · Geometric (13)

| # | Type | Front | Back |
|---|---|---|---|
| d1 | S | Rolling a fair die 20 times — how many 6s? | **Binomial** — fixed independent trials, two outcomes, constant p |
| d2 | S | Emails in a fixed hour; rare, independent, can cluster | **Poisson** — count of rare independent events in an interval |
| d3 | S | Coin flips until the first head | **Geometric** — trials up to the first success |
| d4 | S | Defective items in a batch of 50, fixed defect rate | **Binomial** — 50 fixed trials, constant probability |
| d5 | I | *p* (Binomial) | Probability of success on each single trial |
| d6 | I | *λ* (Poisson) | Expected count per unit time or space |
| d7 | Q | Mean & variance of Binomial(n, p) | E[X] = np, Var[X] = np(1−p) |
| d8 | Q | Mean & variance of Poisson(λ) | Both = λ (mean = variance) |
| d9 | Q | Mean of Geometric (until first success) | E[X] = 1/p |
| d10 | Q | Poisson P(N = 0) | e^(−λ) |
| d11 | T | Poisson approx to Binomial n=20, p=0.4? | No — np = 8 too big; need large n, small p |
| d12 | T | Four conditions to call it Binomial | Fixed n, independent, two outcomes, constant p |
| d13 | I | Why is Geometric memoryless? | Past failures don't change the next trial's odds |

## Continuous RVs — Normal · Exponential · Beta · Uniform (14)

| # | Type | Front | Back |
|---|---|---|---|
| c1 | S | Time between arrivals in a Poisson process | **Exponential** — memoryless gaps |
| c2 | S | Adult heights, symmetric cluster | **Normal** (approx) — CLT from additive factors |
| c3 | S | Number equally likely anywhere in [0, 1] | **Uniform** — flat density |
| c4 | S | Belief about a coin's bias p on [0, 1] | **Beta** — lives on [0, 1] |
| c5 | I | *μ, σ* (Normal) | μ centres the bell; σ sets its width |
| c6 | I | Memoryless property (exp/Poisson) | Elapsed time doesn't change future odds |
| c7 | Q | Mean of Exponential(λ) | E[X] = 1/λ |
| c8 | Q | CDF of Exponential(λ), P(X ≤ x) | 1 − e^(−λx) |
| c9 | Q | PDF vs CDF | PDF = density; CDF = accumulated P(X ≤ x) |
| c10 | T | Is Normal the right default for most data? | No — often skewed/heavy-tailed/multimodal |
| c11 | T | "A PDF can't exceed 1, right?" | Wrong — density can exceed 1; only area = 1 |
| c12 | I | What is Beta(1, 1)? | The Uniform on [0, 1] — a flat prior |
| c13 | Q | The 68–95–99.7 rule | Within 1σ / 2σ / 3σ of μ |
| c14 | I | Standard deviation vs variance | σ = √Var; σ is in the data's own units |

## Bayesian — inference & updating (10)

| # | Type | Front | Back |
|---|---|---|---|
| b1 | Q | Bayes' theorem, P(A \| B) | P(B\|A)·P(A) / P(B) |
| b2 | I | The prior | Belief before seeing data |
| b3 | I | The posterior | Updated belief = prior × likelihood |
| b4 | I | The likelihood | How well each hypothesis explains the data |
| b5 | S | Estimate p from 7/10 heads, no prior | Beta(1,1) prior → posterior |
| b6 | T | Uniform prior ⇒ Bayesian = frequentist? | Close for large n, not identical in principle |
| b7 | I | Conjugate prior | Posterior stays in the prior's family |
| b8 | Q | Beta(α,β) + h heads, t tails posterior | Beta(α+h, β+t) |
| b9 | T | Strong prior, little data — what wins? | The prior dominates |
| b10 | I | The evidence / marginal P(B) | Normalizing constant so posterior sums to 1 |

## Poisson Process — events over time (8)

| # | Type | Front | Back |
|---|---|---|---|
| pp1 | S | Buses: rare, independent, constant rate | **Poisson process** |
| pp2 | Q | Number of events in time t | Poisson(λt) |
| pp3 | Q | Time between events | Exponential(λ) |
| pp4 | Q | P(N = 0) in time t | e^(−λt) |
| pp5 | I | Why memorylessness matters | The wait to the next event doesn't age |
| pp6 | T | "I've waited ages — is the bus due?" | No — memoryless |
| pp7 | I | The rate λ | Events per unit time; expected count = λt |
| pp8 | Q | Merge two Poisson processes | Poisson process, rate λ₁ + λ₂ |

## General — foundations (6)

| # | Type | Front | Back |
|---|---|---|---|
| g1 | I | Independence, P(A ∩ B) = P(A)·P(B) | Knowing B tells you nothing about A |
| g2 | Q | Conditional probability, P(A \| B) | P(A ∩ B) / P(B) |
| g3 | T | Mutually exclusive = independent? | No — they're strongly dependent |
| g4 | I | Expected value | Long-run average, Σ x·P(x) |
| g5 | Q | Complement rule, P(not A) | 1 − P(A) |
| g6 | T | Add vs multiply probabilities | OR adds (minus overlap); AND multiplies (if independent) |
