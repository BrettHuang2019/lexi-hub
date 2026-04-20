# French Stanza Report for idea.md Sentences

Generated from real Stanza `Document.to_dict()` output using the sentences listed in `idea.md`.

## 1. 直陈现在

Sentence: Il chante tous les jours.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| chante | chanter | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Il | lui | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 2 | nsubj |
| 2 | chante | chanter | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 3 | tous | tout | ADJ | Gender=Masc\|Number=Plur | 5 | amod |
| 4 | les | le | DET | Definite=Def\|Number=Plur\|PronType=Art | 5 | det |
| 5 | jours | jour | NOUN | Gender=Masc\|Number=Plur | 2 | obl:mod |
| 6 | . | . | PUNCT | _ | 2 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "chante",
      "lemma": "chanter",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "tous",
      "lemma": "tout",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Plur",
      "head": 5,
      "deprel": "amod",
      "start_char": 10,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 15,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "jours",
      "lemma": "jour",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 2,
      "deprel": "obl:mod",
      "start_char": 19,
      "end_char": 24,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 24,
      "end_char": 25,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 2. 虚拟现在，与上句同形

Sentence: Il faut qu'il chante.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| faut | falloir | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| chante | chanter | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 2 | ccomp |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Il | lui | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 2 | expl:subj |
| 2 | faut | falloir | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 3 | qu' | que | SCONJ | _ | 5 | mark |
| 4 | il | lui | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 5 | nsubj |
| 5 | chante | chanter | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 2 | ccomp |
| 6 | . | . | PUNCT | _ | 2 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 2,
      "deprel": "expl:subj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "faut",
      "lemma": "falloir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 5,
      "deprel": "mark",
      "start_char": 8,
      "end_char": 11,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 11,
      "end_char": 13
    },
    {
      "id": 5,
      "text": "chante",
      "lemma": "chanter",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "ccomp",
      "start_char": 14,
      "end_char": 20,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 20,
      "end_char": 21,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 3. 命令式，与直陈同形

Sentence: Finis ton repas !

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| _ | _ | _ | _ | _ | _ |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Finis | finis | INTJ | _ | 3 | discourse |
| 2 | ton | son | DET | Number=Sing\|Number[psor]=Sing\|Person[psor]=1\|Poss=Yes\|PronType=Prs | 3 | det |
| 3 | repas | repas | NOUN | Gender=Masc\|Number=Sing | 0 | root |
| 4 | ! | ! | PUNCT | _ | 3 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Finis",
      "lemma": "finis",
      "upos": "INTJ",
      "head": 3,
      "deprel": "discourse",
      "start_char": 0,
      "end_char": 5
    },
    {
      "id": 2,
      "text": "ton",
      "lemma": "son",
      "upos": "DET",
      "feats": "Number=Sing|Number[psor]=Sing|Person[psor]=1|Poss=Yes|PronType=Prs",
      "head": 3,
      "deprel": "det",
      "start_char": 6,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "repas",
      "lemma": "repas",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 10,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "!",
      "lemma": "!",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 16,
      "end_char": 17,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 4. 过去完成 + 虚拟

Sentence: J'avais mangé avant qu'il arrive.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| avais | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Imp\|VerbForm=Fin | 3 | aux:tense |
| mangé | manger | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |
| arrive | arriver | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 3 | advcl |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | J' | moi | PRON | Emph=No\|Number=Sing\|Person=1\|PronType=Prs | 3 | nsubj |
| 2 | avais | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Imp\|VerbForm=Fin | 3 | aux:tense |
| 3 | mangé | manger | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |
| 4 | avant | avant | ADP | _ | 7 | mark |
| 5 | qu' | que | SCONJ | _ | 7 | mark |
| 6 | il | lui | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 7 | nsubj |
| 7 | arrive | arriver | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 3 | advcl |
| 8 | . | . | PUNCT | _ | 3 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "J'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "avais",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 2,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "mangé",
      "lemma": "manger",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 8,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADP",
      "head": 7,
      "deprel": "mark",
      "start_char": 14,
      "end_char": 19
    },
    {
      "id": 5,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 20,
      "end_char": 23,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 7,
      "text": "arrive",
      "lemma": "arriver",
      "upos": "VERB",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "advcl",
      "start_char": 26,
      "end_char": 32,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 32,
      "end_char": 33,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 5. 将来完成

Sentence: J'aurai fini avant midi.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| aurai | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 3 | aux:tense |
| fini | finir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | J' | moi | PRON | Emph=No\|Number=Sing\|Person=1\|PronType=Prs | 3 | nsubj |
| 2 | aurai | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 3 | aux:tense |
| 3 | fini | finir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |
| 4 | avant | avant | ADP | _ | 5 | case |
| 5 | midi | midi | NOUN | Gender=Masc\|Number=Sing | 3 | obl:mod |
| 6 | . | . | PUNCT | _ | 3 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "J'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "aurai",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 2,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "fini",
      "lemma": "finir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 8,
      "end_char": 12
    },
    {
      "id": 4,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADP",
      "head": 5,
      "deprel": "case",
      "start_char": 13,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "midi",
      "lemma": "midi",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "obl:mod",
      "start_char": 19,
      "end_char": 23,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 23,
      "end_char": 24,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 6. 条件完成

Sentence: J'aurais voyagé si j'avais eu de l'argent.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| aurais | avoir | AUX | Mood=Cnd\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 3 | aux:tense |
| voyagé | voyager | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |
| avais | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Imp\|VerbForm=Fin | 7 | aux:tense |
| eu | avoir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 3 | advcl |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | J' | moi | PRON | Emph=No\|Number=Sing\|Person=1\|PronType=Prs | 3 | nsubj |
| 2 | aurais | avoir | AUX | Mood=Cnd\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 3 | aux:tense |
| 3 | voyagé | voyager | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |
| 4 | si | si | SCONJ | _ | 7 | mark |
| 5 | j' | moi | PRON | Emph=No\|Number=Sing\|Person=1\|PronType=Prs | 7 | nsubj |
| 6 | avais | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Imp\|VerbForm=Fin | 7 | aux:tense |
| 7 | eu | avoir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 3 | advcl |
| 8 | de | de | ADP | ExtPos=DET | 10 | det |
| 9 | l' | le | DET | Definite=Def\|Number=Sing\|PronType=Art | 8 | fixed |
| 10 | argent | argent | NOUN | Gender=Masc\|Number=Sing | 7 | obj |
| 11 | . | . | PUNCT | _ | 3 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "J'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "aurais",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 2,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "voyagé",
      "lemma": "voyager",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 9,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "si",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 16,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "j'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 19,
      "end_char": 21,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "avais",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 21,
      "end_char": 26
    },
    {
      "id": 7,
      "text": "eu",
      "lemma": "avoir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 3,
      "deprel": "advcl",
      "start_char": 27,
      "end_char": 29
    },
    {
      "id": 8,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "feats": "ExtPos=DET",
      "head": 10,
      "deprel": "det",
      "start_char": 30,
      "end_char": 32
    },
    {
      "id": 9,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "fixed",
      "start_char": 33,
      "end_char": 35,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": "argent",
      "lemma": "argent",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "obj",
      "start_char": 35,
      "end_char": 41,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 41,
      "end_char": 42,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 7. être + 过去分词，测试性数配合

Sentence: Elle est partie hier soir.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 3 | aux:tense |
| partie | partir | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Elle | lui | PRON | Emph=No\|Gender=Fem\|Number=Sing\|Person=3\|PronType=Prs | 3 | nsubj |
| 2 | est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 3 | aux:tense |
| 3 | partie | partir | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |
| 4 | hier | hier | ADV | _ | 3 | advmod |
| 5 | soir | soir | NOUN | Gender=Masc\|Number=Sing | 4 | obl:mod |
| 6 | . | . | PUNCT | _ | 3 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 5,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "partie",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 9,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "hier",
      "lemma": "hier",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 16,
      "end_char": 20
    },
    {
      "id": 5,
      "text": "soir",
      "lemma": "soir",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obl:mod",
      "start_char": 21,
      "end_char": 25,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 25,
      "end_char": 26,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 8. 代词式动词

Sentence: Je me suis levé tôt.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| suis | être | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 4 | aux:tense |
| levé | lever | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Je | moi | PRON | Emph=No\|Number=Sing\|Person=1\|PronType=Prs | 4 | nsubj |
| 2 | me | moi | PRON | Emph=No\|Number=Sing\|Person=1\|PronType=Prs\|Reflex=Yes | 4 | obj |
| 3 | suis | être | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 4 | aux:tense |
| 4 | levé | lever | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |
| 5 | tôt | tôt | ADV | _ | 4 | advmod |
| 6 | . | . | PUNCT | _ | 4 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "me",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs|Reflex=Yes",
      "head": 4,
      "deprel": "obj",
      "start_char": 3,
      "end_char": 5
    },
    {
      "id": 3,
      "text": "suis",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 6,
      "end_char": 10
    },
    {
      "id": 4,
      "text": "levé",
      "lemma": "lever",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 11,
      "end_char": 15
    },
    {
      "id": 5,
      "text": "tôt",
      "lemma": "tôt",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 16,
      "end_char": 19,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 19,
      "end_char": 20,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 9. 被动语态

Sentence: La lettre a été écrite par Marie.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| a | avoir | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:tense |
| été | être | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 5 | aux:pass |
| écrite | écrire | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Pass | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | La | le | DET | Definite=Def\|Gender=Fem\|Number=Sing\|PronType=Art | 2 | det |
| 2 | lettre | lettre | NOUN | Gender=Fem\|Number=Sing | 5 | nsubj:pass |
| 3 | a | avoir | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:tense |
| 4 | été | être | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 5 | aux:pass |
| 5 | écrite | écrire | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Pass | 0 | root |
| 6 | par | par | ADP | _ | 7 | case |
| 7 | Marie | Marie | PROPN | _ | 5 | obl:agent |
| 8 | . | . | PUNCT | _ | 5 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "La",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 2,
      "deprel": "det",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "lettre",
      "lemma": "lettre",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "nsubj:pass",
      "start_char": 3,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 10,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "été",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 5,
      "deprel": "aux:pass",
      "start_char": 12,
      "end_char": 15
    },
    {
      "id": 5,
      "text": "écrite",
      "lemma": "écrire",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 0,
      "deprel": "root",
      "start_char": 16,
      "end_char": 22
    },
    {
      "id": 6,
      "text": "par",
      "lemma": "par",
      "upos": "ADP",
      "head": 7,
      "deprel": "case",
      "start_char": 23,
      "end_char": 26
    },
    {
      "id": 7,
      "text": "Marie",
      "lemma": "Marie",
      "upos": "PROPN",
      "head": 5,
      "deprel": "obl:agent",
      "start_char": 27,
      "end_char": 32,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 32,
      "end_char": 33,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 10. être 的虚拟式，形式有别于直陈

Sentence: Bien qu'il soit fatigué, il travaille.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| soit | être | AUX | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:pass |
| fatigué | fatiguer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Pass | 8 | advcl |
| travaille | travailler | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Bien | bien | ADV | ExtPos=SCONJ | 5 | mark |
| 2 | qu' | que | SCONJ | _ | 1 | fixed |
| 3 | il | lui | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 5 | nsubj |
| 4 | soit | être | AUX | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:pass |
| 5 | fatigué | fatiguer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Pass | 8 | advcl |
| 6 | , | , | PUNCT | _ | 5 | punct |
| 7 | il | lui | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 8 | nsubj |
| 8 | travaille | travailler | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 9 | . | . | PUNCT | _ | 8 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Bien",
      "lemma": "bien",
      "upos": "ADV",
      "feats": "ExtPos=SCONJ",
      "head": 5,
      "deprel": "mark",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 1,
      "deprel": "fixed",
      "start_char": 5,
      "end_char": 8,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 8,
      "end_char": 10
    },
    {
      "id": 4,
      "text": "soit",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:pass",
      "start_char": 11,
      "end_char": 15
    },
    {
      "id": 5,
      "text": "fatigué",
      "lemma": "fatiguer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 8,
      "deprel": "advcl",
      "start_char": 16,
      "end_char": 23,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 23,
      "end_char": 24
    },
    {
      "id": 7,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 25,
      "end_char": 27
    },
    {
      "id": 8,
      "text": "travaille",
      "lemma": "travailler",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 28,
      "end_char": 37,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 37,
      "end_char": 38,
      "misc": "SpaceAfter=No"
    }
  ]
]
```
