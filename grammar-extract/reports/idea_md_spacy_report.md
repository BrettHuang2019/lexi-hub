# French spaCy Report for idea.md Sentences

Generated from spaCy `fr_dep_news_trf` output using the sentences listed in `idea.md`.

## 1. 直陈现在

Sentence: Il chante tous les jours.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| chante | cher | VERB | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | chante | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Il | il | PRON | PRON | Gender=Masc\|Number=Sing\|Person=3 | 1 | chante | nsubj | _ |
| 1 | 3 | chante | cher | VERB | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 1 | chante | ROOT | _ |
| 2 | 10 | tous | tout | ADJ | ADJ | Gender=Masc\|Number=Plur | 4 | jours | amod | _ |
| 3 | 15 | les | le | DET | DET | Definite=Def\|Number=Plur\|PronType=Art | 4 | jours | det | _ |
| 4 | 19 | jours | jour | NOUN | NOUN | Gender=Masc\|Number=Plur | 1 | chante | obj | _ |
| 5 | 24 | . | . | PUNCT | PUNCT | _ | 1 | chante | punct | _ |

Raw spaCy output:

```json
{
  "text": "Il chante tous les jours.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Il chante tous les jours."
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
      "dep_": "nsubj",
      "head_i": 1,
      "head_text": "chante",
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
      "text": "chante",
      "text_with_ws": "chante ",
      "whitespace_": " ",
      "lemma_": "cher",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "ROOT",
      "head_i": 1,
      "head_text": "chante",
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
      "text": "tous",
      "text_with_ws": "tous ",
      "whitespace_": " ",
      "lemma_": "tout",
      "pos_": "ADJ",
      "tag_": "ADJ",
      "morph": "Gender=Masc|Number=Plur",
      "dep_": "amod",
      "head_i": 4,
      "head_text": "jours",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 15,
      "text": "les",
      "text_with_ws": "les ",
      "whitespace_": " ",
      "lemma_": "le",
      "pos_": "DET",
      "tag_": "DET",
      "morph": "Definite=Def|Number=Plur|PronType=Art",
      "dep_": "det",
      "head_i": 4,
      "head_text": "jours",
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
      "text": "jours",
      "text_with_ws": "jours",
      "whitespace_": "",
      "lemma_": "jour",
      "pos_": "NOUN",
      "tag_": "NOUN",
      "morph": "Gender=Masc|Number=Plur",
      "dep_": "obj",
      "head_i": 1,
      "head_text": "chante",
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
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 1,
      "head_text": "chante",
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

## 2. 虚拟现在，与上句同形

Sentence: Il faut qu'il chante.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| faut | falloir | VERB | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | faut | ROOT |
| chante | cher | VERB | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | faut | ccomp |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Il | il | PRON | PRON | Gender=Masc\|Number=Sing\|Person=3 | 1 | faut | expl:subj | _ |
| 1 | 3 | faut | falloir | VERB | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 1 | faut | ROOT | _ |
| 2 | 8 | qu' | que | SCONJ | SCONJ | _ | 4 | chante | mark | _ |
| 3 | 11 | il | il | PRON | PRON | Gender=Masc\|Number=Sing\|Person=3 | 4 | chante | nsubj | _ |
| 4 | 14 | chante | cher | VERB | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 1 | faut | ccomp | _ |
| 5 | 20 | . | . | PUNCT | PUNCT | _ | 1 | faut | punct | _ |

Raw spaCy output:

```json
{
  "text": "Il faut qu'il chante.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Il faut qu'il chante."
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
      "text": "qu'",
      "text_with_ws": "qu'",
      "whitespace_": "",
      "lemma_": "que",
      "pos_": "SCONJ",
      "tag_": "SCONJ",
      "morph": null,
      "dep_": "mark",
      "head_i": 4,
      "head_text": "chante",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx'",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 11,
      "text": "il",
      "text_with_ws": "il ",
      "whitespace_": " ",
      "lemma_": "il",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Sing|Person=3",
      "dep_": "nsubj",
      "head_i": 4,
      "head_text": "chante",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 4,
      "idx": 14,
      "text": "chante",
      "text_with_ws": "chante",
      "whitespace_": "",
      "lemma_": "cher",
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
      "i": 5,
      "idx": 20,
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

## 3. 命令式，与直陈同形

Sentence: Finis ton repas !

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Finis | finir | VERB | VERB | Mood=Imp\|Number=Plur\|Person=2\|Tense=Pres\|VerbForm=Fin | Finis | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Finis | finir | VERB | VERB | Mood=Imp\|Number=Plur\|Person=2\|Tense=Pres\|VerbForm=Fin | 0 | Finis | ROOT | _ |
| 1 | 6 | ton | ton | DET | DET | Number=Sing\|Poss=Yes | 2 | repas | det | _ |
| 2 | 10 | repas | repas | NOUN | NOUN | Gender=Masc\|Number=Sing | 0 | Finis | obj | _ |
| 3 | 16 | ! | ! | PUNCT | PUNCT | _ | 0 | Finis | punct | _ |

Raw spaCy output:

```json
{
  "text": "Finis ton repas !",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Finis ton repas !"
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Finis",
      "text_with_ws": "Finis ",
      "whitespace_": " ",
      "lemma_": "finir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Mood=Imp|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "dep_": "ROOT",
      "head_i": 0,
      "head_text": "Finis",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xxxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 1,
      "idx": 6,
      "text": "ton",
      "text_with_ws": "ton ",
      "whitespace_": " ",
      "lemma_": "ton",
      "pos_": "DET",
      "tag_": "DET",
      "morph": "Number=Sing|Poss=Yes",
      "dep_": "det",
      "head_i": 2,
      "head_text": "repas",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 2,
      "idx": 10,
      "text": "repas",
      "text_with_ws": "repas ",
      "whitespace_": " ",
      "lemma_": "repas",
      "pos_": "NOUN",
      "tag_": "NOUN",
      "morph": "Gender=Masc|Number=Sing",
      "dep_": "obj",
      "head_i": 0,
      "head_text": "Finis",
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
      "text": "!",
      "text_with_ws": "!",
      "whitespace_": "",
      "lemma_": "!",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 0,
      "head_text": "Finis",
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

## 4. 过去完成 + 虚拟

Sentence: J'avais mangé avant qu'il arrive.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| avais | avoir | AUX | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Imp\|VerbForm=Fin | mangé | aux:tense |
| mangé | manger | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | mangé | ROOT |
| arrive | arriver | VERB | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | mangé | advcl |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | J' | je | PRON | PRON | Number=Sing\|Person=1 | 2 | mangé | nsubj | _ |
| 1 | 2 | avais | avoir | AUX | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Imp\|VerbForm=Fin | 2 | mangé | aux:tense | _ |
| 2 | 8 | mangé | manger | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 2 | mangé | ROOT | _ |
| 3 | 14 | avant | avant | ADP | ADP | _ | 6 | arrive | mark | _ |
| 4 | 20 | qu' | que | SCONJ | SCONJ | _ | 6 | arrive | mark | _ |
| 5 | 23 | il | il | PRON | PRON | Gender=Masc\|Number=Sing\|Person=3 | 6 | arrive | expl:subj | _ |
| 6 | 26 | arrive | arriver | VERB | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 2 | mangé | advcl | _ |
| 7 | 32 | . | . | PUNCT | PUNCT | _ | 2 | mangé | punct | _ |

Raw spaCy output:

```json
{
  "text": "J'avais mangé avant qu'il arrive.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "J'avais mangé avant qu'il arrive."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "J'",
      "text_with_ws": "J'",
      "whitespace_": "",
      "lemma_": "je",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Number=Sing|Person=1",
      "dep_": "nsubj",
      "head_i": 2,
      "head_text": "mangé",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "X'",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 2,
      "text": "avais",
      "text_with_ws": "avais ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 2,
      "head_text": "mangé",
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
      "text": "mangé",
      "text_with_ws": "mangé ",
      "whitespace_": " ",
      "lemma_": "manger",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "ROOT",
      "head_i": 2,
      "head_text": "mangé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 3,
      "idx": 14,
      "text": "avant",
      "text_with_ws": "avant ",
      "whitespace_": " ",
      "lemma_": "avant",
      "pos_": "ADP",
      "tag_": "ADP",
      "morph": null,
      "dep_": "mark",
      "head_i": 6,
      "head_text": "arrive",
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
      "text": "qu'",
      "text_with_ws": "qu'",
      "whitespace_": "",
      "lemma_": "que",
      "pos_": "SCONJ",
      "tag_": "SCONJ",
      "morph": null,
      "dep_": "mark",
      "head_i": 6,
      "head_text": "arrive",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx'",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 5,
      "idx": 23,
      "text": "il",
      "text_with_ws": "il ",
      "whitespace_": " ",
      "lemma_": "il",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Sing|Person=3",
      "dep_": "expl:subj",
      "head_i": 6,
      "head_text": "arrive",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 6,
      "idx": 26,
      "text": "arrive",
      "text_with_ws": "arrive",
      "whitespace_": "",
      "lemma_": "arriver",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "advcl",
      "head_i": 2,
      "head_text": "mangé",
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
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 2,
      "head_text": "mangé",
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

## 5. 将来完成

Sentence: J'aurai fini avant midi.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| aurai | avoir | VERB | VERB | Mood=Ind\|Number=Sing\|Person=1\|Tense=Fut\|VerbForm=Fin | fini | aux:tense |
| fini | finir | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | fini | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | J' | je | PRON | PRON | Number=Sing\|Person=1 | 2 | fini | nsubj | _ |
| 1 | 2 | aurai | avoir | VERB | VERB | Mood=Ind\|Number=Sing\|Person=1\|Tense=Fut\|VerbForm=Fin | 2 | fini | aux:tense | _ |
| 2 | 8 | fini | finir | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 2 | fini | ROOT | _ |
| 3 | 13 | avant | avant | ADP | ADP | _ | 4 | midi | case | _ |
| 4 | 19 | midi | midi | NOUN | NOUN | Gender=Masc\|Number=Sing | 2 | fini | obl:mod | _ |
| 5 | 23 | . | . | PUNCT | PUNCT | _ | 2 | fini | punct | _ |

Raw spaCy output:

```json
{
  "text": "J'aurai fini avant midi.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "J'aurai fini avant midi."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "J'",
      "text_with_ws": "J'",
      "whitespace_": "",
      "lemma_": "je",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Number=Sing|Person=1",
      "dep_": "nsubj",
      "head_i": 2,
      "head_text": "fini",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "X'",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 2,
      "text": "aurai",
      "text_with_ws": "aurai ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Mood=Ind|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 2,
      "head_text": "fini",
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
      "text": "fini",
      "text_with_ws": "fini ",
      "whitespace_": " ",
      "lemma_": "finir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "ROOT",
      "head_i": 2,
      "head_text": "fini",
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
      "text": "avant",
      "text_with_ws": "avant ",
      "whitespace_": " ",
      "lemma_": "avant",
      "pos_": "ADP",
      "tag_": "ADP",
      "morph": null,
      "dep_": "case",
      "head_i": 4,
      "head_text": "midi",
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
      "text": "midi",
      "text_with_ws": "midi",
      "whitespace_": "",
      "lemma_": "midi",
      "pos_": "NOUN",
      "tag_": "NOUN",
      "morph": "Gender=Masc|Number=Sing",
      "dep_": "obl:mod",
      "head_i": 2,
      "head_text": "fini",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 5,
      "idx": 23,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 2,
      "head_text": "fini",
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

## 6. 条件完成

Sentence: J'aurais voyagé si j'avais eu de l'argent.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| aurais | avoir | AUX | AUX | Mood=Cnd\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | voyagé | aux:tense |
| voyagé | voyager | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | voyagé | ROOT |
| avais | avoir | AUX | AUX | Mood=Ind\|Number=Plur\|Person=1\|Tense=Imp\|VerbForm=Fin | eu | aux:tense |
| eu | avoir | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | voyagé | advcl |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | J' | je | PRON | PRON | Number=Sing\|Person=1 | 2 | voyagé | nsubj | _ |
| 1 | 2 | aurais | avoir | AUX | AUX | Mood=Cnd\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 2 | voyagé | aux:tense | _ |
| 2 | 9 | voyagé | voyager | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 2 | voyagé | ROOT | _ |
| 3 | 16 | si | si | SCONJ | SCONJ | _ | 6 | eu | mark | _ |
| 4 | 19 | j' | je | PRON | PRON | Number=Sing\|Person=1 | 6 | eu | nsubj | _ |
| 5 | 21 | avais | avoir | AUX | AUX | Mood=Ind\|Number=Plur\|Person=1\|Tense=Imp\|VerbForm=Fin | 6 | eu | aux:tense | _ |
| 6 | 27 | eu | avoir | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 2 | voyagé | advcl | _ |
| 7 | 30 | de | de | ADP | ADP | _ | 9 | argent | det | _ |
| 8 | 33 | l' | le | DET | DET | Definite=Def\|Number=Sing\|PronType=Art | 7 | de | fixed | _ |
| 9 | 35 | argent | argent | NOUN | NOUN | Gender=Masc\|Number=Sing | 6 | eu | obj | _ |
| 10 | 41 | . | . | PUNCT | PUNCT | _ | 2 | voyagé | punct | _ |

Raw spaCy output:

```json
{
  "text": "J'aurais voyagé si j'avais eu de l'argent.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "J'aurais voyagé si j'avais eu de l'argent."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "J'",
      "text_with_ws": "J'",
      "whitespace_": "",
      "lemma_": "je",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Number=Sing|Person=1",
      "dep_": "nsubj",
      "head_i": 2,
      "head_text": "voyagé",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "X'",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 2,
      "text": "aurais",
      "text_with_ws": "aurais ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Cnd|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 2,
      "head_text": "voyagé",
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
      "text": "voyagé",
      "text_with_ws": "voyagé ",
      "whitespace_": " ",
      "lemma_": "voyager",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "ROOT",
      "head_i": 2,
      "head_text": "voyagé",
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
      "text": "si",
      "text_with_ws": "si ",
      "whitespace_": " ",
      "lemma_": "si",
      "pos_": "SCONJ",
      "tag_": "SCONJ",
      "morph": null,
      "dep_": "mark",
      "head_i": 6,
      "head_text": "eu",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 4,
      "idx": 19,
      "text": "j'",
      "text_with_ws": "j'",
      "whitespace_": "",
      "lemma_": "je",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Number=Sing|Person=1",
      "dep_": "nsubj",
      "head_i": 6,
      "head_text": "eu",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "x'",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 5,
      "idx": 21,
      "text": "avais",
      "text_with_ws": "avais ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 6,
      "head_text": "eu",
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
      "text": "eu",
      "text_with_ws": "eu ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "advcl",
      "head_i": 2,
      "head_text": "voyagé",
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
      "text": "de",
      "text_with_ws": "de ",
      "whitespace_": " ",
      "lemma_": "de",
      "pos_": "ADP",
      "tag_": "ADP",
      "morph": null,
      "dep_": "det",
      "head_i": 9,
      "head_text": "argent",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 8,
      "idx": 33,
      "text": "l'",
      "text_with_ws": "l'",
      "whitespace_": "",
      "lemma_": "le",
      "pos_": "DET",
      "tag_": "DET",
      "morph": "Definite=Def|Number=Sing|PronType=Art",
      "dep_": "fixed",
      "head_i": 7,
      "head_text": "de",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "x'",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 9,
      "idx": 35,
      "text": "argent",
      "text_with_ws": "argent",
      "whitespace_": "",
      "lemma_": "argent",
      "pos_": "NOUN",
      "tag_": "NOUN",
      "morph": "Gender=Masc|Number=Sing",
      "dep_": "obj",
      "head_i": 6,
      "head_text": "eu",
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
      "head_i": 2,
      "head_text": "voyagé",
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

## 7. être + 过去分词，测试性数配合

Sentence: Elle est partie hier soir.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| est | être | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | partie | aux:tense |
| partie | partir | VERB | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part | partie | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Elle | lui | PRON | PRON | Gender=Fem\|Number=Sing\|Person=3 | 2 | partie | nsubj | _ |
| 1 | 5 | est | être | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 2 | partie | aux:tense | _ |
| 2 | 9 | partie | partir | VERB | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part | 2 | partie | ROOT | _ |
| 3 | 16 | hier | hier | ADV | ADV | _ | 2 | partie | advmod | _ |
| 4 | 21 | soir | soir | NOUN | NOUN | Gender=Masc\|Number=Sing | 2 | partie | obl:mod | _ |
| 5 | 25 | . | . | PUNCT | PUNCT | _ | 2 | partie | punct | _ |

Raw spaCy output:

```json
{
  "text": "Elle est partie hier soir.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Elle est partie hier soir."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Elle",
      "text_with_ws": "Elle ",
      "whitespace_": " ",
      "lemma_": "lui",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Fem|Number=Sing|Person=3",
      "dep_": "nsubj",
      "head_i": 2,
      "head_text": "partie",
      "is_sent_start": true,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 1,
      "idx": 5,
      "text": "est",
      "text_with_ws": "est ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 2,
      "head_text": "partie",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 2,
      "idx": 9,
      "text": "partie",
      "text_with_ws": "partie ",
      "whitespace_": " ",
      "lemma_": "partir",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "ROOT",
      "head_i": 2,
      "head_text": "partie",
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
      "text": "hier",
      "text_with_ws": "hier ",
      "whitespace_": " ",
      "lemma_": "hier",
      "pos_": "ADV",
      "tag_": "ADV",
      "morph": null,
      "dep_": "advmod",
      "head_i": 2,
      "head_text": "partie",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 4,
      "idx": 21,
      "text": "soir",
      "text_with_ws": "soir",
      "whitespace_": "",
      "lemma_": "soir",
      "pos_": "NOUN",
      "tag_": "NOUN",
      "morph": "Gender=Masc|Number=Sing",
      "dep_": "obl:mod",
      "head_i": 2,
      "head_text": "partie",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 5,
      "idx": 25,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 2,
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

## 8. 代词式动词

Sentence: Je me suis levé tôt.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| suis | être | AUX | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | levé | aux:tense |
| levé | lever | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | levé | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Je | je | PRON | PRON | Number=Sing\|Person=1 | 3 | levé | nsubj | _ |
| 1 | 3 | me | me | PRON | PRON | Number=Sing\|Person=1\|Reflex=Yes | 3 | levé | expl:comp | _ |
| 2 | 6 | suis | être | AUX | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 3 | levé | aux:tense | _ |
| 3 | 11 | levé | lever | VERB | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 3 | levé | ROOT | _ |
| 4 | 16 | tôt | tôt | ADV | ADV | _ | 3 | levé | advmod | _ |
| 5 | 19 | . | . | PUNCT | PUNCT | _ | 3 | levé | punct | _ |

Raw spaCy output:

```json
{
  "text": "Je me suis levé tôt.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Je me suis levé tôt."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Je",
      "text_with_ws": "Je ",
      "whitespace_": " ",
      "lemma_": "je",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Number=Sing|Person=1",
      "dep_": "nsubj",
      "head_i": 3,
      "head_text": "levé",
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
      "text": "me",
      "text_with_ws": "me ",
      "whitespace_": " ",
      "lemma_": "me",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Number=Sing|Person=1|Reflex=Yes",
      "dep_": "expl:comp",
      "head_i": 3,
      "head_text": "levé",
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
      "text": "suis",
      "text_with_ws": "suis ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 3,
      "head_text": "levé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 11,
      "text": "levé",
      "text_with_ws": "levé ",
      "whitespace_": " ",
      "lemma_": "lever",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "dep_": "ROOT",
      "head_i": 3,
      "head_text": "levé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 4,
      "idx": 16,
      "text": "tôt",
      "text_with_ws": "tôt",
      "whitespace_": "",
      "lemma_": "tôt",
      "pos_": "ADV",
      "tag_": "ADV",
      "morph": null,
      "dep_": "advmod",
      "head_i": 3,
      "head_text": "levé",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 5,
      "idx": 19,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 3,
      "head_text": "levé",
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

## 9. 被动语态

Sentence: La lettre a été écrite par Marie.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| a | avoir | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | écrite | aux:tense |
| été | être | AUX | AUX | Tense=Past\|VerbForm=Part | écrite | aux:pass |
| écrite | écrire | VERB | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Pass | écrite | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | La | le | DET | DET | Definite=Def\|Gender=Fem\|Number=Sing\|PronType=Art | 1 | lettre | det | _ |
| 1 | 3 | lettre | lettre | NOUN | NOUN | Gender=Fem\|Number=Sing | 4 | écrite | nsubj:pass | _ |
| 2 | 10 | a | avoir | AUX | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 4 | écrite | aux:tense | _ |
| 3 | 12 | été | être | AUX | AUX | Tense=Past\|VerbForm=Part | 4 | écrite | aux:pass | _ |
| 4 | 16 | écrite | écrire | VERB | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Pass | 4 | écrite | ROOT | _ |
| 5 | 23 | par | par | ADP | ADP | _ | 6 | Marie | case | _ |
| 6 | 27 | Marie | Marie | PROPN | PROPN | Gender=Fem\|Number=Sing | 4 | écrite | obl:agent | _ |
| 7 | 32 | . | . | PUNCT | PUNCT | _ | 4 | écrite | punct | _ |

Raw spaCy output:

```json
{
  "text": "La lettre a été écrite par Marie.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "La lettre a été écrite par Marie."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "La",
      "text_with_ws": "La ",
      "whitespace_": " ",
      "lemma_": "le",
      "pos_": "DET",
      "tag_": "DET",
      "morph": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "dep_": "det",
      "head_i": 1,
      "head_text": "lettre",
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
      "text": "lettre",
      "text_with_ws": "lettre ",
      "whitespace_": " ",
      "lemma_": "lettre",
      "pos_": "NOUN",
      "tag_": "NOUN",
      "morph": "Gender=Fem|Number=Sing",
      "dep_": "nsubj:pass",
      "head_i": 4,
      "head_text": "écrite",
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
      "text": "a",
      "text_with_ws": "a ",
      "whitespace_": " ",
      "lemma_": "avoir",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:tense",
      "head_i": 4,
      "head_text": "écrite",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "x",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 12,
      "text": "été",
      "text_with_ws": "été ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Tense=Past|VerbForm=Part",
      "dep_": "aux:pass",
      "head_i": 4,
      "head_text": "écrite",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 4,
      "idx": 16,
      "text": "écrite",
      "text_with_ws": "écrite ",
      "whitespace_": " ",
      "lemma_": "écrire",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "dep_": "ROOT",
      "head_i": 4,
      "head_text": "écrite",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 5,
      "idx": 23,
      "text": "par",
      "text_with_ws": "par ",
      "whitespace_": " ",
      "lemma_": "par",
      "pos_": "ADP",
      "tag_": "ADP",
      "morph": null,
      "dep_": "case",
      "head_i": 6,
      "head_text": "Marie",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 6,
      "idx": 27,
      "text": "Marie",
      "text_with_ws": "Marie",
      "whitespace_": "",
      "lemma_": "Marie",
      "pos_": "PROPN",
      "tag_": "PROPN",
      "morph": "Gender=Fem|Number=Sing",
      "dep_": "obl:agent",
      "head_i": 4,
      "head_text": "écrite",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "Xxxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 7,
      "idx": 32,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 4,
      "head_text": "écrite",
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

## 10. être 的虚拟式，形式有别于直陈

Sentence: Bien qu'il soit fatigué, il travaille.

Verb and auxiliary analysis:

| Text | Lemma | POS | Tag | Morph | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| soit | être | AUX | AUX | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | fatigué | aux:pass |
| travaille | travailler | VERB | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | travaille | ROOT |

Full token analysis:

| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Bien | bien | ADV | ADV | _ | 4 | fatigué | mark | _ |
| 1 | 5 | qu' | que | SCONJ | SCONJ | _ | 0 | Bien | fixed | _ |
| 2 | 8 | il | il | PRON | PRON | Gender=Masc\|Number=Sing\|Person=3 | 4 | fatigué | nsubj:pass | _ |
| 3 | 11 | soit | être | AUX | AUX | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 4 | fatigué | aux:pass | _ |
| 4 | 16 | fatigué | fatigué | ADJ | ADJ | Gender=Masc\|Number=Sing | 7 | travaille | advcl | _ |
| 5 | 23 | , | , | PUNCT | PUNCT | _ | 7 | travaille | punct | _ |
| 6 | 25 | il | il | PRON | PRON | Gender=Masc\|Number=Sing\|Person=3 | 7 | travaille | nsubj | _ |
| 7 | 28 | travaille | travailler | VERB | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 7 | travaille | ROOT | _ |
| 8 | 37 | . | . | PUNCT | PUNCT | _ | 7 | travaille | punct | _ |

Raw spaCy output:

```json
{
  "text": "Bien qu'il soit fatigué, il travaille.",
  "model": "fr_dep_news_trf",
  "lang_": "fr",
  "cats": {},
  "sentences": [
    "Bien qu'il soit fatigué, il travaille."
  ],
  "ents": [],
  "tokens": [
    {
      "i": 0,
      "idx": 0,
      "text": "Bien",
      "text_with_ws": "Bien ",
      "whitespace_": " ",
      "lemma_": "bien",
      "pos_": "ADV",
      "tag_": "ADV",
      "morph": null,
      "dep_": "mark",
      "head_i": 4,
      "head_text": "fatigué",
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
      "text": "qu'",
      "text_with_ws": "qu'",
      "whitespace_": "",
      "lemma_": "que",
      "pos_": "SCONJ",
      "tag_": "SCONJ",
      "morph": null,
      "dep_": "fixed",
      "head_i": 0,
      "head_text": "Bien",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx'",
      "is_alpha": false,
      "is_stop": true
    },
    {
      "i": 2,
      "idx": 8,
      "text": "il",
      "text_with_ws": "il ",
      "whitespace_": " ",
      "lemma_": "il",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Sing|Person=3",
      "dep_": "nsubj:pass",
      "head_i": 4,
      "head_text": "fatigué",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 3,
      "idx": 11,
      "text": "soit",
      "text_with_ws": "soit ",
      "whitespace_": " ",
      "lemma_": "être",
      "pos_": "AUX",
      "tag_": "AUX",
      "morph": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "aux:pass",
      "head_i": 4,
      "head_text": "fatigué",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 4,
      "idx": 16,
      "text": "fatigué",
      "text_with_ws": "fatigué",
      "whitespace_": "",
      "lemma_": "fatigué",
      "pos_": "ADJ",
      "tag_": "ADJ",
      "morph": "Gender=Masc|Number=Sing",
      "dep_": "advcl",
      "head_i": 7,
      "head_text": "travaille",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 5,
      "idx": 23,
      "text": ",",
      "text_with_ws": ", ",
      "whitespace_": " ",
      "lemma_": ",",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 7,
      "head_text": "travaille",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": ",",
      "is_alpha": false,
      "is_stop": false
    },
    {
      "i": 6,
      "idx": 25,
      "text": "il",
      "text_with_ws": "il ",
      "whitespace_": " ",
      "lemma_": "il",
      "pos_": "PRON",
      "tag_": "PRON",
      "morph": "Gender=Masc|Number=Sing|Person=3",
      "dep_": "nsubj",
      "head_i": 7,
      "head_text": "travaille",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xx",
      "is_alpha": true,
      "is_stop": true
    },
    {
      "i": 7,
      "idx": 28,
      "text": "travaille",
      "text_with_ws": "travaille",
      "whitespace_": "",
      "lemma_": "travailler",
      "pos_": "VERB",
      "tag_": "VERB",
      "morph": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "dep_": "ROOT",
      "head_i": 7,
      "head_text": "travaille",
      "is_sent_start": false,
      "ent_iob_": "",
      "ent_type_": "",
      "shape_": "xxxx",
      "is_alpha": true,
      "is_stop": false
    },
    {
      "i": 8,
      "idx": 37,
      "text": ".",
      "text_with_ws": ".",
      "whitespace_": "",
      "lemma_": ".",
      "pos_": "PUNCT",
      "tag_": "PUNCT",
      "morph": null,
      "dep_": "punct",
      "head_i": 7,
      "head_text": "travaille",
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
