# French spaCy Report for idea.md Sentences

Generated from spaCy `fr_dep_news_trf` output using the sentences listed in `idea.md`.

## 1. Unlabeled

Sentence: Qu’il vienne immédiatement !

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| vienne | venir | VERB | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | vienne | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Qu’ | qu’ | SCONJ | SCONJ | _ | 2 | vienne | mark | _ |
| 1 | 3 | il | il | PRON | PRON | Gender=Masc\|Number=Sing\|Person=3 | 2 | vienne | nsubj | _ |
| 2 | 6 | vienne | venir | VERB | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 2 | vienne | ROOT | _ |
| 3 | 13 | immédiatement | immédiatement | ADV | ADV | _ | 2 | vienne | advmod | _ |
| 4 | 27 | ! | ! | PUNCT | PUNCT | _ | 2 | vienne | punct | _ |

Raw spaCy output:

```json
{
  "text": "Qu’il vienne immédiatement !",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Qu’il vienne immédiatement !"
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Qu’",
      "text_with_ws": "Qu’",
      "whitespace_": "",
      "lemma_": "qu’",
      "pos_": "SCONJ",
      "tag_": "SCONJ",
      "morph": null,
      "dep_": "mark",
      "head_i": 2,
      "head_text": "vienne",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xx’",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 3,
      "text": "il",
      "text_with_ws": "il ",
      "whitespace_": " ",
      "lemma_": "il",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Sing|Person=3",
      "dep_": "nsubj",
      "head_i": 2,
      "head_text": "vienne",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 2,
      "idx": 6,
      "text": "vienne",
      "text_with_ws": "vienne ",
      "whitespace_": " ",
      "lemma_": "venir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "ROOT",
      "head_i": 2,
      "head_text": "vienne",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 3,
      "idx": 13,
      "text": "immédiatement",
      "text_with_ws": "immédiatement ",
      "whitespace_": " ",
      "lemma_": "immédiatement",
      "pos_": "ADV",
      "tag_": "ADV",
      "morph": null,
      "dep_": "advmod",
      "head_i": 2,
      "head_text": "vienne",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 4,
      "idx": 27,
      "text": "!",
      "text_with_ws": "!",
      "whitespace_": "",
      "lemma_": "!",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 2,
      "head_text": "vienne",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "!",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```

## 2. Unlabeled

Sentence: Sois prudent, même si tu crois avoir raison.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Sois | être | VERB | VERB | Mood=Imp\|Number=Plur\|Person=2\|Tense=Pres\|VerbForm=Fin | Sois | ROOT |
| crois | croire | VERB | VERB | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | prudent | advcl |
| avoir | avoir | VERB | VERB | VerbForm=Inf | crois | xcomp |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Sois | être | VERB | VERB | Mood=Imp\|Number=Plur\|Person=2\|Tense=Pres\|VerbForm=Fin | 0 | Sois | ROOT | _ |
| 1 | 5 | prudent | prudent | ADJ | ADJ | Gender=Masc\|Number=Sing | 0 | Sois | xcomp | _ |
| 2 | 12 | , | , | PUNCT | PUNCT | _ | 1 | prudent | punct | _ |
| 3 | 14 | même | même | ADV | ADV | _ | 6 | crois | mark | _ |
| 4 | 19 | si | si | SCONJ | SCONJ | _ | 3 | même | fixed | _ |
| 5 | 22 | tu | tu | PRON | PRON | Number=Plur\|Person=2 | 6 | crois | nsubj | _ |
| 6 | 25 | crois | croire | VERB | VERB | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 1 | prudent | advcl | _ |
| 7 | 31 | avoir | avoir | VERB | VERB | VerbForm=Inf | 6 | crois | xcomp | _ |
| 8 | 37 | raison | raison | NOUN | NOUN | Gender=Fem\|Number=Sing | 7 | avoir | obj | _ |
| 9 | 43 | . | . | PUNCT | PUNCT | _ | 0 | Sois | punct | _ |

Raw spaCy output:

```json
{
  "text": "Sois prudent, même si tu crois avoir raison.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Sois prudent, même si tu crois avoir raison."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Sois",
      "text_with_ws": "Sois ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Mood=Imp|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "dep_": "ROOT",
      "head_i": 0,
      "head_text": "Sois",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 1,
      "idx": 5,
      "text": "prudent",
      "text_with_ws": "prudent",
      "whitespace_": "",
      "lemma_": "prudent",
      "pos_": "ADJ",
      "tag_": "ADJ",
      "morph": "Gender=Masc|Number=Sing",
      "dep_": "xcomp",
      "head_i": 0,
      "head_text": "Sois",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 2,
      "idx": 12,
      "text": ",",
      "text_with_ws": ", ",
      "whitespace_": " ",
      "lemma_": ",",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 1,
      "head_text": "prudent",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ",",
      "is_alpha": false,
      "is_stop": false
    },
    {
      "i": 3,
      "idx": 14,
      "text": "même",
      "text_with_ws": "même ",
      "whitespace_": " ",
      "lemma_": "même",
      "pos_": "ADV",
      "tag_": "ADV",
      "morph": null,
      "dep_": "mark",
      "head_i": 6,
      "head_text": "crois",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 4,
      "idx": 19,
      "text": "si",
      "text_with_ws": "si ",
      "whitespace_": " ",
      "lemma_": "si",
      "pos_": "SCONJ",
      "tag_": "SCONJ",
      "morph": null,
      "dep_": "fixed",
      "head_i": 3,
      "head_text": "même",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 5,
      "idx": 22,
      "text": "tu",
      "text_with_ws": "tu ",
      "whitespace_": " ",
      "lemma_": "tu",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Number=Plur|Person=2",
      "dep_": "nsubj",
      "head_i": 6,
      "head_text": "crois",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 6,
      "idx": 25,
      "text": "crois",
      "text_with_ws": "crois ",
      "whitespace_": " ",
      "lemma_": "croire",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "dep_": "advcl",
      "head_i": 1,
      "head_text": "prudent",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 7,
      "idx": 31,
      "text": "avoir",
      "text_with_ws": "avoir ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "VerbForm=Inf",
      "dep_": "xcomp",
      "head_i": 6,
      "head_text": "crois",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 8,
      "idx": 37,
      "text": "raison",
      "text_with_ws": "raison",
      "whitespace_": "",
      "lemma_": "raison",
      "pos_": "NOUN",
      "tag_": "NOUN",
      "morph": "Gender=Fem|Number=Sing",
      "dep_": "obj",
      "head_i": 7,
      "head_text": "avoir",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 9,
      "idx": 43,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 0,
      "head_text": "Sois",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ".",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```

## 3. Unlabeled

Sentence: Ayant terminé son travail, elle serait déjà partie.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Ayant | avoir | AUX | AUX | Tense=Pres\|VerbForm=Part | terminé | aux:tense |
| terminé | terminer | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | partie | advcl |
| serait | être | AUX | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | partie | aux:tense |
| partie | partir | VERB | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part | partie | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Ayant | avoir | AUX | AUX | Tense=Pres\|VerbForm=Part | 1 | terminé | aux:tense | _ |
| 1 | 6 | terminé | terminer | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 8 | partie | advcl | _ |
| 2 | 14 | son | son | DET | DET | Number=Sing\|Poss=Yes | 3 | travail | det | _ |
| 3 | 18 | travail | travail | NOUN | NOUN | Gender=Masc\|Number=Sing | 1 | terminé | obj | _ |
| 4 | 25 | , | , | PUNCT | PUNCT | _ | 8 | partie | punct | _ |
| 5 | 27 | elle | lui | PRON | PRON | Gender=Fem\|Number=Sing\|Person=3 | 8 | partie | nsubj | _ |
| 6 | 32 | serait | être | AUX | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 8 | partie | aux:tense | _ |
| 7 | 39 | déjà | déjà | ADV | ADV | _ | 8 | partie | advmod | _ |
| 8 | 44 | partie | partir | VERB | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part | 8 | partie | ROOT | _ |
| 9 | 50 | . | . | PUNCT | PUNCT | _ | 8 | partie | punct | _ |

Raw spaCy output:

```json
{
  "text": "Ayant terminé son travail, elle serait déjà partie.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Ayant terminé son travail, elle serait déjà partie."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Ayant",
      "text_with_ws": "Ayant ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Tense=Pres|VerbForm=Part",
      "dep_": "aux:tense",
      "head_i": 1,
      "head_text": "terminé",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xxxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 6,
      "text": "terminé",
      "text_with_ws": "terminé ",
      "whitespace_": " ",
      "lemma_": "terminer",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "advcl",
      "head_i": 8,
      "head_text": "partie",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 2,
      "idx": 14,
      "text": "son",
      "text_with_ws": "son ",
      "whitespace_": " ",
      "lemma_": "son",
      "pos_": "DET",
      "tag_": "DET",
      "morph": "Number=Sing|Poss=Yes",
      "dep_": "det",
      "head_i": 3,
      "head_text": "travail",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 18,
      "text": "travail",
      "text_with_ws": "travail",
      "whitespace_": "",
      "lemma_": "travail",
      "pos_": "NOUN",
      "tag_": "NOUN",
      "morph": "Gender=Masc|Number=Sing",
      "dep_": "obj",
      "head_i": 1,
      "head_text": "terminé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 4,
      "idx": 25,
      "text": ",",
      "text_with_ws": ", ",
      "whitespace_": " ",
      "lemma_": ",",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 8,
      "head_text": "partie",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ",",
      "is_alpha": false,
      "is_stop": false
    },
    {
      "i": 5,
      "idx": 27,
      "text": "elle",
      "text_with_ws": "elle ",
      "whitespace_": " ",
      "lemma_": "lui",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Fem|Number=Sing|Person=3",
      "dep_": "nsubj",
      "head_i": 8,
      "head_text": "partie",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 6,
      "idx": 32,
      "text": "serait",
      "text_with_ws": "serait ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 8,
      "head_text": "partie",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 7,
      "idx": 39,
      "text": "déjà",
      "text_with_ws": "déjà ",
      "whitespace_": " ",
      "lemma_": "déjà",
      "pos_": "ADV",
      "tag_": "ADV",
      "morph": null,
      "dep_": "advmod",
      "head_i": 8,
      "head_text": "partie",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 8,
      "idx": 44,
      "text": "partie",
      "text_with_ws": "partie",
      "whitespace_": "",
      "lemma_": "partir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "ROOT",
      "head_i": 8,
      "head_text": "partie",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 9,
      "idx": 50,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 8,
      "head_text": "partie",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ".",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```

## 4. Unlabeled

Sentence: Les lettres qu’elle s’est écrites ont disparu.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| est | être | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | écrites | aux:tense |
| écrites | écrire | VERB | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part | lettres | acl:relcl |
| ont | avoir | AUX | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | disparu | aux:tense |
| disparu | disparaître | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | disparu | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Les | le | DET | DET | Definite=Def\|Number=Plur\|PronType=Art | 1 | lettres | det | _ |
| 1 | 4 | lettres | lettre | NOUN | NOUN | Gender=Fem\|Number=Plur | 8 | disparu | nsubj | _ |
| 2 | 12 | qu’ | qu’ | PRON | PRON | PronType=Rel | 6 | écrites | obj | _ |
| 3 | 15 | elle | lui | PRON | PRON | Gender=Fem\|Number=Sing\|Person=3 | 6 | écrites | nsubj | _ |
| 4 | 20 | s’ | s’ | PRON | PRON | Person=3\|Reflex=Yes | 6 | écrites | expl:comp | _ |
| 5 | 22 | est | être | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 6 | écrites | aux:tense | _ |
| 6 | 26 | écrites | écrire | VERB | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part | 1 | lettres | acl:relcl | _ |
| 7 | 34 | ont | avoir | AUX | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 8 | disparu | aux:tense | _ |
| 8 | 38 | disparu | disparaître | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 8 | disparu | ROOT | _ |
| 9 | 45 | . | . | PUNCT | PUNCT | _ | 8 | disparu | punct | _ |

Raw spaCy output:

```json
{
  "text": "Les lettres qu’elle s’est écrites ont disparu.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Les lettres qu’elle s’est écrites ont disparu."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Les",
      "text_with_ws": "Les ",
      "whitespace_": " ",
      "lemma_": "le",
      "pos_": "DET",
      "tag_": "DET",
      "morph": "Definite=Def|Number=Plur|PronType=Art",
      "dep_": "det",
      "head_i": 1,
      "head_text": "lettres",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 4,
      "text": "lettres",
      "text_with_ws": "lettres ",
      "whitespace_": " ",
      "lemma_": "lettre",
      "pos_": "NOUN",
      "tag_": "NOUN",
      "morph": "Gender=Fem|Number=Plur",
      "dep_": "nsubj",
      "head_i": 8,
      "head_text": "disparu",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 2,
      "idx": 12,
      "text": "qu’",
      "text_with_ws": "qu’",
      "whitespace_": "",
      "lemma_": "qu’",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "PronType=Rel",
      "dep_": "obj",
      "head_i": 6,
      "head_text": "écrites",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx’",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 15,
      "text": "elle",
      "text_with_ws": "elle ",
      "whitespace_": " ",
      "lemma_": "lui",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Fem|Number=Sing|Person=3",
      "dep_": "nsubj",
      "head_i": 6,
      "head_text": "écrites",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 4,
      "idx": 20,
      "text": "s’",
      "text_with_ws": "s’",
      "whitespace_": "",
      "lemma_": "s’",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Person=3|Reflex=Yes",
      "dep_": "expl:comp",
      "head_i": 6,
      "head_text": "écrites",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "x’",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 5,
      "idx": 22,
      "text": "est",
      "text_with_ws": "est ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 6,
      "head_text": "écrites",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 6,
      "idx": 26,
      "text": "écrites",
      "text_with_ws": "écrites ",
      "whitespace_": " ",
      "lemma_": "écrire",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part",
      "dep_": "acl:relcl",
      "head_i": 1,
      "head_text": "lettres",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 7,
      "idx": 34,
      "text": "ont",
      "text_with_ws": "ont ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 8,
      "head_text": "disparu",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 8,
      "idx": 38,
      "text": "disparu",
      "text_with_ws": "disparu",
      "whitespace_": "",
      "lemma_": "disparaître",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "ROOT",
      "head_i": 8,
      "head_text": "disparu",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 9,
      "idx": 45,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 8,
      "head_text": "disparu",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ".",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```

## 5. Unlabeled

Sentence: Ils se sont parlé, puis ils se sont revus.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| sont | être | AUX | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | parlé | aux:tense |
| parlé | parler | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | parlé | ROOT |
| sont | être | AUX | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | revus | aux:tense |
| revus | revoir | VERB | VERB | Gender=Masc\|Number=Plur\|Tense=Past\|VerbForm=Part | parlé | conj |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Ils | il | PRON | PRON | Gender=Masc\|Number=Plur\|Person=3 | 3 | parlé | nsubj | _ |
| 1 | 4 | se | se | PRON | PRON | Person=3\|Reflex=Yes | 3 | parlé | obj | _ |
| 2 | 7 | sont | être | AUX | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 3 | parlé | aux:tense | _ |
| 3 | 12 | parlé | parler | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 3 | parlé | ROOT | _ |
| 4 | 17 | , | , | PUNCT | PUNCT | _ | 3 | parlé | punct | _ |
| 5 | 19 | puis | pouvoir | CCONJ | CCONJ | _ | 9 | revus | cc | _ |
| 6 | 24 | ils | il | PRON | PRON | Gender=Masc\|Number=Plur\|Person=3 | 9 | revus | nsubj | _ |
| 7 | 28 | se | se | PRON | PRON | Person=3\|Reflex=Yes | 9 | revus | obj | _ |
| 8 | 31 | sont | être | AUX | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | revus | aux:tense | _ |
| 9 | 36 | revus | revoir | VERB | VERB | Gender=Masc\|Number=Plur\|Tense=Past\|VerbForm=Part | 3 | parlé | conj | _ |
| 10 | 41 | . | . | PUNCT | PUNCT | _ | 3 | parlé | punct | _ |

Raw spaCy output:

```json
{
  "text": "Ils se sont parlé, puis ils se sont revus.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Ils se sont parlé, puis ils se sont revus."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Ils",
      "text_with_ws": "Ils ",
      "whitespace_": " ",
      "lemma_": "il",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Plur|Person=3",
      "dep_": "nsubj",
      "head_i": 3,
      "head_text": "parlé",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 4,
      "text": "se",
      "text_with_ws": "se ",
      "whitespace_": " ",
      "lemma_": "se",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Person=3|Reflex=Yes",
      "dep_": "obj",
      "head_i": 3,
      "head_text": "parlé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 2,
      "idx": 7,
      "text": "sont",
      "text_with_ws": "sont ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 3,
      "head_text": "parlé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 12,
      "text": "parlé",
      "text_with_ws": "parlé",
      "whitespace_": "",
      "lemma_": "parler",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "ROOT",
      "head_i": 3,
      "head_text": "parlé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 4,
      "idx": 17,
      "text": ",",
      "text_with_ws": ", ",
      "whitespace_": " ",
      "lemma_": ",",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 3,
      "head_text": "parlé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ",",
      "is_alpha": false,
      "is_stop": false
    },
    {
      "i": 5,
      "idx": 19,
      "text": "puis",
      "text_with_ws": "puis ",
      "whitespace_": " ",
      "lemma_": "pouvoir",
      "pos_": "CCONJ",
      "tag_": "CCONJ",
      "morph": null,
      "dep_": "cc",
      "head_i": 9,
      "head_text": "revus",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 6,
      "idx": 24,
      "text": "ils",
      "text_with_ws": "ils ",
      "whitespace_": " ",
      "lemma_": "il",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Plur|Person=3",
      "dep_": "nsubj",
      "head_i": 9,
      "head_text": "revus",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 7,
      "idx": 28,
      "text": "se",
      "text_with_ws": "se ",
      "whitespace_": " ",
      "lemma_": "se",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Person=3|Reflex=Yes",
      "dep_": "obj",
      "head_i": 9,
      "head_text": "revus",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 8,
      "idx": 31,
      "text": "sont",
      "text_with_ws": "sont ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 9,
      "head_text": "revus",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 9,
      "idx": 36,
      "text": "revus",
      "text_with_ws": "revus",
      "whitespace_": "",
      "lemma_": "revoir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part",
      "dep_": "conj",
      "head_i": 3,
      "head_text": "parlé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 10,
      "idx": 41,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 3,
      "head_text": "parlé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ".",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```

## 6. Unlabeled

Sentence: Il faut qu’elles soient revenues avant minuit.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| faut | falloir | VERB | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | faut | ROOT |
| soient | être | AUX | AUX | Mood=Sub\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | revenues | aux:pass |
| revenues | revenir | VERB | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part | faut | ccomp |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Il | il | PRON | PRON | Gender=Masc\|Number=Sing\|Person=3 | 1 | faut | expl:subj | _ |
| 1 | 3 | faut | falloir | VERB | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 1 | faut | ROOT | _ |
| 2 | 8 | qu’ | qu’ | SCONJ | SCONJ | _ | 5 | revenues | mark | _ |
| 3 | 11 | elles | lui | PRON | PRON | Gender=Fem\|Number=Plur\|Person=3 | 5 | revenues | nsubj:pass | _ |
| 4 | 17 | soient | être | AUX | AUX | Mood=Sub\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | revenues | aux:pass | _ |
| 5 | 24 | revenues | revenir | VERB | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part | 1 | faut | ccomp | _ |
| 6 | 33 | avant | avant | ADP | ADP | _ | 7 | minuit | case | _ |
| 7 | 39 | minuit | minuit | NOUN | NOUN | Gender=Masc\|Number=Sing | 5 | revenues | obl:mod | _ |
| 8 | 45 | . | . | PUNCT | PUNCT | _ | 1 | faut | punct | _ |

Raw spaCy output:

```json
{
  "text": "Il faut qu’elles soient revenues avant minuit.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Il faut qu’elles soient revenues avant minuit."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Il",
      "text_with_ws": "Il ",
      "whitespace_": " ",
      "lemma_": "il",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Sing|Person=3",
      "dep_": "expl:subj",
      "head_i": 1,
      "head_text": "faut",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 3,
      "text": "faut",
      "text_with_ws": "faut ",
      "whitespace_": " ",
      "lemma_": "falloir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "ROOT",
      "head_i": 1,
      "head_text": "faut",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 2,
      "idx": 8,
      "text": "qu’",
      "text_with_ws": "qu’",
      "whitespace_": "",
      "lemma_": "qu’",
      "pos_": "SCONJ",
      "tag_": "SCONJ",
      "morph": null,
      "dep_": "mark",
      "head_i": 5,
      "head_text": "revenues",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx’",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 11,
      "text": "elles",
      "text_with_ws": "elles ",
      "whitespace_": " ",
      "lemma_": "lui",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Fem|Number=Plur|Person=3",
      "dep_": "nsubj:pass",
      "head_i": 5,
      "head_text": "revenues",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 4,
      "idx": 17,
      "text": "soient",
      "text_with_ws": "soient ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:pass",
      "head_i": 5,
      "head_text": "revenues",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 5,
      "idx": 24,
      "text": "revenues",
      "text_with_ws": "revenues ",
      "whitespace_": " ",
      "lemma_": "revenir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part",
      "dep_": "ccomp",
      "head_i": 1,
      "head_text": "faut",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 6,
      "idx": 33,
      "text": "avant",
      "text_with_ws": "avant ",
      "whitespace_": " ",
      "lemma_": "avant",
      "pos_": "ADP",
      "tag_": "ADP",
      "morph": null,
      "dep_": "case",
      "head_i": 7,
      "head_text": "minuit",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 7,
      "idx": 39,
      "text": "minuit",
      "text_with_ws": "minuit",
      "whitespace_": "",
      "lemma_": "minuit",
      "pos_": "NOUN",
      "tag_": "NOUN",
      "morph": "Gender=Masc|Number=Sing",
      "dep_": "obl:mod",
      "head_i": 5,
      "head_text": "revenues",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 8,
      "idx": 45,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 1,
      "head_text": "faut",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ".",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```

## 7. Unlabeled

Sentence: Si elle avait su, elle ne serait pas venue.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| avait | avoir | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Imp\|VerbForm=Fin | su | aux:tense |
| su | savoir | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | venue | advcl |
| serait | être | AUX | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | venue | aux:tense |
| venue | venir | VERB | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part | venue | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Si | si | SCONJ | SCONJ | _ | 3 | su | mark | _ |
| 1 | 3 | elle | lui | PRON | PRON | Gender=Fem\|Number=Sing\|Person=3 | 3 | su | nsubj | _ |
| 2 | 8 | avait | avoir | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Imp\|VerbForm=Fin | 3 | su | aux:tense | _ |
| 3 | 14 | su | savoir | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 9 | venue | advcl | _ |
| 4 | 16 | , | , | PUNCT | PUNCT | _ | 9 | venue | punct | _ |
| 5 | 18 | elle | lui | PRON | PRON | Gender=Fem\|Number=Sing\|Person=3 | 9 | venue | nsubj | _ |
| 6 | 23 | ne | ne | ADV | ADV | Polarity=Neg | 9 | venue | advmod | _ |
| 7 | 26 | serait | être | AUX | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | venue | aux:tense | _ |
| 8 | 33 | pas | pas | ADV | ADV | Polarity=Neg | 9 | venue | advmod | _ |
| 9 | 37 | venue | venir | VERB | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part | 9 | venue | ROOT | _ |
| 10 | 42 | . | . | PUNCT | PUNCT | _ | 9 | venue | punct | _ |

Raw spaCy output:

```json
{
  "text": "Si elle avait su, elle ne serait pas venue.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Si elle avait su, elle ne serait pas venue."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Si",
      "text_with_ws": "Si ",
      "whitespace_": " ",
      "lemma_": "si",
      "pos_": "SCONJ",
      "tag_": "SCONJ",
      "morph": null,
      "dep_": "mark",
      "head_i": 3,
      "head_text": "su",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 3,
      "text": "elle",
      "text_with_ws": "elle ",
      "whitespace_": " ",
      "lemma_": "lui",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Fem|Number=Sing|Person=3",
      "dep_": "nsubj",
      "head_i": 3,
      "head_text": "su",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 2,
      "idx": 8,
      "text": "avait",
      "text_with_ws": "avait ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 3,
      "head_text": "su",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 14,
      "text": "su",
      "text_with_ws": "su",
      "whitespace_": "",
      "lemma_": "savoir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "advcl",
      "head_i": 9,
      "head_text": "venue",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 4,
      "idx": 16,
      "text": ",",
      "text_with_ws": ", ",
      "whitespace_": " ",
      "lemma_": ",",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 9,
      "head_text": "venue",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ",",
      "is_alpha": false,
      "is_stop": false
    },
    {
      "i": 5,
      "idx": 18,
      "text": "elle",
      "text_with_ws": "elle ",
      "whitespace_": " ",
      "lemma_": "lui",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Fem|Number=Sing|Person=3",
      "dep_": "nsubj",
      "head_i": 9,
      "head_text": "venue",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 6,
      "idx": 23,
      "text": "ne",
      "text_with_ws": "ne ",
      "whitespace_": " ",
      "lemma_": "ne",
      "pos_": "ADV",
      "tag_": "ADV",
      "morph": "Polarity=Neg",
      "dep_": "advmod",
      "head_i": 9,
      "head_text": "venue",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 7,
      "idx": 26,
      "text": "serait",
      "text_with_ws": "serait ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 9,
      "head_text": "venue",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 8,
      "idx": 33,
      "text": "pas",
      "text_with_ws": "pas ",
      "whitespace_": " ",
      "lemma_": "pas",
      "pos_": "ADV",
      "tag_": "ADV",
      "morph": "Polarity=Neg",
      "dep_": "advmod",
      "head_i": 9,
      "head_text": "venue",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 9,
      "idx": 37,
      "text": "venue",
      "text_with_ws": "venue",
      "whitespace_": "",
      "lemma_": "venir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "ROOT",
      "head_i": 9,
      "head_text": "venue",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 10,
      "idx": 42,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 9,
      "head_text": "venue",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ".",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```

## 8. Unlabeled

Sentence: Quand il aura fini, nous commencerons sans lui.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| aura | avoir | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Fut\|VerbForm=Fin | fini | aux:tense |
| fini | finir | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | commencerons | advcl |
| commencerons | commencer | VERB | VERB | Mood=Ind\|Number=Plur\|Person=1\|Tense=Fut\|VerbForm=Fin | commencerons | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Quand | quand | SCONJ | SCONJ | _ | 3 | fini | mark | _ |
| 1 | 6 | il | il | PRON | PRON | Gender=Masc\|Number=Sing\|Person=3 | 3 | fini | nsubj | _ |
| 2 | 9 | aura | avoir | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Fut\|VerbForm=Fin | 3 | fini | aux:tense | _ |
| 3 | 14 | fini | finir | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 6 | commencerons | advcl | _ |
| 4 | 18 | , | , | PUNCT | PUNCT | _ | 6 | commencerons | punct | _ |
| 5 | 20 | nous | nous | PRON | PRON | Number=Plur\|Person=1 | 6 | commencerons | nsubj | _ |
| 6 | 25 | commencerons | commencer | VERB | VERB | Mood=Ind\|Number=Plur\|Person=1\|Tense=Fut\|VerbForm=Fin | 6 | commencerons | ROOT | _ |
| 7 | 38 | sans | sans | ADP | ADP | _ | 8 | lui | case | _ |
| 8 | 43 | lui | luire | PRON | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 6 | commencerons | obl:mod | _ |
| 9 | 46 | . | . | PUNCT | PUNCT | _ | 6 | commencerons | punct | _ |

Raw spaCy output:

```json
{
  "text": "Quand il aura fini, nous commencerons sans lui.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Quand il aura fini, nous commencerons sans lui."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Quand",
      "text_with_ws": "Quand ",
      "whitespace_": " ",
      "lemma_": "quand",
      "pos_": "SCONJ",
      "tag_": "SCONJ",
      "morph": null,
      "dep_": "mark",
      "head_i": 3,
      "head_text": "fini",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xxxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 6,
      "text": "il",
      "text_with_ws": "il ",
      "whitespace_": " ",
      "lemma_": "il",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Sing|Person=3",
      "dep_": "nsubj",
      "head_i": 3,
      "head_text": "fini",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 2,
      "idx": 9,
      "text": "aura",
      "text_with_ws": "aura ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 3,
      "head_text": "fini",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 14,
      "text": "fini",
      "text_with_ws": "fini",
      "whitespace_": "",
      "lemma_": "finir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "advcl",
      "head_i": 6,
      "head_text": "commencerons",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 4,
      "idx": 18,
      "text": ",",
      "text_with_ws": ", ",
      "whitespace_": " ",
      "lemma_": ",",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 6,
      "head_text": "commencerons",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ",",
      "is_alpha": false,
      "is_stop": false
    },
    {
      "i": 5,
      "idx": 20,
      "text": "nous",
      "text_with_ws": "nous ",
      "whitespace_": " ",
      "lemma_": "nous",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Number=Plur|Person=1",
      "dep_": "nsubj",
      "head_i": 6,
      "head_text": "commencerons",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 6,
      "idx": 25,
      "text": "commencerons",
      "text_with_ws": "commencerons ",
      "whitespace_": " ",
      "lemma_": "commencer",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin",
      "dep_": "ROOT",
      "head_i": 6,
      "head_text": "commencerons",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 7,
      "idx": 38,
      "text": "sans",
      "text_with_ws": "sans ",
      "whitespace_": " ",
      "lemma_": "sans",
      "pos_": "ADP",
      "tag_": "ADP",
      "morph": null,
      "dep_": "case",
      "head_i": 8,
      "head_text": "lui",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 8,
      "idx": 43,
      "text": "lui",
      "text_with_ws": "lui",
      "whitespace_": "",
      "lemma_": "luire",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "dep_": "obl:mod",
      "head_i": 6,
      "head_text": "commencerons",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 9,
      "idx": 46,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 6,
      "head_text": "commencerons",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ".",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```

## 9. Unlabeled

Sentence: Eussiez-vous accepté, tout aurait été différent.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Eussiez | avoir | VERB | VERB | Mood=Ind\|Number=Plur\|Person=2\|Tense=Pres\|VerbForm=Fin | accepté | aux:tense |
| accepté | accepter | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | accepté | ROOT |
| aurait | avoir | AUX | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | différent | aux:tense |
| été | être | AUX | AUX | Tense=Past\|VerbForm=Part | différent | cop |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Eussiez | avoir | VERB | VERB | Mood=Ind\|Number=Plur\|Person=2\|Tense=Pres\|VerbForm=Fin | 2 | accepté | aux:tense | _ |
| 1 | 7 | -vous | vous | PRON | PRON | Number=Plur\|Person=2 | 0 | Eussiez | nsubj | _ |
| 2 | 13 | accepté | accepter | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 2 | accepté | ROOT | _ |
| 3 | 20 | , | , | PUNCT | PUNCT | _ | 2 | accepté | punct | _ |
| 4 | 22 | tout | tout | PRON | PRON | Gender=Masc\|Number=Sing | 7 | différent | nsubj | _ |
| 5 | 27 | aurait | avoir | AUX | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 7 | différent | aux:tense | _ |
| 6 | 34 | été | être | AUX | AUX | Tense=Past\|VerbForm=Part | 7 | différent | cop | _ |
| 7 | 38 | différent | différent | ADJ | ADJ | Gender=Masc\|Number=Sing | 2 | accepté | advcl | _ |
| 8 | 47 | . | . | PUNCT | PUNCT | _ | 2 | accepté | punct | _ |

Raw spaCy output:

```json
{
  "text": "Eussiez-vous accepté, tout aurait été différent.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Eussiez-vous accepté, tout aurait été différent."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Eussiez",
      "text_with_ws": "Eussiez",
      "whitespace_": "",
      "lemma_": "avoir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 2,
      "head_text": "accepté",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xxxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 1,
      "idx": 7,
      "text": "-vous",
      "text_with_ws": "-vous ",
      "whitespace_": " ",
      "lemma_": "vous",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Number=Plur|Person=2",
      "dep_": "nsubj",
      "head_i": 0,
      "head_text": "Eussiez",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "-xxxx",
      "is_alpha": false,
      "is_stop": false
    },
    {
      "i": 2,
      "idx": 13,
      "text": "accepté",
      "text_with_ws": "accepté",
      "whitespace_": "",
      "lemma_": "accepter",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "ROOT",
      "head_i": 2,
      "head_text": "accepté",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 3,
      "idx": 20,
      "text": ",",
      "text_with_ws": ", ",
      "whitespace_": " ",
      "lemma_": ",",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 2,
      "head_text": "accepté",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ",",
      "is_alpha": false,
      "is_stop": false
    },
    {
      "i": 4,
      "idx": 22,
      "text": "tout",
      "text_with_ws": "tout ",
      "whitespace_": " ",
      "lemma_": "tout",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Sing",
      "dep_": "nsubj",
      "head_i": 7,
      "head_text": "différent",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 5,
      "idx": 27,
      "text": "aurait",
      "text_with_ws": "aurait ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 7,
      "head_text": "différent",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 6,
      "idx": 34,
      "text": "été",
      "text_with_ws": "été ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Tense=Past|VerbForm=Part",
      "dep_": "cop",
      "head_i": 7,
      "head_text": "différent",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 7,
      "idx": 38,
      "text": "différent",
      "text_with_ws": "différent",
      "whitespace_": "",
      "lemma_": "différent",
      "pos_": "ADJ",
      "tag_": "ADJ",
      "morph": "Gender=Masc|Number=Sing",
      "dep_": "advcl",
      "head_i": 2,
      "head_text": "accepté",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 8,
      "idx": 47,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 2,
      "head_text": "accepté",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ".",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```

## 10. Unlabeled

Sentence: Leurs décisions ont été contestées puis annulées.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| ont | avoir | AUX | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | contestées | aux:tense |
| été | être | AUX | AUX | Tense=Past\|VerbForm=Part | contestées | aux:pass |
| contestées | contester | VERB | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part\|Voice=Pass | contestées | ROOT |
| annulées | annuler | VERB | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part | contestées | conj |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Leurs | leur | DET | DET | Number=Plur\|Poss=Yes | 1 | décisions | det | _ |
| 1 | 6 | décisions | décision | NOUN | NOUN | Gender=Fem\|Number=Plur | 4 | contestées | nsubj:pass | _ |
| 2 | 16 | ont | avoir | AUX | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 4 | contestées | aux:tense | _ |
| 3 | 20 | été | être | AUX | AUX | Tense=Past\|VerbForm=Part | 4 | contestées | aux:pass | _ |
| 4 | 24 | contestées | contester | VERB | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part\|Voice=Pass | 4 | contestées | ROOT | _ |
| 5 | 35 | puis | pouvoir | CCONJ | CCONJ | _ | 6 | annulées | cc | _ |
| 6 | 40 | annulées | annuler | VERB | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part | 4 | contestées | conj | _ |
| 7 | 48 | . | . | PUNCT | PUNCT | _ | 4 | contestées | punct | _ |

Raw spaCy output:

```json
{
  "text": "Leurs décisions ont été contestées puis annulées.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Leurs décisions ont été contestées puis annulées."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Leurs",
      "text_with_ws": "Leurs ",
      "whitespace_": " ",
      "lemma_": "leur",
      "pos_": "DET",
      "tag_": "DET",
      "morph": "Number=Plur|Poss=Yes",
      "dep_": "det",
      "head_i": 1,
      "head_text": "décisions",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xxxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 6,
      "text": "décisions",
      "text_with_ws": "décisions ",
      "whitespace_": " ",
      "lemma_": "décision",
      "pos_": "NOUN",
      "tag_": "NOUN",
      "morph": "Gender=Fem|Number=Plur",
      "dep_": "nsubj:pass",
      "head_i": 4,
      "head_text": "contestées",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 2,
      "idx": 16,
      "text": "ont",
      "text_with_ws": "ont ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 4,
      "head_text": "contestées",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 20,
      "text": "été",
      "text_with_ws": "été ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Tense=Past|VerbForm=Part",
      "dep_": "aux:pass",
      "head_i": 4,
      "head_text": "contestées",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 4,
      "idx": 24,
      "text": "contestées",
      "text_with_ws": "contestées ",
      "whitespace_": " ",
      "lemma_": "contester",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass",
      "dep_": "ROOT",
      "head_i": 4,
      "head_text": "contestées",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 5,
      "idx": 35,
      "text": "puis",
      "text_with_ws": "puis ",
      "whitespace_": " ",
      "lemma_": "pouvoir",
      "pos_": "CCONJ",
      "tag_": "CCONJ",
      "morph": null,
      "dep_": "cc",
      "head_i": 6,
      "head_text": "annulées",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 6,
      "idx": 40,
      "text": "annulées",
      "text_with_ws": "annulées",
      "whitespace_": "",
      "lemma_": "annuler",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part",
      "dep_": "conj",
      "head_i": 4,
      "head_text": "contestées",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 7,
      "idx": 48,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 4,
      "head_text": "contestées",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ".",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```

## 11. Unlabeled

Sentence: Cette maison s’est vendue très vite.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| est | être | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | vendue | aux:tense |
| vendue | vendre | VERB | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part | vendue | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Cette | ce | DET | DET | Gender=Fem\|Number=Sing\|PronType=Dem | 1 | maison | det | _ |
| 1 | 6 | maison | maison | NOUN | NOUN | Gender=Fem\|Number=Sing | 4 | vendue | nsubj | _ |
| 2 | 13 | s’ | s’ | PRON | PRON | Person=3\|Reflex=Yes | 4 | vendue | expl:comp | _ |
| 3 | 15 | est | être | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 4 | vendue | aux:tense | _ |
| 4 | 19 | vendue | vendre | VERB | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part | 4 | vendue | ROOT | _ |
| 5 | 26 | très | très | ADV | ADV | _ | 6 | vite | advmod | _ |
| 6 | 31 | vite | vite | ADV | ADV | _ | 4 | vendue | advmod | _ |
| 7 | 35 | . | . | PUNCT | PUNCT | _ | 4 | vendue | punct | _ |

Raw spaCy output:

```json
{
  "text": "Cette maison s’est vendue très vite.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Cette maison s’est vendue très vite."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Cette",
      "text_with_ws": "Cette ",
      "whitespace_": " ",
      "lemma_": "ce",
      "pos_": "DET",
      "tag_": "DET",
      "morph": "Gender=Fem|Number=Sing|PronType=Dem",
      "dep_": "det",
      "head_i": 1,
      "head_text": "maison",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xxxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 6,
      "text": "maison",
      "text_with_ws": "maison ",
      "whitespace_": " ",
      "lemma_": "maison",
      "pos_": "NOUN",
      "tag_": "NOUN",
      "morph": "Gender=Fem|Number=Sing",
      "dep_": "nsubj",
      "head_i": 4,
      "head_text": "vendue",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 2,
      "idx": 13,
      "text": "s’",
      "text_with_ws": "s’",
      "whitespace_": "",
      "lemma_": "s’",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Person=3|Reflex=Yes",
      "dep_": "expl:comp",
      "head_i": 4,
      "head_text": "vendue",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "x’",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 15,
      "text": "est",
      "text_with_ws": "est ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 4,
      "head_text": "vendue",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 4,
      "idx": 19,
      "text": "vendue",
      "text_with_ws": "vendue ",
      "whitespace_": " ",
      "lemma_": "vendre",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "ROOT",
      "head_i": 4,
      "head_text": "vendue",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 5,
      "idx": 26,
      "text": "très",
      "text_with_ws": "très ",
      "whitespace_": " ",
      "lemma_": "très",
      "pos_": "ADV",
      "tag_": "ADV",
      "morph": null,
      "dep_": "advmod",
      "head_i": 6,
      "head_text": "vite",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 6,
      "idx": 31,
      "text": "vite",
      "text_with_ws": "vite",
      "whitespace_": "",
      "lemma_": "vite",
      "pos_": "ADV",
      "tag_": "ADV",
      "morph": null,
      "dep_": "advmod",
      "head_i": 4,
      "head_text": "vendue",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 7,
      "idx": 35,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 4,
      "head_text": "vendue",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ".",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```

## 12. Unlabeled

Sentence: Il paraît qu’elle l’aurait vu hier.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| paraît | paraître | VERB | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | paraît | ROOT |
| aurait | avoir | AUX | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | vu | aux:tense |
| vu | voir | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | paraît | ccomp |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Il | il | PRON | PRON | Gender=Masc\|Number=Sing\|Person=3 | 1 | paraît | expl:subj | _ |
| 1 | 3 | paraît | paraître | VERB | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 1 | paraît | ROOT | _ |
| 2 | 10 | qu’ | qu’ | SCONJ | SCONJ | _ | 6 | vu | mark | _ |
| 3 | 13 | elle | lui | PRON | PRON | Gender=Fem\|Number=Sing\|Person=3 | 6 | vu | nsubj | _ |
| 4 | 18 | l’ | l’ | PRON | PRON | Number=Sing\|Person=3 | 6 | vu | obj | _ |
| 5 | 20 | aurait | avoir | AUX | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 6 | vu | aux:tense | _ |
| 6 | 27 | vu | voir | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 1 | paraît | ccomp | _ |
| 7 | 30 | hier | hier | ADV | ADV | _ | 6 | vu | advmod | _ |
| 8 | 34 | . | . | PUNCT | PUNCT | _ | 1 | paraît | punct | _ |

Raw spaCy output:

```json
{
  "text": "Il paraît qu’elle l’aurait vu hier.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Il paraît qu’elle l’aurait vu hier."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Il",
      "text_with_ws": "Il ",
      "whitespace_": " ",
      "lemma_": "il",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Sing|Person=3",
      "dep_": "expl:subj",
      "head_i": 1,
      "head_text": "paraît",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 3,
      "text": "paraît",
      "text_with_ws": "paraît ",
      "whitespace_": " ",
      "lemma_": "paraître",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "ROOT",
      "head_i": 1,
      "head_text": "paraît",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 2,
      "idx": 10,
      "text": "qu’",
      "text_with_ws": "qu’",
      "whitespace_": "",
      "lemma_": "qu’",
      "pos_": "SCONJ",
      "tag_": "SCONJ",
      "morph": null,
      "dep_": "mark",
      "head_i": 6,
      "head_text": "vu",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx’",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 13,
      "text": "elle",
      "text_with_ws": "elle ",
      "whitespace_": " ",
      "lemma_": "lui",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Fem|Number=Sing|Person=3",
      "dep_": "nsubj",
      "head_i": 6,
      "head_text": "vu",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 4,
      "idx": 18,
      "text": "l’",
      "text_with_ws": "l’",
      "whitespace_": "",
      "lemma_": "l’",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Number=Sing|Person=3",
      "dep_": "obj",
      "head_i": 6,
      "head_text": "vu",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "x’",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 5,
      "idx": 20,
      "text": "aurait",
      "text_with_ws": "aurait ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 6,
      "head_text": "vu",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 6,
      "idx": 27,
      "text": "vu",
      "text_with_ws": "vu ",
      "whitespace_": " ",
      "lemma_": "voir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "ccomp",
      "head_i": 1,
      "head_text": "paraît",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 7,
      "idx": 30,
      "text": "hier",
      "text_with_ws": "hier",
      "whitespace_": "",
      "lemma_": "hier",
      "pos_": "ADV",
      "tag_": "ADV",
      "morph": null,
      "dep_": "advmod",
      "head_i": 6,
      "head_text": "vu",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 8,
      "idx": 34,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 1,
      "head_text": "paraît",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ".",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```

## 13. Unlabeled

Sentence: Le livre que j’ai laissé tomber est abîmé.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| ai | avoir | AUX | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | laissé | aux:tense |
| laissé | laisser | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | livre | acl:relcl |
| tomber | tomber | VERB | VERB | VerbForm=Inf | laissé | xcomp |
| est | être | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | abîmé | aux:pass |
| abîmé | abîmer | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Pass | abîmé | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Le | le | DET | DET | Definite=Def\|Gender=Masc\|Number=Sing\|PronType=Art | 1 | livre | det | _ |
| 1 | 3 | livre | livre | NOUN | NOUN | Gender=Masc\|Number=Sing | 8 | abîmé | nsubj:pass | _ |
| 2 | 9 | que | que | PRON | PRON | PronType=Rel | 5 | laissé | dep | _ |
| 3 | 13 | j’ | j’ | PRON | PRON | Number=Sing\|Person=1 | 5 | laissé | nsubj | _ |
| 4 | 15 | ai | avoir | AUX | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 5 | laissé | aux:tense | _ |
| 5 | 18 | laissé | laisser | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 1 | livre | acl:relcl | _ |
| 6 | 25 | tomber | tomber | VERB | VERB | VerbForm=Inf | 5 | laissé | xcomp | _ |
| 7 | 32 | est | être | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 8 | abîmé | aux:pass | _ |
| 8 | 36 | abîmé | abîmer | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Pass | 8 | abîmé | ROOT | _ |
| 9 | 41 | . | . | PUNCT | PUNCT | _ | 8 | abîmé | punct | _ |

Raw spaCy output:

```json
{
  "text": "Le livre que j’ai laissé tomber est abîmé.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Le livre que j’ai laissé tomber est abîmé."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Le",
      "text_with_ws": "Le ",
      "whitespace_": " ",
      "lemma_": "le",
      "pos_": "DET",
      "tag_": "DET",
      "morph": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "dep_": "det",
      "head_i": 1,
      "head_text": "livre",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 3,
      "text": "livre",
      "text_with_ws": "livre ",
      "whitespace_": " ",
      "lemma_": "livre",
      "pos_": "NOUN",
      "tag_": "NOUN",
      "morph": "Gender=Masc|Number=Sing",
      "dep_": "nsubj:pass",
      "head_i": 8,
      "head_text": "abîmé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 2,
      "idx": 9,
      "text": "que",
      "text_with_ws": "que ",
      "whitespace_": " ",
      "lemma_": "que",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "PronType=Rel",
      "dep_": "dep",
      "head_i": 5,
      "head_text": "laissé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 13,
      "text": "j’",
      "text_with_ws": "j’",
      "whitespace_": "",
      "lemma_": "j’",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Number=Sing|Person=1",
      "dep_": "nsubj",
      "head_i": 5,
      "head_text": "laissé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "x’",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 4,
      "idx": 15,
      "text": "ai",
      "text_with_ws": "ai ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 5,
      "head_text": "laissé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 5,
      "idx": 18,
      "text": "laissé",
      "text_with_ws": "laissé ",
      "whitespace_": " ",
      "lemma_": "laisser",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "acl:relcl",
      "head_i": 1,
      "head_text": "livre",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 6,
      "idx": 25,
      "text": "tomber",
      "text_with_ws": "tomber ",
      "whitespace_": " ",
      "lemma_": "tomber",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "VerbForm=Inf",
      "dep_": "xcomp",
      "head_i": 5,
      "head_text": "laissé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 7,
      "idx": 32,
      "text": "est",
      "text_with_ws": "est ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:pass",
      "head_i": 8,
      "head_text": "abîmé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 8,
      "idx": 36,
      "text": "abîmé",
      "text_with_ws": "abîmé",
      "whitespace_": "",
      "lemma_": "abîmer",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "dep_": "ROOT",
      "head_i": 8,
      "head_text": "abîmé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 9,
      "idx": 41,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 8,
      "head_text": "abîmé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ".",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```

## 14. Unlabeled

Sentence: Encore faut-il qu’on puisse le prouver.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| faut | falloir | VERB | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | faut | ROOT |
| puisse | pouvoir | VERB | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | faut | ccomp |
| prouver | prouver | VERB | VERB | VerbForm=Inf | puisse | xcomp |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Encore | encore | ADV | ADV | _ | 1 | faut | advmod | _ |
| 1 | 7 | faut | falloir | VERB | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 1 | faut | ROOT | _ |
| 2 | 11 | -il | il | PRON | PRON | Gender=Masc\|Number=Sing\|Person=3 | 1 | faut | dep | _ |
| 3 | 15 | qu’ | qu’ | SCONJ | SCONJ | _ | 5 | puisse | mark | _ |
| 4 | 18 | on | on | PRON | PRON | Number=Sing\|Person=3 | 5 | puisse | nsubj | _ |
| 5 | 21 | puisse | pouvoir | VERB | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 1 | faut | ccomp | _ |
| 6 | 28 | le | le | PRON | PRON | Gender=Masc\|Number=Sing\|Person=3 | 7 | prouver | obj | _ |
| 7 | 31 | prouver | prouver | VERB | VERB | VerbForm=Inf | 5 | puisse | xcomp | _ |
| 8 | 38 | . | . | PUNCT | PUNCT | _ | 1 | faut | punct | _ |

Raw spaCy output:

```json
{
  "text": "Encore faut-il qu’on puisse le prouver.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Encore faut-il qu’on puisse le prouver."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Encore",
      "text_with_ws": "Encore ",
      "whitespace_": " ",
      "lemma_": "encore",
      "pos_": "ADV",
      "tag_": "ADV",
      "morph": null,
      "dep_": "advmod",
      "head_i": 1,
      "head_text": "faut",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xxxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 7,
      "text": "faut",
      "text_with_ws": "faut",
      "whitespace_": "",
      "lemma_": "falloir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "ROOT",
      "head_i": 1,
      "head_text": "faut",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 2,
      "idx": 11,
      "text": "-il",
      "text_with_ws": "-il ",
      "whitespace_": " ",
      "lemma_": "il",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Sing|Person=3",
      "dep_": "dep",
      "head_i": 1,
      "head_text": "faut",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "-xx",
      "is_alpha": false,
      "is_stop": false
    },
    {
      "i": 3,
      "idx": 15,
      "text": "qu’",
      "text_with_ws": "qu’",
      "whitespace_": "",
      "lemma_": "qu’",
      "pos_": "SCONJ",
      "tag_": "SCONJ",
      "morph": null,
      "dep_": "mark",
      "head_i": 5,
      "head_text": "puisse",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx’",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 4,
      "idx": 18,
      "text": "on",
      "text_with_ws": "on ",
      "whitespace_": " ",
      "lemma_": "on",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Number=Sing|Person=3",
      "dep_": "nsubj",
      "head_i": 5,
      "head_text": "puisse",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 5,
      "idx": 21,
      "text": "puisse",
      "text_with_ws": "puisse ",
      "whitespace_": " ",
      "lemma_": "pouvoir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "ccomp",
      "head_i": 1,
      "head_text": "faut",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 6,
      "idx": 28,
      "text": "le",
      "text_with_ws": "le ",
      "whitespace_": " ",
      "lemma_": "le",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Sing|Person=3",
      "dep_": "obj",
      "head_i": 7,
      "head_text": "prouver",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 7,
      "idx": 31,
      "text": "prouver",
      "text_with_ws": "prouver",
      "whitespace_": "",
      "lemma_": "prouver",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "VerbForm=Inf",
      "dep_": "xcomp",
      "head_i": 5,
      "head_text": "puisse",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 8,
      "idx": 38,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 1,
      "head_text": "faut",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ".",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```

## 15. Unlabeled

Sentence: Rentré trop tard, il s’est fait gronder par sa mère.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Rentré | rentrer | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | gronder | advcl |
| est | être | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | gronder | aux:tense |
| fait | faire | AUX | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | gronder | dep |
| gronder | gronder | VERB | VERB | VerbForm=Inf | gronder | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Rentré | rentrer | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 8 | gronder | advcl | _ |
| 1 | 7 | trop | trop | ADV | ADV | _ | 2 | tard | advmod | _ |
| 2 | 12 | tard | tard | ADV | ADV | _ | 0 | Rentré | advmod | _ |
| 3 | 16 | , | , | PUNCT | PUNCT | _ | 8 | gronder | punct | _ |
| 4 | 18 | il | il | PRON | PRON | Gender=Masc\|Number=Sing\|Person=3 | 8 | gronder | nsubj:pass | _ |
| 5 | 21 | s’ | s’ | PRON | PRON | Person=3\|Reflex=Yes | 8 | gronder | expl:comp | _ |
| 6 | 23 | est | être | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 8 | gronder | aux:tense | _ |
| 7 | 27 | fait | faire | AUX | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 8 | gronder | dep | _ |
| 8 | 32 | gronder | gronder | VERB | VERB | VerbForm=Inf | 8 | gronder | ROOT | _ |
| 9 | 40 | par | par | ADP | ADP | _ | 11 | mère | case | _ |
| 10 | 44 | sa | son | DET | DET | Gender=Fem\|Number=Sing\|Poss=Yes | 11 | mère | det | _ |
| 11 | 47 | mère | mère | NOUN | NOUN | Gender=Fem\|Number=Sing | 8 | gronder | obl:agent | _ |
| 12 | 51 | . | . | PUNCT | PUNCT | _ | 8 | gronder | punct | _ |

Raw spaCy output:

```json
{
  "text": "Rentré trop tard, il s’est fait gronder par sa mère.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Rentré trop tard, il s’est fait gronder par sa mère."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Rentré",
      "text_with_ws": "Rentré ",
      "whitespace_": " ",
      "lemma_": "rentrer",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "advcl",
      "head_i": 8,
      "head_text": "gronder",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xxxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 1,
      "idx": 7,
      "text": "trop",
      "text_with_ws": "trop ",
      "whitespace_": " ",
      "lemma_": "trop",
      "pos_": "ADV",
      "tag_": "ADV",
      "morph": null,
      "dep_": "advmod",
      "head_i": 2,
      "head_text": "tard",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 2,
      "idx": 12,
      "text": "tard",
      "text_with_ws": "tard",
      "whitespace_": "",
      "lemma_": "tard",
      "pos_": "ADV",
      "tag_": "ADV",
      "morph": null,
      "dep_": "advmod",
      "head_i": 0,
      "head_text": "Rentré",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 3,
      "idx": 16,
      "text": ",",
      "text_with_ws": ", ",
      "whitespace_": " ",
      "lemma_": ",",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 8,
      "head_text": "gronder",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ",",
      "is_alpha": false,
      "is_stop": false
    },
    {
      "i": 4,
      "idx": 18,
      "text": "il",
      "text_with_ws": "il ",
      "whitespace_": " ",
      "lemma_": "il",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Sing|Person=3",
      "dep_": "nsubj:pass",
      "head_i": 8,
      "head_text": "gronder",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 5,
      "idx": 21,
      "text": "s’",
      "text_with_ws": "s’",
      "whitespace_": "",
      "lemma_": "s’",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Person=3|Reflex=Yes",
      "dep_": "expl:comp",
      "head_i": 8,
      "head_text": "gronder",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "x’",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 6,
      "idx": 23,
      "text": "est",
      "text_with_ws": "est ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 8,
      "head_text": "gronder",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 7,
      "idx": 27,
      "text": "fait",
      "text_with_ws": "fait ",
      "whitespace_": " ",
      "lemma_": "faire",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "dep",
      "head_i": 8,
      "head_text": "gronder",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 8,
      "idx": 32,
      "text": "gronder",
      "text_with_ws": "gronder ",
      "whitespace_": " ",
      "lemma_": "gronder",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "VerbForm=Inf",
      "dep_": "ROOT",
      "head_i": 8,
      "head_text": "gronder",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 9,
      "idx": 40,
      "text": "par",
      "text_with_ws": "par ",
      "whitespace_": " ",
      "lemma_": "par",
      "pos_": "ADP",
      "tag_": "ADP",
      "morph": null,
      "dep_": "case",
      "head_i": 11,
      "head_text": "mère",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 10,
      "idx": 44,
      "text": "sa",
      "text_with_ws": "sa ",
      "whitespace_": " ",
      "lemma_": "son",
      "pos_": "DET",
      "tag_": "DET",
      "morph": "Gender=Fem|Number=Sing|Poss=Yes",
      "dep_": "det",
      "head_i": 11,
      "head_text": "mère",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 11,
      "idx": 47,
      "text": "mère",
      "text_with_ws": "mère",
      "whitespace_": "",
      "lemma_": "mère",
      "pos_": "NOUN",
      "tag_": "NOUN",
      "morph": "Gender=Fem|Number=Sing",
      "dep_": "obl:agent",
      "head_i": 8,
      "head_text": "gronder",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 12,
      "idx": 51,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 8,
      "head_text": "gronder",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ".",
      "is_alpha": false,
      "is_stop": false
    }
  ]
}
```
