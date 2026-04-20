# French Trankit Report for idea.md Sentences

Generated from real Trankit output using the sentences listed in `idea.md`.

## 1. Unlabeled

Sentence: Qu’il vienne immédiatement !

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| vienne | venir | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Qu’ | qu’ | SCONJ | _ | 3 | mark |
| 2 | il | il | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 3 | nsubj |
| 3 | vienne | venir | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 4 | immédiatement | immédiatement | ADV | _ | 3 | advmod |
| 5 | ! | ! | PUNCT | _ | 3 | punct |

Raw Trankit output:

```json
{
  "text": "Qu’il vienne immédiatement !",
  "tokens": [
    {
      "id": 1,
      "text": "Qu’",
      "upos": "SCONJ",
      "head": 3,
      "deprel": "mark",
      "span": [
        0,
        3
      ],
      "lemma": "qu’",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "il",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "span": [
        3,
        5
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "vienne",
      "upos": "VERB",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "span": [
        6,
        12
      ],
      "lemma": "venir",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "immédiatement",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "span": [
        13,
        26
      ],
      "lemma": "immédiatement",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "!",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "span": [
        27,
        28
      ],
      "lemma": "!",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 2. Unlabeled

Sentence: Sois prudent, même si tu crois avoir raison.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| Sois | être | AUX | Mood=Imp\|Number=Plur\|Person=2\|Tense=Pres\|VerbForm=Fin | 2 | cop |
| crois | croire | VERB | Mood=Ind\|Number=Sing\|Person=2\|Tense=Pres\|VerbForm=Fin | 2 | advcl |
| avoir | avoir | VERB | VerbForm=Inf | 7 | xcomp |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Sois | être | AUX | Mood=Imp\|Number=Plur\|Person=2\|Tense=Pres\|VerbForm=Fin | 2 | cop |
| 2 | prudent | prudent | ADJ | Gender=Masc\|Number=Sing | 0 | root |
| 3 | , | , | PUNCT | _ | 7 | punct |
| 4 | même | même | ADV | _ | 7 | advmod |
| 5 | si | si | SCONJ | _ | 7 | mark |
| 6 | tu | il | PRON | Number=Sing\|Person=2\|PronType=Prs | 7 | nsubj |
| 7 | crois | croire | VERB | Mood=Ind\|Number=Sing\|Person=2\|Tense=Pres\|VerbForm=Fin | 2 | advcl |
| 8 | avoir | avoir | VERB | VerbForm=Inf | 7 | xcomp |
| 9 | raison | raison | NOUN | Gender=Fem\|Number=Sing | 8 | obj |
| 10 | . | . | PUNCT | _ | 2 | punct |

Raw Trankit output:

```json
{
  "text": "Sois prudent, même si tu crois avoir raison.",
  "tokens": [
    {
      "id": 1,
      "text": "Sois",
      "upos": "AUX",
      "feats": "Mood=Imp|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "cop",
      "span": [
        0,
        4
      ],
      "lemma": "être",
      "ner": "S-LOC"
    },
    {
      "id": 2,
      "text": "prudent",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 0,
      "deprel": "root",
      "span": [
        5,
        12
      ],
      "lemma": "prudent",
      "ner": "O"
    },
    {
      "id": 3,
      "text": ",",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "span": [
        12,
        13
      ],
      "lemma": ",",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "même",
      "upos": "ADV",
      "head": 7,
      "deprel": "advmod",
      "span": [
        14,
        18
      ],
      "lemma": "même",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "si",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "span": [
        19,
        21
      ],
      "lemma": "si",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "tu",
      "upos": "PRON",
      "feats": "Number=Sing|Person=2|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "span": [
        22,
        24
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "crois",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "advcl",
      "span": [
        25,
        30
      ],
      "lemma": "croire",
      "ner": "O"
    },
    {
      "id": 8,
      "text": "avoir",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 7,
      "deprel": "xcomp",
      "span": [
        31,
        36
      ],
      "lemma": "avoir",
      "ner": "O"
    },
    {
      "id": 9,
      "text": "raison",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "obj",
      "span": [
        37,
        43
      ],
      "lemma": "raison",
      "ner": "O"
    },
    {
      "id": 10,
      "text": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "span": [
        43,
        44
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 3. Unlabeled

Sentence: Ayant terminé son travail, elle serait déjà partie.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| Ayant | avoir | AUX | Tense=Pres\|VerbForm=Part | 2 | aux:tense |
| terminé | terminer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 9 | advcl |
| serait | être | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | cop |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Ayant | avoir | AUX | Tense=Pres\|VerbForm=Part | 2 | aux:tense |
| 2 | terminé | terminer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 9 | advcl |
| 3 | son | son | DET | Gender=Masc\|Number=Sing\|Poss=Yes\|PronType=Prs | 4 | det |
| 4 | travail | travail | NOUN | Gender=Masc\|Number=Sing | 2 | obj |
| 5 | , | , | PUNCT | _ | 2 | punct |
| 6 | elle | il | PRON | Gender=Fem\|Number=Sing\|Person=3\|PronType=Prs | 9 | nsubj |
| 7 | serait | être | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | cop |
| 8 | déjà | déjà | ADV | _ | 9 | advmod |
| 9 | partie | partie | NOUN | Gender=Fem\|Number=Sing | 0 | root |
| 10 | . | . | PUNCT | _ | 9 | punct |

Raw Trankit output:

```json
{
  "text": "Ayant terminé son travail, elle serait déjà partie.",
  "tokens": [
    {
      "id": 1,
      "text": "Ayant",
      "upos": "AUX",
      "feats": "Tense=Pres|VerbForm=Part",
      "head": 2,
      "deprel": "aux:tense",
      "span": [
        0,
        5
      ],
      "lemma": "avoir",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "terminé",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 9,
      "deprel": "advcl",
      "span": [
        6,
        13
      ],
      "lemma": "terminer",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "son",
      "upos": "DET",
      "feats": "Gender=Masc|Number=Sing|Poss=Yes|PronType=Prs",
      "head": 4,
      "deprel": "det",
      "span": [
        14,
        17
      ],
      "lemma": "son",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "travail",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 2,
      "deprel": "obj",
      "span": [
        18,
        25
      ],
      "lemma": "travail",
      "ner": "O"
    },
    {
      "id": 5,
      "text": ",",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "span": [
        25,
        26
      ],
      "lemma": ",",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "elle",
      "upos": "PRON",
      "feats": "Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "nsubj",
      "span": [
        27,
        31
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "serait",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "cop",
      "span": [
        32,
        38
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 8,
      "text": "déjà",
      "upos": "ADV",
      "head": 9,
      "deprel": "advmod",
      "span": [
        39,
        43
      ],
      "lemma": "déjà",
      "ner": "O"
    },
    {
      "id": 9,
      "text": "partie",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 0,
      "deprel": "root",
      "span": [
        44,
        50
      ],
      "lemma": "partie",
      "ner": "O"
    },
    {
      "id": 10,
      "text": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "span": [
        50,
        51
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 4. Unlabeled

Sentence: Les lettres qu’elle s’est écrites ont disparu.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 7 | aux:tense |
| écrites | écrire | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part | 2 | acl:relcl |
| ont | avoir | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | aux:tense |
| disparu | disparaître | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Les | le | DET | Definite=Def\|Gender=Fem\|Number=Plur\|PronType=Art | 2 | det |
| 2 | lettres | lettre | NOUN | Gender=Fem\|Number=Plur | 9 | nsubj |
| 3 | qu’ | qu’ | PRON | PronType=Rel | 7 | obj |
| 4 | elle | il | PRON | Gender=Fem\|Number=Sing\|Person=3\|PronType=Prs | 7 | nsubj |
| 5 | s’ | s’ | PRON | Person=3\|PronType=Prs | 7 | iobj |
| 6 | est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 7 | aux:tense |
| 7 | écrites | écrire | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part | 2 | acl:relcl |
| 8 | ont | avoir | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | aux:tense |
| 9 | disparu | disparaître | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| 10 | . | . | PUNCT | _ | 9 | punct |

Raw Trankit output:

```json
{
  "text": "Les lettres qu’elle s’est écrites ont disparu.",
  "tokens": [
    {
      "id": 1,
      "text": "Les",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Plur|PronType=Art",
      "head": 2,
      "deprel": "det",
      "span": [
        0,
        3
      ],
      "lemma": "le",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "lettres",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 9,
      "deprel": "nsubj",
      "span": [
        4,
        11
      ],
      "lemma": "lettre",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "qu’",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 7,
      "deprel": "obj",
      "span": [
        12,
        15
      ],
      "lemma": "qu’",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "elle",
      "upos": "PRON",
      "feats": "Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "span": [
        15,
        19
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "s’",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs",
      "head": 7,
      "deprel": "iobj",
      "span": [
        20,
        22
      ],
      "lemma": "s’",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "est",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "span": [
        22,
        25
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "écrites",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part",
      "head": 2,
      "deprel": "acl:relcl",
      "span": [
        26,
        33
      ],
      "lemma": "écrire",
      "ner": "O"
    },
    {
      "id": 8,
      "text": "ont",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:tense",
      "span": [
        34,
        37
      ],
      "lemma": "avoir",
      "ner": "O"
    },
    {
      "id": 9,
      "text": "disparu",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "span": [
        38,
        45
      ],
      "lemma": "disparaître",
      "ner": "O"
    },
    {
      "id": 10,
      "text": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "span": [
        45,
        46
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 5. Unlabeled

Sentence: Ils se sont parlé, puis ils se sont revus.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| sont | être | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 4 | aux:tense |
| parlé | parler | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| sont | être | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 10 | aux:tense |
| revus | revoir | VERB | Gender=Masc\|Number=Plur\|Tense=Past\|VerbForm=Part | 4 | conj |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Ils | il | PRON | Gender=Masc\|Number=Plur\|Person=3\|PronType=Prs | 4 | nsubj |
| 2 | se | se | PRON | Person=3\|PronType=Prs | 4 | iobj |
| 3 | sont | être | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 4 | aux:tense |
| 4 | parlé | parler | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| 5 | , | , | PUNCT | _ | 10 | punct |
| 6 | puis | puis | ADV | _ | 10 | cc |
| 7 | ils | il | PRON | Gender=Masc\|Number=Plur\|Person=3\|PronType=Prs | 10 | nsubj |
| 8 | se | se | PRON | Person=3\|PronType=Prs | 10 | obj |
| 9 | sont | être | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 10 | aux:tense |
| 10 | revus | revoir | VERB | Gender=Masc\|Number=Plur\|Tense=Past\|VerbForm=Part | 4 | conj |
| 11 | . | . | PUNCT | _ | 4 | punct |

Raw Trankit output:

```json
{
  "text": "Ils se sont parlé, puis ils se sont revus.",
  "tokens": [
    {
      "id": 1,
      "text": "Ils",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Plur|Person=3|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "span": [
        0,
        3
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "se",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs",
      "head": 4,
      "deprel": "iobj",
      "span": [
        4,
        6
      ],
      "lemma": "se",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "sont",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "span": [
        7,
        11
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "parlé",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "span": [
        12,
        17
      ],
      "lemma": "parler",
      "ner": "O"
    },
    {
      "id": 5,
      "text": ",",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "span": [
        17,
        18
      ],
      "lemma": ",",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "puis",
      "upos": "ADV",
      "head": 10,
      "deprel": "cc",
      "span": [
        19,
        23
      ],
      "lemma": "puis",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "ils",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Plur|Person=3|PronType=Prs",
      "head": 10,
      "deprel": "nsubj",
      "span": [
        24,
        27
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 8,
      "text": "se",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs",
      "head": 10,
      "deprel": "obj",
      "span": [
        28,
        30
      ],
      "lemma": "se",
      "ner": "O"
    },
    {
      "id": 9,
      "text": "sont",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 10,
      "deprel": "aux:tense",
      "span": [
        31,
        35
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 10,
      "text": "revus",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part",
      "head": 4,
      "deprel": "conj",
      "span": [
        36,
        41
      ],
      "lemma": "revoir",
      "ner": "O"
    },
    {
      "id": 11,
      "text": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "span": [
        41,
        42
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 6. Unlabeled

Sentence: Il faut qu’elles soient revenues avant minuit.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| faut | falloir | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| soient | être | AUX | Mood=Sub\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 6 | aux:tense |
| revenues | revenir | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part | 2 | ccomp |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Il | il | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 2 | expl:subj |
| 2 | faut | falloir | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 3 | qu’ | qu’ | SCONJ | _ | 6 | mark |
| 4 | elles | il | PRON | Gender=Fem\|Number=Plur\|Person=3\|PronType=Prs | 6 | nsubj |
| 5 | soient | être | AUX | Mood=Sub\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 6 | aux:tense |
| 6 | revenues | revenir | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part | 2 | ccomp |
| 7 | avant | avant | ADP | _ | 8 | case |
| 8 | minuit | minuit | NOUN | Gender=Masc\|Number=Sing | 6 | obl |
| 9 | . | . | PUNCT | _ | 2 | punct |

Raw Trankit output:

```json
{
  "text": "Il faut qu’elles soient revenues avant minuit.",
  "tokens": [
    {
      "id": 1,
      "text": "Il",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 2,
      "deprel": "expl:subj",
      "span": [
        0,
        2
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "faut",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "span": [
        3,
        7
      ],
      "lemma": "falloir",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "qu’",
      "upos": "SCONJ",
      "head": 6,
      "deprel": "mark",
      "span": [
        8,
        11
      ],
      "lemma": "qu’",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "elles",
      "upos": "PRON",
      "feats": "Gender=Fem|Number=Plur|Person=3|PronType=Prs",
      "head": 6,
      "deprel": "nsubj",
      "span": [
        11,
        16
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "soient",
      "upos": "AUX",
      "feats": "Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 6,
      "deprel": "aux:tense",
      "span": [
        17,
        23
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "revenues",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part",
      "head": 2,
      "deprel": "ccomp",
      "span": [
        24,
        32
      ],
      "lemma": "revenir",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "avant",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "span": [
        33,
        38
      ],
      "lemma": "avant",
      "ner": "O"
    },
    {
      "id": 8,
      "text": "minuit",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 6,
      "deprel": "obl",
      "span": [
        39,
        45
      ],
      "lemma": "minuit",
      "ner": "O"
    },
    {
      "id": 9,
      "text": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "span": [
        45,
        46
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 7. Unlabeled

Sentence: Si elle avait su, elle ne serait pas venue.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| avait | avoir | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Imp\|VerbForm=Fin | 4 | aux:tense |
| su | savoir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 10 | advcl |
| serait | être | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 10 | aux:tense |
| venue | venir | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Si | si | SCONJ | _ | 4 | mark |
| 2 | elle | il | PRON | Gender=Fem\|Number=Sing\|Person=3\|PronType=Prs | 4 | nsubj |
| 3 | avait | avoir | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Imp\|VerbForm=Fin | 4 | aux:tense |
| 4 | su | savoir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 10 | advcl |
| 5 | , | , | PUNCT | _ | 4 | punct |
| 6 | elle | il | PRON | Gender=Fem\|Number=Sing\|Person=3\|PronType=Prs | 10 | nsubj |
| 7 | ne | ne | ADV | Polarity=Neg | 10 | advmod |
| 8 | serait | être | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 10 | aux:tense |
| 9 | pas | pas | ADV | Polarity=Neg | 10 | advmod |
| 10 | venue | venir | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| 11 | . | . | PUNCT | _ | 10 | punct |

Raw Trankit output:

```json
{
  "text": "Si elle avait su, elle ne serait pas venue.",
  "tokens": [
    {
      "id": 1,
      "text": "Si",
      "upos": "SCONJ",
      "head": 4,
      "deprel": "mark",
      "span": [
        0,
        2
      ],
      "lemma": "si",
      "ner": "S-MISC"
    },
    {
      "id": 2,
      "text": "elle",
      "upos": "PRON",
      "feats": "Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "span": [
        3,
        7
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "avait",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "span": [
        8,
        13
      ],
      "lemma": "avoir",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "su",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 10,
      "deprel": "advcl",
      "span": [
        14,
        16
      ],
      "lemma": "savoir",
      "ner": "O"
    },
    {
      "id": 5,
      "text": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "span": [
        16,
        17
      ],
      "lemma": ",",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "elle",
      "upos": "PRON",
      "feats": "Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 10,
      "deprel": "nsubj",
      "span": [
        18,
        22
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 10,
      "deprel": "advmod",
      "span": [
        23,
        25
      ],
      "lemma": "ne",
      "ner": "O"
    },
    {
      "id": 8,
      "text": "serait",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 10,
      "deprel": "aux:tense",
      "span": [
        26,
        32
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 9,
      "text": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 10,
      "deprel": "advmod",
      "span": [
        33,
        36
      ],
      "lemma": "pas",
      "ner": "O"
    },
    {
      "id": 10,
      "text": "venue",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "span": [
        37,
        42
      ],
      "lemma": "venir",
      "ner": "O"
    },
    {
      "id": 11,
      "text": ".",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "span": [
        42,
        43
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 8. Unlabeled

Sentence: Quand il aura fini, nous commencerons sans lui.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| aura | avoir | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Fut\|VerbForm=Fin | 4 | aux:tense |
| fini | finir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 7 | advcl |
| commencerons | commencer | VERB | Mood=Ind\|Number=Plur\|Person=1\|Tense=Fut\|VerbForm=Fin | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Quand | quand | SCONJ | _ | 4 | mark |
| 2 | il | il | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 4 | nsubj |
| 3 | aura | avoir | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Fut\|VerbForm=Fin | 4 | aux:tense |
| 4 | fini | finir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 7 | advcl |
| 5 | , | , | PUNCT | _ | 4 | punct |
| 6 | nous | il | PRON | Number=Plur\|Person=1\|PronType=Prs | 7 | nsubj |
| 7 | commencerons | commencer | VERB | Mood=Ind\|Number=Plur\|Person=1\|Tense=Fut\|VerbForm=Fin | 0 | root |
| 8 | sans | sans | ADP | _ | 9 | case |
| 9 | lui | lui | PRON | Number=Sing\|Person=3\|PronType=Prs | 7 | obl |
| 10 | . | . | PUNCT | _ | 7 | punct |

Raw Trankit output:

```json
{
  "text": "Quand il aura fini, nous commencerons sans lui.",
  "tokens": [
    {
      "id": 1,
      "text": "Quand",
      "upos": "SCONJ",
      "head": 4,
      "deprel": "mark",
      "span": [
        0,
        5
      ],
      "lemma": "quand",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "il",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "span": [
        6,
        8
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "aura",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "span": [
        9,
        13
      ],
      "lemma": "avoir",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "fini",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 7,
      "deprel": "advcl",
      "span": [
        14,
        18
      ],
      "lemma": "finir",
      "ner": "O"
    },
    {
      "id": 5,
      "text": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "span": [
        18,
        19
      ],
      "lemma": ",",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "nous",
      "upos": "PRON",
      "feats": "Number=Plur|Person=1|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "span": [
        20,
        24
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "commencerons",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "span": [
        25,
        37
      ],
      "lemma": "commencer",
      "ner": "O"
    },
    {
      "id": 8,
      "text": "sans",
      "upos": "ADP",
      "head": 9,
      "deprel": "case",
      "span": [
        38,
        42
      ],
      "lemma": "sans",
      "ner": "O"
    },
    {
      "id": 9,
      "text": "lui",
      "upos": "PRON",
      "feats": "Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "obl",
      "span": [
        43,
        46
      ],
      "lemma": "lui",
      "ner": "O"
    },
    {
      "id": 10,
      "text": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "span": [
        46,
        47
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 9. Unlabeled

Sentence: Eussiez-vous accepté, tout aurait été différent.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| Eussiez-vous | Eussiet-ver | AUX | Number=Plur\|Person=2\|PronType=Prs | 2 | aux:tense |
| accepté | accepter | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| aurait | avoir | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 7 | aux:tense |
| été | être | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 7 | cop |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Eussiez-vous | Eussiet-ver | AUX | Number=Plur\|Person=2\|PronType=Prs | 2 | aux:tense |
| 2 | accepté | accepter | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| 3 | , | , | PUNCT | _ | 7 | punct |
| 4 | tout | tout | PRON | Gender=Masc\|Number=Sing | 7 | nsubj |
| 5 | aurait | avoir | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 7 | aux:tense |
| 6 | été | être | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 7 | cop |
| 7 | différent | différent | ADJ | Gender=Masc\|Number=Sing | 2 | conj |
| 8 | . | . | PUNCT | _ | 2 | punct |

Raw Trankit output:

```json
{
  "text": "Eussiez-vous accepté, tout aurait été différent.",
  "tokens": [
    {
      "id": 1,
      "text": "Eussiez-vous",
      "upos": "AUX",
      "feats": "Number=Plur|Person=2|PronType=Prs",
      "head": 2,
      "deprel": "aux:tense",
      "span": [
        0,
        12
      ],
      "lemma": "Eussiet-ver",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "accepté",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "span": [
        13,
        20
      ],
      "lemma": "accepter",
      "ner": "O"
    },
    {
      "id": 3,
      "text": ",",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "span": [
        20,
        21
      ],
      "lemma": ",",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "tout",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "nsubj",
      "span": [
        22,
        26
      ],
      "lemma": "tout",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "aurait",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "span": [
        27,
        33
      ],
      "lemma": "avoir",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "été",
      "upos": "AUX",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 7,
      "deprel": "cop",
      "span": [
        34,
        37
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "différent",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 2,
      "deprel": "conj",
      "span": [
        38,
        47
      ],
      "lemma": "différent",
      "ner": "O"
    },
    {
      "id": 8,
      "text": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "span": [
        47,
        48
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 10. Unlabeled

Sentence: Leurs décisions ont été contestées puis annulées.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| ont | avoir | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:tense |
| été | être | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 5 | aux:pass |
| contestées | contester | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part | 0 | root |
| annulées | annuler | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part | 5 | conj |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Leurs | son | DET | Gender=Fem\|Number=Plur\|Poss=Yes\|PronType=Prs | 2 | det |
| 2 | décisions | décision | NOUN | Gender=Fem\|Number=Plur | 5 | nsubj:pass |
| 3 | ont | avoir | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:tense |
| 4 | été | être | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 5 | aux:pass |
| 5 | contestées | contester | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part | 0 | root |
| 6 | puis | puis | ADV | _ | 7 | cc |
| 7 | annulées | annuler | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part | 5 | conj |
| 8 | . | . | PUNCT | _ | 5 | punct |

Raw Trankit output:

```json
{
  "text": "Leurs décisions ont été contestées puis annulées.",
  "tokens": [
    {
      "id": 1,
      "text": "Leurs",
      "upos": "DET",
      "feats": "Gender=Fem|Number=Plur|Poss=Yes|PronType=Prs",
      "head": 2,
      "deprel": "det",
      "span": [
        0,
        5
      ],
      "lemma": "son",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "décisions",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 5,
      "deprel": "nsubj:pass",
      "span": [
        6,
        15
      ],
      "lemma": "décision",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "ont",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "span": [
        16,
        19
      ],
      "lemma": "avoir",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "été",
      "upos": "AUX",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 5,
      "deprel": "aux:pass",
      "span": [
        20,
        23
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "contestées",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "span": [
        24,
        34
      ],
      "lemma": "contester",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "puis",
      "upos": "ADV",
      "head": 7,
      "deprel": "cc",
      "span": [
        35,
        39
      ],
      "lemma": "puis",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "annulées",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part",
      "head": 5,
      "deprel": "conj",
      "span": [
        40,
        48
      ],
      "lemma": "annuler",
      "ner": "O"
    },
    {
      "id": 8,
      "text": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "span": [
        48,
        49
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 11. Unlabeled

Sentence: Cette maison s’est vendue très vite.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:tense |
| vendue | vendre | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Cette | ce | DET | Gender=Fem\|Number=Sing\|PronType=Dem | 2 | det |
| 2 | maison | maison | NOUN | Gender=Fem\|Number=Sing | 5 | nsubj |
| 3 | s’ | s’ | PRON | Person=3\|PronType=Prs | 5 | expl:pass |
| 4 | est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:tense |
| 5 | vendue | vendre | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| 6 | très | très | ADV | _ | 7 | advmod |
| 7 | vite. | vite. | ADV | _ | 5 | advmod |

Raw Trankit output:

```json
{
  "text": "Cette maison s’est vendue très vite.",
  "tokens": [
    {
      "id": 1,
      "text": "Cette",
      "upos": "DET",
      "feats": "Gender=Fem|Number=Sing|PronType=Dem",
      "head": 2,
      "deprel": "det",
      "span": [
        0,
        5
      ],
      "lemma": "ce",
      "ner": "S-LOC"
    },
    {
      "id": 2,
      "text": "maison",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "nsubj",
      "span": [
        6,
        12
      ],
      "lemma": "maison",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "s’",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs",
      "head": 5,
      "deprel": "expl:pass",
      "span": [
        13,
        15
      ],
      "lemma": "s’",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "est",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "span": [
        15,
        18
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "vendue",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "span": [
        19,
        25
      ],
      "lemma": "vendre",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "très",
      "upos": "ADV",
      "head": 7,
      "deprel": "advmod",
      "span": [
        26,
        30
      ],
      "lemma": "très",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "vite.",
      "upos": "ADV",
      "head": 5,
      "deprel": "advmod",
      "span": [
        31,
        36
      ],
      "lemma": "vite.",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 12. Unlabeled

Sentence: Il paraît qu’elle l’aurait vu hier.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| paraît | paraître | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| aurait | avoir | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 7 | aux:tense |
| vu | voir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 2 | ccomp |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Il | il | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 2 | expl:subj |
| 2 | paraît | paraître | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 3 | qu’ | qu’ | SCONJ | _ | 7 | mark |
| 4 | elle | il | PRON | Gender=Fem\|Number=Sing\|Person=3\|PronType=Prs | 7 | nsubj |
| 5 | l’ | le | PRON | Number=Sing\|Person=3\|PronType=Prs | 7 | obj |
| 6 | aurait | avoir | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 7 | aux:tense |
| 7 | vu | voir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 2 | ccomp |
| 8 | hier | hier | ADV | _ | 7 | advmod |
| 9 | . | . | PUNCT | _ | 2 | punct |

Raw Trankit output:

```json
{
  "text": "Il paraît qu’elle l’aurait vu hier.",
  "tokens": [
    {
      "id": 1,
      "text": "Il",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 2,
      "deprel": "expl:subj",
      "span": [
        0,
        2
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "paraît",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "span": [
        3,
        9
      ],
      "lemma": "paraître",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "qu’",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "span": [
        10,
        13
      ],
      "lemma": "qu’",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "elle",
      "upos": "PRON",
      "feats": "Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "span": [
        13,
        17
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "l’",
      "upos": "PRON",
      "feats": "Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "obj",
      "span": [
        18,
        20
      ],
      "lemma": "le",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "aurait",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "span": [
        20,
        26
      ],
      "lemma": "avoir",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "vu",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 2,
      "deprel": "ccomp",
      "span": [
        27,
        29
      ],
      "lemma": "voir",
      "ner": "O"
    },
    {
      "id": 8,
      "text": "hier",
      "upos": "ADV",
      "head": 7,
      "deprel": "advmod",
      "span": [
        30,
        34
      ],
      "lemma": "hier",
      "ner": "O"
    },
    {
      "id": 9,
      "text": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "span": [
        34,
        35
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 13. Unlabeled

Sentence: Le livre que j’ai laissé tomber est abîmé.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| ai | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 6 | aux:tense |
| laissé | laisser | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 2 | acl:relcl |
| tomber | tomber | VERB | VerbForm=Inf | 6 | xcomp |
| est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | aux:tense |
| abîmé | abîmer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Le | le | DET | Definite=Def\|Gender=Masc\|Number=Sing\|PronType=Art | 2 | det |
| 2 | livre | livre | NOUN | Gender=Masc\|Number=Sing | 9 | nsubj |
| 3 | que | que | PRON | PronType=Rel | 6 | obj |
| 4 | j’ | il | PRON | Number=Sing\|Person=1\|PronType=Prs | 6 | nsubj |
| 5 | ai | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 6 | aux:tense |
| 6 | laissé | laisser | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 2 | acl:relcl |
| 7 | tomber | tomber | VERB | VerbForm=Inf | 6 | xcomp |
| 8 | est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | aux:tense |
| 9 | abîmé | abîmer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| 10 | . | . | PUNCT | _ | 9 | punct |

Raw Trankit output:

```json
{
  "text": "Le livre que j’ai laissé tomber est abîmé.",
  "tokens": [
    {
      "id": 1,
      "text": "Le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 2,
      "deprel": "det",
      "span": [
        0,
        2
      ],
      "lemma": "le",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "livre",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "nsubj",
      "span": [
        3,
        8
      ],
      "lemma": "livre",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 6,
      "deprel": "obj",
      "span": [
        9,
        12
      ],
      "lemma": "que",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "j’",
      "upos": "PRON",
      "feats": "Number=Sing|Person=1|PronType=Prs",
      "head": 6,
      "deprel": "nsubj",
      "span": [
        13,
        15
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "ai",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 6,
      "deprel": "aux:tense",
      "span": [
        15,
        17
      ],
      "lemma": "avoir",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "laissé",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 2,
      "deprel": "acl:relcl",
      "span": [
        18,
        24
      ],
      "lemma": "laisser",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "tomber",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 6,
      "deprel": "xcomp",
      "span": [
        25,
        31
      ],
      "lemma": "tomber",
      "ner": "O"
    },
    {
      "id": 8,
      "text": "est",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:tense",
      "span": [
        32,
        35
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 9,
      "text": "abîmé",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "span": [
        36,
        41
      ],
      "lemma": "abîmer",
      "ner": "O"
    },
    {
      "id": 10,
      "text": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "span": [
        41,
        42
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 14. Unlabeled

Sentence: Encore faut-il qu’on puisse le prouver.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| faut | falloir | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| puisse | pouvoir | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 2 | ccomp |
| prouver | prouver | VERB | VerbForm=Inf | 6 | xcomp |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Encore | encore | ADV | _ | 2 | advmod |
| 2 | faut | falloir | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 3 | -il | il | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 2 | nsubj |
| 4 | qu’ | qu’ | SCONJ | _ | 6 | mark |
| 5 | on | on | PRON | Gender=Masc\|Number=Sing\|Person=3 | 6 | nsubj |
| 6 | puisse | pouvoir | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 2 | ccomp |
| 7 | le | le | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 8 | obj |
| 8 | prouver | prouver | VERB | VerbForm=Inf | 6 | xcomp |
| 9 | . | . | PUNCT | _ | 2 | punct |

Raw Trankit output:

```json
{
  "text": "Encore faut-il qu’on puisse le prouver.",
  "tokens": [
    {
      "id": 1,
      "text": "Encore",
      "upos": "ADV",
      "head": 2,
      "deprel": "advmod",
      "span": [
        0,
        6
      ],
      "lemma": "encore",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "faut",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "span": [
        7,
        11
      ],
      "lemma": "falloir",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "-il",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 2,
      "deprel": "nsubj",
      "span": [
        11,
        14
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "qu’",
      "upos": "SCONJ",
      "head": 6,
      "deprel": "mark",
      "span": [
        15,
        18
      ],
      "lemma": "qu’",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "on",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3",
      "head": 6,
      "deprel": "nsubj",
      "span": [
        18,
        20
      ],
      "lemma": "on",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "puisse",
      "upos": "VERB",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "ccomp",
      "span": [
        21,
        27
      ],
      "lemma": "pouvoir",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "le",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 8,
      "deprel": "obj",
      "span": [
        28,
        30
      ],
      "lemma": "le",
      "ner": "O"
    },
    {
      "id": 8,
      "text": "prouver",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 6,
      "deprel": "xcomp",
      "span": [
        31,
        38
      ],
      "lemma": "prouver",
      "ner": "O"
    },
    {
      "id": 9,
      "text": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "span": [
        38,
        39
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 15. Unlabeled

Sentence: Rentré trop tard, il s’est fait gronder par sa mère.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| Rentré | rentrer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 9 | advcl |
| est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | aux:tense |
| fait | faire | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 9 | aux:caus |
| gronder | gronder | VERB | VerbForm=Inf | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Rentré | rentrer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 9 | advcl |
| 2 | trop | trop | ADV | _ | 3 | advmod |
| 3 | tard | tard | ADV | _ | 1 | advmod |
| 4 | , | , | PUNCT | _ | 1 | punct |
| 5 | il | il | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 9 | nsubj:caus |
| 6 | s’ | s’ | PRON | Person=3\|PronType=Prs | 9 | obj |
| 7 | est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | aux:tense |
| 8 | fait | faire | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 9 | aux:caus |
| 9 | gronder | gronder | VERB | VerbForm=Inf | 0 | root |
| 10 | par | par | ADP | _ | 12 | case |
| 11 | sa | son | DET | Gender=Fem\|Number=Sing\|Poss=Yes\|PronType=Prs | 12 | det |
| 12 | mère | mère | NOUN | Gender=Fem\|Number=Sing | 9 | obl:agent |
| 13 | . | . | PUNCT | _ | 9 | punct |

Raw Trankit output:

```json
{
  "text": "Rentré trop tard, il s’est fait gronder par sa mère.",
  "tokens": [
    {
      "id": 1,
      "text": "Rentré",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 9,
      "deprel": "advcl",
      "span": [
        0,
        6
      ],
      "lemma": "rentrer",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "trop",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "span": [
        7,
        11
      ],
      "lemma": "trop",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "tard",
      "upos": "ADV",
      "head": 1,
      "deprel": "advmod",
      "span": [
        12,
        16
      ],
      "lemma": "tard",
      "ner": "O"
    },
    {
      "id": 4,
      "text": ",",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "span": [
        16,
        17
      ],
      "lemma": ",",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "il",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "nsubj:caus",
      "span": [
        18,
        20
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "s’",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs",
      "head": 9,
      "deprel": "obj",
      "span": [
        21,
        23
      ],
      "lemma": "s’",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "est",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:tense",
      "span": [
        23,
        26
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 8,
      "text": "fait",
      "upos": "AUX",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 9,
      "deprel": "aux:caus",
      "span": [
        27,
        31
      ],
      "lemma": "faire",
      "ner": "O"
    },
    {
      "id": 9,
      "text": "gronder",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 0,
      "deprel": "root",
      "span": [
        32,
        39
      ],
      "lemma": "gronder",
      "ner": "O"
    },
    {
      "id": 10,
      "text": "par",
      "upos": "ADP",
      "head": 12,
      "deprel": "case",
      "span": [
        40,
        43
      ],
      "lemma": "par",
      "ner": "O"
    },
    {
      "id": 11,
      "text": "sa",
      "upos": "DET",
      "feats": "Gender=Fem|Number=Sing|Poss=Yes|PronType=Prs",
      "head": 12,
      "deprel": "det",
      "span": [
        44,
        46
      ],
      "lemma": "son",
      "ner": "O"
    },
    {
      "id": 12,
      "text": "mère",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 9,
      "deprel": "obl:agent",
      "span": [
        47,
        51
      ],
      "lemma": "mère",
      "ner": "O"
    },
    {
      "id": 13,
      "text": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "span": [
        51,
        52
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```
