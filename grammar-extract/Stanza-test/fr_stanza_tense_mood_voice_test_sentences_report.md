# French Stanza Raw JSON Report for Tense, Mood, and Voice Test Sentences

Generated from real Stanza `Document.to_dict()` output using `Stanza-test/fr_stanza_tense_mood_voice_test_sentences.txt`.

## 1. Sentence

Sentence: Je mange une pomme pendant que tu lis le journal.

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
      "end_char": 18
    },
    {
      "id": 5,
      "text": "pendant",
      "lemma": "pendant",
      "upos": "ADP",
      "head": 8,
      "deprel": "mark",
      "start_char": 19,
      "end_char": 26
    },
    {
      "id": 6,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 8,
      "deprel": "mark",
      "start_char": 27,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 31,
      "end_char": 33
    },
    {
      "id": 8,
      "text": "lis",
      "lemma": "lire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "advcl",
      "start_char": 34,
      "end_char": 37
    },
    {
      "id": 9,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 10,
      "deprel": "det",
      "start_char": 38,
      "end_char": 40
    },
    {
      "id": 10,
      "text": "journal",
      "lemma": "journal",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 8,
      "deprel": "obj",
      "start_char": 41,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 2. Sentence

Sentence: Je mangeais une pomme quand le téléphone a sonné.

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
      "end_char": 21
    },
    {
      "id": 5,
      "text": "quand",
      "lemma": "quand",
      "upos": "SCONJ",
      "head": 9,
      "deprel": "mark",
      "start_char": 22,
      "end_char": 27
    },
    {
      "id": 6,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 28,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "téléphone",
      "lemma": "téléphone",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 31,
      "end_char": 40
    },
    {
      "id": 8,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:tense",
      "start_char": 41,
      "end_char": 42
    },
    {
      "id": 9,
      "text": "sonné",
      "lemma": "sonner",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 2,
      "deprel": "advcl",
      "start_char": 43,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 3. Sentence

Sentence: Nous regardions la mer tandis que les enfants jouaient.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "regardions",
      "lemma": "regardier",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 15
    },
    {
      "id": 3,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 4,
      "deprel": "det",
      "start_char": 16,
      "end_char": 18
    },
    {
      "id": 4,
      "text": "mer",
      "lemma": "mer",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "obj",
      "start_char": 19,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "tandis",
      "lemma": "tandis",
      "upos": "ADV",
      "feats": "ExtPos=SCONJ",
      "head": 9,
      "deprel": "mark",
      "start_char": 23,
      "end_char": 29
    },
    {
      "id": 6,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 5,
      "deprel": "fixed",
      "start_char": 30,
      "end_char": 33
    },
    {
      "id": 7,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 34,
      "end_char": 37
    },
    {
      "id": 8,
      "text": "enfants",
      "lemma": "enfant",
      "upos": "NOUN",
      "feats": "Number=Plur",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 38,
      "end_char": 45
    },
    {
      "id": 9,
      "text": "jouaient",
      "lemma": "jouer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 2,
      "deprel": "advcl",
      "start_char": 46,
      "end_char": 54,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 54,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 4. Sentence

Sentence: Il pleuvait depuis trois heures et personne ne sortait.

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
      "text": "pleuvait",
      "lemma": "pleuvoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "depuis",
      "lemma": "depuis",
      "upos": "ADP",
      "head": 5,
      "deprel": "case",
      "start_char": 12,
      "end_char": 18
    },
    {
      "id": 4,
      "text": "trois",
      "lemma": "trois",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 5,
      "deprel": "nummod",
      "start_char": 19,
      "end_char": 24
    },
    {
      "id": 5,
      "text": "heures",
      "lemma": "heure",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 2,
      "deprel": "obl:mod",
      "start_char": 25,
      "end_char": 31
    },
    {
      "id": 6,
      "text": "et",
      "lemma": "et",
      "upos": "CCONJ",
      "head": 9,
      "deprel": "cc",
      "start_char": 32,
      "end_char": 34
    },
    {
      "id": 7,
      "text": "personne",
      "lemma": "personne",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|PronType=Neg",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 35,
      "end_char": 43
    },
    {
      "id": 8,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 9,
      "deprel": "advmod",
      "start_char": 44,
      "end_char": 46
    },
    {
      "id": 9,
      "text": "sortait",
      "lemma": "sortir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 2,
      "deprel": "conj",
      "start_char": 47,
      "end_char": 54,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 54,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 5. Sentence

Sentence: Elle écrivait souvent à son frère lorsqu'il vivait à Lyon.

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
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "écrivait",
      "lemma": "écrire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 13
    },
    {
      "id": 3,
      "text": "souvent",
      "lemma": "souvent",
      "upos": "ADV",
      "head": 2,
      "deprel": "advmod",
      "start_char": 14,
      "end_char": 21
    },
    {
      "id": 4,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 6,
      "deprel": "case",
      "start_char": 22,
      "end_char": 23
    },
    {
      "id": 5,
      "text": "son",
      "lemma": "son",
      "upos": "DET",
      "feats": "Gender=Masc|Number=Sing|Number[psor]=Sing|Person[psor]=3|Poss=Yes|PronType=Prs",
      "head": 6,
      "deprel": "det",
      "start_char": 24,
      "end_char": 27
    },
    {
      "id": 6,
      "text": "frère",
      "lemma": "frère",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 2,
      "deprel": "obl:arg",
      "start_char": 28,
      "end_char": 33
    },
    {
      "id": 7,
      "text": "lorsqu'",
      "lemma": "lorsque",
      "upos": "SCONJ",
      "head": 9,
      "deprel": "mark",
      "start_char": 34,
      "end_char": 41,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 41,
      "end_char": 43
    },
    {
      "id": 9,
      "text": "vivait",
      "lemma": "vivre",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 2,
      "deprel": "advcl",
      "start_char": 44,
      "end_char": 50
    },
    {
      "id": 10,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 11,
      "deprel": "case",
      "start_char": 51,
      "end_char": 52
    },
    {
      "id": 11,
      "text": "Lyon",
      "lemma": "Lyon",
      "upos": "PROPN",
      "head": 9,
      "deprel": "obl:arg",
      "start_char": 53,
      "end_char": 57,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 57,
      "end_char": 58,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 6. Sentence

Sentence: Vous disiez toujours que cette solution était impossible.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Vous",
      "lemma": "vous",
      "upos": "PRON",
      "feats": "Number=Plur|Person=2|PronType=Prs",
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "disiez",
      "lemma": "dire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "toujours",
      "lemma": "toujours",
      "upos": "ADV",
      "head": 2,
      "deprel": "advmod",
      "start_char": 12,
      "end_char": 20
    },
    {
      "id": 4,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 8,
      "deprel": "mark",
      "start_char": 21,
      "end_char": 24
    },
    {
      "id": 5,
      "text": "cette",
      "lemma": "ce",
      "upos": "DET",
      "feats": "Gender=Fem|Number=Sing|PronType=Dem",
      "head": 6,
      "deprel": "det",
      "start_char": 25,
      "end_char": 30
    },
    {
      "id": 6,
      "text": "solution",
      "lemma": "solution",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 31,
      "end_char": 39
    },
    {
      "id": 7,
      "text": "était",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 8,
      "deprel": "cop",
      "start_char": 40,
      "end_char": 45
    },
    {
      "id": 8,
      "text": "impossible",
      "lemma": "impossible",
      "upos": "ADJ",
      "feats": "Number=Sing",
      "head": 2,
      "deprel": "ccomp",
      "start_char": 46,
      "end_char": 56,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 56,
      "end_char": 57,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 7. Sentence

Sentence: Je mangerai après la réunion.

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
      "text": "après",
      "lemma": "après",
      "upos": "ADP",
      "head": 5,
      "deprel": "case",
      "start_char": 12,
      "end_char": 17
    },
    {
      "id": 4,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 5,
      "text": "réunion",
      "lemma": "réunion",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "obl:mod",
      "start_char": 21,
      "end_char": 28,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 28,
      "end_char": 29,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 8. Sentence

Sentence: Nous partirons dès que le signal sera donné.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "partirons",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 14
    },
    {
      "id": 3,
      "text": "dès",
      "lemma": "dès",
      "upos": "ADP",
      "head": 8,
      "deprel": "mark",
      "start_char": 15,
      "end_char": 18
    },
    {
      "id": 4,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 8,
      "deprel": "mark",
      "start_char": 19,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 6,
      "text": "signal",
      "lemma": "signal",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 8,
      "deprel": "nsubj:pass",
      "start_char": 26,
      "end_char": 32
    },
    {
      "id": 7,
      "text": "sera",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 8,
      "deprel": "aux:pass",
      "start_char": 33,
      "end_char": 37
    },
    {
      "id": 8,
      "text": "donné",
      "lemma": "donner",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 2,
      "deprel": "advcl",
      "start_char": 38,
      "end_char": 43,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
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

## 9. Sentence

Sentence: Ils prendront la parole quand le président les invitera.

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
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 3
    },
    {
      "id": 2,
      "text": "prendront",
      "lemma": "prendre",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 4,
      "end_char": 13
    },
    {
      "id": 3,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 4,
      "deprel": "det",
      "start_char": 14,
      "end_char": 16
    },
    {
      "id": 4,
      "text": "parole",
      "lemma": "parole",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "obj",
      "start_char": 17,
      "end_char": 23
    },
    {
      "id": 5,
      "text": "quand",
      "lemma": "quand",
      "upos": "SCONJ",
      "head": 9,
      "deprel": "mark",
      "start_char": 24,
      "end_char": 29
    },
    {
      "id": 6,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 30,
      "end_char": 32
    },
    {
      "id": 7,
      "text": "président",
      "lemma": "président",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 33,
      "end_char": 42
    },
    {
      "id": 8,
      "text": "les",
      "lemma": "eux",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "obj",
      "start_char": 43,
      "end_char": 46
    },
    {
      "id": 9,
      "text": "invitera",
      "lemma": "inviter",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 2,
      "deprel": "advcl",
      "start_char": 47,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 55,
      "end_char": 56,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 10. Sentence

Sentence: Tu verras mieux si tu allumes la lampe.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "verras",
      "lemma": "voir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "mieux",
      "lemma": "mieux",
      "upos": "ADV",
      "head": 2,
      "deprel": "advmod",
      "start_char": 10,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "si",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 6,
      "deprel": "mark",
      "start_char": 16,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 19,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "allumes",
      "lemma": "allumer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "advcl",
      "start_char": 22,
      "end_char": 29
    },
    {
      "id": 7,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 30,
      "end_char": 32
    },
    {
      "id": 8,
      "text": "lampe",
      "lemma": "lampe",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 6,
      "deprel": "obj",
      "start_char": 33,
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

## 11. Sentence

Sentence: Je mangeai rapidement puis je sortis sans bruit.

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
      "text": "mangeai",
      "lemma": "manger",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "rapidement",
      "lemma": "rapidement",
      "upos": "ADV",
      "head": 2,
      "deprel": "advmod",
      "start_char": 11,
      "end_char": 21
    },
    {
      "id": 4,
      "text": "puis",
      "lemma": "puis",
      "upos": "CCONJ",
      "head": 6,
      "deprel": "cc",
      "start_char": 22,
      "end_char": 26
    },
    {
      "id": 5,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 27,
      "end_char": 29
    },
    {
      "id": 6,
      "text": "sortis",
      "lemma": "sortir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "conj",
      "start_char": 30,
      "end_char": 36
    },
    {
      "id": 7,
      "text": "sans",
      "lemma": "sans",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 37,
      "end_char": 41
    },
    {
      "id": 8,
      "text": "bruit",
      "lemma": "bruit",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 6,
      "deprel": "obl:mod",
      "start_char": 42,
      "end_char": 47,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 47,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 12. Sentence

Sentence: Il entra, salua l'assemblée et s'assit au premier rang.

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
      "text": "entra",
      "lemma": "entrer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 8,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 8,
      "end_char": 9
    },
    {
      "id": 4,
      "text": "salua",
      "lemma": "saluer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin",
      "head": 2,
      "deprel": "conj",
      "start_char": 10,
      "end_char": 15
    },
    {
      "id": 5,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 16,
      "end_char": 18,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "assemblée",
      "lemma": "assemblée",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 4,
      "deprel": "obj",
      "start_char": 18,
      "end_char": 27
    },
    {
      "id": 7,
      "text": "et",
      "lemma": "et",
      "upos": "CCONJ",
      "head": 9,
      "deprel": "cc",
      "start_char": 28,
      "end_char": 30
    },
    {
      "id": 8,
      "text": "s'",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 9,
      "deprel": "expl:pv",
      "start_char": 31,
      "end_char": 33,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": "assit",
      "lemma": "asseoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin",
      "head": 2,
      "deprel": "conj",
      "start_char": 33,
      "end_char": 38
    },
    {
      "id": [
        10,
        11
      ],
      "text": "au",
      "start_char": 39,
      "end_char": 41
    },
    {
      "id": 10,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 13,
      "deprel": "case"
    },
    {
      "id": 11,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 13,
      "deprel": "det"
    },
    {
      "id": 12,
      "text": "premier",
      "lemma": "premier",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 13,
      "deprel": "amod",
      "start_char": 42,
      "end_char": 49
    },
    {
      "id": 13,
      "text": "rang",
      "lemma": "rang",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "obl:arg",
      "start_char": 50,
      "end_char": 54,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 54,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 13. Sentence

Sentence: Nous reçûmes la lettre le jour même.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "reçûmes",
      "lemma": "recevoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 12
    },
    {
      "id": 3,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 4,
      "deprel": "det",
      "start_char": 13,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "lettre",
      "lemma": "lettre",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "obj",
      "start_char": 16,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 6,
      "text": "jour",
      "lemma": "jour",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 2,
      "deprel": "obl:mod",
      "start_char": 26,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "même",
      "lemma": "même",
      "upos": "ADV",
      "head": 6,
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
      "head": 2,
      "deprel": "punct",
      "start_char": 35,
      "end_char": 36,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 14. Sentence

Sentence: Elle voulut répondre, mais personne ne l'écouta.

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
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "voulut",
      "lemma": "vouloir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "répondre",
      "lemma": "répondre",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 2,
      "deprel": "xcomp",
      "start_char": 12,
      "end_char": 20,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 20,
      "end_char": 21
    },
    {
      "id": 5,
      "text": "mais",
      "lemma": "mais",
      "upos": "CCONJ",
      "head": 9,
      "deprel": "cc",
      "start_char": 22,
      "end_char": 26
    },
    {
      "id": 6,
      "text": "personne",
      "lemma": "personne",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|PronType=Neg",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 27,
      "end_char": 35
    },
    {
      "id": 7,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 9,
      "deprel": "advmod",
      "start_char": 36,
      "end_char": 38
    },
    {
      "id": 8,
      "text": "l'",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "obj",
      "start_char": 39,
      "end_char": 41,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": "écouta",
      "lemma": "écouter",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin",
      "head": 2,
      "deprel": "conj",
      "start_char": 41,
      "end_char": 47,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 47,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 15. Sentence

Sentence: Ils partirent avant que la nuit ne tombât.

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
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 3
    },
    {
      "id": 2,
      "text": "partirent",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 4,
      "end_char": 13
    },
    {
      "id": 3,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADP",
      "head": 8,
      "deprel": "mark",
      "start_char": 14,
      "end_char": 19
    },
    {
      "id": 4,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 8,
      "deprel": "mark",
      "start_char": 20,
      "end_char": 23
    },
    {
      "id": 5,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 24,
      "end_char": 26
    },
    {
      "id": 6,
      "text": "nuit",
      "lemma": "nuit",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 27,
      "end_char": 31
    },
    {
      "id": 7,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 8,
      "deprel": "advmod",
      "start_char": 32,
      "end_char": 34
    },
    {
      "id": 8,
      "text": "tombât",
      "lemma": "tombir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "advcl",
      "start_char": 35,
      "end_char": 41,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 41,
      "end_char": 42,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 16. Sentence

Sentence: Je viens de terminer le dossier.

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
      "text": "viens",
      "lemma": "venir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 4,
      "deprel": "mark",
      "start_char": 9,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "terminer",
      "lemma": "terminer",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 2,
      "deprel": "xcomp",
      "start_char": 12,
      "end_char": 20
    },
    {
      "id": 5,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 21,
      "end_char": 23
    },
    {
      "id": 6,
      "text": "dossier",
      "lemma": "dossier",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obj",
      "start_char": 24,
      "end_char": 31,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 31,
      "end_char": 32,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 17. Sentence

Sentence: Nous avons mangé avant de reprendre la route.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "avons",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 5,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "mangé",
      "lemma": "manger",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 11,
      "end_char": 16
    },
    {
      "id": 4,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 17,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 6,
      "deprel": "mark",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 6,
      "text": "reprendre",
      "lemma": "reprendre",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 4,
      "deprel": "xcomp",
      "start_char": 26,
      "end_char": 35
    },
    {
      "id": 7,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 36,
      "end_char": 38
    },
    {
      "id": 8,
      "text": "route",
      "lemma": "route",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 6,
      "deprel": "obj",
      "start_char": 39,
      "end_char": 44,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 44,
      "end_char": 45,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 18. Sentence

Sentence: Elle a compris ce que tu voulais dire.

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
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 5,
      "end_char": 6
    },
    {
      "id": 3,
      "text": "compris",
      "lemma": "comprendre",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 7,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "ce",
      "lemma": "ce",
      "upos": "PRON",
      "feats": "Gender=Masc|Person=3|PronType=Dem",
      "head": 3,
      "deprel": "obj",
      "start_char": 15,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 8,
      "deprel": "obj",
      "start_char": 18,
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
      "text": "voulais",
      "lemma": "vouloir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Imp|VerbForm=Fin",
      "head": 4,
      "deprel": "acl:relcl",
      "start_char": 25,
      "end_char": 32
    },
    {
      "id": 8,
      "text": "dire",
      "lemma": "dire",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 7,
      "deprel": "xcomp",
      "start_char": 33,
      "end_char": 37,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 37,
      "end_char": 38,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 19. Sentence

Sentence: Ils sont arrivés plus tôt que prévu.

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
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 3
    },
    {
      "id": 2,
      "text": "sont",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 4,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "arrivés",
      "lemma": "arriver",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 9,
      "end_char": 16
    },
    {
      "id": 4,
      "text": "plus",
      "lemma": "plus",
      "upos": "ADV",
      "head": 5,
      "deprel": "advmod",
      "start_char": 17,
      "end_char": 21
    },
    {
      "id": 5,
      "text": "tôt",
      "lemma": "tôt",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 22,
      "end_char": 25
    },
    {
      "id": 6,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 26,
      "end_char": 29
    },
    {
      "id": 7,
      "text": "prévu",
      "lemma": "prévoir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 4,
      "deprel": "ccomp",
      "start_char": 30,
      "end_char": 35,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 35,
      "end_char": 36,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 20. Sentence

Sentence: Tu t'es souvenu de son adresse au dernier moment.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "t'",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 4,
      "deprel": "obj",
      "start_char": 3,
      "end_char": 5,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "es",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 5,
      "end_char": 7
    },
    {
      "id": 4,
      "text": "souvenu",
      "lemma": "souvenir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "start_char": 8,
      "end_char": 15
    },
    {
      "id": 5,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 7,
      "deprel": "case",
      "start_char": 16,
      "end_char": 18
    },
    {
      "id": 6,
      "text": "son",
      "lemma": "son",
      "upos": "DET",
      "feats": "Number=Sing|Number[psor]=Sing|Person[psor]=3|Poss=Yes|PronType=Prs",
      "head": 7,
      "deprel": "det",
      "start_char": 19,
      "end_char": 22
    },
    {
      "id": 7,
      "text": "adresse",
      "lemma": "adresse",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 4,
      "deprel": "obl:arg",
      "start_char": 23,
      "end_char": 30
    },
    {
      "id": [
        8,
        9
      ],
      "text": "au",
      "start_char": 31,
      "end_char": 33
    },
    {
      "id": 8,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 11,
      "deprel": "case"
    },
    {
      "id": 9,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det"
    },
    {
      "id": 10,
      "text": "dernier",
      "lemma": "dernier",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 11,
      "deprel": "amod",
      "start_char": 34,
      "end_char": 41
    },
    {
      "id": 11,
      "text": "moment",
      "lemma": "moment",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obl:mod",
      "start_char": 42,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 21. Sentence

Sentence: J'avais mangé quand elle est arrivée.

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
      "text": "quand",
      "lemma": "quand",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 14,
      "end_char": 19
    },
    {
      "id": 5,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 20,
      "end_char": 24
    },
    {
      "id": 6,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 25,
      "end_char": 28
    },
    {
      "id": 7,
      "text": "arrivée",
      "lemma": "arriver",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 3,
      "deprel": "advcl",
      "start_char": 29,
      "end_char": 36,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 36,
      "end_char": 37,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 22. Sentence

Sentence: Nous avions déjà signé le contrat avant que l'erreur soit découverte.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "avions",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 5,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "déjà",
      "lemma": "déjà",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 12,
      "end_char": 16
    },
    {
      "id": 4,
      "text": "signé",
      "lemma": "signer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 17,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 6,
      "text": "contrat",
      "lemma": "contrat",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obj",
      "start_char": 26,
      "end_char": 33
    },
    {
      "id": 7,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADP",
      "head": 12,
      "deprel": "mark",
      "start_char": 34,
      "end_char": 39
    },
    {
      "id": 8,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 12,
      "deprel": "mark",
      "start_char": 40,
      "end_char": 43
    },
    {
      "id": 9,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 10,
      "deprel": "det",
      "start_char": 44,
      "end_char": 46,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": "erreur",
      "lemma": "erreur",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 12,
      "deprel": "nsubj:pass",
      "start_char": 46,
      "end_char": 52
    },
    {
      "id": 11,
      "text": "soit",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 12,
      "deprel": "aux:pass",
      "start_char": 53,
      "end_char": 57
    },
    {
      "id": 12,
      "text": "découverte",
      "lemma": "découvrir",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 4,
      "deprel": "advcl",
      "start_char": 58,
      "end_char": 68,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 68,
      "end_char": 69,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 23. Sentence

Sentence: Il avait plu toute la nuit, alors les rues étaient glissantes.

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
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "avait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 3,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "plu",
      "lemma": "pleuvoir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 9,
      "end_char": 12
    },
    {
      "id": 4,
      "text": "toute",
      "lemma": "tout",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Sing",
      "head": 6,
      "deprel": "amod",
      "start_char": 13,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 19,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "nuit",
      "lemma": "nuit",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 3,
      "deprel": "obj",
      "start_char": 22,
      "end_char": 26,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 12,
      "deprel": "punct",
      "start_char": 26,
      "end_char": 27
    },
    {
      "id": 8,
      "text": "alors",
      "lemma": "alors",
      "upos": "ADV",
      "head": 12,
      "deprel": "advmod",
      "start_char": 28,
      "end_char": 33
    },
    {
      "id": 9,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 10,
      "deprel": "det",
      "start_char": 34,
      "end_char": 37
    },
    {
      "id": 10,
      "text": "rues",
      "lemma": "rue",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 12,
      "deprel": "nsubj",
      "start_char": 38,
      "end_char": 42
    },
    {
      "id": 11,
      "text": "étaient",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 12,
      "deprel": "cop",
      "start_char": 43,
      "end_char": 50
    },
    {
      "id": 12,
      "text": "glissantes",
      "lemma": "glissant",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Plur",
      "head": 3,
      "deprel": "conj",
      "start_char": 51,
      "end_char": 61,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 61,
      "end_char": 62,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 24. Sentence

Sentence: Elle s'était levée tôt parce qu'elle devait partir.

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
      "head": 4,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "s'",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 4,
      "deprel": "obj",
      "start_char": 5,
      "end_char": 7,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "était",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 7,
      "end_char": 12
    },
    {
      "id": 4,
      "text": "levée",
      "lemma": "lever",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 13,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "tôt",
      "lemma": "tôt",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 19,
      "end_char": 22
    },
    {
      "id": 6,
      "text": "parce",
      "lemma": "parce",
      "upos": "ADV",
      "feats": "ExtPos=SCONJ",
      "head": 9,
      "deprel": "mark",
      "start_char": 23,
      "end_char": 28
    },
    {
      "id": 7,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 6,
      "deprel": "fixed",
      "start_char": 29,
      "end_char": 32,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 32,
      "end_char": 36
    },
    {
      "id": 9,
      "text": "devait",
      "lemma": "devoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 4,
      "deprel": "advcl",
      "start_char": 37,
      "end_char": 43
    },
    {
      "id": 10,
      "text": "partir",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 9,
      "deprel": "xcomp",
      "start_char": 44,
      "end_char": 50,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 50,
      "end_char": 51,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 25. Sentence

Sentence: Vous aviez cru qu'il viendrait seul.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Vous",
      "lemma": "vous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=2|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "aviez",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 5,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "cru",
      "lemma": "croire",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 11,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "qu'",
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
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "viendrait",
      "lemma": "venir",
      "upos": "VERB",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "ccomp",
      "start_char": 21,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "seul",
      "lemma": "seul",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 6,
      "deprel": "xcomp",
      "start_char": 31,
      "end_char": 35,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 35,
      "end_char": 36,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 26. Sentence

Sentence: J'aurai fini avant midi.

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

## 27. Sentence

Sentence: Quand tu auras lu le rapport, nous en parlerons.

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
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 6,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "auras",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 9,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "lu",
      "lemma": "lire",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 10,
      "deprel": "advcl",
      "start_char": 15,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "rapport",
      "lemma": "rapport",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obj",
      "start_char": 21,
      "end_char": 28,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 28,
      "end_char": 29
    },
    {
      "id": 8,
      "text": "nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 10,
      "deprel": "nsubj",
      "start_char": 30,
      "end_char": 34
    },
    {
      "id": 9,
      "text": "en",
      "lemma": "en",
      "upos": "PRON",
      "feats": "Emph=No|Person=3|PronType=Prs",
      "head": 10,
      "deprel": "iobj",
      "start_char": 35,
      "end_char": 37
    },
    {
      "id": 10,
      "text": "parlerons",
      "lemma": "parler",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 38,
      "end_char": 47,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 47,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 28. Sentence

Sentence: Ils seront partis lorsque la tempête atteindra la côte.

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
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 3
    },
    {
      "id": 2,
      "text": "seront",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 4,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "partis",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 11,
      "end_char": 17
    },
    {
      "id": 4,
      "text": "lorsque",
      "lemma": "lorsque",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 18,
      "end_char": 25
    },
    {
      "id": 5,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 26,
      "end_char": 28
    },
    {
      "id": 6,
      "text": "tempête",
      "lemma": "tempête",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 29,
      "end_char": 36
    },
    {
      "id": 7,
      "text": "atteindra",
      "lemma": "atteindre",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 3,
      "deprel": "advcl",
      "start_char": 37,
      "end_char": 46
    },
    {
      "id": 8,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 9,
      "deprel": "det",
      "start_char": 47,
      "end_char": 49
    },
    {
      "id": 9,
      "text": "côte",
      "lemma": "côte",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 7,
      "deprel": "obj",
      "start_char": 50,
      "end_char": 54,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 54,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 29. Sentence

Sentence: Elle aura compris la règle après deux exemples.

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
      "text": "aura",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 5,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "compris",
      "lemma": "comprendre",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 10,
      "end_char": 17
    },
    {
      "id": 4,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 5,
      "text": "règle",
      "lemma": "règle",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 3,
      "deprel": "obj",
      "start_char": 21,
      "end_char": 26
    },
    {
      "id": 6,
      "text": "après",
      "lemma": "après",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 27,
      "end_char": 32
    },
    {
      "id": 7,
      "text": "deux",
      "lemma": "deux",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 8,
      "deprel": "nummod",
      "start_char": 33,
      "end_char": 37
    },
    {
      "id": 8,
      "text": "exemples",
      "lemma": "exemple",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 3,
      "deprel": "obl:mod",
      "start_char": 38,
      "end_char": 46,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 46,
      "end_char": 47,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 30. Sentence

Sentence: Nous nous serons rencontrés trois fois avant la conférence.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 4,
      "deprel": "obj",
      "start_char": 5,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "serons",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 10,
      "end_char": 16
    },
    {
      "id": 4,
      "text": "rencontrés",
      "lemma": "rencontrer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 17,
      "end_char": 27
    },
    {
      "id": 5,
      "text": "trois",
      "lemma": "trois",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 6,
      "deprel": "nummod",
      "start_char": 28,
      "end_char": 33
    },
    {
      "id": 6,
      "text": "fois",
      "lemma": "fois",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 4,
      "deprel": "obl:mod",
      "start_char": 34,
      "end_char": 38
    },
    {
      "id": 7,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADP",
      "head": 9,
      "deprel": "case",
      "start_char": 39,
      "end_char": 44
    },
    {
      "id": 8,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 9,
      "deprel": "det",
      "start_char": 45,
      "end_char": 47
    },
    {
      "id": 9,
      "text": "conférence",
      "lemma": "conférence",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 4,
      "deprel": "obl:mod",
      "start_char": 48,
      "end_char": 58,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 58,
      "end_char": 59,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 31. Sentence

Sentence: J'eus terminé le repas lorsque l'alarme retentit.

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
      "text": "eus",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 2,
      "end_char": 5
    },
    {
      "id": 3,
      "text": "terminé",
      "lemma": "terminer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 6,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 14,
      "end_char": 16
    },
    {
      "id": 5,
      "text": "repas",
      "lemma": "repas",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "obj",
      "start_char": 17,
      "end_char": 22
    },
    {
      "id": 6,
      "text": "lorsque",
      "lemma": "lorsque",
      "upos": "SCONJ",
      "head": 9,
      "deprel": "mark",
      "start_char": 23,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 31,
      "end_char": 33,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": "alarme",
      "lemma": "alarme",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 33,
      "end_char": 39
    },
    {
      "id": 9,
      "text": "retentit",
      "lemma": "retentir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "advcl",
      "start_char": 40,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 32. Sentence

Sentence: Dès qu'il eut signé, le notaire ferma le dossier.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Dès",
      "lemma": "dès",
      "upos": "ADP",
      "head": 5,
      "deprel": "mark",
      "start_char": 0,
      "end_char": 3
    },
    {
      "id": 2,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 5,
      "deprel": "mark",
      "start_char": 4,
      "end_char": 7,
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
      "start_char": 7,
      "end_char": 9
    },
    {
      "id": 4,
      "text": "eut",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 10,
      "end_char": 13
    },
    {
      "id": 5,
      "text": "signé",
      "lemma": "signer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 9,
      "deprel": "advcl",
      "start_char": 14,
      "end_char": 19,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 19,
      "end_char": 20
    },
    {
      "id": 7,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 21,
      "end_char": 23
    },
    {
      "id": 8,
      "text": "notaire",
      "lemma": "notaire",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 24,
      "end_char": 31
    },
    {
      "id": 9,
      "text": "ferma",
      "lemma": "fermer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 32,
      "end_char": 37
    },
    {
      "id": 10,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 38,
      "end_char": 40
    },
    {
      "id": 11,
      "text": "dossier",
      "lemma": "dossier",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "obj",
      "start_char": 41,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 33. Sentence

Sentence: Quand nous eûmes franchi le pont, la pluie cessa.

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
      "text": "nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 6,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "eûmes",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 11,
      "end_char": 16
    },
    {
      "id": 4,
      "text": "franchi",
      "lemma": "franchir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 10,
      "deprel": "advcl",
      "start_char": 17,
      "end_char": 24
    },
    {
      "id": 5,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 25,
      "end_char": 27
    },
    {
      "id": 6,
      "text": "pont",
      "lemma": "pont",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obj",
      "start_char": 28,
      "end_char": 32,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 32,
      "end_char": 33
    },
    {
      "id": 8,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 9,
      "deprel": "det",
      "start_char": 34,
      "end_char": 36
    },
    {
      "id": 9,
      "text": "pluie",
      "lemma": "pluie",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 10,
      "deprel": "nsubj",
      "start_char": 37,
      "end_char": 42
    },
    {
      "id": 10,
      "text": "cessa",
      "lemma": "cesser",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 43,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 34. Sentence

Sentence: Après qu'elle eut répondu, le silence revint.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Après",
      "lemma": "après",
      "upos": "ADP",
      "head": 5,
      "deprel": "mark",
      "start_char": 0,
      "end_char": 5
    },
    {
      "id": 2,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 5,
      "deprel": "mark",
      "start_char": 6,
      "end_char": 9,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 9,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "eut",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 14,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "répondu",
      "lemma": "répondre",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 9,
      "deprel": "advcl",
      "start_char": 18,
      "end_char": 25,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 25,
      "end_char": 26
    },
    {
      "id": 7,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 27,
      "end_char": 29
    },
    {
      "id": 8,
      "text": "silence",
      "lemma": "silence",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 30,
      "end_char": 37
    },
    {
      "id": 9,
      "text": "revint",
      "lemma": "revenir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 38,
      "end_char": 44,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 44,
      "end_char": 45,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 35. Sentence

Sentence: Aussitôt qu'ils furent entrés, les portes se refermèrent.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Aussitôt",
      "lemma": "aussitôt",
      "upos": "ADV",
      "feats": "ExtPos=SCONJ",
      "head": 10,
      "deprel": "advmod",
      "start_char": 0,
      "end_char": 8
    },
    {
      "id": 2,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 5,
      "deprel": "mark",
      "start_char": 9,
      "end_char": 12,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "ils",
      "lemma": "eux",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 12,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "furent",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 16,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "entrés",
      "lemma": "entrer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 10,
      "deprel": "advcl",
      "start_char": 23,
      "end_char": 29,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 29,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 31,
      "end_char": 34
    },
    {
      "id": 8,
      "text": "portes",
      "lemma": "porte",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 10,
      "deprel": "nsubj:pass",
      "start_char": 35,
      "end_char": 41
    },
    {
      "id": 9,
      "text": "se",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 10,
      "deprel": "expl:pass",
      "start_char": 42,
      "end_char": 44
    },
    {
      "id": 10,
      "text": "refermèrent",
      "lemma": "refermer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 45,
      "end_char": 56,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 56,
      "end_char": 57,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 36. Sentence

Sentence: Je serais venu si tu m'avais appelé.

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
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "serais",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 3,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "venu",
      "lemma": "venir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 10,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "si",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 8,
      "deprel": "mark",
      "start_char": 15,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "m'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 8,
      "deprel": "obj",
      "start_char": 21,
      "end_char": 23,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": "avais",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Imp|VerbForm=Fin",
      "head": 8,
      "deprel": "aux:tense",
      "start_char": 23,
      "end_char": 28
    },
    {
      "id": 8,
      "text": "appelé",
      "lemma": "appeler",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 3,
      "deprel": "advcl",
      "start_char": 29,
      "end_char": 35,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 35,
      "end_char": 36,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 37. Sentence

Sentence: Elle accepterait l'offre si les conditions étaient plus claires.

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
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "accepterait",
      "lemma": "accepter",
      "upos": "VERB",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 16
    },
    {
      "id": 3,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 4,
      "deprel": "det",
      "start_char": 17,
      "end_char": 19,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "offre",
      "lemma": "offre",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "obj",
      "start_char": 19,
      "end_char": 24
    },
    {
      "id": 5,
      "text": "si",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 10,
      "deprel": "mark",
      "start_char": 25,
      "end_char": 27
    },
    {
      "id": 6,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 28,
      "end_char": 31
    },
    {
      "id": 7,
      "text": "conditions",
      "lemma": "condition",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 10,
      "deprel": "nsubj",
      "start_char": 32,
      "end_char": 42
    },
    {
      "id": 8,
      "text": "étaient",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 10,
      "deprel": "cop",
      "start_char": 43,
      "end_char": 50
    },
    {
      "id": 9,
      "text": "plus",
      "lemma": "plus",
      "upos": "ADV",
      "head": 10,
      "deprel": "advmod",
      "start_char": 51,
      "end_char": 55
    },
    {
      "id": 10,
      "text": "claires",
      "lemma": "clair",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Plur",
      "head": 2,
      "deprel": "advcl",
      "start_char": 56,
      "end_char": 63,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 63,
      "end_char": 64,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 38. Sentence

Sentence: Nous aurions terminé plus tôt sans cette panne.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "aurions",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 5,
      "end_char": 12
    },
    {
      "id": 3,
      "text": "terminé",
      "lemma": "terminer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 13,
      "end_char": 20
    },
    {
      "id": 4,
      "text": "plus",
      "lemma": "plus",
      "upos": "ADV",
      "head": 5,
      "deprel": "advmod",
      "start_char": 21,
      "end_char": 25
    },
    {
      "id": 5,
      "text": "tôt",
      "lemma": "tôt",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 26,
      "end_char": 29
    },
    {
      "id": 6,
      "text": "sans",
      "lemma": "sans",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 30,
      "end_char": 34
    },
    {
      "id": 7,
      "text": "cette",
      "lemma": "ce",
      "upos": "DET",
      "feats": "Gender=Fem|Number=Sing|PronType=Dem",
      "head": 8,
      "deprel": "det",
      "start_char": 35,
      "end_char": 40
    },
    {
      "id": 8,
      "text": "panne",
      "lemma": "panne",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 3,
      "deprel": "obl:mod",
      "start_char": 41,
      "end_char": 46,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 46,
      "end_char": 47,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 39. Sentence

Sentence: Ils auraient pu réussir, mais ils ont abandonné trop vite.

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
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 3
    },
    {
      "id": 2,
      "text": "auraient",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 4,
      "end_char": 12
    },
    {
      "id": 3,
      "text": "pu",
      "lemma": "pouvoir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 13,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "réussir",
      "lemma": "réussir",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 3,
      "deprel": "xcomp",
      "start_char": 16,
      "end_char": 23,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 23,
      "end_char": 24
    },
    {
      "id": 6,
      "text": "mais",
      "lemma": "mais",
      "upos": "CCONJ",
      "head": 9,
      "deprel": "cc",
      "start_char": 25,
      "end_char": 29
    },
    {
      "id": 7,
      "text": "ils",
      "lemma": "eux",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 30,
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
      "text": "abandonné",
      "lemma": "abandonner",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 3,
      "deprel": "conj",
      "start_char": 38,
      "end_char": 47
    },
    {
      "id": 10,
      "text": "trop",
      "lemma": "trop",
      "upos": "ADV",
      "head": 11,
      "deprel": "advmod",
      "start_char": 48,
      "end_char": 52
    },
    {
      "id": 11,
      "text": "vite",
      "lemma": "vite",
      "upos": "ADV",
      "head": 9,
      "deprel": "advmod",
      "start_char": 53,
      "end_char": 57,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 57,
      "end_char": 58,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 40. Sentence

Sentence: Tu devrais relire ce passage avant de l'envoyer.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "devrais",
      "lemma": "devoir",
      "upos": "VERB",
      "feats": "Mood=Cnd|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "relire",
      "lemma": "relire",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 2,
      "deprel": "xcomp",
      "start_char": 11,
      "end_char": 17
    },
    {
      "id": 4,
      "text": "ce",
      "lemma": "ce",
      "upos": "DET",
      "feats": "Gender=Masc|Number=Sing|PronType=Dem",
      "head": 5,
      "deprel": "det",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 5,
      "text": "passage",
      "lemma": "passage",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "obj",
      "start_char": 21,
      "end_char": 28
    },
    {
      "id": 6,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 29,
      "end_char": 34
    },
    {
      "id": 7,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 9,
      "deprel": "mark",
      "start_char": 35,
      "end_char": 37
    },
    {
      "id": 8,
      "text": "l'",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "obj",
      "start_char": 38,
      "end_char": 40,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": "envoyer",
      "lemma": "envoyer",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 6,
      "deprel": "xcomp",
      "start_char": 40,
      "end_char": 47,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 47,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 41. Sentence

Sentence: Il faut que je parte maintenant.

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
      "text": "parte",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "ccomp",
      "start_char": 15,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "maintenant",
      "lemma": "maintenant",
      "upos": "ADV",
      "head": 5,
      "deprel": "advmod",
      "start_char": 21,
      "end_char": 31,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 31,
      "end_char": 32,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 42. Sentence

Sentence: Je doute qu'elle comprenne la situation.

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
      "text": "doute",
      "lemma": "douter",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 5,
      "deprel": "mark",
      "start_char": 9,
      "end_char": 12,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 12,
      "end_char": 16
    },
    {
      "id": 5,
      "text": "comprenne",
      "lemma": "comprendre",
      "upos": "VERB",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "ccomp",
      "start_char": 17,
      "end_char": 26
    },
    {
      "id": 6,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 27,
      "end_char": 29
    },
    {
      "id": 7,
      "text": "situation",
      "lemma": "situation",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "obj",
      "start_char": 30,
      "end_char": 39,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 39,
      "end_char": 40,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 43. Sentence

Sentence: Bien qu'il soit malade, il continue de travailler.

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
      "deprel": "cop",
      "start_char": 11,
      "end_char": 15
    },
    {
      "id": 5,
      "text": "malade",
      "lemma": "malade",
      "upos": "ADJ",
      "feats": "Number=Sing",
      "head": 8,
      "deprel": "advcl",
      "start_char": 16,
      "end_char": 22,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 22,
      "end_char": 23
    },
    {
      "id": 7,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 24,
      "end_char": 26
    },
    {
      "id": 8,
      "text": "continue",
      "lemma": "continuer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 27,
      "end_char": 35
    },
    {
      "id": 9,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 10,
      "deprel": "mark",
      "start_char": 36,
      "end_char": 38
    },
    {
      "id": 10,
      "text": "travailler",
      "lemma": "travailler",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 8,
      "deprel": "xcomp",
      "start_char": 39,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 49,
      "end_char": 50,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 44. Sentence

Sentence: Avant que nous ne commencions, vérifiez les données.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Avant",
      "lemma": "avant",
      "upos": "ADP",
      "head": 5,
      "deprel": "mark",
      "start_char": 0,
      "end_char": 5
    },
    {
      "id": 2,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 5,
      "deprel": "mark",
      "start_char": 6,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 10,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 5,
      "deprel": "advmod",
      "start_char": 15,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "commencions",
      "lemma": "commencier",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 7,
      "deprel": "advcl",
      "start_char": 18,
      "end_char": 29,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 29,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "vérifiez",
      "lemma": "vérifier",
      "upos": "VERB",
      "feats": "Mood=Imp|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 31,
      "end_char": 39
    },
    {
      "id": 8,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 9,
      "deprel": "det",
      "start_char": 40,
      "end_char": 43
    },
    {
      "id": 9,
      "text": "données",
      "lemma": "donnée",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 7,
      "deprel": "obj",
      "start_char": 44,
      "end_char": 51,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 51,
      "end_char": 52,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 45. Sentence

Sentence: Qu'ils viennent immédiatement s'ils veulent participer.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Qu'",
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
      "text": "ils",
      "lemma": "eux",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 6
    },
    {
      "id": 3,
      "text": "viennent",
      "lemma": "venir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 7,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "immédiatement",
      "lemma": "immédiatement",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 16,
      "end_char": 29
    },
    {
      "id": 5,
      "text": "s'",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 30,
      "end_char": 32,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "ils",
      "lemma": "eux",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 32,
      "end_char": 35
    },
    {
      "id": 7,
      "text": "veulent",
      "lemma": "vouloir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "advcl",
      "start_char": 36,
      "end_char": 43
    },
    {
      "id": 8,
      "text": "participer",
      "lemma": "participer",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 7,
      "deprel": "xcomp",
      "start_char": 44,
      "end_char": 54,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 54,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 46. Sentence

Sentence: Il fallait que je parte avant la fermeture.

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
      "text": "fallait",
      "lemma": "falloir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 5,
      "deprel": "mark",
      "start_char": 11,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 15,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "parte",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "ccomp",
      "start_char": 18,
      "end_char": 23
    },
    {
      "id": 6,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 24,
      "end_char": 29
    },
    {
      "id": 7,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 30,
      "end_char": 32
    },
    {
      "id": 8,
      "text": "fermeture",
      "lemma": "fermeture",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "obl:mod",
      "start_char": 33,
      "end_char": 42,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 42,
      "end_char": 43,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 47. Sentence

Sentence: Je voulais qu'elle comprît la gravité du problème.

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
      "text": "voulais",
      "lemma": "vouloir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 5,
      "deprel": "mark",
      "start_char": 11,
      "end_char": 14,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 14,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "comprît",
      "lemma": "comprendre",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "ccomp",
      "start_char": 19,
      "end_char": 26
    },
    {
      "id": 6,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 27,
      "end_char": 29
    },
    {
      "id": 7,
      "text": "gravité",
      "lemma": "gravité",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "obj",
      "start_char": 30,
      "end_char": 37
    },
    {
      "id": [
        8,
        9
      ],
      "text": "du",
      "start_char": 38,
      "end_char": 40
    },
    {
      "id": 8,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 10,
      "deprel": "case"
    },
    {
      "id": 9,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 10,
      "deprel": "det"
    },
    {
      "id": 10,
      "text": "problème",
      "lemma": "problème",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "nmod",
      "start_char": 41,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 49,
      "end_char": 50,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 48. Sentence

Sentence: Bien qu'il fût tard, les témoins parlaient encore.

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
      "head": 4,
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
      "head": 4,
      "deprel": "nsubj",
      "start_char": 8,
      "end_char": 10
    },
    {
      "id": 4,
      "text": "fût",
      "lemma": "être",
      "upos": "VERB",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "advcl",
      "start_char": 11,
      "end_char": 14
    },
    {
      "id": 5,
      "text": "tard",
      "lemma": "tard",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 15,
      "end_char": 19,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 19,
      "end_char": 20
    },
    {
      "id": 7,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 21,
      "end_char": 24
    },
    {
      "id": 8,
      "text": "témoins",
      "lemma": "témoin",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 25,
      "end_char": 32
    },
    {
      "id": 9,
      "text": "parlaient",
      "lemma": "parler",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 33,
      "end_char": 42
    },
    {
      "id": 10,
      "text": "encore",
      "lemma": "encore",
      "upos": "ADV",
      "head": 9,
      "deprel": "advmod",
      "start_char": 43,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 49,
      "end_char": 50,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 49. Sentence

Sentence: Il aurait fallu que nous eussions prévu ce risque.

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
      "head": 3,
      "deprel": "expl:subj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "aurait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 3,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "fallu",
      "lemma": "falloir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 10,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 16,
      "end_char": 19
    },
    {
      "id": 5,
      "text": "nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Number=Plur|Person=1|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 20,
      "end_char": 24
    },
    {
      "id": 6,
      "text": "eussions",
      "lemma": "voir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 25,
      "end_char": 33
    },
    {
      "id": 7,
      "text": "prévu",
      "lemma": "prévoir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 3,
      "deprel": "ccomp",
      "start_char": 34,
      "end_char": 39
    },
    {
      "id": 8,
      "text": "ce",
      "lemma": "ce",
      "upos": "DET",
      "feats": "Gender=Masc|Number=Sing|PronType=Dem",
      "head": 9,
      "deprel": "det",
      "start_char": 40,
      "end_char": 42
    },
    {
      "id": 9,
      "text": "risque",
      "lemma": "risque",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "obj",
      "start_char": 43,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 49,
      "end_char": 50,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 50. Sentence

Sentence: Je craignais qu'ils ne fussent déjà partis.

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
      "text": "craignais",
      "lemma": "crair",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 12
    },
    {
      "id": 3,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 8,
      "deprel": "mark",
      "start_char": 13,
      "end_char": 16,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "ils",
      "lemma": "eux",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 16,
      "end_char": 19
    },
    {
      "id": 5,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 8,
      "deprel": "advmod",
      "start_char": 20,
      "end_char": 22
    },
    {
      "id": 6,
      "text": "fussent",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 8,
      "deprel": "aux:tense",
      "start_char": 23,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "déjà",
      "lemma": "déjà",
      "upos": "ADV",
      "head": 8,
      "deprel": "advmod",
      "start_char": 31,
      "end_char": 35
    },
    {
      "id": 8,
      "text": "partis",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 2,
      "deprel": "ccomp",
      "start_char": 36,
      "end_char": 42,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 42,
      "end_char": 43,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 51. Sentence

Sentence: Mange ta soupe avant qu'elle refroidisse.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Mange",
      "lemma": "manger",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 0,
      "end_char": 5
    },
    {
      "id": 2,
      "text": "ta",
      "lemma": "son",
      "upos": "DET",
      "feats": "Gender=Fem|Number=Sing|Number[psor]=Sing|Person[psor]=1|Poss=Yes|PronType=Prs",
      "head": 3,
      "deprel": "det",
      "start_char": 6,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "soupe",
      "lemma": "soupe",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 1,
      "deprel": "obj",
      "start_char": 9,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADP",
      "head": 7,
      "deprel": "mark",
      "start_char": 15,
      "end_char": 20
    },
    {
      "id": 5,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 21,
      "end_char": 24,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 24,
      "end_char": 28
    },
    {
      "id": 7,
      "text": "refroidisse",
      "lemma": "refroidir",
      "upos": "VERB",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 1,
      "deprel": "advcl",
      "start_char": 29,
      "end_char": 40,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 40,
      "end_char": 41,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 52. Sentence

Sentence: Prenez vos places et éteignez vos téléphones.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Prenez",
      "lemma": "prendre",
      "upos": "VERB",
      "feats": "Mood=Imp|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 0,
      "end_char": 6
    },
    {
      "id": 2,
      "text": "vos",
      "lemma": "son",
      "upos": "DET",
      "feats": "Number=Plur|Number[psor]=Plur|Person[psor]=2|Poss=Yes|PronType=Prs",
      "head": 3,
      "deprel": "det",
      "start_char": 7,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "places",
      "lemma": "place",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 1,
      "deprel": "obj",
      "start_char": 11,
      "end_char": 17
    },
    {
      "id": 4,
      "text": "et",
      "lemma": "et",
      "upos": "CCONJ",
      "head": 5,
      "deprel": "cc",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 5,
      "text": "éteignez",
      "lemma": "éteindre",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 1,
      "deprel": "conj",
      "start_char": 21,
      "end_char": 29
    },
    {
      "id": 6,
      "text": "vos",
      "lemma": "son",
      "upos": "DET",
      "feats": "Number=Plur|Number[psor]=Plur|Person[psor]=2|Poss=Yes|PronType=Prs",
      "head": 7,
      "deprel": "det",
      "start_char": 30,
      "end_char": 33
    },
    {
      "id": 7,
      "text": "téléphones",
      "lemma": "téléphone",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 5,
      "deprel": "obj",
      "start_char": 34,
      "end_char": 44,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 44,
      "end_char": 45,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 53. Sentence

Sentence: Ne dis rien tant que je n'ai pas terminé.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 2,
      "deprel": "advmod",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "dis",
      "lemma": "dire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 6
    },
    {
      "id": 3,
      "text": "rien",
      "lemma": "rien",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|PronType=Neg",
      "head": 2,
      "deprel": "obj",
      "start_char": 7,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "tant",
      "lemma": "tant",
      "upos": "ADV",
      "head": 10,
      "deprel": "mark",
      "start_char": 12,
      "end_char": 16
    },
    {
      "id": 5,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 4,
      "deprel": "fixed",
      "start_char": 17,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 10,
      "deprel": "nsubj",
      "start_char": 21,
      "end_char": 23
    },
    {
      "id": 7,
      "text": "n'",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 10,
      "deprel": "advmod",
      "start_char": 24,
      "end_char": 26,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": "ai",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 10,
      "deprel": "aux:tense",
      "start_char": 26,
      "end_char": 28
    },
    {
      "id": 9,
      "text": "pas",
      "lemma": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 10,
      "deprel": "advmod",
      "start_char": 29,
      "end_char": 32
    },
    {
      "id": 10,
      "text": "terminé",
      "lemma": "terminer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 2,
      "deprel": "advcl",
      "start_char": 33,
      "end_char": 40,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 40,
      "end_char": 41,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 54. Sentence

Sentence: Soyons prudents lorsque nous traverserons la route.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Soyons",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "cop",
      "start_char": 0,
      "end_char": 6
    },
    {
      "id": 2,
      "text": "prudents",
      "lemma": "prudent",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Plur",
      "head": 0,
      "deprel": "root",
      "start_char": 7,
      "end_char": 15
    },
    {
      "id": 3,
      "text": "lorsque",
      "lemma": "lorsque",
      "upos": "SCONJ",
      "head": 5,
      "deprel": "mark",
      "start_char": 16,
      "end_char": 23
    },
    {
      "id": 4,
      "text": "nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 24,
      "end_char": 28
    },
    {
      "id": 5,
      "text": "traverserons",
      "lemma": "traverser",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "advcl",
      "start_char": 29,
      "end_char": 41
    },
    {
      "id": 6,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 42,
      "end_char": 44
    },
    {
      "id": 7,
      "text": "route",
      "lemma": "route",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "obj",
      "start_char": 45,
      "end_char": 50,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 50,
      "end_char": 51,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 55. Sentence

Sentence: Veuillez signer ici et dater le formulaire.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Veuillez",
      "lemma": "vouloir",
      "upos": "VERB",
      "feats": "Mood=Imp|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 0,
      "end_char": 8
    },
    {
      "id": 2,
      "text": "signer",
      "lemma": "signer",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 1,
      "deprel": "xcomp",
      "start_char": 9,
      "end_char": 15
    },
    {
      "id": 3,
      "text": "ici",
      "lemma": "ici",
      "upos": "ADV",
      "head": 2,
      "deprel": "advmod",
      "start_char": 16,
      "end_char": 19
    },
    {
      "id": 4,
      "text": "et",
      "lemma": "et",
      "upos": "CCONJ",
      "head": 5,
      "deprel": "cc",
      "start_char": 20,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "dater",
      "lemma": "dater",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 2,
      "deprel": "conj",
      "start_char": 23,
      "end_char": 28
    },
    {
      "id": 6,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 29,
      "end_char": 31
    },
    {
      "id": 7,
      "text": "formulaire",
      "lemma": "formulaire",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 2,
      "deprel": "obj",
      "start_char": 32,
      "end_char": 42,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 42,
      "end_char": 43,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 56. Sentence

Sentence: Le dossier est examiné par deux experts indépendants.

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
      "text": "dossier",
      "lemma": "dossier",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "nsubj:pass",
      "start_char": 3,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:pass",
      "start_char": 11,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "examiné",
      "lemma": "examiner",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 0,
      "deprel": "root",
      "start_char": 15,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "par",
      "lemma": "par",
      "upos": "ADP",
      "head": 7,
      "deprel": "case",
      "start_char": 23,
      "end_char": 26
    },
    {
      "id": 6,
      "text": "deux",
      "lemma": "deux",
      "upos": "NUM",
      "feats": "NumType=Card",
      "head": 7,
      "deprel": "nummod",
      "start_char": 27,
      "end_char": 31
    },
    {
      "id": 7,
      "text": "experts",
      "lemma": "expert",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 4,
      "deprel": "obl:agent",
      "start_char": 32,
      "end_char": 39
    },
    {
      "id": 8,
      "text": "indépendants",
      "lemma": "indépendant",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Plur",
      "head": 7,
      "deprel": "amod",
      "start_char": 40,
      "end_char": 52,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 52,
      "end_char": 53,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 57. Sentence

Sentence: La maison a été vendue en moins d'une semaine.

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
      "text": "maison",
      "lemma": "maison",
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
      "text": "vendue",
      "lemma": "vendre",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 0,
      "deprel": "root",
      "start_char": 16,
      "end_char": 22
    },
    {
      "id": 6,
      "text": "en",
      "lemma": "en",
      "upos": "ADP",
      "head": 7,
      "deprel": "case",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 7,
      "text": "moins",
      "lemma": "moins",
      "upos": "ADV",
      "feats": "ExtPos=PRON",
      "head": 5,
      "deprel": "obl:mod",
      "start_char": 26,
      "end_char": 31
    },
    {
      "id": 8,
      "text": "d'",
      "lemma": "de",
      "upos": "ADP",
      "head": 10,
      "deprel": "case",
      "start_char": 32,
      "end_char": 34,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": "une",
      "lemma": "un",
      "upos": "NUM",
      "feats": "Gender=Fem|Number=Sing",
      "head": 10,
      "deprel": "nummod",
      "start_char": 34,
      "end_char": 37
    },
    {
      "id": 10,
      "text": "semaine",
      "lemma": "semaine",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 7,
      "deprel": "obl:arg",
      "start_char": 38,
      "end_char": 45,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 45,
      "end_char": 46,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 58. Sentence

Sentence: Les résultats seront publiés demain matin.

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
      "text": "résultats",
      "lemma": "résultat",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 4,
      "deprel": "nsubj:pass",
      "start_char": 4,
      "end_char": 13
    },
    {
      "id": 3,
      "text": "seront",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:pass",
      "start_char": 14,
      "end_char": 20
    },
    {
      "id": 4,
      "text": "publiés",
      "lemma": "publier",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 0,
      "deprel": "root",
      "start_char": 21,
      "end_char": 28
    },
    {
      "id": 5,
      "text": "demain",
      "lemma": "demain",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 29,
      "end_char": 35
    },
    {
      "id": 6,
      "text": "matin",
      "lemma": "matin",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "obl:mod",
      "start_char": 36,
      "end_char": 41,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
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

## 59. Sentence

Sentence: La décision avait été contestée par plusieurs associations.

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
      "text": "décision",
      "lemma": "décision",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "nsubj:pass",
      "start_char": 3,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "avait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 12,
      "end_char": 17
    },
    {
      "id": 4,
      "text": "été",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 5,
      "deprel": "aux:pass",
      "start_char": 18,
      "end_char": 21
    },
    {
      "id": 5,
      "text": "contestée",
      "lemma": "contester",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 0,
      "deprel": "root",
      "start_char": 22,
      "end_char": 31
    },
    {
      "id": 6,
      "text": "par",
      "lemma": "par",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 32,
      "end_char": 35
    },
    {
      "id": 7,
      "text": "plusieurs",
      "lemma": "plusieurs",
      "upos": "DET",
      "feats": "Number=Plur|PronType=Ind",
      "head": 8,
      "deprel": "det",
      "start_char": 36,
      "end_char": 45
    },
    {
      "id": 8,
      "text": "associations",
      "lemma": "association",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 5,
      "deprel": "obl:agent",
      "start_char": 46,
      "end_char": 58,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 58,
      "end_char": 59,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 60. Sentence

Sentence: Les témoins auraient été interrogés plus tôt si le juge l'avait demandé.

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
      "text": "témoins",
      "lemma": "témoin",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 5,
      "deprel": "nsubj:pass",
      "start_char": 4,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "auraient",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 12,
      "end_char": 20
    },
    {
      "id": 4,
      "text": "été",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Number=Sing|Tense=Past|VerbForm=Part",
      "head": 5,
      "deprel": "aux:pass",
      "start_char": 21,
      "end_char": 24
    },
    {
      "id": 5,
      "text": "interrogés",
      "lemma": "interroger",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 0,
      "deprel": "root",
      "start_char": 25,
      "end_char": 35
    },
    {
      "id": 6,
      "text": "plus",
      "lemma": "plus",
      "upos": "ADV",
      "head": 7,
      "deprel": "advmod",
      "start_char": 36,
      "end_char": 40
    },
    {
      "id": 7,
      "text": "tôt",
      "lemma": "tôt",
      "upos": "ADV",
      "head": 5,
      "deprel": "advmod",
      "start_char": 41,
      "end_char": 44
    },
    {
      "id": 8,
      "text": "si",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 13,
      "deprel": "mark",
      "start_char": 45,
      "end_char": 47
    },
    {
      "id": 9,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 10,
      "deprel": "det",
      "start_char": 48,
      "end_char": 50
    },
    {
      "id": 10,
      "text": "juge",
      "lemma": "juge",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 13,
      "deprel": "nsubj",
      "start_char": 51,
      "end_char": 55
    },
    {
      "id": 11,
      "text": "l'",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=3|PronType=Prs",
      "head": 13,
      "deprel": "obj",
      "start_char": 56,
      "end_char": 58,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": "avait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 13,
      "deprel": "aux:tense",
      "start_char": 58,
      "end_char": 63
    },
    {
      "id": 13,
      "text": "demandé",
      "lemma": "demander",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 5,
      "deprel": "advcl",
      "start_char": 64,
      "end_char": 71,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 71,
      "end_char": 72,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 61. Sentence

Sentence: La porte se ferme automatiquement à vingt heures.

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
      "text": "porte",
      "lemma": "porte",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 4,
      "deprel": "nsubj:pass",
      "start_char": 3,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "se",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 4,
      "deprel": "expl:pass",
      "start_char": 9,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "ferme",
      "lemma": "fermer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 12,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "automatiquement",
      "lemma": "automatiquement",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 18,
      "end_char": 33
    },
    {
      "id": 6,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 34,
      "end_char": 35
    },
    {
      "id": 7,
      "text": "vingt",
      "lemma": "vingt",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 8,
      "deprel": "nummod",
      "start_char": 36,
      "end_char": 41
    },
    {
      "id": 8,
      "text": "heures",
      "lemma": "heure",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 4,
      "deprel": "obl:mod",
      "start_char": 42,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 62. Sentence

Sentence: Ce livre se vend très bien depuis sa sortie.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Ce",
      "lemma": "ce",
      "upos": "DET",
      "feats": "Gender=Masc|Number=Sing|PronType=Dem",
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
      "head": 4,
      "deprel": "nsubj:pass",
      "start_char": 3,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "se",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 4,
      "deprel": "expl:pass",
      "start_char": 9,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "vend",
      "lemma": "vendre",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 12,
      "end_char": 16
    },
    {
      "id": 5,
      "text": "très",
      "lemma": "très",
      "upos": "ADV",
      "head": 6,
      "deprel": "advmod",
      "start_char": 17,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "bien",
      "lemma": "bien",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 22,
      "end_char": 26
    },
    {
      "id": 7,
      "text": "depuis",
      "lemma": "depuis",
      "upos": "ADP",
      "head": 9,
      "deprel": "case",
      "start_char": 27,
      "end_char": 33
    },
    {
      "id": 8,
      "text": "sa",
      "lemma": "son",
      "upos": "DET",
      "feats": "Gender=Fem|Number=Sing|Number[psor]=Sing|Person[psor]=3|Poss=Yes|PronType=Prs",
      "head": 9,
      "deprel": "det",
      "start_char": 34,
      "end_char": 36
    },
    {
      "id": 9,
      "text": "sortie",
      "lemma": "sortie",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 4,
      "deprel": "obl:mod",
      "start_char": 37,
      "end_char": 43,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 43,
      "end_char": 44,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 63. Sentence

Sentence: Elle s'est coupée en préparant le dîner.

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
      "head": 4,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "s'",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 4,
      "deprel": "expl:pass",
      "start_char": 5,
      "end_char": 7,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 7,
      "end_char": 10
    },
    {
      "id": 4,
      "text": "coupée",
      "lemma": "couper",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 11,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "en",
      "lemma": "en",
      "upos": "ADP",
      "head": 6,
      "deprel": "mark",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "préparant",
      "lemma": "préparer",
      "upos": "VERB",
      "feats": "Tense=Pres|VerbForm=Part",
      "head": 4,
      "deprel": "advcl",
      "start_char": 21,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 31,
      "end_char": 33
    },
    {
      "id": 8,
      "text": "dîner",
      "lemma": "dîner",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 6,
      "deprel": "obj",
      "start_char": 34,
      "end_char": 39,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 39,
      "end_char": 40,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 64. Sentence

Sentence: Ils se sont parlé sans se comprendre vraiment.

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
      "end_char": 17
    },
    {
      "id": 5,
      "text": "sans",
      "lemma": "sans",
      "upos": "ADP",
      "head": 7,
      "deprel": "mark",
      "start_char": 18,
      "end_char": 22
    },
    {
      "id": 6,
      "text": "se",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 7,
      "deprel": "expl:pv",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 7,
      "text": "comprendre",
      "lemma": "comprendre",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 4,
      "deprel": "advcl",
      "start_char": 26,
      "end_char": 36
    },
    {
      "id": 8,
      "text": "vraiment",
      "lemma": "vraiment",
      "upos": "ADV",
      "head": 7,
      "deprel": "advmod",
      "start_char": 37,
      "end_char": 45,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 45,
      "end_char": 46,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 65. Sentence

Sentence: Les preuves se sont accumulées au fil de l'enquête.

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
      "text": "preuves",
      "lemma": "preuve",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 5,
      "deprel": "nsubj:pass",
      "start_char": 4,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "se",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 5,
      "deprel": "expl:pass",
      "start_char": 12,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "sont",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 15,
      "end_char": 19
    },
    {
      "id": 5,
      "text": "accumulées",
      "lemma": "accumuler",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 20,
      "end_char": 30
    },
    {
      "id": [
        6,
        7
      ],
      "text": "au",
      "start_char": 31,
      "end_char": 33
    },
    {
      "id": 6,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 8,
      "deprel": "case"
    },
    {
      "id": 7,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "det"
    },
    {
      "id": 8,
      "text": "fil",
      "lemma": "fil",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "obl:mod",
      "start_char": 34,
      "end_char": 37
    },
    {
      "id": 9,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 11,
      "deprel": "case",
      "start_char": 38,
      "end_char": 40
    },
    {
      "id": 10,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 41,
      "end_char": 43,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": "enquête",
      "lemma": "enquête",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "nmod",
      "start_char": 43,
      "end_char": 50,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 50,
      "end_char": 51,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 66. Sentence

Sentence: Il pleut sur la ville depuis l'aube.

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
      "text": "pleut",
      "lemma": "pleuvoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "sur",
      "lemma": "sur",
      "upos": "ADP",
      "head": 5,
      "deprel": "case",
      "start_char": 9,
      "end_char": 12
    },
    {
      "id": 4,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 13,
      "end_char": 15
    },
    {
      "id": 5,
      "text": "ville",
      "lemma": "ville",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "obl:mod",
      "start_char": 16,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "depuis",
      "lemma": "depuis",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 22,
      "end_char": 28
    },
    {
      "id": 7,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 29,
      "end_char": 31,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": "aube",
      "lemma": "aube",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "obl:mod",
      "start_char": 31,
      "end_char": 35,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 35,
      "end_char": 36,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 67. Sentence

Sentence: Il y a trois solutions possibles.

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
      "head": 3,
      "deprel": "expl:subj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "y",
      "lemma": "y",
      "upos": "PRON",
      "feats": "Emph=No|Person=3|PronType=Prs",
      "head": 3,
      "deprel": "expl:comp",
      "start_char": 3,
      "end_char": 4
    },
    {
      "id": 3,
      "text": "a",
      "lemma": "avoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 6
    },
    {
      "id": 4,
      "text": "trois",
      "lemma": "trois",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 5,
      "deprel": "nummod",
      "start_char": 7,
      "end_char": 12
    },
    {
      "id": 5,
      "text": "solutions",
      "lemma": "solution",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 3,
      "deprel": "obj",
      "start_char": 13,
      "end_char": 22
    },
    {
      "id": 6,
      "text": "possibles",
      "lemma": "possible",
      "upos": "ADJ",
      "feats": "Number=Plur",
      "head": 5,
      "deprel": "amod",
      "start_char": 23,
      "end_char": 32,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
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

## 68. Sentence

Sentence: Il s'agit d'un problème plus complexe qu'il n'y paraît.

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
      "head": 3,
      "deprel": "expl:subj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "s'",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 3,
      "deprel": "expl:pv",
      "start_char": 3,
      "end_char": 5,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "agit",
      "lemma": "agir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 9
    },
    {
      "id": 4,
      "text": "d'",
      "lemma": "de",
      "upos": "ADP",
      "head": 6,
      "deprel": "case",
      "start_char": 10,
      "end_char": 12,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": "un",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Masc|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 12,
      "end_char": 14
    },
    {
      "id": 6,
      "text": "problème",
      "lemma": "problème",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "obl:arg",
      "start_char": 15,
      "end_char": 23
    },
    {
      "id": 7,
      "text": "plus",
      "lemma": "plus",
      "upos": "ADV",
      "head": 8,
      "deprel": "advmod",
      "start_char": 24,
      "end_char": 28
    },
    {
      "id": 8,
      "text": "complexe",
      "lemma": "complexe",
      "upos": "ADJ",
      "feats": "Number=Sing",
      "head": 6,
      "deprel": "amod",
      "start_char": 29,
      "end_char": 37
    },
    {
      "id": 9,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 13,
      "deprel": "mark",
      "start_char": 38,
      "end_char": 41,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 13,
      "deprel": "expl:subj",
      "start_char": 41,
      "end_char": 43
    },
    {
      "id": 11,
      "text": "n'",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 13,
      "deprel": "advmod",
      "start_char": 44,
      "end_char": 46,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": "y",
      "lemma": "y",
      "upos": "PRON",
      "feats": "Emph=No|Person=3|PronType=Prs",
      "head": 13,
      "deprel": "expl:comp",
      "start_char": 46,
      "end_char": 47
    },
    {
      "id": 13,
      "text": "paraît",
      "lemma": "paraître",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "ccomp",
      "start_char": 48,
      "end_char": 54,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 54,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 69. Sentence

Sentence: Il manque deux pages au dossier.

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
      "text": "manque",
      "lemma": "manquer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "deux",
      "lemma": "deux",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 4,
      "deprel": "nummod",
      "start_char": 10,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "pages",
      "lemma": "page",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 2,
      "deprel": "obj",
      "start_char": 15,
      "end_char": 20
    },
    {
      "id": [
        5,
        6
      ],
      "text": "au",
      "start_char": 21,
      "end_char": 23
    },
    {
      "id": 5,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 7,
      "deprel": "case"
    },
    {
      "id": 6,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det"
    },
    {
      "id": 7,
      "text": "dossier",
      "lemma": "dossier",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 2,
      "deprel": "obl:arg",
      "start_char": 24,
      "end_char": 31,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 31,
      "end_char": 32,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 70. Sentence

Sentence: Il est arrivé un accident près de la gare.

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
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 3,
      "end_char": 6
    },
    {
      "id": 3,
      "text": "arrivé",
      "lemma": "arriver",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 7,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "un",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Masc|Number=Sing|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 14,
      "end_char": 16
    },
    {
      "id": 5,
      "text": "accident",
      "lemma": "accident",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "obj",
      "start_char": 17,
      "end_char": 25
    },
    {
      "id": 6,
      "text": "près",
      "lemma": "près",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 26,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 9,
      "deprel": "case",
      "start_char": 31,
      "end_char": 33
    },
    {
      "id": 8,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 9,
      "deprel": "det",
      "start_char": 34,
      "end_char": 36
    },
    {
      "id": 9,
      "text": "gare",
      "lemma": "gare",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 6,
      "deprel": "obl:arg",
      "start_char": 37,
      "end_char": 41,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
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

## 71. Sentence

Sentence: Il paraît que le ministre démissionnera ce soir.

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
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 6,
      "deprel": "mark",
      "start_char": 10,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 14,
      "end_char": 16
    },
    {
      "id": 5,
      "text": "ministre",
      "lemma": "ministre",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 17,
      "end_char": 25
    },
    {
      "id": 6,
      "text": "démissionnera",
      "lemma": "démissionner",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 2,
      "deprel": "csubj",
      "start_char": 26,
      "end_char": 39
    },
    {
      "id": 7,
      "text": "ce",
      "lemma": "ce",
      "upos": "DET",
      "feats": "Gender=Masc|Number=Sing|PronType=Dem",
      "head": 8,
      "deprel": "det",
      "start_char": 40,
      "end_char": 42
    },
    {
      "id": 8,
      "text": "soir",
      "lemma": "soir",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 6,
      "deprel": "obl:mod",
      "start_char": 43,
      "end_char": 47,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 47,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 72. Sentence

Sentence: Il faisait si froid que les vitres gelaient.

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
      "text": "faisait",
      "lemma": "faire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "si",
      "lemma": "si",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 11,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "froid",
      "lemma": "froid",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 2,
      "deprel": "xcomp",
      "start_char": 14,
      "end_char": 19
    },
    {
      "id": 5,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 8,
      "deprel": "mark",
      "start_char": 20,
      "end_char": 23
    },
    {
      "id": 6,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 24,
      "end_char": 27
    },
    {
      "id": 7,
      "text": "vitres",
      "lemma": "vitre",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 28,
      "end_char": 34
    },
    {
      "id": 8,
      "text": "gelaient",
      "lemma": "geler",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "ccomp",
      "start_char": 35,
      "end_char": 43,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
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

## 73. Sentence

Sentence: Il aurait fallu prévenir les riverains plus tôt.

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
      "head": 3,
      "deprel": "expl:subj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "aurait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 3,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "fallu",
      "lemma": "falloir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 10,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "prévenir",
      "lemma": "prévenir",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 3,
      "deprel": "ccomp",
      "start_char": 16,
      "end_char": 24
    },
    {
      "id": 5,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 25,
      "end_char": 28
    },
    {
      "id": 6,
      "text": "riverains",
      "lemma": "riverain",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 4,
      "deprel": "obj",
      "start_char": 29,
      "end_char": 38
    },
    {
      "id": 7,
      "text": "plus",
      "lemma": "plus",
      "upos": "ADV",
      "head": 8,
      "deprel": "advmod",
      "start_char": 39,
      "end_char": 43
    },
    {
      "id": 8,
      "text": "tôt",
      "lemma": "tôt",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 44,
      "end_char": 47,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 47,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 74. Sentence

Sentence: Il semble que personne n'ait compris la consigne.

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
      "text": "semble",
      "lemma": "sembler",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 10,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "personne",
      "lemma": "personne",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|PronType=Neg",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 14,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "n'",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 7,
      "deprel": "advmod",
      "start_char": 23,
      "end_char": 25,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "ait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 25,
      "end_char": 28
    },
    {
      "id": 7,
      "text": "compris",
      "lemma": "comprendre",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 2,
      "deprel": "ccomp",
      "start_char": 29,
      "end_char": 36
    },
    {
      "id": 8,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 9,
      "deprel": "det",
      "start_char": 37,
      "end_char": 39
    },
    {
      "id": 9,
      "text": "consigne",
      "lemma": "consigne",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 7,
      "deprel": "obj",
      "start_char": 40,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 75. Sentence

Sentence: Il se peut que la réunion soit annulée.

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
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "se",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 3,
      "deprel": "expl:pv",
      "start_char": 3,
      "end_char": 5
    },
    {
      "id": 3,
      "text": "peut",
      "lemma": "pouvoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 6,
      "end_char": 10
    },
    {
      "id": 4,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 8,
      "deprel": "mark",
      "start_char": 11,
      "end_char": 14
    },
    {
      "id": 5,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 15,
      "end_char": 17
    },
    {
      "id": 6,
      "text": "réunion",
      "lemma": "réunion",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "nsubj:pass",
      "start_char": 18,
      "end_char": 25
    },
    {
      "id": 7,
      "text": "soit",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 8,
      "deprel": "aux:pass",
      "start_char": 26,
      "end_char": 30
    },
    {
      "id": 8,
      "text": "annulée",
      "lemma": "annuler",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 3,
      "deprel": "ccomp",
      "start_char": 31,
      "end_char": 38,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 38,
      "end_char": 39,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 76. Sentence

Sentence: Je vais partir dans cinq minutes.

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
      "text": "vais",
      "lemma": "aller",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "partir",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 2,
      "deprel": "xcomp",
      "start_char": 8,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "dans",
      "lemma": "dans",
      "upos": "ADP",
      "head": 6,
      "deprel": "case",
      "start_char": 15,
      "end_char": 19
    },
    {
      "id": 5,
      "text": "cinq",
      "lemma": "cinq",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 6,
      "deprel": "nummod",
      "start_char": 20,
      "end_char": 24
    },
    {
      "id": 6,
      "text": "minutes",
      "lemma": "minute",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 3,
      "deprel": "obl:mod",
      "start_char": 25,
      "end_char": 32,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 32,
      "end_char": 33,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 77. Sentence

Sentence: Nous venons de recevoir les résultats.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "venons",
      "lemma": "venir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 4,
      "deprel": "mark",
      "start_char": 12,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "recevoir",
      "lemma": "recevoir",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 2,
      "deprel": "xcomp",
      "start_char": 15,
      "end_char": 23
    },
    {
      "id": 5,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 24,
      "end_char": 27
    },
    {
      "id": 6,
      "text": "résultats",
      "lemma": "résultat",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 4,
      "deprel": "obj",
      "start_char": 28,
      "end_char": 37,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 37,
      "end_char": 38,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 78. Sentence

Sentence: Elle est en train de préparer son exposé.

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
      "deprel": "cop",
      "start_char": 5,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "en",
      "lemma": "en",
      "upos": "ADP",
      "head": 0,
      "deprel": "root",
      "start_char": 9,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "train",
      "lemma": "train",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "fixed",
      "start_char": 12,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 6,
      "deprel": "mark",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "préparer",
      "lemma": "préparer",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 3,
      "deprel": "xcomp",
      "start_char": 21,
      "end_char": 29
    },
    {
      "id": 7,
      "text": "son",
      "lemma": "son",
      "upos": "DET",
      "feats": "Gender=Masc|Number=Sing|Number[psor]=Sing|Person[psor]=3|Poss=Yes|PronType=Prs",
      "head": 8,
      "deprel": "det",
      "start_char": 30,
      "end_char": 33
    },
    {
      "id": 8,
      "text": "exposé",
      "lemma": "exposé",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 6,
      "deprel": "obj",
      "start_char": 34,
      "end_char": 40,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 40,
      "end_char": 41,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 79. Sentence

Sentence: Ils allaient signer quand l'avocat a demandé une pause.

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
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 3
    },
    {
      "id": 2,
      "text": "allaient",
      "lemma": "aller",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 4,
      "end_char": 12
    },
    {
      "id": 3,
      "text": "signer",
      "lemma": "signer",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 2,
      "deprel": "xcomp",
      "start_char": 13,
      "end_char": 19
    },
    {
      "id": 4,
      "text": "quand",
      "lemma": "quand",
      "upos": "SCONJ",
      "head": 8,
      "deprel": "mark",
      "start_char": 20,
      "end_char": 25
    },
    {
      "id": 5,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 26,
      "end_char": 28,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "avocat",
      "lemma": "avocat",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 28,
      "end_char": 34
    },
    {
      "id": 7,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 8,
      "deprel": "aux:tense",
      "start_char": 35,
      "end_char": 36
    },
    {
      "id": 8,
      "text": "demandé",
      "lemma": "demander",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 3,
      "deprel": "advcl",
      "start_char": 37,
      "end_char": 44
    },
    {
      "id": 9,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 10,
      "deprel": "det",
      "start_char": 45,
      "end_char": 48
    },
    {
      "id": 10,
      "text": "pause",
      "lemma": "pause",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "obj",
      "start_char": 49,
      "end_char": 54,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 54,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 80. Sentence

Sentence: Tu avais failli tomber en descendant l'escalier.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "avais",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Imp|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 3,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "failli",
      "lemma": "faillir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 9,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "tomber",
      "lemma": "tomber",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 3,
      "deprel": "xcomp",
      "start_char": 16,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "en",
      "lemma": "en",
      "upos": "ADP",
      "head": 6,
      "deprel": "mark",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 6,
      "text": "descendant",
      "lemma": "descendre",
      "upos": "VERB",
      "feats": "Tense=Pres|VerbForm=Part",
      "head": 4,
      "deprel": "advcl",
      "start_char": 26,
      "end_char": 36
    },
    {
      "id": 7,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 37,
      "end_char": 39,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": "escalier",
      "lemma": "escalier",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 6,
      "deprel": "obj",
      "start_char": 39,
      "end_char": 47,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 47,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 81. Sentence

Sentence: Je fais réparer ma voiture par un mécanicien.

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
      "head": 3,
      "deprel": "nsubj:caus",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "fais",
      "lemma": "faire",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:caus",
      "start_char": 3,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "réparer",
      "lemma": "réparer",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 0,
      "deprel": "root",
      "start_char": 8,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "ma",
      "lemma": "son",
      "upos": "DET",
      "feats": "Gender=Fem|Number=Sing|Number[psor]=Sing|Person[psor]=1|Poss=Yes|PronType=Prs",
      "head": 5,
      "deprel": "det",
      "start_char": 16,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "voiture",
      "lemma": "voiture",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 3,
      "deprel": "obj",
      "start_char": 19,
      "end_char": 26
    },
    {
      "id": 6,
      "text": "par",
      "lemma": "par",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 27,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "un",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Masc|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 31,
      "end_char": 33
    },
    {
      "id": 8,
      "text": "mécanicien",
      "lemma": "mécanicien",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "obl:agent",
      "start_char": 34,
      "end_char": 44,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 44,
      "end_char": 45,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 82. Sentence

Sentence: Elle laisse parler les enfants avant de répondre.

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
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "laisse",
      "lemma": "laisser",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "parler",
      "lemma": "parler",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 2,
      "deprel": "xcomp",
      "start_char": 12,
      "end_char": 18
    },
    {
      "id": 4,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 19,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "enfants",
      "lemma": "enfant",
      "upos": "NOUN",
      "feats": "Number=Plur",
      "head": 3,
      "deprel": "obj",
      "start_char": 23,
      "end_char": 30
    },
    {
      "id": 6,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 31,
      "end_char": 36
    },
    {
      "id": 7,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 8,
      "deprel": "mark",
      "start_char": 37,
      "end_char": 39
    },
    {
      "id": 8,
      "text": "répondre",
      "lemma": "répondre",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 6,
      "deprel": "xcomp",
      "start_char": 40,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 83. Sentence

Sentence: Nous avons vu partir le dernier train.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "avons",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 5,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "vu",
      "lemma": "voir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 11,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "partir",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 3,
      "deprel": "xcomp",
      "start_char": 14,
      "end_char": 20
    },
    {
      "id": 5,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 21,
      "end_char": 23
    },
    {
      "id": 6,
      "text": "dernier",
      "lemma": "dernier",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "amod",
      "start_char": 24,
      "end_char": 31
    },
    {
      "id": 7,
      "text": "train",
      "lemma": "train",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obj",
      "start_char": 32,
      "end_char": 37,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 37,
      "end_char": 38,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 84. Sentence

Sentence: Il entendait chanter les voisins chaque soir.

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
      "text": "entendait",
      "lemma": "entendre",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 12
    },
    {
      "id": 3,
      "text": "chanter",
      "lemma": "chanter",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 2,
      "deprel": "xcomp",
      "start_char": 13,
      "end_char": 20
    },
    {
      "id": 4,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 21,
      "end_char": 24
    },
    {
      "id": 5,
      "text": "voisins",
      "lemma": "voisin",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 3,
      "deprel": "obj",
      "start_char": 25,
      "end_char": 32
    },
    {
      "id": 6,
      "text": "chaque",
      "lemma": "chaque",
      "upos": "DET",
      "feats": "Number=Sing|PronType=Ind",
      "head": 7,
      "deprel": "det",
      "start_char": 33,
      "end_char": 39
    },
    {
      "id": 7,
      "text": "soir",
      "lemma": "soir",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "obl:mod",
      "start_char": 40,
      "end_char": 44,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 44,
      "end_char": 45,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 85. Sentence

Sentence: Je lui ai fait relire le contrat avant signature.

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
      "head": 5,
      "deprel": "nsubj:caus",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "lui",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 5,
      "deprel": "iobj:agent",
      "start_char": 3,
      "end_char": 6
    },
    {
      "id": 3,
      "text": "ai",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 7,
      "end_char": 9
    },
    {
      "id": 4,
      "text": "fait",
      "lemma": "faire",
      "upos": "AUX",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 5,
      "deprel": "aux:caus",
      "start_char": 10,
      "end_char": 14
    },
    {
      "id": 5,
      "text": "relire",
      "lemma": "relire",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 0,
      "deprel": "root",
      "start_char": 15,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 22,
      "end_char": 24
    },
    {
      "id": 7,
      "text": "contrat",
      "lemma": "contrat",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "obj:agent",
      "start_char": 25,
      "end_char": 32
    },
    {
      "id": 8,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADP",
      "head": 9,
      "deprel": "case",
      "start_char": 33,
      "end_char": 38
    },
    {
      "id": 9,
      "text": "signature",
      "lemma": "signature",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "obl:mod",
      "start_char": 39,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
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

## 86. Sentence

Sentence: Ayant terminé son travail, elle rentra chez elle.

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
      "head": 7,
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
      "head": 7,
      "deprel": "nsubj",
      "start_char": 27,
      "end_char": 31
    },
    {
      "id": 7,
      "text": "rentra",
      "lemma": "rentrer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 32,
      "end_char": 38
    },
    {
      "id": 8,
      "text": "chez",
      "lemma": "chez",
      "upos": "ADP",
      "head": 9,
      "deprel": "case",
      "start_char": 39,
      "end_char": 43
    },
    {
      "id": 9,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=Yes|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "obl:mod",
      "start_char": 44,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 87. Sentence

Sentence: En traversant la rue, il regardait son téléphone.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "En",
      "lemma": "en",
      "upos": "ADP",
      "head": 2,
      "deprel": "mark",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "traversant",
      "lemma": "traverser",
      "upos": "VERB",
      "feats": "Tense=Pres|VerbForm=Part",
      "head": 7,
      "deprel": "advcl",
      "start_char": 3,
      "end_char": 13
    },
    {
      "id": 3,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 4,
      "deprel": "det",
      "start_char": 14,
      "end_char": 16
    },
    {
      "id": 4,
      "text": "rue",
      "lemma": "rue",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "obj",
      "start_char": 17,
      "end_char": 20,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 20,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 22,
      "end_char": 24
    },
    {
      "id": 7,
      "text": "regardait",
      "lemma": "regarder",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 25,
      "end_char": 34
    },
    {
      "id": 8,
      "text": "son",
      "lemma": "son",
      "upos": "DET",
      "feats": "Gender=Masc|Number=Sing|Number[psor]=Sing|Person[psor]=3|Poss=Yes|PronType=Prs",
      "head": 9,
      "deprel": "det",
      "start_char": 35,
      "end_char": 38
    },
    {
      "id": 9,
      "text": "téléphone",
      "lemma": "téléphone",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "obj",
      "start_char": 39,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 88. Sentence

Sentence: Fatigués par le voyage, les enfants se sont endormis rapidement.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Fatigués",
      "lemma": "fatiguer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 10,
      "deprel": "advcl",
      "start_char": 0,
      "end_char": 8
    },
    {
      "id": 2,
      "text": "par",
      "lemma": "par",
      "upos": "ADP",
      "head": 4,
      "deprel": "case",
      "start_char": 9,
      "end_char": 12
    },
    {
      "id": 3,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 4,
      "deprel": "det",
      "start_char": 13,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "voyage",
      "lemma": "voyage",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 1,
      "deprel": "obl:agent",
      "start_char": 16,
      "end_char": 22,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 22,
      "end_char": 23
    },
    {
      "id": 6,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 24,
      "end_char": 27
    },
    {
      "id": 7,
      "text": "enfants",
      "lemma": "enfant",
      "upos": "NOUN",
      "feats": "Number=Plur",
      "head": 10,
      "deprel": "nsubj",
      "start_char": 28,
      "end_char": 35
    },
    {
      "id": 8,
      "text": "se",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 10,
      "deprel": "obj",
      "start_char": 36,
      "end_char": 38
    },
    {
      "id": 9,
      "text": "sont",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 10,
      "deprel": "aux:tense",
      "start_char": 39,
      "end_char": 43
    },
    {
      "id": 10,
      "text": "endormis",
      "lemma": "endormir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 44,
      "end_char": 52
    },
    {
      "id": 11,
      "text": "rapidement",
      "lemma": "rapidement",
      "upos": "ADV",
      "head": 10,
      "deprel": "advmod",
      "start_char": 53,
      "end_char": 63,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 63,
      "end_char": 64,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 89. Sentence

Sentence: La lettre écrite hier contenait plusieurs erreurs.

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
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "écrite",
      "lemma": "écrire",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 2,
      "deprel": "acl",
      "start_char": 10,
      "end_char": 16
    },
    {
      "id": 4,
      "text": "hier",
      "lemma": "hier",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 17,
      "end_char": 21
    },
    {
      "id": 5,
      "text": "contenait",
      "lemma": "contenir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 22,
      "end_char": 31
    },
    {
      "id": 6,
      "text": "plusieurs",
      "lemma": "plusieurs",
      "upos": "DET",
      "feats": "Number=Plur|PronType=Ind",
      "head": 7,
      "deprel": "det",
      "start_char": 32,
      "end_char": 41
    },
    {
      "id": 7,
      "text": "erreurs",
      "lemma": "erreur",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 5,
      "deprel": "obj",
      "start_char": 42,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 49,
      "end_char": 50,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 90. Sentence

Sentence: Les documents signés seront archivés demain.

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
      "text": "documents",
      "lemma": "document",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 5,
      "deprel": "nsubj:pass",
      "start_char": 4,
      "end_char": 13
    },
    {
      "id": 3,
      "text": "signés",
      "lemma": "signer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 2,
      "deprel": "acl",
      "start_char": 14,
      "end_char": 20
    },
    {
      "id": 4,
      "text": "seront",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:pass",
      "start_char": 21,
      "end_char": 27
    },
    {
      "id": 5,
      "text": "archivés",
      "lemma": "archiver",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 0,
      "deprel": "root",
      "start_char": 28,
      "end_char": 36
    },
    {
      "id": 6,
      "text": "demain",
      "lemma": "demain",
      "upos": "ADV",
      "head": 5,
      "deprel": "advmod",
      "start_char": 37,
      "end_char": 43,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 43,
      "end_char": 44,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 91. Sentence

Sentence: Si tu viens demain, je te montrerai ce que j'ai trouvé.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Si",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 3,
      "deprel": "mark",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 5
    },
    {
      "id": 3,
      "text": "viens",
      "lemma": "venir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 8,
      "deprel": "advcl",
      "start_char": 6,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "demain",
      "lemma": "demain",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 12,
      "end_char": 18,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 18,
      "end_char": 19
    },
    {
      "id": 6,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 20,
      "end_char": 22
    },
    {
      "id": 7,
      "text": "te",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 8,
      "deprel": "iobj",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 8,
      "text": "montrerai",
      "lemma": "montrer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 26,
      "end_char": 35
    },
    {
      "id": 9,
      "text": "ce",
      "lemma": "ce",
      "upos": "PRON",
      "feats": "Gender=Masc|Person=3|PronType=Dem",
      "head": 8,
      "deprel": "obj",
      "start_char": 36,
      "end_char": 38
    },
    {
      "id": 10,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 13,
      "deprel": "obj",
      "start_char": 39,
      "end_char": 42
    },
    {
      "id": 11,
      "text": "j'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 13,
      "deprel": "nsubj",
      "start_char": 43,
      "end_char": 45,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": "ai",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 13,
      "deprel": "aux:tense",
      "start_char": 45,
      "end_char": 47
    },
    {
      "id": 13,
      "text": "trouvé",
      "lemma": "trouver",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 9,
      "deprel": "acl:relcl",
      "start_char": 48,
      "end_char": 54,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 54,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 92. Sentence

Sentence: Si tu venais demain, je te montrerais ce que j'aurais préparé.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Si",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 3,
      "deprel": "mark",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 5
    },
    {
      "id": 3,
      "text": "venais",
      "lemma": "venir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Imp|VerbForm=Fin",
      "head": 8,
      "deprel": "advcl",
      "start_char": 6,
      "end_char": 12
    },
    {
      "id": 4,
      "text": "demain",
      "lemma": "demain",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 13,
      "end_char": 19,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 19,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 21,
      "end_char": 23
    },
    {
      "id": 7,
      "text": "te",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 8,
      "deprel": "iobj",
      "start_char": 24,
      "end_char": 26
    },
    {
      "id": 8,
      "text": "montrerais",
      "lemma": "montrer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 27,
      "end_char": 37
    },
    {
      "id": 9,
      "text": "ce",
      "lemma": "ce",
      "upos": "PRON",
      "feats": "Gender=Masc|Person=3|PronType=Dem",
      "head": 8,
      "deprel": "obj",
      "start_char": 38,
      "end_char": 40
    },
    {
      "id": 10,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 13,
      "deprel": "obj",
      "start_char": 41,
      "end_char": 44
    },
    {
      "id": 11,
      "text": "j'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 13,
      "deprel": "nsubj",
      "start_char": 45,
      "end_char": 47,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": "aurais",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 13,
      "deprel": "aux:tense",
      "start_char": 47,
      "end_char": 53
    },
    {
      "id": 13,
      "text": "préparé",
      "lemma": "préparer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 9,
      "deprel": "acl:relcl",
      "start_char": 54,
      "end_char": 61,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 61,
      "end_char": 62,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 93. Sentence

Sentence: Si tu étais venu hier, tu aurais vu ce que nous avions construit.

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
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 5
    },
    {
      "id": 3,
      "text": "étais",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Imp|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 6,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "venu",
      "lemma": "venir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 9,
      "deprel": "advcl",
      "start_char": 12,
      "end_char": 16
    },
    {
      "id": 5,
      "text": "hier",
      "lemma": "hier",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 17,
      "end_char": 21,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 21,
      "end_char": 22
    },
    {
      "id": 7,
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 8,
      "text": "aurais",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:tense",
      "start_char": 26,
      "end_char": 32
    },
    {
      "id": 9,
      "text": "vu",
      "lemma": "voir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "start_char": 33,
      "end_char": 35
    },
    {
      "id": 10,
      "text": "ce",
      "lemma": "ce",
      "upos": "PRON",
      "feats": "Gender=Masc|Person=3|PronType=Dem",
      "head": 9,
      "deprel": "obj",
      "start_char": 36,
      "end_char": 38
    },
    {
      "id": 11,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 14,
      "deprel": "obj",
      "start_char": 39,
      "end_char": 42
    },
    {
      "id": 12,
      "text": "nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 14,
      "deprel": "nsubj",
      "start_char": 43,
      "end_char": 47
    },
    {
      "id": 13,
      "text": "avions",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 14,
      "deprel": "aux:tense",
      "start_char": 48,
      "end_char": 54
    },
    {
      "id": 14,
      "text": "construit",
      "lemma": "construire",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 10,
      "deprel": "acl:relcl",
      "start_char": 55,
      "end_char": 64,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 64,
      "end_char": 65,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 94. Sentence

Sentence: Quand elle aura fini ce qu'elle avait commencé, elle pourra se reposer.

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
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 6,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "aura",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 11,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "fini",
      "lemma": "finir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 12,
      "deprel": "advcl",
      "start_char": 16,
      "end_char": 20
    },
    {
      "id": 5,
      "text": "ce",
      "lemma": "ce",
      "upos": "PRON",
      "feats": "Gender=Masc|Person=3|PronType=Dem",
      "head": 4,
      "deprel": "obj",
      "start_char": 21,
      "end_char": 23
    },
    {
      "id": 6,
      "text": "qu'",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 9,
      "deprel": "obj",
      "start_char": 24,
      "end_char": 27,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
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
      "id": 8,
      "text": "avait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:tense",
      "start_char": 32,
      "end_char": 37
    },
    {
      "id": 9,
      "text": "commencé",
      "lemma": "commencer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 5,
      "deprel": "acl:relcl",
      "start_char": 38,
      "end_char": 46,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 46,
      "end_char": 47
    },
    {
      "id": 11,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 12,
      "deprel": "nsubj",
      "start_char": 48,
      "end_char": 52
    },
    {
      "id": 12,
      "text": "pourra",
      "lemma": "pouvoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 53,
      "end_char": 59
    },
    {
      "id": 13,
      "text": "se",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 14,
      "deprel": "expl:pass",
      "start_char": 60,
      "end_char": 62
    },
    {
      "id": 14,
      "text": "reposer",
      "lemma": "reposer",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 12,
      "deprel": "xcomp",
      "start_char": 63,
      "end_char": 70,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 12,
      "deprel": "punct",
      "start_char": 70,
      "end_char": 71,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 95. Sentence

Sentence: Il m'a dit qu'il partirait dès qu'il aurait reçu la confirmation.

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
      "head": 4,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "m'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 4,
      "deprel": "iobj",
      "start_char": 3,
      "end_char": 5,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 5,
      "end_char": 6
    },
    {
      "id": 4,
      "text": "dit",
      "lemma": "dire",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 7,
      "end_char": 10
    },
    {
      "id": 5,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 11,
      "end_char": 14,
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
      "start_char": 14,
      "end_char": 16
    },
    {
      "id": 7,
      "text": "partirait",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "ccomp",
      "start_char": 17,
      "end_char": 26
    },
    {
      "id": 8,
      "text": "dès",
      "lemma": "dès",
      "upos": "ADP",
      "head": 12,
      "deprel": "mark",
      "start_char": 27,
      "end_char": 30
    },
    {
      "id": 9,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 12,
      "deprel": "mark",
      "start_char": 31,
      "end_char": 34,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 12,
      "deprel": "nsubj",
      "start_char": 34,
      "end_char": 36
    },
    {
      "id": 11,
      "text": "aurait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 12,
      "deprel": "aux:tense",
      "start_char": 37,
      "end_char": 43
    },
    {
      "id": 12,
      "text": "reçu",
      "lemma": "recevoir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 7,
      "deprel": "advcl",
      "start_char": 44,
      "end_char": 48
    },
    {
      "id": 13,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 14,
      "deprel": "det",
      "start_char": 49,
      "end_char": 51
    },
    {
      "id": 14,
      "text": "confirmation",
      "lemma": "confirmation",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 12,
      "deprel": "obj",
      "start_char": 52,
      "end_char": 64,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 64,
      "end_char": 65,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 96. Sentence

Sentence: Je ne pense pas qu'il ait compris ce que nous voulions obtenir.

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
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 3,
      "deprel": "advmod",
      "start_char": 3,
      "end_char": 5
    },
    {
      "id": 3,
      "text": "pense",
      "lemma": "penser",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 6,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "pas",
      "lemma": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 3,
      "deprel": "advmod",
      "start_char": 12,
      "end_char": 15
    },
    {
      "id": 5,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 8,
      "deprel": "mark",
      "start_char": 16,
      "end_char": 19,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 19,
      "end_char": 21
    },
    {
      "id": 7,
      "text": "ait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 8,
      "deprel": "aux:tense",
      "start_char": 22,
      "end_char": 25
    },
    {
      "id": 8,
      "text": "compris",
      "lemma": "comprendre",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 3,
      "deprel": "ccomp",
      "start_char": 26,
      "end_char": 33
    },
    {
      "id": 9,
      "text": "ce",
      "lemma": "ce",
      "upos": "PRON",
      "feats": "Gender=Masc|Person=3|PronType=Dem",
      "head": 8,
      "deprel": "obj",
      "start_char": 34,
      "end_char": 36
    },
    {
      "id": 10,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 13,
      "deprel": "obj",
      "start_char": 37,
      "end_char": 40
    },
    {
      "id": 11,
      "text": "nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 12,
      "deprel": "nsubj",
      "start_char": 41,
      "end_char": 45
    },
    {
      "id": 12,
      "text": "voulions",
      "lemma": "vouloir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 9,
      "deprel": "acl:relcl",
      "start_char": 46,
      "end_char": 54
    },
    {
      "id": 13,
      "text": "obtenir",
      "lemma": "obtenir",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 12,
      "deprel": "xcomp",
      "start_char": 55,
      "end_char": 62,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 62,
      "end_char": 63,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 97. Sentence

Sentence: Crois-tu qu'elle sera partie avant que nous arrivions ?

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Crois",
      "lemma": "croire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 0,
      "end_char": 5,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "-tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 1,
      "deprel": "nsubj",
      "start_char": 5,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 6,
      "deprel": "mark",
      "start_char": 9,
      "end_char": 12,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 12,
      "end_char": 16
    },
    {
      "id": 5,
      "text": "sera",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 6,
      "deprel": "aux:tense",
      "start_char": 17,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "partie",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 1,
      "deprel": "ccomp",
      "start_char": 22,
      "end_char": 28
    },
    {
      "id": 7,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADP",
      "head": 10,
      "deprel": "mark",
      "start_char": 29,
      "end_char": 34
    },
    {
      "id": 8,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 10,
      "deprel": "mark",
      "start_char": 35,
      "end_char": 38
    },
    {
      "id": 9,
      "text": "nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Number=Plur|Person=1|PronType=Prs",
      "head": 10,
      "deprel": "nsubj",
      "start_char": 39,
      "end_char": 43
    },
    {
      "id": 10,
      "text": "arrivions",
      "lemma": "arrivier",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 6,
      "deprel": "advcl",
      "start_char": 44,
      "end_char": 53
    },
    {
      "id": 11,
      "text": "?",
      "lemma": "?",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 54,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 98. Sentence

Sentence: Je me demande s'ils auraient accepté si on leur avait expliqué les risques.

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
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "me",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 3,
      "deprel": "iobj",
      "start_char": 3,
      "end_char": 5
    },
    {
      "id": 3,
      "text": "demande",
      "lemma": "demander",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 6,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "s'",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 14,
      "end_char": 16,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": "ils",
      "lemma": "eux",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 16,
      "end_char": 19
    },
    {
      "id": 6,
      "text": "auraient",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 20,
      "end_char": 28
    },
    {
      "id": 7,
      "text": "accepté",
      "lemma": "accepter",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 3,
      "deprel": "ccomp",
      "start_char": 29,
      "end_char": 36
    },
    {
      "id": 8,
      "text": "si",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 12,
      "deprel": "mark",
      "start_char": 37,
      "end_char": 39
    },
    {
      "id": 9,
      "text": "on",
      "lemma": "on",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Ind",
      "head": 12,
      "deprel": "nsubj",
      "start_char": 40,
      "end_char": 42
    },
    {
      "id": 10,
      "text": "leur",
      "lemma": "eux",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=3|PronType=Prs",
      "head": 12,
      "deprel": "iobj",
      "start_char": 43,
      "end_char": 47
    },
    {
      "id": 11,
      "text": "avait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 12,
      "deprel": "aux:tense",
      "start_char": 48,
      "end_char": 53
    },
    {
      "id": 12,
      "text": "expliqué",
      "lemma": "expliquer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 7,
      "deprel": "advcl",
      "start_char": 54,
      "end_char": 62
    },
    {
      "id": 13,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 14,
      "deprel": "det",
      "start_char": 63,
      "end_char": 66
    },
    {
      "id": 14,
      "text": "risques",
      "lemma": "risque",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 12,
      "deprel": "obj",
      "start_char": 67,
      "end_char": 74,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 74,
      "end_char": 75,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 99. Sentence

Sentence: Le rapport que j'ai lu hier sera corrigé par l'équipe qui l'avait rédigé.

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
      "text": "rapport",
      "lemma": "rapport",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "nsubj:pass",
      "start_char": 3,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 6,
      "deprel": "obj",
      "start_char": 11,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "j'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 15,
      "end_char": 17,
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
      "start_char": 17,
      "end_char": 19
    },
    {
      "id": 6,
      "text": "lu",
      "lemma": "lire",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 2,
      "deprel": "acl:relcl",
      "start_char": 20,
      "end_char": 22
    },
    {
      "id": 7,
      "text": "hier",
      "lemma": "hier",
      "upos": "ADV",
      "head": 6,
      "deprel": "advmod",
      "start_char": 23,
      "end_char": 27
    },
    {
      "id": 8,
      "text": "sera",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:pass",
      "start_char": 28,
      "end_char": 32
    },
    {
      "id": 9,
      "text": "corrigé",
      "lemma": "corriger",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 0,
      "deprel": "root",
      "start_char": 33,
      "end_char": 40
    },
    {
      "id": 10,
      "text": "par",
      "lemma": "par",
      "upos": "ADP",
      "head": 12,
      "deprel": "case",
      "start_char": 41,
      "end_char": 44
    },
    {
      "id": 11,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 12,
      "deprel": "det",
      "start_char": 45,
      "end_char": 47,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": "équipe",
      "lemma": "équipe",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 9,
      "deprel": "obl:agent",
      "start_char": 47,
      "end_char": 53
    },
    {
      "id": 13,
      "text": "qui",
      "lemma": "qui",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 16,
      "deprel": "nsubj",
      "start_char": 54,
      "end_char": 57
    },
    {
      "id": 14,
      "text": "l'",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=3|PronType=Prs",
      "head": 16,
      "deprel": "obj",
      "start_char": 58,
      "end_char": 60,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": "avait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 16,
      "deprel": "aux:tense",
      "start_char": 60,
      "end_char": 65
    },
    {
      "id": 16,
      "text": "rédigé",
      "lemma": "rédiger",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 12,
      "deprel": "acl:relcl",
      "start_char": 66,
      "end_char": 72,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 17,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 72,
      "end_char": 73,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 100. Sentence

Sentence: La clé que tu croyais avoir perdue se trouvait dans le manteau que tu portais.

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
      "text": "clé",
      "lemma": "clé",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 6
    },
    {
      "id": 3,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 5,
      "deprel": "obj",
      "start_char": 7,
      "end_char": 10
    },
    {
      "id": 4,
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 11,
      "end_char": 13
    },
    {
      "id": 5,
      "text": "croyais",
      "lemma": "croire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Imp|VerbForm=Fin",
      "head": 2,
      "deprel": "acl:relcl",
      "start_char": 14,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "avoir",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "VerbForm=Inf",
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 22,
      "end_char": 27
    },
    {
      "id": 7,
      "text": "perdue",
      "lemma": "perdre",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 5,
      "deprel": "xcomp",
      "start_char": 28,
      "end_char": 34
    },
    {
      "id": 8,
      "text": "se",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 9,
      "deprel": "expl:pass",
      "start_char": 35,
      "end_char": 37
    },
    {
      "id": 9,
      "text": "trouvait",
      "lemma": "trouver",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 38,
      "end_char": 46
    },
    {
      "id": 10,
      "text": "dans",
      "lemma": "dans",
      "upos": "ADP",
      "head": 12,
      "deprel": "case",
      "start_char": 47,
      "end_char": 51
    },
    {
      "id": 11,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 12,
      "deprel": "det",
      "start_char": 52,
      "end_char": 54
    },
    {
      "id": 12,
      "text": "manteau",
      "lemma": "manteau",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "obl:arg",
      "start_char": 55,
      "end_char": 62
    },
    {
      "id": 13,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 15,
      "deprel": "obj",
      "start_char": 63,
      "end_char": 66
    },
    {
      "id": 14,
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 15,
      "deprel": "nsubj",
      "start_char": 67,
      "end_char": 69
    },
    {
      "id": 15,
      "text": "portais",
      "lemma": "porter",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Imp|VerbForm=Fin",
      "head": 12,
      "deprel": "acl:relcl",
      "start_char": 70,
      "end_char": 77,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 16,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 77,
      "end_char": 78,
      "misc": "SpaceAfter=No"
    }
  ]
]
```
