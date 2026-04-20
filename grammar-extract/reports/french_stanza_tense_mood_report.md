# French Stanza Tense and Mood Report

Generated from real Stanza `Document.to_dict()` output.

## Present indicative

Sentence: Je mange une pomme.

Target verb analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| mange | manger | VERB | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Je | moi | PRON | Emph=No\|Number=Sing\|Person=1\|PronType=Prs | 2 | nsubj |
| 2 | mange | manger | VERB | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 3 | une | un | DET | Definite=Ind\|Gender=Fem\|Number=Sing\|PronType=Art | 4 | det |
| 4 | pomme | pomme | NOUN | Gender=Fem\|Number=Sing | 2 | obj |
| 5 | . | . | PUNCT | _ | 2 | punct |

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
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "mange",
      "lemma": "manger",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 4,
      "deprel": "det",
      "start_char": 9,
      "end_char": 12
    },
    {
      "id": 4,
      "text": "pomme",
      "lemma": "pomme",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "obj",
      "start_char": 13,
      "end_char": 18,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 18,
      "end_char": 19,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## Past participle in passe compose

Sentence: J'ai mangé une pomme.

Target verb analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| mangé | manger | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | J' | moi | PRON | Emph=No\|Number=Sing\|Person=1\|PronType=Prs | 3 | nsubj |
| 2 | ai | avoir | AUX | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 3 | aux:tense |
| 3 | mangé | manger | VERB | Gender=Masc\|Number=Sing\|Tense=Past\|VerbForm=Part\|Voice=Act | 0 | root |
| 4 | une | un | DET | Definite=Ind\|Gender=Fem\|Number=Sing\|PronType=Art | 5 | det |
| 5 | pomme | pomme | NOUN | Gender=Fem\|Number=Sing | 3 | obj |
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
      "text": "ai",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 2,
      "end_char": 4
    },
    {
      "id": 3,
      "text": "mangé",
      "lemma": "manger",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 10
    },
    {
      "id": 4,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 11,
      "end_char": 14
    },
    {
      "id": 5,
      "text": "pomme",
      "lemma": "pomme",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 3,
      "deprel": "obj",
      "start_char": 15,
      "end_char": 20,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 20,
      "end_char": 21,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## Imperfect indicative

Sentence: Je mangeais une pomme.

Target verb analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| mangeais | manger | VERB | Mood=Ind\|Number=Sing\|Person=1\|Tense=Imp\|VerbForm=Fin | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Je | moi | PRON | Emph=No\|Number=Sing\|Person=1\|PronType=Prs | 2 | nsubj |
| 2 | mangeais | manger | VERB | Mood=Ind\|Number=Sing\|Person=1\|Tense=Imp\|VerbForm=Fin | 0 | root |
| 3 | une | un | DET | Definite=Ind\|Gender=Fem\|Number=Sing\|PronType=Art | 4 | det |
| 4 | pomme | pomme | NOUN | Gender=Fem\|Number=Sing | 2 | obj |
| 5 | . | . | PUNCT | _ | 2 | punct |

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
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "mangeais",
      "lemma": "manger",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 4,
      "deprel": "det",
      "start_char": 12,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "pomme",
      "lemma": "pomme",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "obj",
      "start_char": 16,
      "end_char": 21,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 21,
      "end_char": 22,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## Future indicative

Sentence: Je mangerai une pomme.

Target verb analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| mangerai | manger | VERB | Mood=Ind\|Number=Sing\|Person=1\|Tense=Fut\|VerbForm=Fin | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Je | moi | PRON | Emph=No\|Number=Sing\|Person=1\|PronType=Prs | 2 | nsubj |
| 2 | mangerai | manger | VERB | Mood=Ind\|Number=Sing\|Person=1\|Tense=Fut\|VerbForm=Fin | 0 | root |
| 3 | une | un | DET | Definite=Ind\|Gender=Fem\|Number=Sing\|PronType=Art | 4 | det |
| 4 | pomme | pomme | NOUN | Gender=Fem\|Number=Sing | 2 | obj |
| 5 | . | . | PUNCT | _ | 2 | punct |

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
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "mangerai",
      "lemma": "manger",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 4,
      "deprel": "det",
      "start_char": 12,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "pomme",
      "lemma": "pomme",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "obj",
      "start_char": 16,
      "end_char": 21,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 21,
      "end_char": 22,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## Conditional

Sentence: Je voudrais une pomme.

Target verb analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| voudrais | vouloir | VERB | Mood=Cnd\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Je | moi | PRON | Emph=No\|Number=Sing\|Person=1\|PronType=Prs | 2 | nsubj |
| 2 | voudrais | vouloir | VERB | Mood=Cnd\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 3 | une | un | DET | Definite=Ind\|Gender=Fem\|Number=Sing\|PronType=Art | 4 | det |
| 4 | pomme | pomme | NOUN | Gender=Fem\|Number=Sing | 2 | obj |
| 5 | . | . | PUNCT | _ | 2 | punct |

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
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "voudrais",
      "lemma": "vouloir",
      "upos": "VERB",
      "feats": "Mood=Cnd|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 4,
      "deprel": "det",
      "start_char": 12,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "pomme",
      "lemma": "pomme",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "obj",
      "start_char": 16,
      "end_char": 21,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 21,
      "end_char": 22,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## Subjunctive

Sentence: Il faut que je mange une pomme.

Target verb analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| mange | manger | VERB | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 2 | ccomp |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Il | lui | PRON | Emph=No\|Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs | 2 | expl:subj |
| 2 | faut | falloir | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 3 | que | que | SCONJ | _ | 5 | mark |
| 4 | je | moi | PRON | Emph=No\|Number=Sing\|Person=1\|PronType=Prs | 5 | nsubj |
| 5 | mange | manger | VERB | Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin | 2 | ccomp |
| 6 | une | un | DET | Definite=Ind\|Gender=Fem\|Number=Sing\|PronType=Art | 7 | det |
| 7 | pomme | pomme | NOUN | Gender=Fem\|Number=Sing | 5 | obj |
| 8 | . | . | PUNCT | _ | 2 | punct |

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
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 5,
      "deprel": "mark",
      "start_char": 8,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 12,
      "end_char": 14
    },
    {
      "id": 5,
      "text": "mange",
      "lemma": "manger",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "ccomp",
      "start_char": 15,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 21,
      "end_char": 24
    },
    {
      "id": 7,
      "text": "pomme",
      "lemma": "pomme",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "obj",
      "start_char": 25,
      "end_char": 30,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 30,
      "end_char": 31,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## Imperative

Sentence: Mange la pomme.

Target verb analysis:

| Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- |
| Mange | manger | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |

Full token analysis:

| ID | Text | Lemma | UPOS | Features | Head | Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Mange | manger | VERB | Mood=Ind\|Number=Sing\|Person=3\|Tense=Pres\|VerbForm=Fin | 0 | root |
| 2 | la | le | DET | Definite=Def\|Gender=Fem\|Number=Sing\|PronType=Art | 3 | det |
| 3 | pomme | pomme | NOUN | Gender=Fem\|Number=Sing | 1 | obj |
| 4 | . | . | PUNCT | _ | 1 | punct |

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Mange",
      "lemma": "manger",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 0,
      "end_char": 5
    },
    {
      "id": 2,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 3,
      "deprel": "det",
      "start_char": 6,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "pomme",
      "lemma": "pomme",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 1,
      "deprel": "obj",
      "start_char": 9,
      "end_char": 14,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 14,
      "end_char": 15,
      "misc": "SpaceAfter=No"
    }
  ]
]
```
