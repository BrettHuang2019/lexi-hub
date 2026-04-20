# French Chunk (意群) Segmentation — Implementation Plan

## Goal

Given a French sentence, split it into **meaningful chunks (意群)** and store them in the database. These chunks power the flashcard system's progressive display: word → chunk → sentence.

---

## Tool Choice

**Use Stanza** with the default French model (`fr`).

Why: Best label precision for French — handles causatives (`aux:caus`), pronominal passives (`expl:pass`), light verbs (`obj:lvc`), and subject subtypes (`nsubj:caus`) correctly. Clean tokenization with no known bugs on our test sentences.

```python
import stanza
nlp = stanza.Pipeline('fr', processors='tokenize,pos,lemma,depparse')
```

---

## Core Algorithm

### Step 1: Parse the sentence

Run Stanza to get the dependency tree. Each token has: `id`, `text`, `lemma`, `upos`, `deprel`, `head`, `feats`.

### Step 2: Identify clause roots

Walk the tokens and find **clause heads** — tokens whose `deprel` is one of:

| deprel | Meaning |
|--------|---------|
| `root` | Main clause |
| `advcl` | Adverbial clause ("Si elle avait su", "Ayant terminé son travail") |
| `ccomp` | Complement clause ("qu'elles soient revenues") |
| `csubj` | Clausal subject ("qu'elle l'aurait vu") |
| `acl:relcl` | Relative clause ("qu'elle s'est écrites") |
| `conj` | Coordinated clause ("puis ils se sont revus") |

Each clause head defines one chunk.

### Step 3: Collect each chunk's tokens

For each clause head, collect all tokens in its **subtree** (all descendants in the dep tree), sorted by token position. This gives you the chunk's text span.

**Key rule**: A token belongs to the chunk of its nearest clause-level ancestor, not necessarily its direct head.

### Step 4: Handle edge cases

| Case | Rule |
|------|------|
| **Conjunctions/punctuation between clauses** (`puis`, `,`) | Attach to the clause they introduce (the `conj` clause), not the preceding one |
| **Subordinators** (`que`, `si`, `quand`) | Keep with the subordinate clause (they have `mark` deprel pointing to the clause head) |
| **Prepositional phrases** (`avant minuit`, `sans lui`, `par sa mère`) | Stay with their clause head — they're part of the same chunk |
| **Negation** (`ne...pas`) | Glue to verb — they already point to the verb head |
| **Compound tenses** (`s'est fait gronder`) | All auxiliaries (`aux:tense`, `aux:caus`, `aux:pass`) + reflexive pronouns point to the same verb head — they stay together automatically |

---

## Example Walkthrough

**Sentence**: `Si elle avait su, elle ne serait pas venue.`

Stanza parse:

```
Si(mark→su) elle(nsubj→su) avait(aux:tense→su) su(advcl→venue)
,
elle(nsubj→venue) ne(advmod→venue) serait(aux:tense→venue) pas(advmod→venue) venue(root)
```

**Clause heads found**: `su` (advcl), `venue` (root)

**Chunk 1** — subtree of `su`: `Si elle avait su`
**Chunk 2** — subtree of `venue`: `elle ne serait pas venue`

Result:
```json
[
  { "chunk_index": 0, "text": "Si elle avait su" },
  { "chunk_index": 1, "text": "elle ne serait pas venue" }
]
```

---

## Another Example

**Sentence**: `Rentré trop tard, il s'est fait gronder par sa mère.`

**Clause heads**: `Rentré` (advcl), `gronder` (root)

**Chunk 1**: `Rentré trop tard` — advcl subtree
**Chunk 2**: `il s'est fait gronder par sa mère` — root subtree

---

## Data Model

```
Sentence
  ├── id
  ├── text: "Si elle avait su, elle ne serait pas venue."
  └── audio_url

Chunk
  ├── id
  ├── sentence_id (FK)
  ├── chunk_index (0, 1, 2...)
  ├── text: "Si elle avait su"
  ├── start_token_index: 0
  └── end_token_index: 3

Word
  ├── id
  ├── chunk_id (FK)
  ├── text: "su"
  ├── lemma: "savoir"
  ├── pos: "VERB"
  ├── position_in_chunk: 3
```

---

## Function Signature

```python
def segment_sentence(text: str) -> list[dict]:
    """
    Input:  "Si elle avait su, elle ne serait pas venue."
    Output: [
        {
            "chunk_index": 0,
            "text": "Si elle avait su",
            "tokens": [
                {"id": 1, "text": "Si", "lemma": "si", "upos": "SCONJ", "deprel": "mark"},
                {"id": 2, "text": "elle", "lemma": "lui", "upos": "PRON", "deprel": "nsubj"},
                {"id": 3, "text": "avait", "lemma": "avoir", "upos": "AUX", "deprel": "aux:tense"},
                {"id": 4, "text": "su", "lemma": "savoir", "upos": "VERB", "deprel": "advcl"},
            ]
        },
        {
            "chunk_index": 1,
            "text": "elle ne serait pas venue",
            "tokens": [...]
        }
    ]
    """
```

---

## Test Cases

Use these 15 sentences to validate. Expected chunk splits:

| # | Sentence | Expected Chunks |
|---|----------|----------------|
| 1 | Qu'il vienne immédiatement ! | `[Qu'il vienne immédiatement]` (single chunk) |
| 2 | Sois prudent, même si tu crois avoir raison. | `[Sois prudent]` / `[même si tu crois avoir raison]` |
| 3 | Ayant terminé son travail, elle serait déjà partie. | `[Ayant terminé son travail]` / `[elle serait déjà partie]` |
| 4 | Les lettres qu'elle s'est écrites ont disparu. | `[Les lettres]` + `[qu'elle s'est écrites]` + `[ont disparu]` OR `[Les lettres qu'elle s'est écrites]` / `[ont disparu]` |
| 5 | Ils se sont parlé, puis ils se sont revus. | `[Ils se sont parlé]` / `[puis ils se sont revus]` |
| 6 | Il faut qu'elles soient revenues avant minuit. | `[Il faut]` / `[qu'elles soient revenues avant minuit]` |
| 7 | Si elle avait su, elle ne serait pas venue. | `[Si elle avait su]` / `[elle ne serait pas venue]` |
| 8 | Quand il aura fini, nous commencerons sans lui. | `[Quand il aura fini]` / `[nous commencerons sans lui]` |
| 9 | Eussiez-vous accepté, tout aurait été différent. | `[Eussiez-vous accepté]` / `[tout aurait été différent]` |
| 10 | Leurs décisions ont été contestées puis annulées. | `[Leurs décisions ont été contestées]` / `[puis annulées]` |
| 11 | Cette maison s'est vendue très vite. | `[Cette maison s'est vendue très vite]` (single chunk) |
| 12 | Il paraît qu'elle l'aurait vu hier. | `[Il paraît]` / `[qu'elle l'aurait vu hier]` |
| 13 | Le livre que j'ai laissé tomber est abîmé. | `[Le livre que j'ai laissé tomber]` / `[est abîmé]` |
| 14 | Encore faut-il qu'on puisse le prouver. | `[Encore faut-il]` / `[qu'on puisse le prouver]` |
| 15 | Rentré trop tard, il s'est fait gronder par sa mère. | `[Rentré trop tard]` / `[il s'est fait gronder par sa mère]` |

---

## Decision: Relative Clauses (Sentence #4 & #13)

Relative clauses (`acl:relcl`) can either be:
- **Separate chunk**: `[Les lettres]` / `[qu'elle s'est écrites]` / `[ont disparu]`
- **Merged with head noun**: `[Les lettres qu'elle s'est écrites]` / `[ont disparu]`

**Recommendation**: Merge short relative clauses (≤ 5 tokens) with the head noun. Split long ones. This is a tunable parameter — start merged and see how learners respond.

---

## Out of Scope (for now)

- SRS scheduling logic
- Flashcard display mode switching
- Audio segmentation per chunk