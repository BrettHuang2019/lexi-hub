# French Stanza Tense, Mood, and Voice Performance Review

Source reviewed: `grammar-extract/Stanza-test/fr_stanza_tense_mood_voice_test_sentences_report.md`

The source file is a raw Stanza `Document.to_dict()` dump for 100 French sentences selected to exercise tense, mood, voice, compound tenses, pronominal constructions, auxiliaries, and verbal periphrases. It is not a gold-annotated benchmark, so this review is a qualitative audit of likely downstream extraction behavior.

## Overall Assessment

Stanza is useful as a first-pass French parser for this set, but the raw features are not reliable enough to use directly as tense/mood/voice ground truth.

It performs best on:

- Ordinary present, imperfect, future, and conditional forms when the surface form is unambiguous.
- Basic compound tenses with `avoir` or `être` plus a past participle.
- Canonical passives with `être` plus a past participle.
- Many infinitival, participial, causative, and perception-verb constructions.

The largest extraction risks are:

- Some future and past historic forms are mislabeled as present.
- Many subjunctive contexts are mislabeled as indicative.
- Imperatives are only partially recognized.
- Compound tense semantics must be reconstructed from auxiliary chains.
- `Voice=Pass` is mostly useful for true passives, but it also appears on at least one active `être`-auxiliary intransitive.

## High-Impact Findings

### 1. Several future forms are mislabeled as present

Examples:

- Sentence 8: `partirons` in `Nous partirons...` is tagged `Tense=Pres`, not future.
- Sentence 10: `verras` in `Tu verras...` is tagged `Tense=Pres`, not future.
- Sentence 27: both `auras` and `parlerons` are tagged `Tense=Pres`, even though the sentence contains future perfect plus simple future.
- Sentence 54: `traverserons` is tagged `Tense=Pres`, not future.

Other future forms are correct, for example `mangerai`, `prendront`, `invitera`, `atteindra`, `seront`, `aura`, `sera`, and `pourra`.

Impact: high. A downstream extractor that trusts `Tense=Fut` will under-detect future tense and produce inconsistent lessons or statistics. Add morphology-level fallback rules for common future endings, especially `-rai`, `-ras`, `-ra`, `-rons`, `-rez`, `-ront`.

### 2. Simple past and imperfect are not consistently separated from present

Examples:

- Sentence 6: `disiez` is tagged `Tense=Pres`, but in `Vous disiez...` it is imperfect.
- Sentence 11: `mangeai` and `sortis` are tagged `Tense=Pres`; both are past historic in context.
- Sentence 12 is better: `entra`, `salua`, and `s'assit` are correctly tagged `Tense=Past`.

Impact: high for tense classification. French forms that overlap with present or have rare literary endings need a fallback that considers sentence context and orthography.

### 3. Subjunctive recognition is uneven

Correct or useful cases:

- Sentence 42: `comprenne` is tagged `Mood=Sub`.
- Sentence 43: `soit` is tagged `Mood=Sub`.
- Sentence 75: passive `soit annulée` is tagged with subjunctive auxiliary `soit`.
- Sentence 96: `ait compris` preserves `Mood=Sub` on `ait`.

Missed or problematic cases:

- Sentence 41: `parte` after `Il faut que...` is tagged `Mood=Ind`.
- Sentence 44: `commencions` after `Avant que...` is tagged `Mood=Ind|Tense=Imp`; it should be present subjunctive.
- Sentence 45: jussive `Qu'ils viennent...` is tagged indicative.
- Sentence 46: `parte` after `Il fallait que...` is tagged indicative.
- Sentence 47: literary imperfect subjunctive `comprît` is tagged indicative present.
- Sentence 49: `eussions` is lemmatized as `voir` and tagged indicative present, although it is an auxiliary form of `avoir` in a subjunctive-plus-que-parfait context.
- Sentence 50: `fussent` in `qu'ils ne fussent déjà partis` is tagged indicative imperfect, not subjunctive.
- Sentence 97: `arrivions` after `avant que` is tagged indicative imperfect, not present subjunctive.

Impact: high. For subjunctive extraction, Stanza should be treated as a candidate signal, not a source of truth. Add trigger-aware checks for `il faut que`, `avant que`, `bien que`, `douter que`, `craindre que`, negative belief verbs, and jussive `Que + subject`.

### 4. Imperatives are only partially recognized

Correct or useful cases:

- Sentence 51: `Mange` is recognized as `Mood=Imp`.
- Sentence 52: `Prenez` is recognized as `Mood=Imp`.
- Sentence 55: `Veuillez` is recognized as `Mood=Imp`.

Missed cases:

- Sentence 52: coordinated `éteignez` is tagged indicative, even though it is also imperative.
- Sentence 53: negative imperative `Ne dis rien...` is tagged indicative.
- Sentence 54: `Soyons prudents...` is tagged indicative/copular instead of imperative.

Impact: medium to high. Imperative extraction should not rely only on `Mood=Imp`; add rules for sentence-initial verb forms, negated imperatives, and imperative coordination.

### 5. Compound tenses require reconstruction from auxiliary chains

Stanza usually represents compound tenses by putting tense and mood on the auxiliary and `Tense=Past|VerbForm=Part` on the lexical participle. That is expected UD-style output, but it means the lexical head alone does not contain the full French tense.

Examples:

- Sentence 21: `avais mangé` must be reconstructed as plus-que-parfait from `avais` + `mangé`.
- Sentence 26: `aurai fini` must be reconstructed as futur antérieur, even though `aurai` is tagged `Tense=Pres`.
- Sentence 36: `serais venu` must be reconstructed as conditionnel passé.
- Sentence 57: `a été vendue` must be reconstructed as passé composé passive.
- Sentence 60: `auraient été interrogés` must be reconstructed as conditionnel passé passive.
- Sentence 95: `aurait reçu` is tagged with conditional auxiliary and past participle, but semantically functions as future anterior in reported speech.

Impact: high. Build extraction around verb groups, not isolated token features. For each lexical verb, collect `aux:tense`, `aux:pass`, `cop`, and `aux:caus` dependents, then classify the full chain.

### 6. Passive voice is mostly good, with important edge cases

Good passive cases:

- Sentence 56: `est examiné` has `aux:pass` and `Voice=Pass`.
- Sentence 57: `a été vendue` has `été` as `aux:pass` and `vendue` as `Voice=Pass`.
- Sentence 58: `seront publiés` is correctly passive.
- Sentence 59: `avait été contestée` is correctly passive.
- Sentence 60: `auraient été interrogés` is correctly passive.
- Sentence 75: `soit annulée` is correctly passive subjunctive.
- Sentence 99: `sera corrigé` is correctly passive with an `obl:agent`.

Problematic case:

- Sentence 97: `sera partie` is tagged with `Voice=Pass` on `partie`, but `partir` with `être` is an active intransitive compound tense, not passive.

Pronominal cases:

- Sentences 61 and 62 are pronominal passive-like (`se ferme`, `se vend`) but do not expose `Voice=Pass`.
- Sentences 63 to 65 are reflexive/reciprocal/pronominal active uses and correctly should not be treated as canonical passives.

Impact: high if voice labels feed grammar cards. Do not classify `Voice=Pass` alone as passive; require `aux:pass` or a pronominal passive pattern, and whitelist `être`-auxiliary intransitives such as `partir`, `arriver`, `venir`, `aller`, `entrer`, `sortir`, `naître`, `mourir`, etc.

### 7. Lemma errors affect morphology repair

Examples:

- Sentence 3: `regardions` is lemmatized as `regardier`.
- Sentence 44: `commencions` is lemmatized as `commencier`.
- Sentence 49: `eussions` is lemmatized as `voir`.
- Sentence 50: `craignais` is lemmatized as `crair`.
- Sentence 97: `arrivions` is lemmatized as `arrivier`.

Impact: medium. If fallback rules use lemmas to infer tense/mood, add guardrails for invalid lemmas and prefer surface-form analysis when the lemma is suspicious.

## What Works Well

Stanza gives usable structure for many target constructions:

- Present and imperfect examples are generally clear for simple forms like `mange`, `lis`, `mangeais`, `pleuvait`, `vivait`, and `jouaient`.
- Future and conditional examples are often correct when not affected by the failures above: `mangerai`, `prendront`, `invitera`, `accepterait`, `devrais`, and `auraient`.
- The parser reliably marks many auxiliaries as `aux:tense`, passives as `aux:pass`, and causatives as `aux:caus`.
- Infinitives and participles are usually identifiable with `VerbForm=Inf` and `VerbForm=Part`.
- Causative and perception constructions are reasonably recoverable:
  - Sentence 81: `fais réparer` uses `aux:caus`.
  - Sentence 85: `ai fait relire` uses `fait` as `aux:caus`.
  - Sentences 82 to 84 expose `laisser`, `voir`, and `entendre` with infinitival complements.

## Practical Recommendations

1. Extract verb groups before assigning grammar labels.

For each lexical verb, collect attached auxiliaries and clitics. Classify tense, mood, and voice from the full group, not from the participle token alone.

2. Add morphology fallback rules.

Use surface endings to repair likely future, conditional, past historic, imperative, and subjunctive misses. Keep the rules conservative and log conflicts when Stanza and the fallback disagree.

3. Add trigger-aware subjunctive checks.

For clauses introduced by `que` after modal/impersonal/subjunctive-trigger expressions, mark Stanza indicative analyses as suspect when the surface form is compatible with subjunctive.

4. Treat `Voice=Pass` as a signal, not a final classification.

Canonical passive should require an `aux:pass` chain or a recognized pronominal passive pattern. Active `être`-auxiliary intransitives need explicit handling.

5. Keep regression tests for the observed failures.

Recommended cases:

- `Nous partirons...`, `Tu verras...`, `nous en parlerons`.
- `Je mangeai... puis je sortis...`.
- `Il faut que je parte`, `Avant que nous commencions`, `Qu'ils viennent`.
- `Ne dis rien`, `Soyons prudents`, coordinated `Prenez... et éteignez...`.
- `J'aurai fini`, `Nous aurions terminé`, `auraient été interrogés`.
- `elle sera partie` versus `le rapport sera corrigé`.

## Bottom Line

The raw Stanza report is a useful parser trace, but it should not be treated as a gold source for French tense, mood, and voice. It is strong enough to bootstrap extraction if the application reconstructs verb groups and applies targeted correction rules. Without those corrections, the highest-risk outputs are future tense, subjunctive mood, imperative mood, compound tense labels, and passive versus active `être`-auxiliary constructions.
