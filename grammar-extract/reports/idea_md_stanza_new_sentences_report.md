# French Stanza Report for idea.md Sentences

Generated from real Stanza `Document.to_dict()` output using the sentences listed in `idea.md`.

## 1. Unlabeled

Sentence: Qu’il vienne immédiatement !

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| vienne | venir | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Qu’ | que | SCONJ | _ | 3 | mark |
| 2 | il | lui | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 3 | nsubj |
| 3 | vienne | venir | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 4 | immédiatement | immédiatement | ADV | _ | 3 | advmod |
| 5 | ! | ! | PUNCT | _ | 3 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Qu’",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 3,
      "deprel": "mark",
      "start_char": 0,
      "end_char": 3,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 5
    },
    {
      "id": 3,
      "text": "vienne",
      "lemma": "venir",
      "upos": "VERB",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 6,
      "end_char": 12
    },
    {
      "id": 4,
      "text": "immédiatement",
      "lemma": "immédiatement",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 13,
      "end_char": 26
    },
    {
      "id": 5,
      "text": "!",
      "lemma": "!",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 27,
      "end_char": 28,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 2. Unlabeled

Sentence: Sois prudent, même si tu crois avoir raison.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| Sois | être | AUX | Mood=Ind\|Number=Sing\|Person=2\|Tense=Pres\|VerbForm=Fin | 2 | cop |
| crois | croire | VERB | Mood=Ind\|Number=Sing\|Person=2\|Tense=Pres\|VerbForm=Fin | 2 | advcl |
| avoir | avoir | VERB | VerbForm=Inf | 7 | xcomp |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Sois | être | AUX | Mood=Ind\|Number=Sing\|Person=2\|Tense=Pres\|VerbForm=Fin | 2 | cop |
| 2 | prudent | prudent | ADJ | Gender=Masc\|Number=Sing | 0 | root |
| 3 | , | , | PUNCT | _ | 7 | punct |
| 4 | même | même | ADV | _ | 7 | advmod |
| 5 | si | si | SCONJ | _ | 7 | mark |
| 6 | tu | toi | PRON | Emph=No\|Number=Sing\|Person=2\|PronType=Prs | 7 | nsubj |
| 7 | crois | croire | VERB | Mood=Ind\|Number=Sing\|Person=2\|Tense=Pres\|VerbForm=Fin | 2 | advcl |
| 8 | avoir | avoir | VERB | VerbForm=Inf | 7 | xcomp |
| 9 | raison | raison | NOUN | Gender=Fem\|Number=Sing | 8 | obj:lvc |
| 10 | . | . | PUNCT | _ | 2 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Sois",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "cop",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "prudent",
      "lemma": "prudent",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 12,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 12,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "même",
      "lemma": "même",
      "upos": "ADV",
      "head": 7,
      "deprel": "advmod",
      "start_char": 14,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "si",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 19,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 22,
      "end_char": 24
    },
    {
      "id": 7,
      "text": "crois",
      "lemma": "croire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "advcl",
      "start_char": 25,
      "end_char": 30
    },
    {
      "id": 8,
      "text": "avoir",
      "lemma": "avoir",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 7,
      "deprel": "xcomp",
      "start_char": 31,
      "end_char": 36
    },
    {
      "id": 9,
      "text": "raison",
      "lemma": "raison",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "obj:lvc",
      "start_char": 37,
      "end_char": 43,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 43,
      "end_char": 44,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 3. Unlabeled

Sentence: Ayant terminé son travail, elle serait déjà partie.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| Ayant | avoir | AUX | Tense=Pres\|VerbForm=Part | 2 | aux:tense |
| terminé | terminer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 9 | advcl |
| serait | être | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | aux:tense |
| partie | partir | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Ayant | avoir | AUX | Tense=Pres\|VerbForm=Part | 2 | aux:tense |
| 2 | terminé | terminer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 9 | advcl |
| 3 | son | son | DET | Gender=Masc\|Number=Sing\|Number[psor]=Sing\|Person[psor]=3\|Poss=Yes\|PronType=Prs | 4 | det |
| 4 | travail | travail | NOUN | Gender=Masc\|Number=Sing | 2 | obj |
| 5 | , | , | PUNCT | _ | 2 | punct |
| 6 | elle | lui | PRON | Emph=No\|Gender=Fem\|Number=Sing\|Person=3\|PronType=Prs | 9 | nsubj |
| 7 | serait | être | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | aux:tense |
| 8 | déjà | déjà | ADV | _ | 9 | advmod |
| 9 | partie | partir | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |
| 10 | . | . | PUNCT | _ | 9 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Ayant",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Tense=Pres|VerbForm=Part",
      "head": 2,
      "deprel": "aux:tense",
      "start_char": 0,
      "end_char": 5
    },
    {
      "id": 2,
      "text": "terminé",
      "lemma": "terminer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 9,
      "deprel": "advcl",
      "start_char": 6,
      "end_char": 13
    },
    {
      "id": 3,
      "text": "son",
      "lemma": "son",
      "upos": "DET",
      "feats": "Gender=Masc|Number=Sing|Number[psor]=Sing|Person[psor]=3|Poss=Yes|PronType=Prs",
      "head": 4,
      "deprel": "det",
      "start_char": 14,
      "end_char": 17
    },
    {
      "id": 4,
      "text": "travail",
      "lemma": "travail",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 2,
      "deprel": "obj",
      "start_char": 18,
      "end_char": 25,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 25,
      "end_char": 26
    },
    {
      "id": 6,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 27,
      "end_char": 31
    },
    {
      "id": 7,
      "text": "serait",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:tense",
      "start_char": 32,
      "end_char": 38
    },
    {
      "id": 8,
      "text": "déjà",
      "lemma": "déjà",
      "upos": "ADV",
      "head": 9,
      "deprel": "advmod",
      "start_char": 39,
      "end_char": 43
    },
    {
      "id": 9,
      "text": "partie",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 44,
      "end_char": 50,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 50,
      "end_char": 51,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 4. Unlabeled

Sentence: Les lettres qu’elle s’est écrites ont disparu.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 7 | aux:tense |
| écrites | écrire | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part\|Voice=Act | 2 | acl:relcl |
| ont | avoir | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | aux:tense |
| disparu | disparaître | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Les | le | DET | Definite=Def\|Number=Plur\|PronType=Art | 2 | det |
| 2 | lettres | lettre | NOUN | Gender=Fem\|Number=Plur | 9 | nsubj |
| 3 | qu’ | que | PRON | PronType=Rel | 7 | obj |
| 4 | elle | lui | PRON | Emph=No\|Gender=Fem\|Number=Sing\|Person=3\|PronType=Prs | 7 | nsubj |
| 5 | s’ | soi | PRON | Person=3\|PronType=Prs\|Reflex=Yes | 7 | expl:pv |
| 6 | est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 7 | aux:tense |
| 7 | écrites | écrire | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part\|Voice=Act | 2 | acl:relcl |
| 8 | ont | avoir | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | aux:tense |
| 9 | disparu | disparaître | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |
| 10 | . | . | PUNCT | _ | 9 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 2,
      "deprel": "det",
      "start_char": 0,
      "end_char": 3
    },
    {
      "id": 2,
      "text": "lettres",
      "lemma": "lettre",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 4,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "qu’",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 7,
      "deprel": "obj",
      "start_char": 12,
      "end_char": 15,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 15,
      "end_char": 19
    },
    {
      "id": 5,
      "text": "s’",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 7,
      "deprel": "expl:pv",
      "start_char": 20,
      "end_char": 22,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 22,
      "end_char": 25
    },
    {
      "id": 7,
      "text": "écrites",
      "lemma": "écrire",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 2,
      "deprel": "acl:relcl",
      "start_char": 26,
      "end_char": 33
    },
    {
      "id": 8,
      "text": "ont",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:tense",
      "start_char": 34,
      "end_char": 37
    },
    {
      "id": 9,
      "text": "disparu",
      "lemma": "disparaître",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 38,
      "end_char": 45,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 45,
      "end_char": 46,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 5. Unlabeled

Sentence: Ils se sont parlé, puis ils se sont revus.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| sont | être | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 4 | aux:tense |
| parlé | parler | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |
| sont | être | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 10 | aux:tense |
| revus | revoir | VERB | Gender=Masc\|Number=Plur\|Tense=Past\|VerbForm=Part\|Voice=Act | 4 | conj |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Ils | eux | PRON | Emph=No\|Gender=Masc\|Number=Plur\|Person=3\|PronType=Prs | 4 | nsubj |
| 2 | se | soi | PRON | Person=3\|PronType=Prs\|Reflex=Yes | 4 | obj |
| 3 | sont | être | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 4 | aux:tense |
| 4 | parlé | parler | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |
| 5 | , | , | PUNCT | _ | 10 | punct |
| 6 | puis | puis | CCONJ | _ | 10 | cc |
| 7 | ils | eux | PRON | Emph=No\|Gender=Masc\|Number=Plur\|Person=3\|PronType=Prs | 10 | nsubj |
| 8 | se | soi | PRON | Person=3\|PronType=Prs\|Reflex=Yes | 10 | expl:pv |
| 9 | sont | être | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 10 | aux:tense |
| 10 | revus | revoir | VERB | Gender=Masc\|Number=Plur\|Tense=Past\|VerbForm=Part\|Voice=Act | 4 | conj |
| 11 | . | . | PUNCT | _ | 4 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Ils",
      "lemma": "eux",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 3
    },
    {
      "id": 2,
      "text": "se",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 4,
      "deprel": "obj",
      "start_char": 4,
      "end_char": 6
    },
    {
      "id": 3,
      "text": "sont",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 7,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "parlé",
      "lemma": "parler",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 12,
      "end_char": 17,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 17,
      "end_char": 18
    },
    {
      "id": 6,
      "text": "puis",
      "lemma": "puis",
      "upos": "CCONJ",
      "head": 10,
      "deprel": "cc",
      "start_char": 19,
      "end_char": 23
    },
    {
      "id": 7,
      "text": "ils",
      "lemma": "eux",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs",
      "head": 10,
      "deprel": "nsubj",
      "start_char": 24,
      "end_char": 27
    },
    {
      "id": 8,
      "text": "se",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 10,
      "deprel": "expl:pv",
      "start_char": 28,
      "end_char": 30
    },
    {
      "id": 9,
      "text": "sont",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 10,
      "deprel": "aux:tense",
      "start_char": 31,
      "end_char": 35
    },
    {
      "id": 10,
      "text": "revus",
      "lemma": "revoir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 4,
      "deprel": "conj",
      "start_char": 36,
      "end_char": 41,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 41,
      "end_char": 42,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 6. Unlabeled

Sentence: Il faut qu’elles soient revenues avant minuit.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| faut | falloir | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| soient | être | AUX | Mood=Sub\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 6 | aux:pass |
| revenues | revenir | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part\|Voice=Act | 2 | ccomp |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Il | lui | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 2 | expl:subj |
| 2 | faut | falloir | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 3 | qu’ | que | SCONJ | _ | 6 | mark |
| 4 | elles | eux | PRON | Emph=No\|Gender=Fem\|Number=Plur\|Person=3\|PronType=Prs | 6 | nsubj:pass |
| 5 | soient | être | AUX | Mood=Sub\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 6 | aux:pass |
| 6 | revenues | revenir | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part\|Voice=Act | 2 | ccomp |
| 7 | avant | avant | ADP | _ | 8 | case |
| 8 | minuit | minuit | NOUN | Gender=Masc\|Number=Sing | 6 | obl:mod |
| 9 | . | . | PUNCT | _ | 2 | punct |

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
      "text": "qu’",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 6,
      "deprel": "mark",
      "start_char": 8,
      "end_char": 11,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "elles",
      "lemma": "eux",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Plur|Person=3|PronType=Prs",
      "head": 6,
      "deprel": "nsubj:pass",
      "start_char": 11,
      "end_char": 16
    },
    {
      "id": 5,
      "text": "soient",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 6,
      "deprel": "aux:pass",
      "start_char": 17,
      "end_char": 23
    },
    {
      "id": 6,
      "text": "revenues",
      "lemma": "revenir",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 2,
      "deprel": "ccomp",
      "start_char": 24,
      "end_char": 32
    },
    {
      "id": 7,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 33,
      "end_char": 38
    },
    {
      "id": 8,
      "text": "minuit",
      "lemma": "minuit",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 6,
      "deprel": "obl:mod",
      "start_char": 39,
      "end_char": 45,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 45,
      "end_char": 46,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 7. Unlabeled

Sentence: Si elle avait su, elle ne serait pas venue.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| avait | avoir | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Imp\|VerbForm=Fin | 4 | aux:tense |
| su | savoir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 10 | advcl |
| serait | être | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 10 | aux:pass |
| venue | venir | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Si | si | SCONJ | _ | 4 | mark |
| 2 | elle | lui | PRON | Emph=No\|Gender=Fem\|Number=Sing\|Person=3\|PronType=Prs | 4 | nsubj |
| 3 | avait | avoir | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Imp\|VerbForm=Fin | 4 | aux:tense |
| 4 | su | savoir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 10 | advcl |
| 5 | , | , | PUNCT | _ | 4 | punct |
| 6 | elle | lui | PRON | Emph=No\|Gender=Fem\|Number=Sing\|Person=3\|PronType=Prs | 10 | nsubj:pass |
| 7 | ne | ne | ADV | Polarity=Neg | 10 | advmod |
| 8 | serait | être | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 10 | aux:pass |
| 9 | pas | pas | ADV | Polarity=Neg | 10 | advmod |
| 10 | venue | venir | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |
| 11 | . | . | PUNCT | _ | 10 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Si",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 4,
      "deprel": "mark",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "avait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 8,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "su",
      "lemma": "savoir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 10,
      "deprel": "advcl",
      "start_char": 14,
      "end_char": 16,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 16,
      "end_char": 17
    },
    {
      "id": 6,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 10,
      "deprel": "nsubj:pass",
      "start_char": 18,
      "end_char": 22
    },
    {
      "id": 7,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 10,
      "deprel": "advmod",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 8,
      "text": "serait",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 10,
      "deprel": "aux:pass",
      "start_char": 26,
      "end_char": 32
    },
    {
      "id": 9,
      "text": "pas",
      "lemma": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 10,
      "deprel": "advmod",
      "start_char": 33,
      "end_char": 36
    },
    {
      "id": 10,
      "text": "venue",
      "lemma": "venir",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 37,
      "end_char": 42,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 42,
      "end_char": 43,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 8. Unlabeled

Sentence: Quand il aura fini, nous commencerons sans lui.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| aura | avoir | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Fut\|VerbForm=Fin | 4 | aux:tense |
| fini | finir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 7 | advcl |
| commencerons | commencer | VERB | Mood=Ind\|Number=Plur\|Person=1\|Tense=Fut\|VerbForm=Fin | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Quand | quand | SCONJ | _ | 4 | mark |
| 2 | il | lui | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 4 | nsubj |
| 3 | aura | avoir | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Fut\|VerbForm=Fin | 4 | aux:tense |
| 4 | fini | finir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 7 | advcl |
| 5 | , | , | PUNCT | _ | 4 | punct |
| 6 | nous | nous | PRON | Emph=No\|Number=Plur\|Person=1\|PronType=Prs | 7 | nsubj |
| 7 | commencerons | commencer | VERB | Mood=Ind\|Number=Plur\|Person=1\|Tense=Fut\|VerbForm=Fin | 0 | root |
| 8 | sans | sans | ADP | _ | 9 | case |
| 9 | lui | lui | PRON | Emph=Yes\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 7 | obl:mod |
| 10 | . | . | PUNCT | _ | 7 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Quand",
      "lemma": "quand",
      "upos": "SCONJ",
      "head": 4,
      "deprel": "mark",
      "start_char": 0,
      "end_char": 5
    },
    {
      "id": 2,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 6,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "aura",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 9,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "fini",
      "lemma": "finir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 7,
      "deprel": "advcl",
      "start_char": 14,
      "end_char": 18,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 18,
      "end_char": 19
    },
    {
      "id": 6,
      "text": "nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 20,
      "end_char": 24
    },
    {
      "id": 7,
      "text": "commencerons",
      "lemma": "commencer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 25,
      "end_char": 37
    },
    {
      "id": 8,
      "text": "sans",
      "lemma": "sans",
      "upos": "ADP",
      "head": 9,
      "deprel": "case",
      "start_char": 38,
      "end_char": 42
    },
    {
      "id": 9,
      "text": "lui",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=Yes|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "obl:mod",
      "start_char": 43,
      "end_char": 46,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 46,
      "end_char": 47,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 9. Unlabeled

Sentence: Eussiez-vous accepté, tout aurait été différent.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| Eussiez | être | AUX | Mood=Ind\|Number=Plur\|Person=2\|Tense=Pres\|VerbForm=Fin | 3 | aux:pass |
| accepté | accepter | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Pass | 8 | advcl |
| aurait | avoir | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 8 | aux:tense |
| été | être | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 8 | cop |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Eussiez | être | AUX | Mood=Ind\|Number=Plur\|Person=2\|Tense=Pres\|VerbForm=Fin | 3 | aux:pass |
| 2 | -vous | vous | PRON | Number=Plur\|Person=2\|PronType=Prs | 3 | nsubj:pass |
| 3 | accepté | accepter | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Pass | 8 | advcl |
| 4 | , | , | PUNCT | _ | 3 | punct |
| 5 | tout | tout | PRON | Gender=Masc\|Number=Sing\|Person=3\|PronType=Ind | 8 | nsubj |
| 6 | aurait | avoir | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 8 | aux:tense |
| 7 | été | être | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 8 | cop |
| 8 | différent | différent | ADJ | Gender=Masc\|Number=Sing | 0 | root |
| 9 | . | . | PUNCT | _ | 8 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Eussiez",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:pass",
      "start_char": 0,
      "end_char": 7,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "-vous",
      "lemma": "vous",
      "upos": "PRON",
      "feats": "Number=Plur|Person=2|PronType=Prs",
      "head": 3,
      "deprel": "nsubj:pass",
      "start_char": 7,
      "end_char": 12
    },
    {
      "id": 3,
      "text": "accepté",
      "lemma": "accepter",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 8,
      "deprel": "advcl",
      "start_char": 13,
      "end_char": 20,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 20,
      "end_char": 21
    },
    {
      "id": 5,
      "text": "tout",
      "lemma": "tout",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Ind",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 22,
      "end_char": 26
    },
    {
      "id": 6,
      "text": "aurait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 8,
      "deprel": "aux:tense",
      "start_char": 27,
      "end_char": 33
    },
    {
      "id": 7,
      "text": "été",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 8,
      "deprel": "cop",
      "start_char": 34,
      "end_char": 37
    },
    {
      "id": 8,
      "text": "différent",
      "lemma": "différent",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 38,
      "end_char": 47,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 47,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 10. Unlabeled

Sentence: Leurs décisions ont été contestées puis annulées.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| ont | avoir | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:tense |
| été | être | AUX | Number=Sing\|Tense=Past\|VerbForm=Part | 5 | aux:pass |
| contestées | contester | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part\|Voice=Pass | 0 | root |
| annulées | annuler | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part\|Voice=Pass | 5 | conj |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Leurs | son | DET | Number=Plur\|Poss=Yes\|PronType=Prs | 2 | det |
| 2 | décisions | décision | NOUN | Gender=Fem\|Number=Plur | 5 | nsubj:pass |
| 3 | ont | avoir | AUX | Mood=Ind\|Number=Plur\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:tense |
| 4 | été | être | AUX | Number=Sing\|Tense=Past\|VerbForm=Part | 5 | aux:pass |
| 5 | contestées | contester | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part\|Voice=Pass | 0 | root |
| 6 | puis | puis | CCONJ | _ | 7 | cc |
| 7 | annulées | annuler | VERB | Gender=Fem\|Number=Plur\|Tense=Past\|VerbForm=Part\|Voice=Pass | 5 | conj |
| 8 | . | . | PUNCT | _ | 5 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Leurs",
      "lemma": "son",
      "upos": "DET",
      "feats": "Number=Plur|Poss=Yes|PronType=Prs",
      "head": 2,
      "deprel": "det",
      "start_char": 0,
      "end_char": 5
    },
    {
      "id": 2,
      "text": "décisions",
      "lemma": "décision",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 5,
      "deprel": "nsubj:pass",
      "start_char": 6,
      "end_char": 15
    },
    {
      "id": 3,
      "text": "ont",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 16,
      "end_char": 19
    },
    {
      "id": 4,
      "text": "été",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Number=Sing|Tense=Past|VerbForm=Part",
      "head": 5,
      "deprel": "aux:pass",
      "start_char": 20,
      "end_char": 23
    },
    {
      "id": 5,
      "text": "contestées",
      "lemma": "contester",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 0,
      "deprel": "root",
      "start_char": 24,
      "end_char": 34
    },
    {
      "id": 6,
      "text": "puis",
      "lemma": "puis",
      "upos": "CCONJ",
      "head": 7,
      "deprel": "cc",
      "start_char": 35,
      "end_char": 39
    },
    {
      "id": 7,
      "text": "annulées",
      "lemma": "annuler",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 5,
      "deprel": "conj",
      "start_char": 40,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 11. Unlabeled

Sentence: Cette maison s’est vendue très vite.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:tense |
| vendue | vendre | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Cette | ce | DET | Gender=Fem\|Number=Sing\|PronType=Dem | 2 | det |
| 2 | maison | maison | NOUN | Gender=Fem\|Number=Sing | 5 | nsubj:pass |
| 3 | s’ | soi | PRON | Person=3\|PronType=Prs\|Reflex=Yes | 5 | expl:pass |
| 4 | est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 5 | aux:tense |
| 5 | vendue | vendre | VERB | Gender=Fem\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |
| 6 | très | très | ADV | _ | 7 | advmod |
| 7 | vite | vite | ADV | _ | 5 | advmod |
| 8 | . | . | PUNCT | _ | 5 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Cette",
      "lemma": "ce",
      "upos": "DET",
      "feats": "Gender=Fem|Number=Sing|PronType=Dem",
      "head": 2,
      "deprel": "det",
      "start_char": 0,
      "end_char": 5
    },
    {
      "id": 2,
      "text": "maison",
      "lemma": "maison",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "nsubj:pass",
      "start_char": 6,
      "end_char": 12
    },
    {
      "id": 3,
      "text": "s’",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 5,
      "deprel": "expl:pass",
      "start_char": 13,
      "end_char": 15,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 15,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "vendue",
      "lemma": "vendre",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 19,
      "end_char": 25
    },
    {
      "id": 6,
      "text": "très",
      "lemma": "très",
      "upos": "ADV",
      "head": 7,
      "deprel": "advmod",
      "start_char": 26,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "vite",
      "lemma": "vite",
      "upos": "ADV",
      "head": 5,
      "deprel": "advmod",
      "start_char": 31,
      "end_char": 35,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 35,
      "end_char": 36,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 12. Unlabeled

Sentence: Il paraît qu’elle l’aurait vu hier.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| paraît | paraître | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| aurait | avoir | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 7 | aux:tense |
| vu | voir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 2 | csubj |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Il | lui | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 2 | expl:subj |
| 2 | paraît | paraître | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 3 | qu’ | que | SCONJ | _ | 7 | mark |
| 4 | elle | lui | PRON | Emph=No\|Gender=Fem\|Number=Sing\|Person=3\|PronType=Prs | 7 | nsubj |
| 5 | l’ | lui | PRON | Emph=No\|Number=Sing\|Person=3\|PronType=Prs | 7 | obj |
| 6 | aurait | avoir | AUX | Mood=Cnd\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 7 | aux:tense |
| 7 | vu | voir | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 2 | csubj |
| 8 | hier | hier | ADV | _ | 7 | advmod |
| 9 | . | . | PUNCT | _ | 2 | punct |

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
      "text": "paraît",
      "lemma": "paraître",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "qu’",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 10,
      "end_char": 13,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 13,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "l’",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "obj",
      "start_char": 18,
      "end_char": 20,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "aurait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 20,
      "end_char": 26
    },
    {
      "id": 7,
      "text": "vu",
      "lemma": "voir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 2,
      "deprel": "csubj",
      "start_char": 27,
      "end_char": 29
    },
    {
      "id": 8,
      "text": "hier",
      "lemma": "hier",
      "upos": "ADV",
      "head": 7,
      "deprel": "advmod",
      "start_char": 30,
      "end_char": 34,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 34,
      "end_char": 35,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 13. Unlabeled

Sentence: Le livre que j’ai laissé tomber est abîmé.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| ai | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 6 | aux:tense |
| laissé | laisser | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 2 | acl:relcl |
| tomber | tomber | VERB | VerbForm=Inf | 6 | xcomp |
| est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | aux:pass |
| abîmé | abîmer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Pass | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Le | le | DET | Definite=Def\|Gender=Masc\|Number=Sing\|PronType=Art | 2 | det |
| 2 | livre | livre | NOUN | Gender=Masc\|Number=Sing | 9 | nsubj:pass |
| 3 | que | que | PRON | PronType=Rel | 7 | obj |
| 4 | j’ | moi | PRON | Emph=No\|Number=Sing\|Person=1\|PronType=Prs | 6 | nsubj |
| 5 | ai | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 6 | aux:tense |
| 6 | laissé | laisser | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 2 | acl:relcl |
| 7 | tomber | tomber | VERB | VerbForm=Inf | 6 | xcomp |
| 8 | est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | aux:pass |
| 9 | abîmé | abîmer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Pass | 0 | root |
| 10 | . | . | PUNCT | _ | 9 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 2,
      "deprel": "det",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "livre",
      "lemma": "livre",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "nsubj:pass",
      "start_char": 3,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 7,
      "deprel": "obj",
      "start_char": 9,
      "end_char": 12
    },
    {
      "id": 4,
      "text": "j’",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 13,
      "end_char": 15,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": "ai",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 6,
      "deprel": "aux:tense",
      "start_char": 15,
      "end_char": 17
    },
    {
      "id": 6,
      "text": "laissé",
      "lemma": "laisser",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 2,
      "deprel": "acl:relcl",
      "start_char": 18,
      "end_char": 24
    },
    {
      "id": 7,
      "text": "tomber",
      "lemma": "tomber",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 6,
      "deprel": "xcomp",
      "start_char": 25,
      "end_char": 31
    },
    {
      "id": 8,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:pass",
      "start_char": 32,
      "end_char": 35
    },
    {
      "id": 9,
      "text": "abîmé",
      "lemma": "abîmer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 0,
      "deprel": "root",
      "start_char": 36,
      "end_char": 41,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 41,
      "end_char": 42,
      "misc": "SpaceAfter=No"
    }
  ]
]
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
| 3 | -il | lui | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 2 | expl:subj |
| 4 | qu’ | que | SCONJ | _ | 6 | mark |
| 5 | on | on | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Ind | 6 | nsubj |
| 6 | puisse | pouvoir | VERB | Mood=Sub\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 2 | ccomp |
| 7 | le | lui | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 8 | obj |
| 8 | prouver | prouver | VERB | VerbForm=Inf | 6 | xcomp |
| 9 | . | . | PUNCT | _ | 2 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Encore",
      "lemma": "encore",
      "upos": "ADV",
      "head": 2,
      "deprel": "advmod",
      "start_char": 0,
      "end_char": 6
    },
    {
      "id": 2,
      "text": "faut",
      "lemma": "falloir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 7,
      "end_char": 11,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "-il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 2,
      "deprel": "expl:subj",
      "start_char": 11,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "qu’",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 6,
      "deprel": "mark",
      "start_char": 15,
      "end_char": 18,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": "on",
      "lemma": "on",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Ind",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "puisse",
      "lemma": "pouvoir",
      "upos": "VERB",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "ccomp",
      "start_char": 21,
      "end_char": 27
    },
    {
      "id": 7,
      "text": "le",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 8,
      "deprel": "obj",
      "start_char": 28,
      "end_char": 30
    },
    {
      "id": 8,
      "text": "prouver",
      "lemma": "prouver",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 6,
      "deprel": "xcomp",
      "start_char": 31,
      "end_char": 38,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 38,
      "end_char": 39,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 15. Unlabeled

Sentence: Rentré trop tard, il s’est fait gronder par sa mère.

Verb and auxiliary analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| Rentré | rentrer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Pass | 9 | advcl |
| est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | aux:tense |
| fait | faire | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 9 | aux:caus |
| gronder | gronder | VERB | VerbForm=Inf | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Rentré | rentrer | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Pass | 9 | advcl |
| 2 | trop | trop | ADV | _ | 3 | advmod |
| 3 | tard | tard | ADV | _ | 1 | advmod |
| 4 | , | , | PUNCT | _ | 1 | punct |
| 5 | il | lui | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 9 | nsubj:caus |
| 6 | s’ | soi | PRON | Person=3\|PronType=Prs\|Reflex=Yes | 9 | obj |
| 7 | est | être | AUX | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 9 | aux:tense |
| 8 | fait | faire | AUX | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part | 9 | aux:caus |
| 9 | gronder | gronder | VERB | VerbForm=Inf | 0 | root |
| 10 | par | par | ADP | _ | 12 | case |
| 11 | sa | son | DET | Gender=Fem\|Number=Sing\|Number[psor]=Sing\|Person[psor]=3\|Poss=Yes\|PronType=Prs | 12 | det |
| 12 | mère | mère | NOUN | Gender=Fem\|Number=Sing | 9 | obl:agent |
| 13 | . | . | PUNCT | _ | 9 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Rentré",
      "lemma": "rentrer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 9,
      "deprel": "advcl",
      "start_char": 0,
      "end_char": 6
    },
    {
      "id": 2,
      "text": "trop",
      "lemma": "trop",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 7,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "tard",
      "lemma": "tard",
      "upos": "ADV",
      "head": 1,
      "deprel": "advmod",
      "start_char": 12,
      "end_char": 16,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 16,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "nsubj:caus",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "s’",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 9,
      "deprel": "obj",
      "start_char": 21,
      "end_char": 23,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:tense",
      "start_char": 23,
      "end_char": 26
    },
    {
      "id": 8,
      "text": "fait",
      "lemma": "faire",
      "upos": "AUX",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 9,
      "deprel": "aux:caus",
      "start_char": 27,
      "end_char": 31
    },
    {
      "id": 9,
      "text": "gronder",
      "lemma": "gronder",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 0,
      "deprel": "root",
      "start_char": 32,
      "end_char": 39
    },
    {
      "id": 10,
      "text": "par",
      "lemma": "par",
      "upos": "ADP",
      "head": 12,
      "deprel": "case",
      "start_char": 40,
      "end_char": 43
    },
    {
      "id": 11,
      "text": "sa",
      "lemma": "son",
      "upos": "DET",
      "feats": "Gender=Fem|Number=Sing|Number[psor]=Sing|Person[psor]=3|Poss=Yes|PronType=Prs",
      "head": 12,
      "deprel": "det",
      "start_char": 44,
      "end_char": 46
    },
    {
      "id": 12,
      "text": "mère",
      "lemma": "mère",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 9,
      "deprel": "obl:agent",
      "start_char": 47,
      "end_char": 51,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 51,
      "end_char": 52,
      "misc": "SpaceAfter=No"
    }
  ]
]
```
