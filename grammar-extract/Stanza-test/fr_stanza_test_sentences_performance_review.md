# French Stanza Test Sentences Performance Review

Source reviewed: `grammar-extract/Stanza-test/fr_stanza_test_sentences_report.md`

The source file is a raw `Document.to_dict()` dump, not an accuracy report with gold annotations. This review is therefore a qualitative audit of Stanza's French output across the 100 test sentences, focused on POS tags, lemmas, dependency labels, tokenization, sentence splitting, and robustness on noisy text.

## Overall Assessment

Stanza performs well on standard written French. It reliably finds the main predicate, subjects, direct objects, determiners, prepositional dependents, relative clauses, auxiliaries, and many participial/passive structures. It is especially useful for normal prose, news-style sentences, and many formal/legal examples.

The weakest areas are:

- Hyphenated imperative clitic chains.
- Informal speech and fillers.
- Some quoted strings, filenames, hashtags, emails, and technical tokens.
- A few lexical lemmas.
- Some dependency attachments in clefts, fragmentary/no-verb sentences, comparative constructions, and complex punctuation.

For downstream grammar extraction, Stanza is good enough as a first parse, but the output needs correction rules or confidence handling for the error categories below.

## What It Handles Well

1. Basic declaratives and verb morphology

Examples:

- `Le chat dort sur le canapé.`
- `Elle ne comprend pas la question.`
- `La décision que le ministre a annoncée hier divise les syndicats.`

The parser correctly identifies finite verb roots, subjects, objects, negation adverbs, determiners, and ordinary prepositional phrases.

2. Compound tenses and auxiliaries

Examples:

- `Nous avons mangé avant de partir.`
- `J'ai acheté trois pommes, deux poires et un kilo de riz.`
- `La candidate, soutenue par une coalition fragile, a promis de "réparer le pays".`

Auxiliaries are generally labeled as `AUX` with `aux:tense`, and past participles are usually selected as the verbal heads.

3. Relative clauses

Examples:

- `Ce livre, que je croyais perdu, était dans mon sac.`
- `L'homme qui avait vu l'accident dont parlait le journal a finalement témoigné.`
- `Les données dont nous disposons ne suffisent pas à établir une tendance fiable.`

The parser usually preserves the head noun and attaches relative clauses with `acl:relcl`, with relative pronouns as objects, subjects, or indirect objects.

4. Several French-specific constructions

Good examples include:

- `Les pommes que j'ai fait cuire sont restées trop fermes.`: causative `fait cuire` is analyzed with `aux:caus` and `nsubj:caus`.
- `Il y a eu un avant et un après-Covid...`: existential `il y a` is handled with expletive labels.
- Passive examples such as `a été adopté` and `a été utilisé` are mostly coherent.

## Major Mistakes Spotted

### 1. Imperative clitic tokenization is poor

Sentence 24:

`Donne-le-moi avant que je change d'avis.`

Stanza outputs `Donne-le-moi` as one token tagged `INTJ` with `discourse`, and makes `change` the root. This is wrong. The expected analysis should recognize `Donne` as an imperative verb root, with `le` and `moi` as clitic complements, and the `avant que...` clause as subordinate.

Impact: high. Any grammar extractor looking for imperative mood, object pronouns, or clitic order will miss this sentence entirely.

Sentence 77:

`Va-t'en !`

Stanza parses `Va` as the root verb but keeps `-t'en` as one `ADV`. This misses the clitic structure of `t'en`.

Impact: high for imperative/clitic lessons.

### 2. Informal contractions and spoken fillers are unstable

Sentence 30:

`Ben, franchement, j'en sais rien.`

`Ben` is tagged as `PROPN` and attached as `dislocated`. It is better treated as an interjection or discourse marker.

Sentence 31:

`T'as vu le prix du café maintenant ?`

The contracted `T'` is handled as a subject pronoun, which is useful, but this is still an informal spelling case that should be tested carefully if the downstream task depends on normalized French.

Sentence 32:

`On se capte après le boulot, ok ?`

`ok` is correctly treated as `INTJ`, but the reflexive/reciprocal `se` is labeled `obj`; depending on the target grammar, this may need a special colloquial-pronominal handling rule.

Impact: medium. Informal input is usable, but discourse markers and colloquial pronominals are noisy.

### 3. Some lemmas are clearly wrong

Sentence 50:

`Les données dont nous disposons ne suffisent pas à établir une tendance fiable.`

`suffisent` is lemmatized as `suffiser`; the correct lemma is `suffire`.

Sentence 82:

`J'irai à Québec, à Montréal ou peut-être à Trois-Rivières.`

`irai` is lemmatized as `iraindre`; the correct lemma is `aller`.

Impact: high for vocabulary extraction, conjugation lookup, dictionary linking, and spaced-repetition card generation.

### 4. Named entities and technical strings are often tokenized or tagged awkwardly

Sentence 34:

`M. Dupont, né le 03/04/1980, habite au 12 bis rue Victor-Hugo.`

`M.` is tagged as `NOUN` and made the syntactic subject, while `Dupont` becomes an `nmod` dependent. The better head is the person/name expression, not the abbreviation alone.

Sentence 36:

`La société Alpha-Bêta a levé 3,5 millions d'euros en série A.`

The final `A.` is one `X` token, apparently absorbing the sentence-final period. The period is not separated as punctuation.

Sentence 39:

`Le hashtag #OnVousRépond a été utilisé plus de 20 000 fois.`

The hashtag is split into `#` as `SYM` plus `OnVousRépond` as `PROPN`. That may be acceptable for raw NLP, but it is not ideal if the application wants hashtags as atomic tokens.

Sentence 42:

`Le rendez-vous aura lieu au rez-de-chaussée, salle B-204.`

`rendez-vous` is split into `rendez` + `-vous`, with `rendez` treated as a noun and `-vous` as a pronoun/appositive. For this lexicalized noun, that is wrong.

Impact: medium to high. These cases matter for real-world text ingestion, named-entity handling, and preserving user-visible strings.

### 5. Quoted speech sometimes gets the wrong syntactic center

Sentence 22:

`"Je n'ai rien vu", répète le gardien, les mains tremblantes.`

Stanza makes `vu` the root and attaches `répète` as `parataxis:insert`. Linguistically this is defensible for a quote-first construction, but for many extraction tasks the reporting verb `répète` is the main event. The parse also makes `les mains` an apposition of `gardien`, where an absolute construction analysis would be more useful.

Sentence 61:

`La présentatrice coupe court à la polémique : "On va vérifier les chiffres."`

The quote is attached through `va` as `parataxis`, which is usable but not very semantically explicit. Downstream code should not assume quoted clauses are always `ccomp`.

Impact: medium. Acceptable for surface parsing, risky for event extraction.

### 6. Some dependency roots are debatable or wrong for extraction

Sentence 45:

`Plus elle lisait le rapport, moins elle comprenait la conclusion.`

Stanza chooses `lisait` as the root and makes `comprenait` a conjunct. For the comparative correlative construction, the second clause often carries the main assertion. This parse may be hard to use for chunking.

Sentence 74:

`N'eût été la vigilance d'une riveraine, l'incendie se serait propagé plus vite.`

Stanza makes `vigilance` the root and attaches `propagé` as a conjunct. For semantic extraction, the main clause is `l'incendie se serait propagé`; the initial inverted condition is subordinate.

Sentence 99:

`Ce que je veux, c'est que ça fonctionne du premier coup.`

Stanza makes `fonctionne` the root, while `est` is `cop`. This is plausible under UD-style copular analysis, but the punctuation is attached to `est` rather than the root, which is inconsistent and may matter for tree traversal.

Impact: medium. Many of these are not catastrophic, but they need special treatment if the project extracts "main clause" or "main predicate" chunks.

### 7. Some function-word labels are odd

Sentence 25:

`Il s'en est fallu de peu pour que l'accord échoue.`

`de` is labeled `advmod` and `peu` is `fixed`; the idiom is recognized partially but the analysis is not intuitive.

Sentence 57:

`Dans les quartiers populaires, beaucoup redoutent une nouvelle hausse des loyers.`

`beaucoup` is tagged as `ADV` but used as `nsubj`. Here it behaves pronominally as the subject.

Sentence 88:

`Combien de personnes avez-vous invitées exactement ?`

`Combien` is labeled `nsubj`, while `personnes` is attached as `obl:arg`. The object phrase `Combien de personnes` should function as the object of `invitées`.

Impact: medium. These affect question analysis, quantifier extraction, and subject/object detection.

## Smaller Issues

- Sentence 6: `vendredi` is tagged as `NOUN`; that is acceptable in UD-style French, but downstream date/time handling may prefer temporal normalization.
- Sentence 9 and 33: time expressions like `8 h 12` and `14 h 30` are broken into ordinary numeric/noun pieces. This is expected but should be normalized separately.
- Sentence 37: punctuation around `"Erreur 404 - page introuvable."` is awkward; the sentence-final period is attached inside the quote while the quote mark attaches to the main verb.
- Sentence 48: `adjectifs` is attached as `conj` of `propres`, not of `noms`, which is likely wrong for `noms propres et adjectifs`.
- Sentence 65: in `que devrions-nous faire`, `que` is attached to `devrions`; for extraction it should be associated with `faire`.
- Sentence 68: `distinguées` is tagged as `VERB` rather than `ADJ` in `salutations distinguées`.
- Sentence 71: `que si` is split as `que` advmod plus `si` marker; acceptable, but it encodes the restrictive condition indirectly.
- Sentence 80: quoted imperative `Ouvrez vos cahiers` is handled better than sentence 24 because there is no hyphenated clitic chain.

## Practical Recommendations

1. Add post-processing for imperative clitic chains:

- Detect forms like `Donne-le-moi`, `Va-t'en`, `Dites-le-nous`, `Prends-en`.
- Split or annotate them before grammar extraction.
- Do not trust `INTJ` on hyphenated imperative-looking tokens.

2. Add lemma correction exceptions for common high-value errors:

- `suffisent` / `suffit` / related forms -> `suffire` if Stanza returns `suffiser`.
- `irai`, `iras`, `ira`, `irons`, `irez`, `iront` -> `aller` if Stanza returns an invalid lemma.

3. Preserve technical strings before parsing when needed:

- Emails, filenames, hashtags, URLs/domains, file extensions, version-like names, and abbreviations should be protected or normalized if they need to remain atomic.

4. Treat quoted text and parataxis carefully:

- Do not assume the syntactic root is the communicative main event.
- For quote-first sentences, look for reporting verbs attached as `parataxis` or `parataxis:insert`.

5. Add extraction tests for the known failure modes:

- Imperative + clitic: `Donne-le-moi`, `Va-t'en`.
- Lemma sanity: `suffisent`, `irai`.
- Technical tokens: `rendez-vous`, `série A.`, hashtags, filenames.
- Questions with quantifiers: `Combien de personnes...`.
- No-verb fragments: `Silence dans la salle`, `retour à la case départ`.

## Bottom Line

Stanza is a strong baseline for French grammar extraction on clean, standard sentences. The raw output is most reliable for finite predicates, normal noun phrases, prepositional phrases, relative clauses, auxiliaries, and many passive/participial structures.

It should not be used unfiltered for imperative clitics, lexicalized hyphenated expressions, informal fillers, technical strings, or lemma-sensitive vocabulary workflows. Those cases need targeted post-processing and regression tests before using this output as ground truth.
