# French Trankit Report for idea.md Sentences

Generated from real Trankit output using the sentences listed in `idea.md`.

## 1. 直陈现在

Sentence: Il chante tous les jours.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| chante | chanter | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Il | il | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 2 | nsubj |
| 2 | chante | chanter | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 3 | tous | tout | ADJ | Gender=Masc\|Number=Plur | 5 | amod |
| 4 | les | le | DET | Definite=Def\|Gender=Masc\|Number=Plur\|PronType=Art | 5 | det |
| 5 | jours | jour | NOUN | Gender=Masc\|Number=Plur | 2 | obl |
| 6 | . | . | PUNCT | _ | 2 | punct |

Raw Trankit output:

```json
{
  "text": "Il chante tous les jours.",
  "tokens": [
    {
      "id": 1,
      "text": "Il",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 2,
      "deprel": "nsubj",
      "span": [
        0,
        2
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "chante",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "span": [
        3,
        9
      ],
      "lemma": "chanter",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "tous",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Plur",
      "head": 5,
      "deprel": "amod",
      "span": [
        10,
        14
      ],
      "lemma": "tout",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "les",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Plur|PronType=Art",
      "head": 5,
      "deprel": "det",
      "span": [
        15,
        18
      ],
      "lemma": "le",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "jours",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 2,
      "deprel": "obl",
      "span": [
        19,
        24
      ],
      "lemma": "jour",
      "ner": "O"
    },
    {
      "id": 6,
      "text": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "span": [
        24,
        25
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 2. 虚拟现在，与上句同形

Sentence: Il faut qu'il chante.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| faut | falloir | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| chante | chanter | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 2 | ccomp |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Il | il | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 2 | expl:subj |
| 2 | faut | falloir | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 3 | qu' | que | SCONJ | _ | 5 | mark |
| 4 | il | il | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 5 | nsubj |
| 5 | chante | chanter | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 2 | ccomp |
| 6 | . | . | PUNCT | _ | 2 | punct |

Raw Trankit output:

```json
{
  "text": "Il faut qu'il chante.",
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
      "text": "qu'",
      "upos": "SCONJ",
      "head": 5,
      "deprel": "mark",
      "span": [
        8,
        11
      ],
      "lemma": "que",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "il",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "span": [
        11,
        13
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "chante",
      "upos": "VERB",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "ccomp",
      "span": [
        14,
        20
      ],
      "lemma": "chanter",
      "ner": "O"
    },
    {
      "id": 6,
      "text": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "span": [
        20,
        21
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 3. 命令式，与直陈同形

Sentence: Finis ton repas !

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| Finis | finir | VERB | Mood=Imp\|Number=Sing\|Person=2\|Tense=Pres\|VerbForm=Fin | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Finis | finir | VERB | Mood=Imp\|Number=Sing\|Person=2\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 2 | ton | son | DET | Gender=Masc\|Number=Sing\|Poss=Yes\|PronType=Prs | 3 | det |
| 3 | repas | repas | NOUN | Gender=Masc\|Number=Sing | 1 | obj |
| 4 | ! | ! | PUNCT | _ | 1 | punct |

Raw Trankit output:

```json
{
  "text": "Finis ton repas !",
  "tokens": [
    {
      "id": 1,
      "text": "Finis",
      "upos": "VERB",
      "feats": "Mood=Imp|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "span": [
        0,
        5
      ],
      "lemma": "finir",
      "ner": "S-MISC"
    },
    {
      "id": 2,
      "text": "ton",
      "upos": "DET",
      "feats": "Gender=Masc|Number=Sing|Poss=Yes|PronType=Prs",
      "head": 3,
      "deprel": "det",
      "span": [
        6,
        9
      ],
      "lemma": "son",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "repas",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 1,
      "deprel": "obj",
      "span": [
        10,
        15
      ],
      "lemma": "repas",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "!",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "span": [
        16,
        17
      ],
      "lemma": "!",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 4. 过去完成 + 虚拟

Sentence: J'avais mangé avant qu'il arrive.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| avais | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Imp\|VerbForm=Fin | 3 | aux:tense |
| mangé | manger | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| arrive | arriver | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 3 | advcl |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | J' | il | PRON | Number=Sing\|Person=1\|PronType=Prs | 3 | nsubj |
| 2 | avais | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Imp\|VerbForm=Fin | 3 | aux:tense |
| 3 | mangé | manger | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| 4 | avant | avant | ADP | _ | 7 | mark |
| 5 | qu' | que | SCONJ | _ | 7 | mark |
| 6 | il | il | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 7 | nsubj |
| 7 | arrive | arriver | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 3 | advcl |
| 8 | . | . | PUNCT | _ | 3 | punct |

Raw Trankit output:

```json
{
  "text": "J'avais mangé avant qu'il arrive.",
  "tokens": [
    {
      "id": 1,
      "text": "J'",
      "upos": "PRON",
      "feats": "Number=Sing|Person=1|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "span": [
        0,
        2
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "avais",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "span": [
        2,
        7
      ],
      "lemma": "avoir",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "mangé",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "span": [
        8,
        13
      ],
      "lemma": "manger",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "avant",
      "upos": "ADP",
      "head": 7,
      "deprel": "mark",
      "span": [
        14,
        19
      ],
      "lemma": "avant",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "qu'",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "span": [
        20,
        23
      ],
      "lemma": "que",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "il",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "span": [
        23,
        25
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "arrive",
      "upos": "VERB",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "advcl",
      "span": [
        26,
        32
      ],
      "lemma": "arriver",
      "ner": "O"
    },
    {
      "id": 8,
      "text": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "span": [
        32,
        33
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 5. 将来完成

Sentence: J'aurai fini avant midi.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| aurai | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Fut\|VerbForm=Fin | 3 | aux:tense |
| fini | finir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | J' | il | PRON | Number=Sing\|Person=1\|PronType=Prs | 3 | nsubj |
| 2 | aurai | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Fut\|VerbForm=Fin | 3 | aux:tense |
| 3 | fini | finir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| 4 | avant | avant | ADP | _ | 5 | case |
| 5 | midi | midi | NOUN | Gender=Masc\|Number=Sing | 3 | obl |
| 6 | . | . | PUNCT | _ | 3 | punct |

Raw Trankit output:

```json
{
  "text": "J'aurai fini avant midi.",
  "tokens": [
    {
      "id": 1,
      "text": "J'",
      "upos": "PRON",
      "feats": "Number=Sing|Person=1|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "span": [
        0,
        2
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "aurai",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "span": [
        2,
        7
      ],
      "lemma": "avoir",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "fini",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "span": [
        8,
        12
      ],
      "lemma": "finir",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "avant",
      "upos": "ADP",
      "head": 5,
      "deprel": "case",
      "span": [
        13,
        18
      ],
      "lemma": "avant",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "midi",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "obl",
      "span": [
        19,
        23
      ],
      "lemma": "midi",
      "ner": "O"
    },
    {
      "id": 6,
      "text": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "span": [
        23,
        24
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 6. 条件完成

Sentence: J'aurais voyagé si j'avais eu de l'argent.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| aurais | avoir | AUX | Mood=Cnd\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 3 | aux:tense |
| voyagé | voyager | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| avais | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Imp\|VerbForm=Fin | 7 | aux:tense |
| eu | avoir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 3 | advcl |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | J' | il | PRON | Number=Sing\|Person=1\|PronType=Prs | 3 | nsubj |
| 2 | aurais | avoir | AUX | Mood=Cnd\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 3 | aux:tense |
| 3 | voyagé | voyager | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| 4 | si | si | SCONJ | _ | 7 | mark |
| 5 | j' | il | PRON | Number=Sing\|Person=1\|PronType=Prs | 7 | nsubj |
| 6 | avais | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Imp\|VerbForm=Fin | 7 | aux:tense |
| 7 | eu | avoir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 3 | advcl |
| 8 | de | de | ADP | _ | 10 | det |
| 9 | l' | le | DET | Definite=Def\|Gender=Masc\|Number=Sing\|PronType=Art | 8 | fixed |
| 10 | argent | argent | NOUN | Gender=Masc\|Number=Sing | 7 | obj |
| 11 | . | . | PUNCT | _ | 3 | punct |

Raw Trankit output:

```json
{
  "text": "J'aurais voyagé si j'avais eu de l'argent.",
  "tokens": [
    {
      "id": 1,
      "text": "J'",
      "upos": "PRON",
      "feats": "Number=Sing|Person=1|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "span": [
        0,
        2
      ],
      "lemma": "il",
      "ner": "S-ORG"
    },
    {
      "id": 2,
      "text": "aurais",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "span": [
        2,
        8
      ],
      "lemma": "avoir",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "voyagé",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "span": [
        9,
        15
      ],
      "lemma": "voyager",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "si",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "span": [
        16,
        18
      ],
      "lemma": "si",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "j'",
      "upos": "PRON",
      "feats": "Number=Sing|Person=1|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "span": [
        19,
        21
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "avais",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "span": [
        21,
        26
      ],
      "lemma": "avoir",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "eu",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 3,
      "deprel": "advcl",
      "span": [
        27,
        29
      ],
      "lemma": "avoir",
      "ner": "O"
    },
    {
      "id": 8,
      "text": "de",
      "upos": "ADP",
      "head": 10,
      "deprel": "det",
      "span": [
        30,
        32
      ],
      "lemma": "de",
      "ner": "O"
    },
    {
      "id": 9,
      "text": "l'",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "fixed",
      "span": [
        33,
        35
      ],
      "lemma": "le",
      "ner": "O"
    },
    {
      "id": 10,
      "text": "argent",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "obj",
      "span": [
        35,
        41
      ],
      "lemma": "argent",
      "ner": "O"
    },
    {
      "id": 11,
      "text": ".",
      "upos": "PUNCT",
      "head": 3,
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

## 7. être + 过去分词，测试性数配合

Sentence: Elle est partie hier soir.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 3 | cop |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Elle | il | PRON | Gender=Fem\|Number=Sing\|Person=3\|PronType=Prs | 3 | nsubj |
| 2 | est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 3 | cop |
| 3 | partie | partie | NOUN | Gender=Fem\|Number=Sing | 0 | root |
| 4 | hier | hier | ADV | _ | 3 | advmod |
| 5 | soir | soir | NOUN | Gender=Masc\|Number=Sing | 4 | obl |
| 6 | . | . | PUNCT | _ | 3 | punct |

Raw Trankit output:

```json
{
  "text": "Elle est partie hier soir.",
  "tokens": [
    {
      "id": 1,
      "text": "Elle",
      "upos": "PRON",
      "feats": "Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "span": [
        0,
        4
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "est",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "cop",
      "span": [
        5,
        8
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "partie",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 0,
      "deprel": "root",
      "span": [
        9,
        15
      ],
      "lemma": "partie",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "hier",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "span": [
        16,
        20
      ],
      "lemma": "hier",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "soir",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obl",
      "span": [
        21,
        25
      ],
      "lemma": "soir",
      "ner": "O"
    },
    {
      "id": 6,
      "text": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "span": [
        25,
        26
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 8. 代词式动词

Sentence: Je me suis levé tôt.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| suis | être | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 4 | aux:tense |
| levé | lever | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Je | il | PRON | Number=Sing\|Person=1\|PronType=Prs | 4 | nsubj |
| 2 | me | se | PRON | Number=Sing\|Person=1\|PronType=Prs | 4 | obj |
| 3 | suis | être | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 4 | aux:tense |
| 4 | levé | lever | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| 5 | tôt | tôt | ADV | _ | 4 | advmod |
| 6 | . | . | PUNCT | _ | 4 | punct |

Raw Trankit output:

```json
{
  "text": "Je me suis levé tôt.",
  "tokens": [
    {
      "id": 1,
      "text": "Je",
      "upos": "PRON",
      "feats": "Number=Sing|Person=1|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "span": [
        0,
        2
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "me",
      "upos": "PRON",
      "feats": "Number=Sing|Person=1|PronType=Prs",
      "head": 4,
      "deprel": "obj",
      "span": [
        3,
        5
      ],
      "lemma": "se",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "suis",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "span": [
        6,
        10
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "levé",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "span": [
        11,
        15
      ],
      "lemma": "lever",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "tôt",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "span": [
        16,
        19
      ],
      "lemma": "tôt",
      "ner": "O"
    },
    {
      "id": 6,
      "text": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "span": [
        19,
        20
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 9. 被动语态

Sentence: La lettre a été écrite par Marie.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| a | avoir | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:tense |
| été | être | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 5 | aux:pass |
| écrite | écrire | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | La | le | DET | Definite=Def\|Gender=Fem\|Number=Sing\|PronType=Art | 2 | det |
| 2 | lettre | lettre | NOUN | Gender=Fem\|Number=Sing | 5 | nsubj:pass |
| 3 | a | avoir | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:tense |
| 4 | été | être | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 5 | aux:pass |
| 5 | écrite | écrire | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part | 0 | root |
| 6 | par | par | ADP | _ | 7 | case |
| 7 | Marie | Marie | PROPN | _ | 5 | obl:agent |
| 8 | . | . | PUNCT | _ | 5 | punct |

Raw Trankit output:

```json
{
  "text": "La lettre a été écrite par Marie.",
  "tokens": [
    {
      "id": 1,
      "text": "La",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
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
      "text": "lettre",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "nsubj:pass",
      "span": [
        3,
        9
      ],
      "lemma": "lettre",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "a",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "span": [
        10,
        11
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
        12,
        15
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "écrite",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "span": [
        16,
        22
      ],
      "lemma": "écrire",
      "ner": "O"
    },
    {
      "id": 6,
      "text": "par",
      "upos": "ADP",
      "head": 7,
      "deprel": "case",
      "span": [
        23,
        26
      ],
      "lemma": "par",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "Marie",
      "upos": "PROPN",
      "head": 5,
      "deprel": "obl:agent",
      "span": [
        27,
        32
      ],
      "lemma": "Marie",
      "ner": "S-MISC"
    },
    {
      "id": 8,
      "text": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "span": [
        32,
        33
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```

## 10. être 的虚拟式，形式有别于直陈

Sentence: Bien qu'il soit fatigué, il travaille.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| soit | être | AUX | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:tense |
| fatigué | fatiguer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 8 | advcl |
| travaille | travailler | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Bien | bien | ADV | _ | 5 | mark |
| 2 | qu' | que | SCONJ | _ | 1 | fixed |
| 3 | il | il | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 5 | nsubj |
| 4 | soit | être | AUX | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:tense |
| 5 | fatigué | fatiguer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 8 | advcl |
| 6 | , | , | PUNCT | _ | 5 | punct |
| 7 | il | il | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 8 | nsubj |
| 8 | travaille | travailler | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 9 | . | . | PUNCT | _ | 8 | punct |

Raw Trankit output:

```json
{
  "text": "Bien qu'il soit fatigué, il travaille.",
  "tokens": [
    {
      "id": 1,
      "text": "Bien",
      "upos": "ADV",
      "head": 5,
      "deprel": "mark",
      "span": [
        0,
        4
      ],
      "lemma": "bien",
      "ner": "O"
    },
    {
      "id": 2,
      "text": "qu'",
      "upos": "SCONJ",
      "head": 1,
      "deprel": "fixed",
      "span": [
        5,
        8
      ],
      "lemma": "que",
      "ner": "O"
    },
    {
      "id": 3,
      "text": "il",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "span": [
        8,
        10
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 4,
      "text": "soit",
      "upos": "AUX",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "span": [
        11,
        15
      ],
      "lemma": "être",
      "ner": "O"
    },
    {
      "id": 5,
      "text": "fatigué",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 8,
      "deprel": "advcl",
      "span": [
        16,
        23
      ],
      "lemma": "fatiguer",
      "ner": "O"
    },
    {
      "id": 6,
      "text": ",",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "span": [
        23,
        24
      ],
      "lemma": ",",
      "ner": "O"
    },
    {
      "id": 7,
      "text": "il",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 8,
      "deprel": "nsubj",
      "span": [
        25,
        27
      ],
      "lemma": "il",
      "ner": "O"
    },
    {
      "id": 8,
      "text": "travaille",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "span": [
        28,
        37
      ],
      "lemma": "travailler",
      "ner": "O"
    },
    {
      "id": 9,
      "text": ".",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "span": [
        37,
        38
      ],
      "lemma": ".",
      "ner": "O"
    }
  ],
  "lang": "french"
}
```
