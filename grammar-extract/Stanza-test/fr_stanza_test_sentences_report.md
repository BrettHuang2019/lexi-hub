# French Stanza Raw JSON Report for Stanza-test Sentences

Generated from real Stanza `Document.to_dict()` output using `Stanza-test/fr_stanza_test_sentences.txt`.

## 1. Sentence

Sentence: Bonjour, je m'appelle Claire.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Bonjour",
      "lemma": "bonjour",
      "upos": "INTJ",
      "head": 5,
      "deprel": "discourse",
      "start_char": 0,
      "end_char": 7,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 7,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 9,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "m'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 5,
      "deprel": "obj",
      "start_char": 12,
      "end_char": 14,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": "appelle",
      "lemma": "appeler",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 14,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "Claire",
      "lemma": "Claire",
      "upos": "PROPN",
      "head": 5,
      "deprel": "obj",
      "start_char": 22,
      "end_char": 28,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 28,
      "end_char": 29,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 2. Sentence

Sentence: Il pleut depuis ce matin.

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
      "text": "depuis",
      "lemma": "depuis",
      "upos": "ADP",
      "head": 5,
      "deprel": "case",
      "start_char": 9,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "ce",
      "lemma": "ce",
      "upos": "DET",
      "feats": "Gender=Masc|Number=Sing|PronType=Dem",
      "head": 5,
      "deprel": "det",
      "start_char": 16,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "matin",
      "lemma": "matin",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
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

## 3. Sentence

Sentence: Le chat dort sur le canapé.

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
      "text": "chat",
      "lemma": "chat",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "dort",
      "lemma": "dormir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 8,
      "end_char": 12
    },
    {
      "id": 4,
      "text": "sur",
      "lemma": "sur",
      "upos": "ADP",
      "head": 6,
      "deprel": "case",
      "start_char": 13,
      "end_char": 16
    },
    {
      "id": 5,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 17,
      "end_char": 19
    },
    {
      "id": 6,
      "text": "canapé",
      "lemma": "canapé",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "obl:mod",
      "start_char": 20,
      "end_char": 26,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 26,
      "end_char": 27,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 4. Sentence

Sentence: Nous avons mangé avant de partir.

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
      "text": "partir",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 4,
      "deprel": "xcomp",
      "start_char": 26,
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

## 5. Sentence

Sentence: Elle ne comprend pas la question.

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
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 3,
      "deprel": "advmod",
      "start_char": 5,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "comprend",
      "lemma": "comprendre",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 8,
      "end_char": 16
    },
    {
      "id": 4,
      "text": "pas",
      "lemma": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 3,
      "deprel": "advmod",
      "start_char": 17,
      "end_char": 20
    },
    {
      "id": 5,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 21,
      "end_char": 23
    },
    {
      "id": 6,
      "text": "question",
      "lemma": "question",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 3,
      "deprel": "obj",
      "start_char": 24,
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

## 6. Sentence

Sentence: Tu viens demain ou vendredi ?

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
      "text": "viens",
      "lemma": "venir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "demain",
      "lemma": "demain",
      "upos": "ADV",
      "head": 2,
      "deprel": "advmod",
      "start_char": 9,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "ou",
      "lemma": "ou",
      "upos": "CCONJ",
      "head": 5,
      "deprel": "cc",
      "start_char": 16,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "vendredi",
      "lemma": "vendredi",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "conj",
      "start_char": 19,
      "end_char": 27
    },
    {
      "id": 6,
      "text": "?",
      "lemma": "?",
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

## 7. Sentence

Sentence: Les enfants jouent dans la cour de l'école.

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
      "text": "enfants",
      "lemma": "enfant",
      "upos": "NOUN",
      "feats": "Number=Plur",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 4,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "jouent",
      "lemma": "jouer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 12,
      "end_char": 18
    },
    {
      "id": 4,
      "text": "dans",
      "lemma": "dans",
      "upos": "ADP",
      "head": 6,
      "deprel": "case",
      "start_char": 19,
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
      "text": "cour",
      "lemma": "cour",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 3,
      "deprel": "obl:arg",
      "start_char": 27,
      "end_char": 31
    },
    {
      "id": 7,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 9,
      "deprel": "case",
      "start_char": 32,
      "end_char": 34
    },
    {
      "id": 8,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 9,
      "deprel": "det",
      "start_char": 35,
      "end_char": 37,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": "école",
      "lemma": "école",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 6,
      "deprel": "nmod",
      "start_char": 37,
      "end_char": 42,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 42,
      "end_char": 43,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 8. Sentence

Sentence: J'ai acheté trois pommes, deux poires et un kilo de riz.

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
      "text": "acheté",
      "lemma": "acheter",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "trois",
      "lemma": "trois",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 5,
      "deprel": "nummod",
      "start_char": 12,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "pommes",
      "lemma": "pomme",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 3,
      "deprel": "obj",
      "start_char": 18,
      "end_char": 24,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 24,
      "end_char": 25
    },
    {
      "id": 7,
      "text": "deux",
      "lemma": "deux",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 8,
      "deprel": "nummod",
      "start_char": 26,
      "end_char": 30
    },
    {
      "id": 8,
      "text": "poires",
      "lemma": "poire",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 5,
      "deprel": "conj",
      "start_char": 31,
      "end_char": 37
    },
    {
      "id": 9,
      "text": "et",
      "lemma": "et",
      "upos": "CCONJ",
      "head": 11,
      "deprel": "cc",
      "start_char": 38,
      "end_char": 40
    },
    {
      "id": 10,
      "text": "un",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Masc|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 41,
      "end_char": 43
    },
    {
      "id": 11,
      "text": "kilo",
      "lemma": "kilo",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "conj",
      "start_char": 44,
      "end_char": 48
    },
    {
      "id": 12,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 13,
      "deprel": "case",
      "start_char": 49,
      "end_char": 51
    },
    {
      "id": 13,
      "text": "riz",
      "lemma": "riz",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 11,
      "deprel": "nmod",
      "start_char": 52,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 55,
      "end_char": 56,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 9. Sentence

Sentence: Le train de 8 h 12 est arrivé avec dix minutes de retard.

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
      "text": "train",
      "lemma": "train",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 5,
      "deprel": "case",
      "start_char": 9,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "8",
      "lemma": "8",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 5,
      "deprel": "nummod",
      "start_char": 12,
      "end_char": 13
    },
    {
      "id": 5,
      "text": "h",
      "lemma": "h",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 2,
      "deprel": "nmod",
      "start_char": 14,
      "end_char": 15
    },
    {
      "id": 6,
      "text": "12",
      "lemma": "12",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 5,
      "deprel": "nmod",
      "start_char": 16,
      "end_char": 18
    },
    {
      "id": 7,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 8,
      "deprel": "aux:tense",
      "start_char": 19,
      "end_char": 22
    },
    {
      "id": 8,
      "text": "arrivé",
      "lemma": "arriver",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 23,
      "end_char": 29
    },
    {
      "id": 9,
      "text": "avec",
      "lemma": "avec",
      "upos": "ADP",
      "head": 11,
      "deprel": "case",
      "start_char": 30,
      "end_char": 34
    },
    {
      "id": 10,
      "text": "dix",
      "lemma": "dix",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 11,
      "deprel": "nummod",
      "start_char": 35,
      "end_char": 38
    },
    {
      "id": 11,
      "text": "minutes",
      "lemma": "minute",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 8,
      "deprel": "obl:mod",
      "start_char": 39,
      "end_char": 46
    },
    {
      "id": 12,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 13,
      "deprel": "case",
      "start_char": 47,
      "end_char": 49
    },
    {
      "id": 13,
      "text": "retard",
      "lemma": "retard",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 11,
      "deprel": "nmod",
      "start_char": 50,
      "end_char": 56,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 56,
      "end_char": 57,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 10. Sentence

Sentence: Ce livre, que je croyais perdu, était dans mon sac.

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
      "head": 12,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 8,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 8,
      "end_char": 9
    },
    {
      "id": 4,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 7,
      "deprel": "obj",
      "start_char": 10,
      "end_char": 13
    },
    {
      "id": 5,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 14,
      "end_char": 16
    },
    {
      "id": 6,
      "text": "croyais",
      "lemma": "croire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 2,
      "deprel": "acl:relcl",
      "start_char": 17,
      "end_char": 24
    },
    {
      "id": 7,
      "text": "perdu",
      "lemma": "perdre",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 6,
      "deprel": "xcomp",
      "start_char": 25,
      "end_char": 30,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 30,
      "end_char": 31
    },
    {
      "id": 9,
      "text": "était",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 12,
      "deprel": "cop",
      "start_char": 32,
      "end_char": 37
    },
    {
      "id": 10,
      "text": "dans",
      "lemma": "dans",
      "upos": "ADP",
      "head": 12,
      "deprel": "case",
      "start_char": 38,
      "end_char": 42
    },
    {
      "id": 11,
      "text": "mon",
      "lemma": "son",
      "upos": "DET",
      "feats": "Gender=Masc|Number=Sing|Number[psor]=Sing|Person[psor]=1|Poss=Yes|PronType=Prs",
      "head": 12,
      "deprel": "det",
      "start_char": 43,
      "end_char": 46
    },
    {
      "id": 12,
      "text": "sac",
      "lemma": "sac",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 47,
      "end_char": 50,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 12,
      "deprel": "punct",
      "start_char": 50,
      "end_char": 51,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 11. Sentence

Sentence: Si tu avais appelé plus tôt, je serais venu te chercher.

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
      "text": "avais",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Imp|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 6,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "appelé",
      "lemma": "appeler",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 10,
      "deprel": "advcl",
      "start_char": 12,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "plus",
      "lemma": "plus",
      "upos": "ADV",
      "head": 6,
      "deprel": "advmod",
      "start_char": 19,
      "end_char": 23
    },
    {
      "id": 6,
      "text": "tôt",
      "lemma": "tôt",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 24,
      "end_char": 27,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 27,
      "end_char": 28
    },
    {
      "id": 8,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 10,
      "deprel": "nsubj",
      "start_char": 29,
      "end_char": 31
    },
    {
      "id": 9,
      "text": "serais",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 10,
      "deprel": "aux:tense",
      "start_char": 32,
      "end_char": 38
    },
    {
      "id": 10,
      "text": "venu",
      "lemma": "venir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 39,
      "end_char": 43
    },
    {
      "id": 11,
      "text": "te",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 12,
      "deprel": "obj",
      "start_char": 44,
      "end_char": 46
    },
    {
      "id": 12,
      "text": "chercher",
      "lemma": "chercher",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 10,
      "deprel": "xcomp",
      "start_char": 47,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 55,
      "end_char": 56,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 12. Sentence

Sentence: Bien qu'il soit fatigué, Marc continue de travailler.

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
      "text": "Marc",
      "lemma": "Marc",
      "upos": "PROPN",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 25,
      "end_char": 29
    },
    {
      "id": 8,
      "text": "continue",
      "lemma": "continuer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 30,
      "end_char": 38
    },
    {
      "id": 9,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 10,
      "deprel": "mark",
      "start_char": 39,
      "end_char": 41
    },
    {
      "id": 10,
      "text": "travailler",
      "lemma": "travailler",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 8,
      "deprel": "xcomp",
      "start_char": 42,
      "end_char": 52,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 52,
      "end_char": 53,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 13. Sentence

Sentence: La décision que le ministre a annoncée hier divise les syndicats.

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
      "head": 9,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 7,
      "deprel": "obj",
      "start_char": 12,
      "end_char": 15
    },
    {
      "id": 4,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 16,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "ministre",
      "lemma": "ministre",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 19,
      "end_char": 27
    },
    {
      "id": 6,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 28,
      "end_char": 29
    },
    {
      "id": 7,
      "text": "annoncée",
      "lemma": "annoncer",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 2,
      "deprel": "acl:relcl",
      "start_char": 30,
      "end_char": 38
    },
    {
      "id": 8,
      "text": "hier",
      "lemma": "hier",
      "upos": "ADV",
      "head": 7,
      "deprel": "advmod",
      "start_char": 39,
      "end_char": 43
    },
    {
      "id": 9,
      "text": "divise",
      "lemma": "diviser",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 44,
      "end_char": 50
    },
    {
      "id": 10,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 51,
      "end_char": 54
    },
    {
      "id": 11,
      "text": "syndicats",
      "lemma": "syndicat",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 9,
      "deprel": "obj",
      "start_char": 55,
      "end_char": 64,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
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

## 14. Sentence

Sentence: Les résultats, publiés mardi soir, confirment une légère baisse du chômage.

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
      "head": 8,
      "deprel": "nsubj",
      "start_char": 4,
      "end_char": 13,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 13,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "publiés",
      "lemma": "publier",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 2,
      "deprel": "acl",
      "start_char": 15,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "mardi",
      "lemma": "mardi",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obl:mod",
      "start_char": 23,
      "end_char": 28
    },
    {
      "id": 6,
      "text": "soir",
      "lemma": "soir",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "nmod",
      "start_char": 29,
      "end_char": 33,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 33,
      "end_char": 34
    },
    {
      "id": 8,
      "text": "confirment",
      "lemma": "confirmer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 35,
      "end_char": 45
    },
    {
      "id": 9,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 46,
      "end_char": 49
    },
    {
      "id": 10,
      "text": "légère",
      "lemma": "léger",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Sing",
      "head": 11,
      "deprel": "amod",
      "start_char": 50,
      "end_char": 56
    },
    {
      "id": 11,
      "text": "baisse",
      "lemma": "baisse",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "obj",
      "start_char": 57,
      "end_char": 63
    },
    {
      "id": [
        12,
        13
      ],
      "text": "du",
      "start_char": 64,
      "end_char": 66
    },
    {
      "id": 12,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 14,
      "deprel": "case"
    },
    {
      "id": 13,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 14,
      "deprel": "det"
    },
    {
      "id": 14,
      "text": "chômage",
      "lemma": "chômage",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 11,
      "deprel": "nmod",
      "start_char": 67,
      "end_char": 74,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 74,
      "end_char": 75,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 15. Sentence

Sentence: Le président a déclaré que la réforme serait présentée "avant l'été".

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
      "text": "président",
      "lemma": "président",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 12
    },
    {
      "id": 3,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 13,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "déclaré",
      "lemma": "déclarer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 15,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 9,
      "deprel": "mark",
      "start_char": 23,
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
      "text": "réforme",
      "lemma": "réforme",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 9,
      "deprel": "nsubj:pass",
      "start_char": 30,
      "end_char": 37
    },
    {
      "id": 8,
      "text": "serait",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:pass",
      "start_char": 38,
      "end_char": 44
    },
    {
      "id": 9,
      "text": "présentée",
      "lemma": "présenter",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 4,
      "deprel": "ccomp",
      "start_char": 45,
      "end_char": 54
    },
    {
      "id": 10,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 13,
      "deprel": "punct",
      "start_char": 55,
      "end_char": 56,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADP",
      "head": 13,
      "deprel": "case",
      "start_char": 56,
      "end_char": 61
    },
    {
      "id": 12,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 13,
      "deprel": "det",
      "start_char": 62,
      "end_char": 64,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
      "text": "été",
      "lemma": "été",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "obl:mod",
      "start_char": 64,
      "end_char": 67,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 13,
      "deprel": "punct",
      "start_char": 67,
      "end_char": 68,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
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

## 16. Sentence

Sentence: Selon France 2, plusieurs communes ont renforcé leur dispositif de sécurité.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Selon",
      "lemma": "selon",
      "upos": "ADP",
      "head": 2,
      "deprel": "case",
      "start_char": 0,
      "end_char": 5
    },
    {
      "id": 2,
      "text": "France",
      "lemma": "France",
      "upos": "PROPN",
      "head": 8,
      "deprel": "obl:mod",
      "start_char": 6,
      "end_char": 12
    },
    {
      "id": 3,
      "text": "2",
      "lemma": "2",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 2,
      "deprel": "nmod",
      "start_char": 13,
      "end_char": 14,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 14,
      "end_char": 15
    },
    {
      "id": 5,
      "text": "plusieurs",
      "lemma": "plusieurs",
      "upos": "DET",
      "feats": "Number=Plur|PronType=Ind",
      "head": 6,
      "deprel": "det",
      "start_char": 16,
      "end_char": 25
    },
    {
      "id": 6,
      "text": "communes",
      "lemma": "commune",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 26,
      "end_char": 34
    },
    {
      "id": 7,
      "text": "ont",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 8,
      "deprel": "aux:tense",
      "start_char": 35,
      "end_char": 38
    },
    {
      "id": 8,
      "text": "renforcé",
      "lemma": "renforcer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 39,
      "end_char": 47
    },
    {
      "id": 9,
      "text": "leur",
      "lemma": "son",
      "upos": "DET",
      "feats": "Number=Sing|Number[psor]=Plur|Person[psor]=3|Poss=Yes|PronType=Prs",
      "head": 10,
      "deprel": "det",
      "start_char": 48,
      "end_char": 52
    },
    {
      "id": 10,
      "text": "dispositif",
      "lemma": "dispositif",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 8,
      "deprel": "obj",
      "start_char": 53,
      "end_char": 63
    },
    {
      "id": 11,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 12,
      "deprel": "case",
      "start_char": 64,
      "end_char": 66
    },
    {
      "id": 12,
      "text": "sécurité",
      "lemma": "sécurité",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 10,
      "deprel": "nmod",
      "start_char": 67,
      "end_char": 75,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 75,
      "end_char": 76,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 17. Sentence

Sentence: Une journaliste de Radio-Canada a interrogé les habitants après l'inondation.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 2,
      "deprel": "det",
      "start_char": 0,
      "end_char": 3
    },
    {
      "id": 2,
      "text": "journaliste",
      "lemma": "journaliste",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 4,
      "end_char": 15
    },
    {
      "id": 3,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 4,
      "deprel": "case",
      "start_char": 16,
      "end_char": 18
    },
    {
      "id": 4,
      "text": "Radio-Canada",
      "lemma": "Radio-Canada",
      "upos": "PROPN",
      "head": 2,
      "deprel": "nmod",
      "start_char": 19,
      "end_char": 31
    },
    {
      "id": 5,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 6,
      "deprel": "aux:tense",
      "start_char": 32,
      "end_char": 33
    },
    {
      "id": 6,
      "text": "interrogé",
      "lemma": "interroger",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 34,
      "end_char": 43
    },
    {
      "id": 7,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 44,
      "end_char": 47
    },
    {
      "id": 8,
      "text": "habitants",
      "lemma": "habitant",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 6,
      "deprel": "obj",
      "start_char": 48,
      "end_char": 57
    },
    {
      "id": 9,
      "text": "après",
      "lemma": "après",
      "upos": "ADP",
      "head": 11,
      "deprel": "case",
      "start_char": 58,
      "end_char": 63
    },
    {
      "id": 10,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 64,
      "end_char": 66,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": "inondation",
      "lemma": "inondation",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 6,
      "deprel": "obl:mod",
      "start_char": 66,
      "end_char": 76,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 76,
      "end_char": 77,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 18. Sentence

Sentence: Le documentaire diffusé sur Arte revient sur trente ans de négociations climatiques.

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
      "text": "documentaire",
      "lemma": "documentaire",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 15
    },
    {
      "id": 3,
      "text": "diffusé",
      "lemma": "diffuser",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 2,
      "deprel": "acl",
      "start_char": 16,
      "end_char": 23
    },
    {
      "id": 4,
      "text": "sur",
      "lemma": "sur",
      "upos": "ADP",
      "head": 5,
      "deprel": "case",
      "start_char": 24,
      "end_char": 27
    },
    {
      "id": 5,
      "text": "Arte",
      "lemma": "Arte",
      "upos": "PROPN",
      "head": 3,
      "deprel": "obl:mod",
      "start_char": 28,
      "end_char": 32
    },
    {
      "id": 6,
      "text": "revient",
      "lemma": "revenir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 33,
      "end_char": 40
    },
    {
      "id": 7,
      "text": "sur",
      "lemma": "sur",
      "upos": "ADP",
      "head": 9,
      "deprel": "case",
      "start_char": 41,
      "end_char": 44
    },
    {
      "id": 8,
      "text": "trente",
      "lemma": "trente",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 9,
      "deprel": "nummod",
      "start_char": 45,
      "end_char": 51
    },
    {
      "id": 9,
      "text": "ans",
      "lemma": "an",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 6,
      "deprel": "obl:mod",
      "start_char": 52,
      "end_char": 55
    },
    {
      "id": 10,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 11,
      "deprel": "case",
      "start_char": 56,
      "end_char": 58
    },
    {
      "id": 11,
      "text": "négociations",
      "lemma": "négociation",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 9,
      "deprel": "nmod",
      "start_char": 59,
      "end_char": 71
    },
    {
      "id": 12,
      "text": "climatiques",
      "lemma": "climatique",
      "upos": "ADJ",
      "feats": "Number=Plur",
      "head": 11,
      "deprel": "amod",
      "start_char": 72,
      "end_char": 83,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 83,
      "end_char": 84,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 19. Sentence

Sentence: Dans une série policière, l'inspectrice découvre que le témoin principal a menti.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Dans",
      "lemma": "dans",
      "upos": "ADP",
      "head": 3,
      "deprel": "case",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 3,
      "deprel": "det",
      "start_char": 5,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "série",
      "lemma": "série",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "obl:mod",
      "start_char": 9,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "policière",
      "lemma": "policier",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Sing",
      "head": 3,
      "deprel": "amod",
      "start_char": 15,
      "end_char": 24,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 24,
      "end_char": 25
    },
    {
      "id": 6,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 26,
      "end_char": 28,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": "inspectrice",
      "lemma": "inspecteur",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 28,
      "end_char": 39
    },
    {
      "id": 8,
      "text": "découvre",
      "lemma": "découvrir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 40,
      "end_char": 48
    },
    {
      "id": 9,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 14,
      "deprel": "mark",
      "start_char": 49,
      "end_char": 52
    },
    {
      "id": 10,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 53,
      "end_char": 55
    },
    {
      "id": 11,
      "text": "témoin",
      "lemma": "témoin",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 14,
      "deprel": "nsubj",
      "start_char": 56,
      "end_char": 62
    },
    {
      "id": 12,
      "text": "principal",
      "lemma": "principal",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 11,
      "deprel": "amod",
      "start_char": 63,
      "end_char": 72
    },
    {
      "id": 13,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 14,
      "deprel": "aux:tense",
      "start_char": 73,
      "end_char": 74
    },
    {
      "id": 14,
      "text": "menti",
      "lemma": "mentir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 8,
      "deprel": "ccomp",
      "start_char": 75,
      "end_char": 80,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 80,
      "end_char": 81,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 20. Sentence

Sentence: À la fin de l'épisode, personne ne croit encore à l'alibi du voisin.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "À",
      "lemma": "à",
      "upos": "ADP",
      "head": 3,
      "deprel": "case",
      "start_char": 0,
      "end_char": 1
    },
    {
      "id": 2,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 3,
      "deprel": "det",
      "start_char": 2,
      "end_char": 4
    },
    {
      "id": 3,
      "text": "fin",
      "lemma": "fin",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 10,
      "deprel": "obl:mod",
      "start_char": 5,
      "end_char": 8
    },
    {
      "id": 4,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 6,
      "deprel": "case",
      "start_char": 9,
      "end_char": 11
    },
    {
      "id": 5,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 12,
      "end_char": 14,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "épisode",
      "lemma": "épisode",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "nmod",
      "start_char": 14,
      "end_char": 21,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 21,
      "end_char": 22
    },
    {
      "id": 8,
      "text": "personne",
      "lemma": "personne",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|PronType=Neg",
      "head": 10,
      "deprel": "nsubj",
      "start_char": 23,
      "end_char": 31
    },
    {
      "id": 9,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 10,
      "deprel": "advmod",
      "start_char": 32,
      "end_char": 34
    },
    {
      "id": 10,
      "text": "croit",
      "lemma": "croire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 35,
      "end_char": 40
    },
    {
      "id": 11,
      "text": "encore",
      "lemma": "encore",
      "upos": "ADV",
      "head": 10,
      "deprel": "advmod",
      "start_char": 41,
      "end_char": 47
    },
    {
      "id": 12,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 14,
      "deprel": "case",
      "start_char": 48,
      "end_char": 49
    },
    {
      "id": 13,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 14,
      "deprel": "det",
      "start_char": 50,
      "end_char": 52,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": "alibi",
      "lemma": "alibi",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 10,
      "deprel": "obl:arg",
      "start_char": 52,
      "end_char": 57
    },
    {
      "id": [
        15,
        16
      ],
      "text": "du",
      "start_char": 58,
      "end_char": 60
    },
    {
      "id": 15,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 17,
      "deprel": "case"
    },
    {
      "id": 16,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 17,
      "deprel": "det"
    },
    {
      "id": 17,
      "text": "voisin",
      "lemma": "voisin",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 14,
      "deprel": "nmod",
      "start_char": 61,
      "end_char": 67,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 18,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 67,
      "end_char": 68,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 21. Sentence

Sentence: Ce soir-là, sur le plateau télé, tout le monde parlait en même temps.

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
      "text": "soir",
      "lemma": "soir",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 13,
      "deprel": "obl:mod",
      "start_char": 3,
      "end_char": 7,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "-là",
      "lemma": "là",
      "upos": "ADV",
      "head": 2,
      "deprel": "advmod",
      "start_char": 7,
      "end_char": 10,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 10,
      "end_char": 11
    },
    {
      "id": 5,
      "text": "sur",
      "lemma": "sur",
      "upos": "ADP",
      "head": 7,
      "deprel": "case",
      "start_char": 12,
      "end_char": 15
    },
    {
      "id": 6,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 16,
      "end_char": 18
    },
    {
      "id": 7,
      "text": "plateau",
      "lemma": "plateau",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 13,
      "deprel": "obl:mod",
      "start_char": 19,
      "end_char": 26
    },
    {
      "id": 8,
      "text": "télé",
      "lemma": "télé",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Sing",
      "head": 7,
      "deprel": "amod",
      "start_char": 27,
      "end_char": 31,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 31,
      "end_char": 32
    },
    {
      "id": 10,
      "text": "tout",
      "lemma": "tout",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 12,
      "deprel": "amod",
      "start_char": 33,
      "end_char": 37
    },
    {
      "id": 11,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 12,
      "deprel": "det",
      "start_char": 38,
      "end_char": 40
    },
    {
      "id": 12,
      "text": "monde",
      "lemma": "monde",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 13,
      "deprel": "nsubj",
      "start_char": 41,
      "end_char": 46
    },
    {
      "id": 13,
      "text": "parlait",
      "lemma": "parler",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 47,
      "end_char": 54
    },
    {
      "id": 14,
      "text": "en",
      "lemma": "en",
      "upos": "ADP",
      "head": 16,
      "deprel": "case",
      "start_char": 55,
      "end_char": 57
    },
    {
      "id": 15,
      "text": "même",
      "lemma": "même",
      "upos": "ADJ",
      "feats": "Number=Sing",
      "head": 16,
      "deprel": "amod",
      "start_char": 58,
      "end_char": 62
    },
    {
      "id": 16,
      "text": "temps",
      "lemma": "temps",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 13,
      "deprel": "obl:mod",
      "start_char": 63,
      "end_char": 68,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 17,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 13,
      "deprel": "punct",
      "start_char": 68,
      "end_char": 69,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 22. Sentence

Sentence: "Je n'ai rien vu", répète le gardien, les mains tremblantes.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 0,
      "end_char": 1,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "Je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 1,
      "end_char": 3
    },
    {
      "id": 3,
      "text": "n'",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 6,
      "deprel": "advmod",
      "start_char": 4,
      "end_char": 6,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "ai",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 6,
      "deprel": "aux:tense",
      "start_char": 6,
      "end_char": 8
    },
    {
      "id": 5,
      "text": "rien",
      "lemma": "rien",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|PronType=Neg",
      "head": 6,
      "deprel": "obj",
      "start_char": 9,
      "end_char": 13
    },
    {
      "id": 6,
      "text": "vu",
      "lemma": "voir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 14,
      "end_char": 16,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 16,
      "end_char": 17,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 17,
      "end_char": 18
    },
    {
      "id": 9,
      "text": "répète",
      "lemma": "répéter",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 6,
      "deprel": "parataxis:insert",
      "start_char": 19,
      "end_char": 25
    },
    {
      "id": 10,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 26,
      "end_char": 28
    },
    {
      "id": 11,
      "text": "gardien",
      "lemma": "gardien",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 29,
      "end_char": 36,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 14,
      "deprel": "punct",
      "start_char": 36,
      "end_char": 37
    },
    {
      "id": 13,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 14,
      "deprel": "det",
      "start_char": 38,
      "end_char": 41
    },
    {
      "id": 14,
      "text": "mains",
      "lemma": "main",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 11,
      "deprel": "appos",
      "start_char": 42,
      "end_char": 47
    },
    {
      "id": 15,
      "text": "tremblantes",
      "lemma": "tremblant",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Plur",
      "head": 14,
      "deprel": "amod",
      "start_char": 48,
      "end_char": 59,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 16,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 59,
      "end_char": 60,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 23. Sentence

Sentence: Est-ce que tu l'as vu, le message qu'elle m'a envoyé ?

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "cop",
      "start_char": 0,
      "end_char": 3,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "-ce",
      "lemma": "ce",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Dem",
      "head": 7,
      "deprel": "expl:subj",
      "start_char": 3,
      "end_char": 6
    },
    {
      "id": 3,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 7,
      "end_char": 10
    },
    {
      "id": 4,
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 11,
      "end_char": 13
    },
    {
      "id": 5,
      "text": "l'",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "obj",
      "start_char": 14,
      "end_char": 16,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "as",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 16,
      "end_char": 18
    },
    {
      "id": 7,
      "text": "vu",
      "lemma": "voir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 19,
      "end_char": 21,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 21,
      "end_char": 22
    },
    {
      "id": 9,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 10,
      "deprel": "det",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 10,
      "text": "message",
      "lemma": "message",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "parataxis",
      "start_char": 26,
      "end_char": 33
    },
    {
      "id": 11,
      "text": "qu'",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 15,
      "deprel": "obj",
      "start_char": 34,
      "end_char": 37,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 15,
      "deprel": "nsubj",
      "start_char": 37,
      "end_char": 41
    },
    {
      "id": 13,
      "text": "m'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 15,
      "deprel": "iobj",
      "start_char": 42,
      "end_char": 44,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 15,
      "deprel": "aux:tense",
      "start_char": 44,
      "end_char": 45
    },
    {
      "id": 15,
      "text": "envoyé",
      "lemma": "envoyer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 10,
      "deprel": "acl:relcl",
      "start_char": 46,
      "end_char": 52
    },
    {
      "id": 16,
      "text": "?",
      "lemma": "?",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 53,
      "end_char": 54,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 24. Sentence

Sentence: Donne-le-moi avant que je change d'avis.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Donne-le-moi",
      "lemma": "donne-le-moi",
      "upos": "INTJ",
      "head": 5,
      "deprel": "discourse",
      "start_char": 0,
      "end_char": 12
    },
    {
      "id": 2,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADP",
      "head": 5,
      "deprel": "mark",
      "start_char": 13,
      "end_char": 18
    },
    {
      "id": 3,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 5,
      "deprel": "mark",
      "start_char": 19,
      "end_char": 22
    },
    {
      "id": 4,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 5,
      "text": "change",
      "lemma": "changer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 26,
      "end_char": 32
    },
    {
      "id": 6,
      "text": "d'",
      "lemma": "de",
      "upos": "ADP",
      "head": 7,
      "deprel": "case",
      "start_char": 33,
      "end_char": 35,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": "avis",
      "lemma": "avis",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "obl:arg",
      "start_char": 35,
      "end_char": 39,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 39,
      "end_char": 40,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 25. Sentence

Sentence: Il s'en est fallu de peu pour que l'accord échoue.

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
      "head": 5,
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
      "head": 5,
      "deprel": "expl:pv",
      "start_char": 3,
      "end_char": 5,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "en",
      "lemma": "en",
      "upos": "PRON",
      "feats": "Emph=No|Person=3|PronType=Prs",
      "head": 5,
      "deprel": "expl:comp",
      "start_char": 5,
      "end_char": 7
    },
    {
      "id": 4,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 8,
      "end_char": 11
    },
    {
      "id": 5,
      "text": "fallu",
      "lemma": "falloir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 12,
      "end_char": 17
    },
    {
      "id": 6,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "feats": "ExtPos=ADV",
      "head": 5,
      "deprel": "advmod",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 7,
      "text": "peu",
      "lemma": "peu",
      "upos": "ADV",
      "head": 6,
      "deprel": "fixed",
      "start_char": 21,
      "end_char": 24
    },
    {
      "id": 8,
      "text": "pour",
      "lemma": "pour",
      "upos": "ADP",
      "head": 12,
      "deprel": "mark",
      "start_char": 25,
      "end_char": 29
    },
    {
      "id": 9,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 12,
      "deprel": "mark",
      "start_char": 30,
      "end_char": 33
    },
    {
      "id": 10,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 34,
      "end_char": 36,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": "accord",
      "lemma": "accord",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 12,
      "deprel": "nsubj",
      "start_char": 36,
      "end_char": 42
    },
    {
      "id": 12,
      "text": "échoue",
      "lemma": "échouer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "advcl",
      "start_char": 43,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
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

## 26. Sentence

Sentence: Je ne sais pas s'il y en aura assez pour tout le monde.

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
      "text": "sais",
      "lemma": "savoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 6,
      "end_char": 10
    },
    {
      "id": 4,
      "text": "pas",
      "lemma": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 3,
      "deprel": "advmod",
      "start_char": 11,
      "end_char": 14
    },
    {
      "id": 5,
      "text": "s'",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 9,
      "deprel": "mark",
      "start_char": 15,
      "end_char": 17,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "expl:subj",
      "start_char": 17,
      "end_char": 19
    },
    {
      "id": 7,
      "text": "y",
      "lemma": "y",
      "upos": "PRON",
      "feats": "Emph=No|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "expl:comp",
      "start_char": 20,
      "end_char": 21
    },
    {
      "id": 8,
      "text": "en",
      "lemma": "en",
      "upos": "PRON",
      "feats": "Emph=No|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "expl:comp",
      "start_char": 22,
      "end_char": 24
    },
    {
      "id": 9,
      "text": "aura",
      "lemma": "avoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 3,
      "deprel": "advcl",
      "start_char": 25,
      "end_char": 29
    },
    {
      "id": 10,
      "text": "assez",
      "lemma": "assez",
      "upos": "ADV",
      "head": 9,
      "deprel": "advmod",
      "start_char": 30,
      "end_char": 35
    },
    {
      "id": 11,
      "text": "pour",
      "lemma": "pour",
      "upos": "ADP",
      "head": 14,
      "deprel": "case",
      "start_char": 36,
      "end_char": 40
    },
    {
      "id": 12,
      "text": "tout",
      "lemma": "tout",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 14,
      "deprel": "amod",
      "start_char": 41,
      "end_char": 45
    },
    {
      "id": 13,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 14,
      "deprel": "det",
      "start_char": 46,
      "end_char": 48
    },
    {
      "id": 14,
      "text": "monde",
      "lemma": "monde",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "obl:mod",
      "start_char": 49,
      "end_char": 54,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
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

## 27. Sentence

Sentence: Elle m'a dit qu'elle n'y retournerait plus jamais.

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
      "text": "m'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 4,
      "deprel": "iobj",
      "start_char": 5,
      "end_char": 7,
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
      "start_char": 7,
      "end_char": 8
    },
    {
      "id": 4,
      "text": "dit",
      "lemma": "dire",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 9,
      "end_char": 12
    },
    {
      "id": 5,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 9,
      "deprel": "mark",
      "start_char": 13,
      "end_char": 16,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 16,
      "end_char": 20
    },
    {
      "id": 7,
      "text": "n'",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 9,
      "deprel": "advmod",
      "start_char": 21,
      "end_char": 23,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": "y",
      "lemma": "y",
      "upos": "PRON",
      "feats": "Emph=No|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "iobj",
      "start_char": 23,
      "end_char": 24
    },
    {
      "id": 9,
      "text": "retournerait",
      "lemma": "retourner",
      "upos": "VERB",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "ccomp",
      "start_char": 25,
      "end_char": 37
    },
    {
      "id": 10,
      "text": "plus",
      "lemma": "plus",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 9,
      "deprel": "advmod",
      "start_char": 38,
      "end_char": 42
    },
    {
      "id": 11,
      "text": "jamais",
      "lemma": "jamais",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 9,
      "deprel": "advmod",
      "start_char": 43,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 49,
      "end_char": 50,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 28. Sentence

Sentence: Le colis, je l'ai reçu, mais la facture, elle, n'est jamais arrivée.

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
      "text": "colis",
      "lemma": "colis",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "dislocated",
      "start_char": 3,
      "end_char": 8,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 8,
      "end_char": 9
    },
    {
      "id": 4,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 10,
      "end_char": 12
    },
    {
      "id": 5,
      "text": "l'",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "obj",
      "start_char": 13,
      "end_char": 15,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "ai",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 15,
      "end_char": 17
    },
    {
      "id": 7,
      "text": "reçu",
      "lemma": "recevoir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 18,
      "end_char": 22,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 18,
      "deprel": "punct",
      "start_char": 22,
      "end_char": 23
    },
    {
      "id": 9,
      "text": "mais",
      "lemma": "mais",
      "upos": "CCONJ",
      "head": 18,
      "deprel": "cc",
      "start_char": 24,
      "end_char": 28
    },
    {
      "id": 10,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 29,
      "end_char": 31
    },
    {
      "id": 11,
      "text": "facture",
      "lemma": "facture",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 18,
      "deprel": "nsubj",
      "start_char": 32,
      "end_char": 39,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 13,
      "deprel": "punct",
      "start_char": 39,
      "end_char": 40
    },
    {
      "id": 13,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 11,
      "deprel": "appos",
      "start_char": 41,
      "end_char": 45,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 13,
      "deprel": "punct",
      "start_char": 45,
      "end_char": 46
    },
    {
      "id": 15,
      "text": "n'",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 18,
      "deprel": "advmod",
      "start_char": 47,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 16,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 18,
      "deprel": "aux:tense",
      "start_char": 49,
      "end_char": 52
    },
    {
      "id": 17,
      "text": "jamais",
      "lemma": "jamais",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 18,
      "deprel": "advmod",
      "start_char": 53,
      "end_char": 59
    },
    {
      "id": 18,
      "text": "arrivée",
      "lemma": "arriver",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 7,
      "deprel": "conj",
      "start_char": 60,
      "end_char": 67,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 19,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 67,
      "end_char": 68,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 29. Sentence

Sentence: Ça marche pas, ton truc, je te jure.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Ça",
      "lemma": "ça",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Dem",
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "marche",
      "lemma": "marcher",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 3,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "pas",
      "lemma": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 2,
      "deprel": "advmod",
      "start_char": 10,
      "end_char": 13,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 13,
      "end_char": 14
    },
    {
      "id": 5,
      "text": "ton",
      "lemma": "son",
      "upos": "DET",
      "feats": "Number=Sing|Number[psor]=Sing|Person[psor]=1|Poss=Yes|PronType=Prs",
      "head": 6,
      "deprel": "det",
      "start_char": 15,
      "end_char": 18
    },
    {
      "id": 6,
      "text": "truc",
      "lemma": "truc",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 10,
      "deprel": "dislocated",
      "start_char": 19,
      "end_char": 23,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 23,
      "end_char": 24
    },
    {
      "id": 8,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 10,
      "deprel": "nsubj",
      "start_char": 25,
      "end_char": 27
    },
    {
      "id": 9,
      "text": "te",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 10,
      "deprel": "obj",
      "start_char": 28,
      "end_char": 30
    },
    {
      "id": 10,
      "text": "jure",
      "lemma": "jurer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "conj",
      "start_char": 31,
      "end_char": 35,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
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

## 30. Sentence

Sentence: Ben, franchement, j'en sais rien.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Ben",
      "lemma": "Ben",
      "upos": "PROPN",
      "head": 7,
      "deprel": "dislocated",
      "start_char": 0,
      "end_char": 3,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 3,
      "end_char": 4
    },
    {
      "id": 3,
      "text": "franchement",
      "lemma": "franchement",
      "upos": "ADV",
      "head": 7,
      "deprel": "advmod",
      "start_char": 5,
      "end_char": 16,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 16,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "j'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 18,
      "end_char": 20,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "en",
      "lemma": "en",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs",
      "head": 7,
      "deprel": "iobj",
      "start_char": 20,
      "end_char": 22
    },
    {
      "id": 7,
      "text": "sais",
      "lemma": "savoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 23,
      "end_char": 27
    },
    {
      "id": 8,
      "text": "rien",
      "lemma": "rien",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|PronType=Neg",
      "head": 7,
      "deprel": "obj",
      "start_char": 28,
      "end_char": 32,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 32,
      "end_char": 33,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 31. Sentence

Sentence: T'as vu le prix du café maintenant ?

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "T'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "as",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "aux:tense",
      "start_char": 2,
      "end_char": 4
    },
    {
      "id": 3,
      "text": "vu",
      "lemma": "voir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "start_char": 5,
      "end_char": 7
    },
    {
      "id": 4,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 8,
      "end_char": 10
    },
    {
      "id": 5,
      "text": "prix",
      "lemma": "prix",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "obj",
      "start_char": 11,
      "end_char": 15
    },
    {
      "id": [
        6,
        7
      ],
      "text": "du",
      "start_char": 16,
      "end_char": 18
    },
    {
      "id": 6,
      "text": "de",
      "lemma": "de",
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
      "text": "café",
      "lemma": "café",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "nmod",
      "start_char": 19,
      "end_char": 23
    },
    {
      "id": 9,
      "text": "maintenant",
      "lemma": "maintenant",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 24,
      "end_char": 34
    },
    {
      "id": 10,
      "text": "?",
      "lemma": "?",
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

## 32. Sentence

Sentence: On se capte après le boulot, ok ?

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "On",
      "lemma": "on",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Ind",
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
      "deprel": "obj",
      "start_char": 3,
      "end_char": 5
    },
    {
      "id": 3,
      "text": "capte",
      "lemma": "capter",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 6,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "après",
      "lemma": "après",
      "upos": "ADP",
      "head": 6,
      "deprel": "case",
      "start_char": 12,
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
      "text": "boulot",
      "lemma": "boulot",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "obl:mod",
      "start_char": 21,
      "end_char": 27,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 27,
      "end_char": 28
    },
    {
      "id": 8,
      "text": "ok",
      "lemma": "ok",
      "upos": "INTJ",
      "head": 3,
      "deprel": "discourse",
      "start_char": 29,
      "end_char": 31
    },
    {
      "id": 9,
      "text": "?",
      "lemma": "?",
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

## 33. Sentence

Sentence: La réunion aurait dû commencer à 14 h 30 ; elle a finalement été reportée.

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
      "text": "réunion",
      "lemma": "réunion",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "aurait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 11,
      "end_char": 17
    },
    {
      "id": 4,
      "text": "dû",
      "lemma": "devoir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 5,
      "text": "commencer",
      "lemma": "commencer",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 4,
      "deprel": "xcomp",
      "start_char": 21,
      "end_char": 30
    },
    {
      "id": 6,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 31,
      "end_char": 32
    },
    {
      "id": 7,
      "text": "14",
      "lemma": "14",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 8,
      "deprel": "nummod",
      "start_char": 33,
      "end_char": 35
    },
    {
      "id": 8,
      "text": "h",
      "lemma": "h",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 5,
      "deprel": "obl:mod",
      "start_char": 36,
      "end_char": 37
    },
    {
      "id": 9,
      "text": "30",
      "lemma": "30",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 8,
      "deprel": "nmod",
      "start_char": 38,
      "end_char": 40
    },
    {
      "id": 10,
      "text": ";",
      "lemma": ";",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 41,
      "end_char": 42
    }
  ],
  [
    {
      "id": 1,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 5,
      "deprel": "nsubj:pass",
      "start_char": 43,
      "end_char": 47
    },
    {
      "id": 2,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 48,
      "end_char": 49
    },
    {
      "id": 3,
      "text": "finalement",
      "lemma": "finalement",
      "upos": "ADV",
      "head": 5,
      "deprel": "advmod",
      "start_char": 50,
      "end_char": 60
    },
    {
      "id": 4,
      "text": "été",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 5,
      "deprel": "aux:pass",
      "start_char": 61,
      "end_char": 64
    },
    {
      "id": 5,
      "text": "reportée",
      "lemma": "reporter",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 0,
      "deprel": "root",
      "start_char": 65,
      "end_char": 73,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 73,
      "end_char": 74,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 34. Sentence

Sentence: M. Dupont, né le 03/04/1980, habite au 12 bis rue Victor-Hugo.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "M.",
      "lemma": "monsieur",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "Dupont",
      "lemma": "Dupont",
      "upos": "PROPN",
      "head": 1,
      "deprel": "nmod",
      "start_char": 3,
      "end_char": 9,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 9,
      "end_char": 10
    },
    {
      "id": 4,
      "text": "né",
      "lemma": "naître",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 1,
      "deprel": "acl",
      "start_char": 11,
      "end_char": 13
    },
    {
      "id": 5,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 14,
      "end_char": 16
    },
    {
      "id": 6,
      "text": "03/04/1980",
      "lemma": "03/04/1980",
      "upos": "NUM",
      "feats": "Number=Sing",
      "head": 4,
      "deprel": "obl:arg",
      "start_char": 17,
      "end_char": 27,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 27,
      "end_char": 28
    },
    {
      "id": 8,
      "text": "habite",
      "lemma": "habiter",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 29,
      "end_char": 35
    },
    {
      "id": [
        9,
        10
      ],
      "text": "au",
      "start_char": 36,
      "end_char": 38
    },
    {
      "id": 9,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 11,
      "deprel": "case"
    },
    {
      "id": 10,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det"
    },
    {
      "id": 11,
      "text": "12",
      "lemma": "12",
      "upos": "NUM",
      "feats": "Number=Sing",
      "head": 8,
      "deprel": "obl:arg",
      "start_char": 39,
      "end_char": 41
    },
    {
      "id": 12,
      "text": "bis",
      "lemma": "bis",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 11,
      "deprel": "nmod",
      "start_char": 42,
      "end_char": 45
    },
    {
      "id": 13,
      "text": "rue",
      "lemma": "rue",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 11,
      "deprel": "nmod",
      "start_char": 46,
      "end_char": 49
    },
    {
      "id": 14,
      "text": "Victor-Hugo",
      "lemma": "Victor-Hugo",
      "upos": "PROPN",
      "head": 13,
      "deprel": "appos",
      "start_char": 50,
      "end_char": 61,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
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

## 35. Sentence

Sentence: Le coût total s'élève à 1 234,56 euros, hors taxes.

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
      "text": "coût",
      "lemma": "coût",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "nsubj:pass",
      "start_char": 3,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "total",
      "lemma": "total",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 2,
      "deprel": "amod",
      "start_char": 8,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "s'",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 5,
      "deprel": "expl:pass",
      "start_char": 14,
      "end_char": 16,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": "élève",
      "lemma": "élever",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 16,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 22,
      "end_char": 23
    },
    {
      "id": 7,
      "text": "1 234,56",
      "lemma": "1 234,56",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 8,
      "deprel": "nummod",
      "start_char": 24,
      "end_char": 32
    },
    {
      "id": 8,
      "text": "euros",
      "lemma": "euro",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 5,
      "deprel": "obl:arg",
      "start_char": 33,
      "end_char": 38,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 11,
      "deprel": "punct",
      "start_char": 38,
      "end_char": 39
    },
    {
      "id": 10,
      "text": "hors",
      "lemma": "hors",
      "upos": "ADP",
      "head": 11,
      "deprel": "case",
      "start_char": 40,
      "end_char": 44
    },
    {
      "id": 11,
      "text": "taxes",
      "lemma": "taxe",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 5,
      "deprel": "obl:mod",
      "start_char": 45,
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

## 36. Sentence

Sentence: La société Alpha-Bêta a levé 3,5 millions d'euros en série A.

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
      "text": "société",
      "lemma": "société",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "Alpha-Bêta",
      "lemma": "Alpha-Bêta",
      "upos": "PROPN",
      "head": 2,
      "deprel": "appos",
      "start_char": 11,
      "end_char": 21
    },
    {
      "id": 4,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 22,
      "end_char": 23
    },
    {
      "id": 5,
      "text": "levé",
      "lemma": "lever",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 24,
      "end_char": 28
    },
    {
      "id": 6,
      "text": "3,5",
      "lemma": "3,5",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 7,
      "deprel": "nummod",
      "start_char": 29,
      "end_char": 32
    },
    {
      "id": 7,
      "text": "millions",
      "lemma": "million",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 5,
      "deprel": "obj",
      "start_char": 33,
      "end_char": 41
    },
    {
      "id": 8,
      "text": "d'",
      "lemma": "de",
      "upos": "ADP",
      "head": 9,
      "deprel": "case",
      "start_char": 42,
      "end_char": 44,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": "euros",
      "lemma": "euro",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 7,
      "deprel": "nmod",
      "start_char": 44,
      "end_char": 49
    },
    {
      "id": 10,
      "text": "en",
      "lemma": "en",
      "upos": "ADP",
      "head": 11,
      "deprel": "case",
      "start_char": 50,
      "end_char": 52
    },
    {
      "id": 11,
      "text": "série",
      "lemma": "série",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "obl:mod",
      "start_char": 53,
      "end_char": 58
    },
    {
      "id": 12,
      "text": "A.",
      "lemma": "A.",
      "upos": "X",
      "feats": "ExtPos=PROPN",
      "head": 11,
      "deprel": "appos",
      "start_char": 59,
      "end_char": 61,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 37. Sentence

Sentence: Le site example.fr indique : "Erreur 404 - page introuvable."

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
      "text": "site",
      "lemma": "site",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "example.fr",
      "lemma": "example.fr",
      "upos": "SYM",
      "feats": "ExtPos=PROPN",
      "head": 2,
      "deprel": "appos",
      "start_char": 8,
      "end_char": 18
    },
    {
      "id": 4,
      "text": "indique",
      "lemma": "indiquer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 19,
      "end_char": 26
    },
    {
      "id": 5,
      "text": ":",
      "lemma": ":",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 27,
      "end_char": 28
    },
    {
      "id": 6,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 29,
      "end_char": 30,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": "Erreur",
      "lemma": "erreur",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 4,
      "deprel": "parataxis",
      "start_char": 30,
      "end_char": 36
    },
    {
      "id": 8,
      "text": "404",
      "lemma": "404",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 7,
      "deprel": "nmod",
      "start_char": 37,
      "end_char": 40
    },
    {
      "id": 9,
      "text": "-",
      "lemma": "-",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 41,
      "end_char": 42
    },
    {
      "id": 10,
      "text": "page",
      "lemma": "page",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 7,
      "deprel": "nmod",
      "start_char": 43,
      "end_char": 47
    },
    {
      "id": 11,
      "text": "introuvable",
      "lemma": "introuvable",
      "upos": "ADJ",
      "feats": "Number=Sing",
      "head": 10,
      "deprel": "amod",
      "start_char": 48,
      "end_char": 59,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 59,
      "end_char": 60,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 60,
      "end_char": 61,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 38. Sentence

Sentence: Envoyez votre dossier à contact@mairie-lyon.fr avant le 15 mai.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Envoyez",
      "lemma": "envoyer",
      "upos": "VERB",
      "feats": "Mood=Imp|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 0,
      "end_char": 7
    },
    {
      "id": 2,
      "text": "votre",
      "lemma": "son",
      "upos": "DET",
      "feats": "Number=Sing|Number[psor]=Plur|Person[psor]=2|Poss=Yes|PronType=Prs",
      "head": 3,
      "deprel": "det",
      "start_char": 8,
      "end_char": 13
    },
    {
      "id": 3,
      "text": "dossier",
      "lemma": "dossier",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 1,
      "deprel": "obj",
      "start_char": 14,
      "end_char": 21
    },
    {
      "id": 4,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 5,
      "deprel": "case",
      "start_char": 22,
      "end_char": 23
    },
    {
      "id": 5,
      "text": "contact@mairie-lyon.fr",
      "lemma": "contact@mairie-lyon.fr",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 1,
      "deprel": "obl:mod",
      "start_char": 24,
      "end_char": 46
    },
    {
      "id": 6,
      "text": "avant",
      "lemma": "avant",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 47,
      "end_char": 52
    },
    {
      "id": 7,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 53,
      "end_char": 55
    },
    {
      "id": 8,
      "text": "15",
      "lemma": "15",
      "upos": "NUM",
      "feats": "NumType=Card",
      "head": 1,
      "deprel": "obl:mod",
      "start_char": 56,
      "end_char": 58
    },
    {
      "id": 9,
      "text": "mai",
      "lemma": "mai",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 8,
      "deprel": "nmod",
      "start_char": 59,
      "end_char": 62,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 62,
      "end_char": 63,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 39. Sentence

Sentence: Le hashtag #OnVousRépond a été utilisé plus de 20 000 fois.

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
      "text": "hashtag",
      "lemma": "hashtag",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "nsubj:pass",
      "start_char": 3,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "#",
      "lemma": "#",
      "upos": "SYM",
      "feats": "ExtPos=VERB",
      "head": 2,
      "deprel": "appos",
      "start_char": 11,
      "end_char": 12,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "OnVousRépond",
      "lemma": "OnVousRépond",
      "upos": "PROPN",
      "head": 2,
      "deprel": "appos",
      "start_char": 12,
      "end_char": 24
    },
    {
      "id": 5,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 25,
      "end_char": 26
    },
    {
      "id": 6,
      "text": "été",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 7,
      "deprel": "aux:pass",
      "start_char": 27,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "utilisé",
      "lemma": "utiliser",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 0,
      "deprel": "root",
      "start_char": 31,
      "end_char": 38
    },
    {
      "id": 8,
      "text": "plus",
      "lemma": "plus",
      "upos": "ADV",
      "feats": "ExtPos=PRON",
      "head": 7,
      "deprel": "obl:mod",
      "start_char": 39,
      "end_char": 43
    },
    {
      "id": 9,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 11,
      "deprel": "case",
      "start_char": 44,
      "end_char": 46
    },
    {
      "id": 10,
      "text": "20 000",
      "lemma": "20 000",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 11,
      "deprel": "nummod",
      "start_char": 47,
      "end_char": 53
    },
    {
      "id": 11,
      "text": "fois",
      "lemma": "fois",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 8,
      "deprel": "obl:arg",
      "start_char": 54,
      "end_char": 58,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 58,
      "end_char": 59,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 40. Sentence

Sentence: La tempête a touché la Bretagne, la Normandie et les Hauts-de-France.

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
      "text": "tempête",
      "lemma": "tempête",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 11,
      "end_char": 12
    },
    {
      "id": 4,
      "text": "touché",
      "lemma": "toucher",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 13,
      "end_char": 19
    },
    {
      "id": 5,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 20,
      "end_char": 22
    },
    {
      "id": 6,
      "text": "Bretagne",
      "lemma": "Bretagne",
      "upos": "PROPN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 4,
      "deprel": "obj",
      "start_char": 23,
      "end_char": 31,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 31,
      "end_char": 32
    },
    {
      "id": 8,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 9,
      "deprel": "det",
      "start_char": 33,
      "end_char": 35
    },
    {
      "id": 9,
      "text": "Normandie",
      "lemma": "Normandie",
      "upos": "PROPN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 6,
      "deprel": "conj",
      "start_char": 36,
      "end_char": 45
    },
    {
      "id": 10,
      "text": "et",
      "lemma": "et",
      "upos": "CCONJ",
      "head": 12,
      "deprel": "cc",
      "start_char": 46,
      "end_char": 48
    },
    {
      "id": 11,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 12,
      "deprel": "det",
      "start_char": 49,
      "end_char": 52
    },
    {
      "id": 12,
      "text": "Hauts-de-France",
      "lemma": "Hauts-de-France",
      "upos": "PROPN",
      "feats": "Number=Plur",
      "head": 6,
      "deprel": "conj",
      "start_char": 53,
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

## 41. Sentence

Sentence: L'ex-ministre franco-allemande a défendu une position pro-européenne.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "L'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 2,
      "deprel": "det",
      "start_char": 0,
      "end_char": 2,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "ex-ministre",
      "lemma": "ex-ministre",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 2,
      "end_char": 13
    },
    {
      "id": 3,
      "text": "franco-allemande",
      "lemma": "franco-allemand",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "amod",
      "start_char": 14,
      "end_char": 30
    },
    {
      "id": 4,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 31,
      "end_char": 32
    },
    {
      "id": 5,
      "text": "défendu",
      "lemma": "défendre",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 33,
      "end_char": 40
    },
    {
      "id": 6,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 41,
      "end_char": 44
    },
    {
      "id": 7,
      "text": "position",
      "lemma": "position",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "obj",
      "start_char": 45,
      "end_char": 53
    },
    {
      "id": 8,
      "text": "pro-européenne",
      "lemma": "pro-européen",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Sing",
      "head": 7,
      "deprel": "amod",
      "start_char": 54,
      "end_char": 68,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 68,
      "end_char": 69,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 42. Sentence

Sentence: Le rendez-vous aura lieu au rez-de-chaussée, salle B-204.

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
      "text": "rendez",
      "lemma": "rendre",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 9,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "-vous",
      "lemma": "vous",
      "upos": "PRON",
      "feats": "Number=Plur|Person=2|PronType=Prs",
      "head": 2,
      "deprel": "appos",
      "start_char": 9,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "aura",
      "lemma": "avoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 15,
      "end_char": 19
    },
    {
      "id": 5,
      "text": "lieu",
      "lemma": "lieu",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obj:lvc",
      "start_char": 20,
      "end_char": 24
    },
    {
      "id": [
        6,
        7
      ],
      "text": "au",
      "start_char": 25,
      "end_char": 27
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
      "text": "rez-de-chaussée",
      "lemma": "rez-de-chaussée",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obl:mod",
      "start_char": 28,
      "end_char": 43,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 43,
      "end_char": 44
    },
    {
      "id": 10,
      "text": "salle",
      "lemma": "salle",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "appos",
      "start_char": 45,
      "end_char": 50
    },
    {
      "id": 11,
      "text": "B-204",
      "lemma": "B-204",
      "upos": "X",
      "feats": "ExtPos=PROPN",
      "head": 10,
      "deprel": "appos",
      "start_char": 51,
      "end_char": 56,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 56,
      "end_char": 57,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 43. Sentence

Sentence: Ce n'est ni simple ni impossible.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Ce",
      "lemma": "ce",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Dem",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "n'",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 5,
      "deprel": "advmod",
      "start_char": 3,
      "end_char": 5,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "cop",
      "start_char": 5,
      "end_char": 8
    },
    {
      "id": 4,
      "text": "ni",
      "lemma": "ni",
      "upos": "CCONJ",
      "head": 5,
      "deprel": "cc",
      "start_char": 9,
      "end_char": 11
    },
    {
      "id": 5,
      "text": "simple",
      "lemma": "simple",
      "upos": "ADJ",
      "feats": "Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 12,
      "end_char": 18
    },
    {
      "id": 6,
      "text": "ni",
      "lemma": "ni",
      "upos": "CCONJ",
      "head": 7,
      "deprel": "cc",
      "start_char": 19,
      "end_char": 21
    },
    {
      "id": 7,
      "text": "impossible",
      "lemma": "impossible",
      "upos": "ADJ",
      "feats": "Number=Sing",
      "head": 5,
      "deprel": "conj",
      "start_char": 22,
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

## 44. Sentence

Sentence: Personne, absolument personne, ne savait où étaient passées les clés.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Personne",
      "lemma": "personne",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|PronType=Neg",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 8,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 8,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "absolument",
      "lemma": "absolument",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 10,
      "end_char": 20
    },
    {
      "id": 4,
      "text": "personne",
      "lemma": "personne",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|PronType=Neg",
      "head": 1,
      "deprel": "appos",
      "start_char": 21,
      "end_char": 29,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 29,
      "end_char": 30
    },
    {
      "id": 6,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 7,
      "deprel": "advmod",
      "start_char": 31,
      "end_char": 33
    },
    {
      "id": 7,
      "text": "savait",
      "lemma": "savoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 34,
      "end_char": 40
    },
    {
      "id": 8,
      "text": "où",
      "lemma": "où",
      "upos": "PRON",
      "feats": "PronType=Int",
      "head": 10,
      "deprel": "iobj",
      "start_char": 41,
      "end_char": 43
    },
    {
      "id": 9,
      "text": "étaient",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 10,
      "deprel": "aux:pass",
      "start_char": 44,
      "end_char": 51
    },
    {
      "id": 10,
      "text": "passées",
      "lemma": "passer",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 7,
      "deprel": "ccomp",
      "start_char": 52,
      "end_char": 59
    },
    {
      "id": 11,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 12,
      "deprel": "det",
      "start_char": 60,
      "end_char": 63
    },
    {
      "id": 12,
      "text": "clés",
      "lemma": "clé",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 10,
      "deprel": "nsubj:pass",
      "start_char": 64,
      "end_char": 68,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 68,
      "end_char": 69,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 45. Sentence

Sentence: Plus elle lisait le rapport, moins elle comprenait la conclusion.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Plus",
      "lemma": "plus",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 5,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "lisait",
      "lemma": "lire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 10,
      "end_char": 16
    },
    {
      "id": 4,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 17,
      "end_char": 19
    },
    {
      "id": 5,
      "text": "rapport",
      "lemma": "rapport",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "obj",
      "start_char": 20,
      "end_char": 27,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 27,
      "end_char": 28
    },
    {
      "id": 7,
      "text": "moins",
      "lemma": "moins",
      "upos": "ADV",
      "head": 9,
      "deprel": "advmod",
      "start_char": 29,
      "end_char": 34
    },
    {
      "id": 8,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 35,
      "end_char": 39
    },
    {
      "id": 9,
      "text": "comprenait",
      "lemma": "comprendre",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 3,
      "deprel": "conj",
      "start_char": 40,
      "end_char": 50
    },
    {
      "id": 10,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 51,
      "end_char": 53
    },
    {
      "id": 11,
      "text": "conclusion",
      "lemma": "conclusion",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 9,
      "deprel": "obj",
      "start_char": 54,
      "end_char": 64,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 64,
      "end_char": 65,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 46. Sentence

Sentence: La voiture que Paul pensait que Marie avait vendue est encore au garage.

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
      "text": "voiture",
      "lemma": "voiture",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 10,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 5,
      "deprel": "obj",
      "start_char": 11,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "Paul",
      "lemma": "Paul",
      "upos": "PROPN",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 15,
      "end_char": 19
    },
    {
      "id": 5,
      "text": "pensait",
      "lemma": "penser",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 2,
      "deprel": "acl:relcl",
      "start_char": 20,
      "end_char": 27
    },
    {
      "id": 6,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 9,
      "deprel": "mark",
      "start_char": 28,
      "end_char": 31
    },
    {
      "id": 7,
      "text": "Marie",
      "lemma": "Marie",
      "upos": "PROPN",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 32,
      "end_char": 37
    },
    {
      "id": 8,
      "text": "avait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:tense",
      "start_char": 38,
      "end_char": 43
    },
    {
      "id": 9,
      "text": "vendue",
      "lemma": "vendre",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 5,
      "deprel": "ccomp",
      "start_char": 44,
      "end_char": 50
    },
    {
      "id": 10,
      "text": "est",
      "lemma": "être",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 51,
      "end_char": 54
    },
    {
      "id": 11,
      "text": "encore",
      "lemma": "encore",
      "upos": "ADV",
      "head": 10,
      "deprel": "advmod",
      "start_char": 55,
      "end_char": 61
    },
    {
      "id": [
        12,
        13
      ],
      "text": "au",
      "start_char": 62,
      "end_char": 64
    },
    {
      "id": 12,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 14,
      "deprel": "case"
    },
    {
      "id": 13,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 14,
      "deprel": "det"
    },
    {
      "id": 14,
      "text": "garage",
      "lemma": "garage",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 10,
      "deprel": "obl:arg",
      "start_char": 65,
      "end_char": 71,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 71,
      "end_char": 72,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 47. Sentence

Sentence: Les amis de mon frère que tu as rencontrés hier déménagent à Nantes.

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
      "text": "amis",
      "lemma": "ami",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 11,
      "deprel": "nsubj",
      "start_char": 4,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 5,
      "deprel": "case",
      "start_char": 9,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "mon",
      "lemma": "son",
      "upos": "DET",
      "feats": "Gender=Masc|Number=Sing|Number[psor]=Sing|Person[psor]=1|Poss=Yes|PronType=Prs",
      "head": 5,
      "deprel": "det",
      "start_char": 12,
      "end_char": 15
    },
    {
      "id": 5,
      "text": "frère",
      "lemma": "frère",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 2,
      "deprel": "nmod",
      "start_char": 16,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 9,
      "deprel": "obj",
      "start_char": 22,
      "end_char": 25
    },
    {
      "id": 7,
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 26,
      "end_char": 28
    },
    {
      "id": 8,
      "text": "as",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:tense",
      "start_char": 29,
      "end_char": 31
    },
    {
      "id": 9,
      "text": "rencontrés",
      "lemma": "rencontrer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 5,
      "deprel": "acl:relcl",
      "start_char": 32,
      "end_char": 42
    },
    {
      "id": 10,
      "text": "hier",
      "lemma": "hier",
      "upos": "ADV",
      "head": 9,
      "deprel": "advmod",
      "start_char": 43,
      "end_char": 47
    },
    {
      "id": 11,
      "text": "déménagent",
      "lemma": "déménager",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 48,
      "end_char": 58
    },
    {
      "id": 12,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 13,
      "deprel": "case",
      "start_char": 59,
      "end_char": 60
    },
    {
      "id": 13,
      "text": "Nantes",
      "lemma": "Nantes",
      "upos": "PROPN",
      "head": 11,
      "deprel": "obl:arg",
      "start_char": 61,
      "end_char": 67,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 11,
      "deprel": "punct",
      "start_char": 67,
      "end_char": 68,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 48. Sentence

Sentence: Le logiciel analyse les phrases, mais il confond parfois noms propres et adjectifs.

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
      "text": "logiciel",
      "lemma": "logiciel",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "analyse",
      "lemma": "analyser",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 12,
      "end_char": 19
    },
    {
      "id": 4,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 20,
      "end_char": 23
    },
    {
      "id": 5,
      "text": "phrases",
      "lemma": "phrase",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 3,
      "deprel": "obj",
      "start_char": 24,
      "end_char": 31,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 31,
      "end_char": 32
    },
    {
      "id": 7,
      "text": "mais",
      "lemma": "mais",
      "upos": "CCONJ",
      "head": 9,
      "deprel": "cc",
      "start_char": 33,
      "end_char": 37
    },
    {
      "id": 8,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 38,
      "end_char": 40
    },
    {
      "id": 9,
      "text": "confond",
      "lemma": "confondre",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "conj",
      "start_char": 41,
      "end_char": 48
    },
    {
      "id": 10,
      "text": "parfois",
      "lemma": "parfois",
      "upos": "ADV",
      "head": 9,
      "deprel": "advmod",
      "start_char": 49,
      "end_char": 56
    },
    {
      "id": 11,
      "text": "noms",
      "lemma": "nom",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 9,
      "deprel": "obj",
      "start_char": 57,
      "end_char": 61
    },
    {
      "id": 12,
      "text": "propres",
      "lemma": "propre",
      "upos": "ADJ",
      "feats": "Number=Plur",
      "head": 11,
      "deprel": "amod",
      "start_char": 62,
      "end_char": 69
    },
    {
      "id": 13,
      "text": "et",
      "lemma": "et",
      "upos": "CCONJ",
      "head": 14,
      "deprel": "cc",
      "start_char": 70,
      "end_char": 72
    },
    {
      "id": 14,
      "text": "adjectifs",
      "lemma": "adjectif",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 12,
      "deprel": "conj",
      "start_char": 73,
      "end_char": 82,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 82,
      "end_char": 83,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 49. Sentence

Sentence: Quand il y a "des" devant un mot, ce n'est pas toujours un article indéfini simple.

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
      "deprel": "expl:subj",
      "start_char": 6,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "y",
      "lemma": "y",
      "upos": "PRON",
      "feats": "Emph=No|Person=3|PronType=Prs",
      "head": 4,
      "deprel": "expl:comp",
      "start_char": 9,
      "end_char": 10
    },
    {
      "id": 4,
      "text": "a",
      "lemma": "avoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 18,
      "deprel": "advcl",
      "start_char": 11,
      "end_char": 12
    },
    {
      "id": 5,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 13,
      "end_char": 14,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "des",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Number=Plur|PronType=Art",
      "head": 4,
      "deprel": "obj",
      "start_char": 14,
      "end_char": 17,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 17,
      "end_char": 18
    },
    {
      "id": 8,
      "text": "devant",
      "lemma": "devant",
      "upos": "ADP",
      "head": 10,
      "deprel": "case",
      "start_char": 19,
      "end_char": 25
    },
    {
      "id": 9,
      "text": "un",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Masc|Number=Sing|PronType=Art",
      "head": 10,
      "deprel": "det",
      "start_char": 26,
      "end_char": 28
    },
    {
      "id": 10,
      "text": "mot",
      "lemma": "mot",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obl:mod",
      "start_char": 29,
      "end_char": 32,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 32,
      "end_char": 33
    },
    {
      "id": 12,
      "text": "ce",
      "lemma": "ce",
      "upos": "PRON",
      "feats": "Gender=Masc|Person=3|PronType=Dem",
      "head": 18,
      "deprel": "nsubj",
      "start_char": 34,
      "end_char": 36
    },
    {
      "id": 13,
      "text": "n'",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 18,
      "deprel": "advmod",
      "start_char": 37,
      "end_char": 39,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 18,
      "deprel": "cop",
      "start_char": 39,
      "end_char": 42
    },
    {
      "id": 15,
      "text": "pas",
      "lemma": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 18,
      "deprel": "advmod",
      "start_char": 43,
      "end_char": 46
    },
    {
      "id": 16,
      "text": "toujours",
      "lemma": "toujours",
      "upos": "ADV",
      "head": 18,
      "deprel": "advmod",
      "start_char": 47,
      "end_char": 55
    },
    {
      "id": 17,
      "text": "un",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Masc|Number=Sing|PronType=Art",
      "head": 18,
      "deprel": "det",
      "start_char": 56,
      "end_char": 58
    },
    {
      "id": 18,
      "text": "article",
      "lemma": "article",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 59,
      "end_char": 66
    },
    {
      "id": 19,
      "text": "indéfini",
      "lemma": "indéfini",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 18,
      "deprel": "amod",
      "start_char": 67,
      "end_char": 75
    },
    {
      "id": 20,
      "text": "simple",
      "lemma": "simple",
      "upos": "ADJ",
      "feats": "Number=Sing",
      "head": 18,
      "deprel": "amod",
      "start_char": 76,
      "end_char": 82,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 21,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 18,
      "deprel": "punct",
      "start_char": 82,
      "end_char": 83,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 50. Sentence

Sentence: Les données dont nous disposons ne suffisent pas à établir une tendance fiable.

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
      "text": "données",
      "lemma": "donnée",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 4,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "dont",
      "lemma": "dont",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 5,
      "deprel": "iobj",
      "start_char": 12,
      "end_char": 16
    },
    {
      "id": 4,
      "text": "nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 17,
      "end_char": 21
    },
    {
      "id": 5,
      "text": "disposons",
      "lemma": "disposer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "acl:relcl",
      "start_char": 22,
      "end_char": 31
    },
    {
      "id": 6,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 7,
      "deprel": "advmod",
      "start_char": 32,
      "end_char": 34
    },
    {
      "id": 7,
      "text": "suffisent",
      "lemma": "suffiser",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 35,
      "end_char": 44
    },
    {
      "id": 8,
      "text": "pas",
      "lemma": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 7,
      "deprel": "advmod",
      "start_char": 45,
      "end_char": 48
    },
    {
      "id": 9,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 10,
      "deprel": "mark",
      "start_char": 49,
      "end_char": 50
    },
    {
      "id": 10,
      "text": "établir",
      "lemma": "établir",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 7,
      "deprel": "xcomp",
      "start_char": 51,
      "end_char": 58
    },
    {
      "id": 11,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 12,
      "deprel": "det",
      "start_char": 59,
      "end_char": 62
    },
    {
      "id": 12,
      "text": "tendance",
      "lemma": "tendance",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 10,
      "deprel": "obj",
      "start_char": 63,
      "end_char": 71
    },
    {
      "id": 13,
      "text": "fiable",
      "lemma": "fiable",
      "upos": "ADJ",
      "feats": "Number=Sing",
      "head": 12,
      "deprel": "amod",
      "start_char": 72,
      "end_char": 78,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 78,
      "end_char": 79,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 51. Sentence

Sentence: Ce dont elle a besoin, ce n'est pas d'un conseil, mais d'un délai.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Ce",
      "lemma": "ce",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Dem",
      "head": 13,
      "deprel": "dislocated",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "dont",
      "lemma": "dont",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 4,
      "deprel": "iobj",
      "start_char": 3,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 8,
      "end_char": 12
    },
    {
      "id": 4,
      "text": "a",
      "lemma": "avoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 1,
      "deprel": "acl:relcl",
      "start_char": 13,
      "end_char": 14
    },
    {
      "id": 5,
      "text": "besoin",
      "lemma": "besoin",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obj:lvc",
      "start_char": 15,
      "end_char": 21,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 21,
      "end_char": 22
    },
    {
      "id": 7,
      "text": "ce",
      "lemma": "ce",
      "upos": "PRON",
      "feats": "Gender=Masc|Person=3|PronType=Dem",
      "head": 13,
      "deprel": "nsubj",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 8,
      "text": "n'",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 13,
      "deprel": "advmod",
      "start_char": 26,
      "end_char": 28,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 13,
      "deprel": "cop",
      "start_char": 28,
      "end_char": 31
    },
    {
      "id": 10,
      "text": "pas",
      "lemma": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 13,
      "deprel": "advmod",
      "start_char": 32,
      "end_char": 35
    },
    {
      "id": 11,
      "text": "d'",
      "lemma": "de",
      "upos": "ADP",
      "head": 13,
      "deprel": "case",
      "start_char": 36,
      "end_char": 38,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": "un",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Masc|Number=Sing|PronType=Art",
      "head": 13,
      "deprel": "det",
      "start_char": 38,
      "end_char": 40
    },
    {
      "id": 13,
      "text": "conseil",
      "lemma": "conseil",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 41,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 18,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49
    },
    {
      "id": 15,
      "text": "mais",
      "lemma": "mais",
      "upos": "CCONJ",
      "head": 18,
      "deprel": "cc",
      "start_char": 50,
      "end_char": 54
    },
    {
      "id": 16,
      "text": "d'",
      "lemma": "de",
      "upos": "ADP",
      "head": 18,
      "deprel": "case",
      "start_char": 55,
      "end_char": 57,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 17,
      "text": "un",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Masc|Number=Sing|PronType=Art",
      "head": 18,
      "deprel": "det",
      "start_char": 57,
      "end_char": 59
    },
    {
      "id": 18,
      "text": "délai",
      "lemma": "délai",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 13,
      "deprel": "conj",
      "start_char": 60,
      "end_char": 65,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 19,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 13,
      "deprel": "punct",
      "start_char": 65,
      "end_char": 66,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 52. Sentence

Sentence: L'homme qui avait vu l'accident dont parlait le journal a finalement témoigné.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "L'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 2,
      "deprel": "det",
      "start_char": 0,
      "end_char": 2,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "homme",
      "lemma": "homme",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 14,
      "deprel": "nsubj",
      "start_char": 2,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "qui",
      "lemma": "qui",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 8,
      "end_char": 11
    },
    {
      "id": 4,
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
      "id": 5,
      "text": "vu",
      "lemma": "voir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 2,
      "deprel": "acl:relcl",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 21,
      "end_char": 23,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": "accident",
      "lemma": "accident",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "obj",
      "start_char": 23,
      "end_char": 31
    },
    {
      "id": 8,
      "text": "dont",
      "lemma": "dont",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 9,
      "deprel": "iobj",
      "start_char": 32,
      "end_char": 36
    },
    {
      "id": 9,
      "text": "parlait",
      "lemma": "parler",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 7,
      "deprel": "acl:relcl",
      "start_char": 37,
      "end_char": 44
    },
    {
      "id": 10,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 45,
      "end_char": 47
    },
    {
      "id": 11,
      "text": "journal",
      "lemma": "journal",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 48,
      "end_char": 55
    },
    {
      "id": 12,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 14,
      "deprel": "aux:tense",
      "start_char": 56,
      "end_char": 57
    },
    {
      "id": 13,
      "text": "finalement",
      "lemma": "finalement",
      "upos": "ADV",
      "head": 14,
      "deprel": "advmod",
      "start_char": 58,
      "end_char": 68
    },
    {
      "id": 14,
      "text": "témoigné",
      "lemma": "témoigner",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 69,
      "end_char": 77,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 14,
      "deprel": "punct",
      "start_char": 77,
      "end_char": 78,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 53. Sentence

Sentence: La candidate, soutenue par une coalition fragile, a promis de "réparer le pays".

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
      "text": "candidate",
      "lemma": "candidate",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 11,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 12,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 12,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "soutenue",
      "lemma": "soutenir",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 2,
      "deprel": "acl",
      "start_char": 14,
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
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 27,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "coalition",
      "lemma": "coalition",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 4,
      "deprel": "obl:agent",
      "start_char": 31,
      "end_char": 40
    },
    {
      "id": 8,
      "text": "fragile",
      "lemma": "fragile",
      "upos": "ADJ",
      "feats": "Number=Sing",
      "head": 7,
      "deprel": "amod",
      "start_char": 41,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49
    },
    {
      "id": 10,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 11,
      "deprel": "aux:tense",
      "start_char": 50,
      "end_char": 51
    },
    {
      "id": 11,
      "text": "promis",
      "lemma": "promettre",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 52,
      "end_char": 58
    },
    {
      "id": 12,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 14,
      "deprel": "mark",
      "start_char": 59,
      "end_char": 61
    },
    {
      "id": 13,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 14,
      "deprel": "punct",
      "start_char": 62,
      "end_char": 63,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": "réparer",
      "lemma": "réparer",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 11,
      "deprel": "xcomp",
      "start_char": 63,
      "end_char": 70
    },
    {
      "id": 15,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 16,
      "deprel": "det",
      "start_char": 71,
      "end_char": 73
    },
    {
      "id": 16,
      "text": "pays",
      "lemma": "pays",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 14,
      "deprel": "obj",
      "start_char": 74,
      "end_char": 78,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 17,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 14,
      "deprel": "punct",
      "start_char": 78,
      "end_char": 79,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 18,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 11,
      "deprel": "punct",
      "start_char": 79,
      "end_char": 80,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 54. Sentence

Sentence: Après trois heures de débat, le texte a été adopté par 289 voix contre 248.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Après",
      "lemma": "après",
      "upos": "ADP",
      "head": 3,
      "deprel": "case",
      "start_char": 0,
      "end_char": 5
    },
    {
      "id": 2,
      "text": "trois",
      "lemma": "trois",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 3,
      "deprel": "nummod",
      "start_char": 6,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "heures",
      "lemma": "heure",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 11,
      "deprel": "obl:mod",
      "start_char": 12,
      "end_char": 18
    },
    {
      "id": 4,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 5,
      "deprel": "case",
      "start_char": 19,
      "end_char": 21
    },
    {
      "id": 5,
      "text": "débat",
      "lemma": "débat",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "nmod",
      "start_char": 22,
      "end_char": 27,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 27,
      "end_char": 28
    },
    {
      "id": 7,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 29,
      "end_char": 31
    },
    {
      "id": 8,
      "text": "texte",
      "lemma": "texte",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 11,
      "deprel": "nsubj:pass",
      "start_char": 32,
      "end_char": 37
    },
    {
      "id": 9,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 11,
      "deprel": "aux:tense",
      "start_char": 38,
      "end_char": 39
    },
    {
      "id": 10,
      "text": "été",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 11,
      "deprel": "aux:pass",
      "start_char": 40,
      "end_char": 43
    },
    {
      "id": 11,
      "text": "adopté",
      "lemma": "adopter",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 0,
      "deprel": "root",
      "start_char": 44,
      "end_char": 50
    },
    {
      "id": 12,
      "text": "par",
      "lemma": "par",
      "upos": "ADP",
      "head": 14,
      "deprel": "case",
      "start_char": 51,
      "end_char": 54
    },
    {
      "id": 13,
      "text": "289",
      "lemma": "289",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 14,
      "deprel": "nummod",
      "start_char": 55,
      "end_char": 58
    },
    {
      "id": 14,
      "text": "voix",
      "lemma": "voix",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 11,
      "deprel": "obl:agent",
      "start_char": 59,
      "end_char": 63
    },
    {
      "id": 15,
      "text": "contre",
      "lemma": "contre",
      "upos": "ADP",
      "head": 16,
      "deprel": "case",
      "start_char": 64,
      "end_char": 70
    },
    {
      "id": 16,
      "text": "248",
      "lemma": "248",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 11,
      "deprel": "obl:mod",
      "start_char": 71,
      "end_char": 74,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 17,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 11,
      "deprel": "punct",
      "start_char": 74,
      "end_char": 75,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 55. Sentence

Sentence: Une panne informatique a perturbé les vols au départ de Roissy pendant la matinée.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 2,
      "deprel": "det",
      "start_char": 0,
      "end_char": 3
    },
    {
      "id": 2,
      "text": "panne",
      "lemma": "panne",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 4,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "informatique",
      "lemma": "informatique",
      "upos": "ADJ",
      "feats": "Number=Sing",
      "head": 2,
      "deprel": "amod",
      "start_char": 10,
      "end_char": 22
    },
    {
      "id": 4,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 23,
      "end_char": 24
    },
    {
      "id": 5,
      "text": "perturbé",
      "lemma": "perturber",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 25,
      "end_char": 33
    },
    {
      "id": 6,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 34,
      "end_char": 37
    },
    {
      "id": 7,
      "text": "vols",
      "lemma": "vol",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 5,
      "deprel": "obj",
      "start_char": 38,
      "end_char": 42
    },
    {
      "id": [
        8,
        9
      ],
      "text": "au",
      "start_char": 43,
      "end_char": 45
    },
    {
      "id": 8,
      "text": "à",
      "lemma": "à",
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
      "text": "départ",
      "lemma": "départ",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "obl:mod",
      "start_char": 46,
      "end_char": 52
    },
    {
      "id": 11,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 12,
      "deprel": "case",
      "start_char": 53,
      "end_char": 55
    },
    {
      "id": 12,
      "text": "Roissy",
      "lemma": "Roissy",
      "upos": "PROPN",
      "head": 10,
      "deprel": "nmod",
      "start_char": 56,
      "end_char": 62
    },
    {
      "id": 13,
      "text": "pendant",
      "lemma": "pendant",
      "upos": "ADP",
      "head": 15,
      "deprel": "case",
      "start_char": 63,
      "end_char": 70
    },
    {
      "id": 14,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 15,
      "deprel": "det",
      "start_char": 71,
      "end_char": 73
    },
    {
      "id": 15,
      "text": "matinée",
      "lemma": "matinée",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "obl:mod",
      "start_char": 74,
      "end_char": 81,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 16,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 81,
      "end_char": 82,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 56. Sentence

Sentence: Les chercheurs affirment que leur modèle réduit les erreurs de traduction de 12 %.

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
      "text": "chercheurs",
      "lemma": "chercheur",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 4,
      "end_char": 14
    },
    {
      "id": 3,
      "text": "affirment",
      "lemma": "affirmer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 15,
      "end_char": 24
    },
    {
      "id": 4,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 25,
      "end_char": 28
    },
    {
      "id": 5,
      "text": "leur",
      "lemma": "son",
      "upos": "DET",
      "feats": "Number=Sing|Number[psor]=Plur|Person[psor]=3|Poss=Yes|PronType=Prs",
      "head": 6,
      "deprel": "det",
      "start_char": 29,
      "end_char": 33
    },
    {
      "id": 6,
      "text": "modèle",
      "lemma": "modèle",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 34,
      "end_char": 40
    },
    {
      "id": 7,
      "text": "réduit",
      "lemma": "réduire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "ccomp",
      "start_char": 41,
      "end_char": 47
    },
    {
      "id": 8,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 9,
      "deprel": "det",
      "start_char": 48,
      "end_char": 51
    },
    {
      "id": 9,
      "text": "erreurs",
      "lemma": "erreur",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 7,
      "deprel": "obj",
      "start_char": 52,
      "end_char": 59
    },
    {
      "id": 10,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 11,
      "deprel": "case",
      "start_char": 60,
      "end_char": 62
    },
    {
      "id": 11,
      "text": "traduction",
      "lemma": "traduction",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 9,
      "deprel": "nmod",
      "start_char": 63,
      "end_char": 73
    },
    {
      "id": 12,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 14,
      "deprel": "case",
      "start_char": 74,
      "end_char": 76
    },
    {
      "id": 13,
      "text": "12",
      "lemma": "12",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 14,
      "deprel": "nummod",
      "start_char": 77,
      "end_char": 79
    },
    {
      "id": 14,
      "text": "%",
      "lemma": "%",
      "upos": "SYM",
      "feats": "ExtPos=NOUN|Number=Plur",
      "head": 9,
      "deprel": "nmod",
      "start_char": 80,
      "end_char": 81,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 81,
      "end_char": 82,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 57. Sentence

Sentence: Dans les quartiers populaires, beaucoup redoutent une nouvelle hausse des loyers.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Dans",
      "lemma": "dans",
      "upos": "ADP",
      "head": 3,
      "deprel": "case",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 3,
      "deprel": "det",
      "start_char": 5,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "quartiers",
      "lemma": "quartier",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 7,
      "deprel": "obl:mod",
      "start_char": 9,
      "end_char": 18
    },
    {
      "id": 4,
      "text": "populaires",
      "lemma": "populaire",
      "upos": "ADJ",
      "feats": "Number=Plur",
      "head": 3,
      "deprel": "amod",
      "start_char": 19,
      "end_char": 29,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 29,
      "end_char": 30
    },
    {
      "id": 6,
      "text": "beaucoup",
      "lemma": "beaucoup",
      "upos": "ADV",
      "feats": "ExtPos=PRON",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 31,
      "end_char": 39
    },
    {
      "id": 7,
      "text": "redoutent",
      "lemma": "redouter",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 40,
      "end_char": 49
    },
    {
      "id": 8,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 10,
      "deprel": "det",
      "start_char": 50,
      "end_char": 53
    },
    {
      "id": 9,
      "text": "nouvelle",
      "lemma": "nouveau",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Sing",
      "head": 10,
      "deprel": "amod",
      "start_char": 54,
      "end_char": 62
    },
    {
      "id": 10,
      "text": "hausse",
      "lemma": "hausse",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 7,
      "deprel": "obj",
      "start_char": 63,
      "end_char": 69
    },
    {
      "id": [
        11,
        12
      ],
      "text": "des",
      "start_char": 70,
      "end_char": 73
    },
    {
      "id": 11,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 13,
      "deprel": "case"
    },
    {
      "id": 12,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 13,
      "deprel": "det"
    },
    {
      "id": 13,
      "text": "loyers",
      "lemma": "loyer",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 10,
      "deprel": "nmod",
      "start_char": 74,
      "end_char": 80,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 80,
      "end_char": 81,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 58. Sentence

Sentence: L'équipe de France s'est imposée 2-1 après un but marqué dans le temps additionnel.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "L'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 2,
      "deprel": "det",
      "start_char": 0,
      "end_char": 2,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "équipe",
      "lemma": "équipe",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 2,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 4,
      "deprel": "case",
      "start_char": 9,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "France",
      "lemma": "France",
      "upos": "PROPN",
      "head": 2,
      "deprel": "nmod",
      "start_char": 12,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "s'",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 7,
      "deprel": "expl:pv",
      "start_char": 19,
      "end_char": 21,
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
      "start_char": 21,
      "end_char": 24
    },
    {
      "id": 7,
      "text": "imposée",
      "lemma": "imposer",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 25,
      "end_char": 32
    },
    {
      "id": 8,
      "text": "2-1",
      "lemma": "2-1",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 7,
      "deprel": "obl:mod",
      "start_char": 33,
      "end_char": 36
    },
    {
      "id": 9,
      "text": "après",
      "lemma": "après",
      "upos": "ADP",
      "head": 11,
      "deprel": "case",
      "start_char": 37,
      "end_char": 42
    },
    {
      "id": 10,
      "text": "un",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Masc|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 43,
      "end_char": 45
    },
    {
      "id": 11,
      "text": "but",
      "lemma": "but",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "obl:mod",
      "start_char": 46,
      "end_char": 49
    },
    {
      "id": 12,
      "text": "marqué",
      "lemma": "marquer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 11,
      "deprel": "acl",
      "start_char": 50,
      "end_char": 56
    },
    {
      "id": 13,
      "text": "dans",
      "lemma": "dans",
      "upos": "ADP",
      "head": 15,
      "deprel": "case",
      "start_char": 57,
      "end_char": 61
    },
    {
      "id": 14,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 15,
      "deprel": "det",
      "start_char": 62,
      "end_char": 64
    },
    {
      "id": 15,
      "text": "temps",
      "lemma": "temps",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 12,
      "deprel": "obl:mod",
      "start_char": 65,
      "end_char": 70
    },
    {
      "id": 16,
      "text": "additionnel",
      "lemma": "additionnel",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 15,
      "deprel": "amod",
      "start_char": 71,
      "end_char": 82,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 17,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 82,
      "end_char": 83,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 59. Sentence

Sentence: Le maire a reconnu des "dysfonctionnements", tout en refusant de démissionner.

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
      "text": "maire",
      "lemma": "maire",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 8
    },
    {
      "id": 3,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 9,
      "end_char": 10
    },
    {
      "id": 4,
      "text": "reconnu",
      "lemma": "reconnaître",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 0,
      "deprel": "root",
      "start_char": 11,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "des",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Number=Plur|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 19,
      "end_char": 22
    },
    {
      "id": 6,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 23,
      "end_char": 24,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": "dysfonctionnements",
      "lemma": "dysfonctionnement",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 4,
      "deprel": "obj",
      "start_char": 24,
      "end_char": 42,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 42,
      "end_char": 43,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 12,
      "deprel": "punct",
      "start_char": 43,
      "end_char": 44
    },
    {
      "id": 10,
      "text": "tout",
      "lemma": "tout",
      "upos": "ADV",
      "head": 12,
      "deprel": "advmod",
      "start_char": 45,
      "end_char": 49
    },
    {
      "id": 11,
      "text": "en",
      "lemma": "en",
      "upos": "ADP",
      "head": 12,
      "deprel": "mark",
      "start_char": 50,
      "end_char": 52
    },
    {
      "id": 12,
      "text": "refusant",
      "lemma": "refuser",
      "upos": "VERB",
      "feats": "Tense=Pres|VerbForm=Part",
      "head": 4,
      "deprel": "advcl",
      "start_char": 53,
      "end_char": 61
    },
    {
      "id": 13,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 14,
      "deprel": "mark",
      "start_char": 62,
      "end_char": 64
    },
    {
      "id": 14,
      "text": "démissionner",
      "lemma": "démissionner",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 12,
      "deprel": "xcomp",
      "start_char": 65,
      "end_char": 77,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 77,
      "end_char": 78,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 60. Sentence

Sentence: Sur Netflix, une comédie française mélange enquête familiale et satire politique.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Sur",
      "lemma": "sur",
      "upos": "ADP",
      "head": 2,
      "deprel": "case",
      "start_char": 0,
      "end_char": 3
    },
    {
      "id": 2,
      "text": "Netflix",
      "lemma": "Netflix",
      "upos": "PROPN",
      "head": 7,
      "deprel": "obl:mod",
      "start_char": 4,
      "end_char": 11,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 11,
      "end_char": 12
    },
    {
      "id": 4,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 13,
      "end_char": 16
    },
    {
      "id": 5,
      "text": "comédie",
      "lemma": "comédie",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 17,
      "end_char": 24
    },
    {
      "id": 6,
      "text": "française",
      "lemma": "français",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "amod",
      "start_char": 25,
      "end_char": 34
    },
    {
      "id": 7,
      "text": "mélange",
      "lemma": "mélanger",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 35,
      "end_char": 42
    },
    {
      "id": 8,
      "text": "enquête",
      "lemma": "enquête",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 7,
      "deprel": "obj",
      "start_char": 43,
      "end_char": 50
    },
    {
      "id": 9,
      "text": "familiale",
      "lemma": "familial",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "amod",
      "start_char": 51,
      "end_char": 60
    },
    {
      "id": 10,
      "text": "et",
      "lemma": "et",
      "upos": "CCONJ",
      "head": 11,
      "deprel": "cc",
      "start_char": 61,
      "end_char": 63
    },
    {
      "id": 11,
      "text": "satire",
      "lemma": "satire",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "conj",
      "start_char": 64,
      "end_char": 70
    },
    {
      "id": 12,
      "text": "politique",
      "lemma": "politique",
      "upos": "ADJ",
      "feats": "Number=Sing",
      "head": 11,
      "deprel": "amod",
      "start_char": 71,
      "end_char": 80,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 80,
      "end_char": 81,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 61. Sentence

Sentence: La présentatrice coupe court à la polémique : "On va vérifier les chiffres."

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
      "text": "présentatrice",
      "lemma": "présentatrice",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 3,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 16
    },
    {
      "id": 3,
      "text": "coupe",
      "lemma": "couper",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 17,
      "end_char": 22
    },
    {
      "id": 4,
      "text": "court",
      "lemma": "court",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "xcomp",
      "start_char": 23,
      "end_char": 28
    },
    {
      "id": 5,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 7,
      "deprel": "case",
      "start_char": 29,
      "end_char": 30
    },
    {
      "id": 6,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 31,
      "end_char": 33
    },
    {
      "id": 7,
      "text": "polémique",
      "lemma": "polémique",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 3,
      "deprel": "obl:arg",
      "start_char": 34,
      "end_char": 43
    },
    {
      "id": 8,
      "text": ":",
      "lemma": ":",
      "upos": "PUNCT",
      "head": 11,
      "deprel": "punct",
      "start_char": 44,
      "end_char": 45
    },
    {
      "id": 9,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 11,
      "deprel": "punct",
      "start_char": 46,
      "end_char": 47,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": "On",
      "lemma": "on",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Ind",
      "head": 11,
      "deprel": "nsubj",
      "start_char": 47,
      "end_char": 49
    },
    {
      "id": 11,
      "text": "va",
      "lemma": "aller",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "parataxis",
      "start_char": 50,
      "end_char": 52
    },
    {
      "id": 12,
      "text": "vérifier",
      "lemma": "vérifier",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 11,
      "deprel": "xcomp",
      "start_char": 53,
      "end_char": 61
    },
    {
      "id": 13,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 14,
      "deprel": "det",
      "start_char": 62,
      "end_char": 65
    },
    {
      "id": 14,
      "text": "chiffres",
      "lemma": "chiffre",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 12,
      "deprel": "obj",
      "start_char": 66,
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
    },
    {
      "id": 16,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 75,
      "end_char": 76,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 62. Sentence

Sentence: Ce film, je l'avais vu quand j'étais petit, mais je ne m'en souvenais presque plus.

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
      "text": "film",
      "lemma": "film",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "dislocated",
      "start_char": 3,
      "end_char": 7,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 7,
      "end_char": 8
    },
    {
      "id": 4,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 9,
      "end_char": 11
    },
    {
      "id": 5,
      "text": "l'",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "obj",
      "start_char": 12,
      "end_char": 14,
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
      "start_char": 14,
      "end_char": 19
    },
    {
      "id": 7,
      "text": "vu",
      "lemma": "voir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 20,
      "end_char": 22
    },
    {
      "id": 8,
      "text": "quand",
      "lemma": "quand",
      "upos": "SCONJ",
      "head": 11,
      "deprel": "mark",
      "start_char": 23,
      "end_char": 28
    },
    {
      "id": 9,
      "text": "j'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 11,
      "deprel": "nsubj",
      "start_char": 29,
      "end_char": 31,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": "étais",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 11,
      "deprel": "cop",
      "start_char": 31,
      "end_char": 36
    },
    {
      "id": 11,
      "text": "petit",
      "lemma": "petit",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "advcl",
      "start_char": 37,
      "end_char": 42,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 18,
      "deprel": "punct",
      "start_char": 42,
      "end_char": 43
    },
    {
      "id": 13,
      "text": "mais",
      "lemma": "mais",
      "upos": "CCONJ",
      "head": 18,
      "deprel": "cc",
      "start_char": 44,
      "end_char": 48
    },
    {
      "id": 14,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 18,
      "deprel": "nsubj",
      "start_char": 49,
      "end_char": 51
    },
    {
      "id": 15,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 18,
      "deprel": "advmod",
      "start_char": 52,
      "end_char": 54
    },
    {
      "id": 16,
      "text": "m'",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 18,
      "deprel": "expl:pv",
      "start_char": 55,
      "end_char": 57,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 17,
      "text": "en",
      "lemma": "en",
      "upos": "PRON",
      "feats": "Emph=No|Person=3|PronType=Prs",
      "head": 18,
      "deprel": "iobj",
      "start_char": 57,
      "end_char": 59
    },
    {
      "id": 18,
      "text": "souvenais",
      "lemma": "souvenir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 7,
      "deprel": "conj",
      "start_char": 60,
      "end_char": 69
    },
    {
      "id": 19,
      "text": "presque",
      "lemma": "presque",
      "upos": "ADV",
      "head": 20,
      "deprel": "advmod",
      "start_char": 70,
      "end_char": 77
    },
    {
      "id": 20,
      "text": "plus",
      "lemma": "plus",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 18,
      "deprel": "advmod",
      "start_char": 78,
      "end_char": 82,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 21,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 82,
      "end_char": 83,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 63. Sentence

Sentence: Il faut que tu fasses attention à ce que tu signes.

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
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 12,
      "end_char": 14
    },
    {
      "id": 5,
      "text": "fasses",
      "lemma": "faire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "ccomp",
      "start_char": 15,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "attention",
      "lemma": "attention",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "obj:lvc",
      "start_char": 22,
      "end_char": 31
    },
    {
      "id": 7,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 32,
      "end_char": 33
    },
    {
      "id": 8,
      "text": "ce",
      "lemma": "ce",
      "upos": "PRON",
      "feats": "Gender=Masc|Person=3|PronType=Dem",
      "head": 5,
      "deprel": "obl:arg",
      "start_char": 34,
      "end_char": 36
    },
    {
      "id": 9,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 11,
      "deprel": "obj",
      "start_char": 37,
      "end_char": 40
    },
    {
      "id": 10,
      "text": "tu",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 11,
      "deprel": "nsubj",
      "start_char": 41,
      "end_char": 43
    },
    {
      "id": 11,
      "text": "signes",
      "lemma": "signer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 8,
      "deprel": "acl:relcl",
      "start_char": 44,
      "end_char": 50,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
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

## 64. Sentence

Sentence: Je doute qu'ils aient compris pourquoi nous étions partis si vite.

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
      "head": 6,
      "deprel": "mark",
      "start_char": 9,
      "end_char": 12,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "ils",
      "lemma": "eux",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 12,
      "end_char": 15
    },
    {
      "id": 5,
      "text": "aient",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 6,
      "deprel": "aux:tense",
      "start_char": 16,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "compris",
      "lemma": "comprendre",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 2,
      "deprel": "ccomp",
      "start_char": 22,
      "end_char": 29
    },
    {
      "id": 7,
      "text": "pourquoi",
      "lemma": "pourquoi",
      "upos": "ADV",
      "feats": "PronType=Int",
      "head": 10,
      "deprel": "advmod",
      "start_char": 30,
      "end_char": 38
    },
    {
      "id": 8,
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
      "id": 9,
      "text": "étions",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin",
      "head": 10,
      "deprel": "aux:tense",
      "start_char": 44,
      "end_char": 50
    },
    {
      "id": 10,
      "text": "partis",
      "lemma": "partir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part",
      "head": 6,
      "deprel": "ccomp",
      "start_char": 51,
      "end_char": 57
    },
    {
      "id": 11,
      "text": "si",
      "lemma": "si",
      "upos": "ADV",
      "head": 12,
      "deprel": "advmod",
      "start_char": 58,
      "end_char": 60
    },
    {
      "id": 12,
      "text": "vite",
      "lemma": "vite",
      "upos": "ADV",
      "head": 10,
      "deprel": "advmod",
      "start_char": 61,
      "end_char": 65,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 65,
      "end_char": 66,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 65. Sentence

Sentence: À supposer qu'il ait raison, que devrions-nous faire maintenant ?

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "À",
      "lemma": "à",
      "upos": "ADP",
      "head": 2,
      "deprel": "mark",
      "start_char": 0,
      "end_char": 1
    },
    {
      "id": 2,
      "text": "supposer",
      "lemma": "supposer",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 9,
      "deprel": "advcl",
      "start_char": 2,
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
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 14,
      "end_char": 16
    },
    {
      "id": 5,
      "text": "ait",
      "lemma": "avoir",
      "upos": "VERB",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "ccomp",
      "start_char": 17,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "raison",
      "lemma": "raison",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "obj:lvc",
      "start_char": 21,
      "end_char": 27,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 27,
      "end_char": 28
    },
    {
      "id": 8,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Int",
      "head": 9,
      "deprel": "obj",
      "start_char": 29,
      "end_char": 32
    },
    {
      "id": 9,
      "text": "devrions",
      "lemma": "devoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 33,
      "end_char": 41,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": "-nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 41,
      "end_char": 46
    },
    {
      "id": 11,
      "text": "faire",
      "lemma": "faire",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 9,
      "deprel": "xcomp",
      "start_char": 47,
      "end_char": 52
    },
    {
      "id": 12,
      "text": "maintenant",
      "lemma": "maintenant",
      "upos": "ADV",
      "head": 11,
      "deprel": "advmod",
      "start_char": 53,
      "end_char": 63
    },
    {
      "id": 13,
      "text": "?",
      "lemma": "?",
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

## 66. Sentence

Sentence: Quoi qu'il arrive, nous garderons une copie du contrat.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Quoi",
      "lemma": "quoi",
      "upos": "INTJ",
      "head": 7,
      "deprel": "discourse",
      "start_char": 0,
      "end_char": 4
    },
    {
      "id": 2,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 4,
      "deprel": "mark",
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
      "text": "arrive",
      "lemma": "arriver",
      "upos": "VERB",
      "feats": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "advcl",
      "start_char": 11,
      "end_char": 17,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 17,
      "end_char": 18
    },
    {
      "id": 6,
      "text": "nous",
      "lemma": "nous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=1|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 19,
      "end_char": 23
    },
    {
      "id": 7,
      "text": "garderons",
      "lemma": "garder",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 24,
      "end_char": 33
    },
    {
      "id": 8,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 9,
      "deprel": "det",
      "start_char": 34,
      "end_char": 37
    },
    {
      "id": 9,
      "text": "copie",
      "lemma": "copie",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 7,
      "deprel": "obj",
      "start_char": 38,
      "end_char": 43
    },
    {
      "id": [
        10,
        11
      ],
      "text": "du",
      "start_char": 44,
      "end_char": 46
    },
    {
      "id": 10,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 12,
      "deprel": "case"
    },
    {
      "id": 11,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 12,
      "deprel": "det"
    },
    {
      "id": 12,
      "text": "contrat",
      "lemma": "contrat",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "nmod",
      "start_char": 47,
      "end_char": 54,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 54,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 67. Sentence

Sentence: Quoique très critiqué, le projet avance.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Quoique",
      "lemma": "quoique",
      "upos": "SCONJ",
      "head": 3,
      "deprel": "mark",
      "start_char": 0,
      "end_char": 7
    },
    {
      "id": 2,
      "text": "très",
      "lemma": "très",
      "upos": "ADV",
      "head": 3,
      "deprel": "advmod",
      "start_char": 8,
      "end_char": 12
    },
    {
      "id": 3,
      "text": "critiqué",
      "lemma": "critiquer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 7,
      "deprel": "advcl",
      "start_char": 13,
      "end_char": 21,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 21,
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
      "text": "projet",
      "lemma": "projet",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 26,
      "end_char": 32
    },
    {
      "id": 7,
      "text": "avance",
      "lemma": "avancer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 33,
      "end_char": 39,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 39,
      "end_char": 40,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 68. Sentence

Sentence: Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

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
      "text": "agréer",
      "lemma": "agréer",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 1,
      "deprel": "xcomp",
      "start_char": 9,
      "end_char": 15,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 15,
      "end_char": 16
    },
    {
      "id": 4,
      "text": "Madame",
      "lemma": "monsieur",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "vocative",
      "start_char": 17,
      "end_char": 23,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 23,
      "end_char": 24
    },
    {
      "id": 6,
      "text": "Monsieur",
      "lemma": "monsieur",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "conj",
      "start_char": 25,
      "end_char": 33,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 33,
      "end_char": 34
    },
    {
      "id": 8,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 9,
      "deprel": "det",
      "start_char": 35,
      "end_char": 37,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": "expression",
      "lemma": "expression",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 2,
      "deprel": "obj",
      "start_char": 37,
      "end_char": 47
    },
    {
      "id": 10,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 12,
      "deprel": "case",
      "start_char": 48,
      "end_char": 50
    },
    {
      "id": 11,
      "text": "mes",
      "lemma": "son",
      "upos": "DET",
      "feats": "Number=Plur|Number[psor]=Sing|Person[psor]=1|Poss=Yes|PronType=Prs",
      "head": 12,
      "deprel": "det",
      "start_char": 51,
      "end_char": 54
    },
    {
      "id": 12,
      "text": "salutations",
      "lemma": "salutation",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 9,
      "deprel": "nmod",
      "start_char": 55,
      "end_char": 66
    },
    {
      "id": 13,
      "text": "distinguées",
      "lemma": "distinguer",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 12,
      "deprel": "acl",
      "start_char": 67,
      "end_char": 78,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 78,
      "end_char": 79,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 69. Sentence

Sentence: Nous vous saurions gré de bien vouloir confirmer la réception de ce courrier.

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
      "text": "vous",
      "lemma": "vous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=2|PronType=Prs",
      "head": 3,
      "deprel": "iobj",
      "start_char": 5,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "saurions",
      "lemma": "savoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 10,
      "end_char": 18
    },
    {
      "id": 4,
      "text": "gré",
      "lemma": "gré",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "obj:lvc",
      "start_char": 19,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 7,
      "deprel": "mark",
      "start_char": 23,
      "end_char": 25
    },
    {
      "id": 6,
      "text": "bien",
      "lemma": "bien",
      "upos": "ADV",
      "head": 7,
      "deprel": "advmod",
      "start_char": 26,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "vouloir",
      "lemma": "vouloir",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 3,
      "deprel": "xcomp",
      "start_char": 31,
      "end_char": 38
    },
    {
      "id": 8,
      "text": "confirmer",
      "lemma": "confirmer",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 7,
      "deprel": "xcomp",
      "start_char": 39,
      "end_char": 48
    },
    {
      "id": 9,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 10,
      "deprel": "det",
      "start_char": 49,
      "end_char": 51
    },
    {
      "id": 10,
      "text": "réception",
      "lemma": "réception",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "obj",
      "start_char": 52,
      "end_char": 61
    },
    {
      "id": 11,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 13,
      "deprel": "case",
      "start_char": 62,
      "end_char": 64
    },
    {
      "id": 12,
      "text": "ce",
      "lemma": "ce",
      "upos": "DET",
      "feats": "Gender=Masc|Number=Sing|PronType=Dem",
      "head": 13,
      "deprel": "det",
      "start_char": 65,
      "end_char": 67
    },
    {
      "id": 13,
      "text": "courrier",
      "lemma": "courrier",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 10,
      "deprel": "nmod",
      "start_char": 68,
      "end_char": 76,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 76,
      "end_char": 77,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 70. Sentence

Sentence: Le tribunal administratif a rejeté la requête au motif qu'elle était tardive.

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
      "text": "tribunal",
      "lemma": "tribunal",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "administratif",
      "lemma": "administratif",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 2,
      "deprel": "amod",
      "start_char": 12,
      "end_char": 25
    },
    {
      "id": 4,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 26,
      "end_char": 27
    },
    {
      "id": 5,
      "text": "rejeté",
      "lemma": "rejeter",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 28,
      "end_char": 34
    },
    {
      "id": 6,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 35,
      "end_char": 37
    },
    {
      "id": 7,
      "text": "requête",
      "lemma": "requête",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "obj",
      "start_char": 38,
      "end_char": 45
    },
    {
      "id": [
        8,
        9
      ],
      "text": "au",
      "start_char": 46,
      "end_char": 48
    },
    {
      "id": 8,
      "text": "à",
      "lemma": "à",
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
      "text": "motif",
      "lemma": "motif",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "obl:mod",
      "start_char": 49,
      "end_char": 54
    },
    {
      "id": 11,
      "text": "qu'",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 14,
      "deprel": "mark",
      "start_char": 55,
      "end_char": 58,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 14,
      "deprel": "nsubj",
      "start_char": 58,
      "end_char": 62
    },
    {
      "id": 13,
      "text": "était",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 14,
      "deprel": "cop",
      "start_char": 63,
      "end_char": 68
    },
    {
      "id": 14,
      "text": "tardive",
      "lemma": "tardif",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Sing",
      "head": 10,
      "deprel": "acl",
      "start_char": 69,
      "end_char": 76,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 76,
      "end_char": 77,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 71. Sentence

Sentence: La clause n'est applicable que si les deux parties y consentent expressément.

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
      "text": "clause",
      "lemma": "clause",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "n'",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 5,
      "deprel": "advmod",
      "start_char": 10,
      "end_char": 12,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "cop",
      "start_char": 12,
      "end_char": 15
    },
    {
      "id": 5,
      "text": "applicable",
      "lemma": "applicable",
      "upos": "ADJ",
      "feats": "Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 16,
      "end_char": 26
    },
    {
      "id": 6,
      "text": "que",
      "lemma": "que",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 12,
      "deprel": "advmod",
      "start_char": 27,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "si",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 12,
      "deprel": "mark",
      "start_char": 31,
      "end_char": 33
    },
    {
      "id": 8,
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
      "id": 9,
      "text": "deux",
      "lemma": "deux",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 10,
      "deprel": "nummod",
      "start_char": 38,
      "end_char": 42
    },
    {
      "id": 10,
      "text": "parties",
      "lemma": "partie",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 12,
      "deprel": "nsubj",
      "start_char": 43,
      "end_char": 50
    },
    {
      "id": 11,
      "text": "y",
      "lemma": "y",
      "upos": "PRON",
      "feats": "Emph=No|Person=3|PronType=Prs",
      "head": 12,
      "deprel": "iobj",
      "start_char": 51,
      "end_char": 52
    },
    {
      "id": 12,
      "text": "consentent",
      "lemma": "consentir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 5,
      "deprel": "advcl",
      "start_char": 53,
      "end_char": 63
    },
    {
      "id": 13,
      "text": "expressément",
      "lemma": "expressément",
      "upos": "ADV",
      "head": 12,
      "deprel": "advmod",
      "start_char": 64,
      "end_char": 76,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 76,
      "end_char": 77,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 72. Sentence

Sentence: Le rapport souligne, en termes prudents, que plusieurs hypothèses restent ouvertes.

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
      "head": 3,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "souligne",
      "lemma": "souligner",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 11,
      "end_char": 19,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 19,
      "end_char": 20
    },
    {
      "id": 5,
      "text": "en",
      "lemma": "en",
      "upos": "ADP",
      "head": 6,
      "deprel": "case",
      "start_char": 21,
      "end_char": 23
    },
    {
      "id": 6,
      "text": "termes",
      "lemma": "terme",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 3,
      "deprel": "obl:mod",
      "start_char": 24,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "prudents",
      "lemma": "prudent",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Plur",
      "head": 6,
      "deprel": "amod",
      "start_char": 31,
      "end_char": 39,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 12,
      "deprel": "punct",
      "start_char": 39,
      "end_char": 40
    },
    {
      "id": 9,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 12,
      "deprel": "mark",
      "start_char": 41,
      "end_char": 44
    },
    {
      "id": 10,
      "text": "plusieurs",
      "lemma": "plusieurs",
      "upos": "DET",
      "feats": "Number=Plur|PronType=Ind",
      "head": 11,
      "deprel": "det",
      "start_char": 45,
      "end_char": 54
    },
    {
      "id": 11,
      "text": "hypothèses",
      "lemma": "hypothèse",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 12,
      "deprel": "nsubj",
      "start_char": 55,
      "end_char": 65
    },
    {
      "id": 12,
      "text": "restent",
      "lemma": "rester",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 3,
      "deprel": "ccomp",
      "start_char": 66,
      "end_char": 73
    },
    {
      "id": 13,
      "text": "ouvertes",
      "lemma": "ouvrir",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 12,
      "deprel": "xcomp",
      "start_char": 74,
      "end_char": 82,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 82,
      "end_char": 83,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 73. Sentence

Sentence: Pourriez-vous, s'il vous plaît, joindre les pièces justificatives manquantes ?

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Pourriez",
      "lemma": "pouvoir",
      "upos": "VERB",
      "feats": "Mood=Imp|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 0,
      "end_char": 8,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "-vous",
      "lemma": "vous",
      "upos": "PRON",
      "feats": "Number=Plur|Person=2|PronType=Prs",
      "head": 1,
      "deprel": "nsubj",
      "start_char": 8,
      "end_char": 13,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 13,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "s'",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 7,
      "deprel": "mark",
      "start_char": 15,
      "end_char": 17,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": "il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "expl:subj",
      "start_char": 17,
      "end_char": 19
    },
    {
      "id": 6,
      "text": "vous",
      "lemma": "vous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=2|PronType=Prs",
      "head": 7,
      "deprel": "iobj",
      "start_char": 20,
      "end_char": 24
    },
    {
      "id": 7,
      "text": "plaît",
      "lemma": "plaire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 1,
      "deprel": "advcl",
      "start_char": 25,
      "end_char": 30,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 30,
      "end_char": 31
    },
    {
      "id": 9,
      "text": "joindre",
      "lemma": "joindre",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 1,
      "deprel": "xcomp",
      "start_char": 32,
      "end_char": 39
    },
    {
      "id": 10,
      "text": "les",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Plur|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 40,
      "end_char": 43
    },
    {
      "id": 11,
      "text": "pièces",
      "lemma": "pièce",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 9,
      "deprel": "obj",
      "start_char": 44,
      "end_char": 50
    },
    {
      "id": 12,
      "text": "justificatives",
      "lemma": "justificatif",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Plur",
      "head": 11,
      "deprel": "amod",
      "start_char": 51,
      "end_char": 65
    },
    {
      "id": 13,
      "text": "manquantes",
      "lemma": "manquant",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Plur",
      "head": 11,
      "deprel": "amod",
      "start_char": 66,
      "end_char": 76
    },
    {
      "id": 14,
      "text": "?",
      "lemma": "?",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 77,
      "end_char": 78,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 74. Sentence

Sentence: N'eût été la vigilance d'une riveraine, l'incendie se serait propagé plus vite.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "N'",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 5,
      "deprel": "advmod",
      "start_char": 0,
      "end_char": 2,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "eût",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 5,
      "deprel": "aux:tense",
      "start_char": 2,
      "end_char": 5
    },
    {
      "id": 3,
      "text": "été",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 5,
      "deprel": "cop",
      "start_char": 6,
      "end_char": 9
    },
    {
      "id": 4,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 10,
      "end_char": 12
    },
    {
      "id": 5,
      "text": "vigilance",
      "lemma": "vigilance",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 13,
      "end_char": 22
    },
    {
      "id": 6,
      "text": "d'",
      "lemma": "de",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 23,
      "end_char": 25,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 25,
      "end_char": 28
    },
    {
      "id": 8,
      "text": "riveraine",
      "lemma": "riverain",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 5,
      "deprel": "nmod",
      "start_char": 29,
      "end_char": 38,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 14,
      "deprel": "punct",
      "start_char": 38,
      "end_char": 39
    },
    {
      "id": 10,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 11,
      "deprel": "det",
      "start_char": 40,
      "end_char": 42,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": "incendie",
      "lemma": "incendie",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 14,
      "deprel": "nsubj",
      "start_char": 42,
      "end_char": 50
    },
    {
      "id": 12,
      "text": "se",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 14,
      "deprel": "expl:pv",
      "start_char": 51,
      "end_char": 53
    },
    {
      "id": 13,
      "text": "serait",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 14,
      "deprel": "aux:tense",
      "start_char": 54,
      "end_char": 60
    },
    {
      "id": 14,
      "text": "propagé",
      "lemma": "propager",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 5,
      "deprel": "conj",
      "start_char": 61,
      "end_char": 68
    },
    {
      "id": 15,
      "text": "plus",
      "lemma": "plus",
      "upos": "ADV",
      "head": 16,
      "deprel": "advmod",
      "start_char": 69,
      "end_char": 73
    },
    {
      "id": 16,
      "text": "vite",
      "lemma": "vite",
      "upos": "ADV",
      "head": 14,
      "deprel": "advmod",
      "start_char": 74,
      "end_char": 78,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 17,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 78,
      "end_char": 79,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 75. Sentence

Sentence: Encore eût-il fallu que les responsables acceptassent de répondre.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Encore",
      "lemma": "encore",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 0,
      "end_char": 6
    },
    {
      "id": 2,
      "text": "eût",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 7,
      "end_char": 10,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "-il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 4,
      "deprel": "expl:subj",
      "start_char": 10,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "fallu",
      "lemma": "falloir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
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
      "text": "responsables",
      "lemma": "responsable",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 28,
      "end_char": 40
    },
    {
      "id": 8,
      "text": "acceptassent",
      "lemma": "acceptasser",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "ccomp",
      "start_char": 41,
      "end_char": 53
    },
    {
      "id": 9,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 10,
      "deprel": "mark",
      "start_char": 54,
      "end_char": 56
    },
    {
      "id": 10,
      "text": "répondre",
      "lemma": "répondre",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 8,
      "deprel": "xcomp",
      "start_char": 57,
      "end_char": 65,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 65,
      "end_char": 66,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 76. Sentence

Sentence: Fût-il premier ministre, il ne pourrait pas tout décider seul.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Fût",
      "lemma": "faire",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "cop",
      "start_char": 0,
      "end_char": 3,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "-il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 6
    },
    {
      "id": 3,
      "text": "premier",
      "lemma": "premier",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "amod",
      "start_char": 7,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "ministre",
      "lemma": "ministre",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 8,
      "deprel": "advcl",
      "start_char": 15,
      "end_char": 23,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 23,
      "end_char": 24
    },
    {
      "id": 6,
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
      "id": 7,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 8,
      "deprel": "advmod",
      "start_char": 28,
      "end_char": 30
    },
    {
      "id": 8,
      "text": "pourrait",
      "lemma": "pouvoir",
      "upos": "VERB",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 31,
      "end_char": 39
    },
    {
      "id": 9,
      "text": "pas",
      "lemma": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 8,
      "deprel": "advmod",
      "start_char": 40,
      "end_char": 43
    },
    {
      "id": 10,
      "text": "tout",
      "lemma": "tout",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Ind",
      "head": 11,
      "deprel": "obj",
      "start_char": 44,
      "end_char": 48
    },
    {
      "id": 11,
      "text": "décider",
      "lemma": "décider",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 8,
      "deprel": "xcomp",
      "start_char": 49,
      "end_char": 56
    },
    {
      "id": 12,
      "text": "seul",
      "lemma": "seul",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 11,
      "deprel": "xcomp",
      "start_char": 57,
      "end_char": 61,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 13,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 61,
      "end_char": 62,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 77. Sentence

Sentence: Va-t'en !

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Va",
      "lemma": "aller",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 0,
      "end_char": 2,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "-t'en",
      "lemma": "tonen",
      "upos": "ADV",
      "head": 1,
      "deprel": "advmod",
      "start_char": 2,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "!",
      "lemma": "!",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 8,
      "end_char": 9,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 78. Sentence

Sentence: Ne t'en fais pas.

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
      "head": 4,
      "deprel": "advmod",
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
      "text": "en",
      "lemma": "en",
      "upos": "PRON",
      "feats": "Emph=No|Person=3|PronType=Prs",
      "head": 4,
      "deprel": "expl:comp",
      "start_char": 5,
      "end_char": 7
    },
    {
      "id": 4,
      "text": "fais",
      "lemma": "faire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 8,
      "end_char": 12
    },
    {
      "id": 5,
      "text": "pas",
      "lemma": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 4,
      "deprel": "advmod",
      "start_char": 13,
      "end_char": 16,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 16,
      "end_char": 17,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 79. Sentence

Sentence: Il y a eu un avant et un après-Covid dans l'organisation du travail.

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
      "head": 4,
      "deprel": "expl:comp",
      "start_char": 3,
      "end_char": 4
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
      "text": "eu",
      "lemma": "avoir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 7,
      "end_char": 9
    },
    {
      "id": 5,
      "text": "un",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Masc|Number=Sing|PronType=Art",
      "head": 6,
      "deprel": "det",
      "start_char": 10,
      "end_char": 12
    },
    {
      "id": 6,
      "text": "avant",
      "lemma": "avant",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obj",
      "start_char": 13,
      "end_char": 18
    },
    {
      "id": 7,
      "text": "et",
      "lemma": "et",
      "upos": "CCONJ",
      "head": 9,
      "deprel": "cc",
      "start_char": 19,
      "end_char": 21
    },
    {
      "id": 8,
      "text": "un",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Masc|Number=Sing|PronType=Art",
      "head": 9,
      "deprel": "det",
      "start_char": 22,
      "end_char": 24
    },
    {
      "id": 9,
      "text": "après-Covid",
      "lemma": "après-Covid",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 6,
      "deprel": "conj",
      "start_char": 25,
      "end_char": 36
    },
    {
      "id": 10,
      "text": "dans",
      "lemma": "dans",
      "upos": "ADP",
      "head": 12,
      "deprel": "case",
      "start_char": 37,
      "end_char": 41
    },
    {
      "id": 11,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 12,
      "deprel": "det",
      "start_char": 42,
      "end_char": 44,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": "organisation",
      "lemma": "organisation",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 4,
      "deprel": "obl:mod",
      "start_char": 44,
      "end_char": 56
    },
    {
      "id": [
        13,
        14
      ],
      "text": "du",
      "start_char": 57,
      "end_char": 59
    },
    {
      "id": 13,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 15,
      "deprel": "case"
    },
    {
      "id": 14,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 15,
      "deprel": "det"
    },
    {
      "id": 15,
      "text": "travail",
      "lemma": "travail",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 12,
      "deprel": "nmod",
      "start_char": 60,
      "end_char": 67,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 16,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 67,
      "end_char": 68,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 80. Sentence

Sentence: La prof a dit : "Ouvrez vos cahiers", puis elle a effacé le tableau.

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
      "text": "prof",
      "lemma": "prof",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 8,
      "end_char": 9
    },
    {
      "id": 4,
      "text": "dit",
      "lemma": "dire",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 10,
      "end_char": 13
    },
    {
      "id": 5,
      "text": ":",
      "lemma": ":",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 14,
      "end_char": 15
    },
    {
      "id": 6,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 16,
      "end_char": 17,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": "Ouvrez",
      "lemma": "ouvrir",
      "upos": "VERB",
      "feats": "Mood=Imp|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "ccomp",
      "start_char": 17,
      "end_char": 23
    },
    {
      "id": 8,
      "text": "vos",
      "lemma": "son",
      "upos": "DET",
      "feats": "Number=Plur|Number[psor]=Plur|Person[psor]=2|Poss=Yes|PronType=Prs",
      "head": 9,
      "deprel": "det",
      "start_char": 24,
      "end_char": 27
    },
    {
      "id": 9,
      "text": "cahiers",
      "lemma": "cahier",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 7,
      "deprel": "obj",
      "start_char": 28,
      "end_char": 35,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 35,
      "end_char": 36,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 15,
      "deprel": "punct",
      "start_char": 36,
      "end_char": 37
    },
    {
      "id": 12,
      "text": "puis",
      "lemma": "puis",
      "upos": "CCONJ",
      "head": 15,
      "deprel": "cc",
      "start_char": 38,
      "end_char": 42
    },
    {
      "id": 13,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 15,
      "deprel": "nsubj",
      "start_char": 43,
      "end_char": 47
    },
    {
      "id": 14,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 15,
      "deprel": "aux:tense",
      "start_char": 48,
      "end_char": 49
    },
    {
      "id": 15,
      "text": "effacé",
      "lemma": "effacer",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 4,
      "deprel": "conj",
      "start_char": 50,
      "end_char": 56
    },
    {
      "id": 16,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 17,
      "deprel": "det",
      "start_char": 57,
      "end_char": 59
    },
    {
      "id": 17,
      "text": "tableau",
      "lemma": "tableau",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 15,
      "deprel": "obj",
      "start_char": 60,
      "end_char": 67,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 18,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 67,
      "end_char": 68,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 81. Sentence

Sentence: Pourquoi Jean-Michel n'a-t-il pas répondu à l'e-mail de sa collègue ?

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Pourquoi",
      "lemma": "pourquoi",
      "upos": "ADV",
      "feats": "PronType=Int",
      "head": 7,
      "deprel": "advmod",
      "start_char": 0,
      "end_char": 8
    },
    {
      "id": 2,
      "text": "Jean-Michel",
      "lemma": "Jean-Michel",
      "upos": "PROPN",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 9,
      "end_char": 20
    },
    {
      "id": 3,
      "text": "n'",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 7,
      "deprel": "advmod",
      "start_char": 21,
      "end_char": 23,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 23,
      "end_char": 24,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": "-t-il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "expl:subj",
      "start_char": 24,
      "end_char": 29
    },
    {
      "id": 6,
      "text": "pas",
      "lemma": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 7,
      "deprel": "advmod",
      "start_char": 30,
      "end_char": 33
    },
    {
      "id": 7,
      "text": "répondu",
      "lemma": "répondre",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 34,
      "end_char": 41
    },
    {
      "id": 8,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 10,
      "deprel": "case",
      "start_char": 42,
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
      "text": "e-mail",
      "lemma": "e-mail",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "obl:arg",
      "start_char": 46,
      "end_char": 52
    },
    {
      "id": 11,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 13,
      "deprel": "case",
      "start_char": 53,
      "end_char": 55
    },
    {
      "id": 12,
      "text": "sa",
      "lemma": "son",
      "upos": "DET",
      "feats": "Gender=Fem|Number=Sing|Number[psor]=Sing|Person[psor]=3|Poss=Yes|PronType=Prs",
      "head": 13,
      "deprel": "det",
      "start_char": 56,
      "end_char": 58
    },
    {
      "id": 13,
      "text": "collègue",
      "lemma": "collègue",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 10,
      "deprel": "nmod",
      "start_char": 59,
      "end_char": 67
    },
    {
      "id": 14,
      "text": "?",
      "lemma": "?",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 68,
      "end_char": 69,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 82. Sentence

Sentence: J'irai à Québec, à Montréal ou peut-être à Trois-Rivières.

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
      "head": 2,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 2,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": "irai",
      "lemma": "iraindre",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 2,
      "end_char": 6
    },
    {
      "id": 3,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 4,
      "deprel": "case",
      "start_char": 7,
      "end_char": 8
    },
    {
      "id": 4,
      "text": "Québec",
      "lemma": "Québec",
      "upos": "PROPN",
      "head": 2,
      "deprel": "obl:arg",
      "start_char": 9,
      "end_char": 15,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 15,
      "end_char": 16
    },
    {
      "id": 6,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 7,
      "deprel": "case",
      "start_char": 17,
      "end_char": 18
    },
    {
      "id": 7,
      "text": "Montréal",
      "lemma": "Montréal",
      "upos": "PROPN",
      "head": 2,
      "deprel": "obl:mod",
      "start_char": 19,
      "end_char": 27
    },
    {
      "id": 8,
      "text": "ou",
      "lemma": "ou",
      "upos": "CCONJ",
      "head": 11,
      "deprel": "cc",
      "start_char": 28,
      "end_char": 30
    },
    {
      "id": 9,
      "text": "peut-être",
      "lemma": "peut-être",
      "upos": "ADV",
      "head": 11,
      "deprel": "advmod",
      "start_char": 31,
      "end_char": 40
    },
    {
      "id": 10,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 11,
      "deprel": "case",
      "start_char": 41,
      "end_char": 42
    },
    {
      "id": 11,
      "text": "Trois-Rivières",
      "lemma": "Trois-Rivières",
      "upos": "PROPN",
      "head": 4,
      "deprel": "conj",
      "start_char": 43,
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

## 83. Sentence

Sentence: Là-bas, on dit souvent "char" pour parler d'une voiture.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Là-bas",
      "lemma": "là-bas",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 0,
      "end_char": 6,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 6,
      "end_char": 7
    },
    {
      "id": 3,
      "text": "on",
      "lemma": "on",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Ind",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 8,
      "end_char": 10
    },
    {
      "id": 4,
      "text": "dit",
      "lemma": "dire",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 11,
      "end_char": 14
    },
    {
      "id": 5,
      "text": "souvent",
      "lemma": "souvent",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 15,
      "end_char": 22
    },
    {
      "id": 6,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 23,
      "end_char": 24,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": "char",
      "lemma": "char",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 4,
      "deprel": "obj",
      "start_char": 24,
      "end_char": 28,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 28,
      "end_char": 29
    },
    {
      "id": 9,
      "text": "pour",
      "lemma": "pour",
      "upos": "ADP",
      "head": 10,
      "deprel": "mark",
      "start_char": 30,
      "end_char": 34
    },
    {
      "id": 10,
      "text": "parler",
      "lemma": "parler",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 4,
      "deprel": "advcl",
      "start_char": 35,
      "end_char": 41
    },
    {
      "id": 11,
      "text": "d'",
      "lemma": "de",
      "upos": "ADP",
      "head": 13,
      "deprel": "case",
      "start_char": 42,
      "end_char": 44,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": "une",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
      "head": 13,
      "deprel": "det",
      "start_char": 44,
      "end_char": 47
    },
    {
      "id": 13,
      "text": "voiture",
      "lemma": "voiture",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 10,
      "deprel": "obl:arg",
      "start_char": 48,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 55,
      "end_char": 56,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 84. Sentence

Sentence: Les pommes que j'ai fait cuire sont restées trop fermes.

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
      "text": "pommes",
      "lemma": "pomme",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 4,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 7,
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
      "head": 7,
      "deprel": "nsubj:caus",
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
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 17,
      "end_char": 19
    },
    {
      "id": 6,
      "text": "fait",
      "lemma": "faire",
      "upos": "AUX",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 7,
      "deprel": "aux:caus",
      "start_char": 20,
      "end_char": 24
    },
    {
      "id": 7,
      "text": "cuire",
      "lemma": "cuire",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 2,
      "deprel": "acl:relcl",
      "start_char": 25,
      "end_char": 30
    },
    {
      "id": 8,
      "text": "sont",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "aux:tense",
      "start_char": 31,
      "end_char": 35
    },
    {
      "id": 9,
      "text": "restées",
      "lemma": "rester",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 36,
      "end_char": 43
    },
    {
      "id": 10,
      "text": "trop",
      "lemma": "trop",
      "upos": "ADV",
      "head": 11,
      "deprel": "advmod",
      "start_char": 44,
      "end_char": 48
    },
    {
      "id": 11,
      "text": "fermes",
      "lemma": "ferme",
      "upos": "ADJ",
      "feats": "Number=Plur",
      "head": 9,
      "deprel": "xcomp",
      "start_char": 49,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 55,
      "end_char": 56,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 85. Sentence

Sentence: Elle s'est laissé convaincre par des arguments qu'elle jugeait pourtant faibles.

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
      "text": "laissé",
      "lemma": "laisser",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 11,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "convaincre",
      "lemma": "convaincre",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 4,
      "deprel": "xcomp",
      "start_char": 18,
      "end_char": 28
    },
    {
      "id": 6,
      "text": "par",
      "lemma": "par",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 29,
      "end_char": 32
    },
    {
      "id": 7,
      "text": "des",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Number=Plur|PronType=Art",
      "head": 8,
      "deprel": "det",
      "start_char": 33,
      "end_char": 36
    },
    {
      "id": 8,
      "text": "arguments",
      "lemma": "argument",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 5,
      "deprel": "obl:arg",
      "start_char": 37,
      "end_char": 46
    },
    {
      "id": 9,
      "text": "qu'",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 11,
      "deprel": "obj",
      "start_char": 47,
      "end_char": 50,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 11,
      "deprel": "nsubj",
      "start_char": 50,
      "end_char": 54
    },
    {
      "id": 11,
      "text": "jugeait",
      "lemma": "juger",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 8,
      "deprel": "acl:relcl",
      "start_char": 55,
      "end_char": 62
    },
    {
      "id": 12,
      "text": "pourtant",
      "lemma": "pourtant",
      "upos": "ADV",
      "head": 13,
      "deprel": "advmod",
      "start_char": 63,
      "end_char": 71
    },
    {
      "id": 13,
      "text": "faibles",
      "lemma": "faible",
      "upos": "ADJ",
      "feats": "Number=Plur",
      "head": 11,
      "deprel": "xcomp",
      "start_char": 72,
      "end_char": 79,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 79,
      "end_char": 80,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 86. Sentence

Sentence: Ils se sont parlé pendant des heures, mais ils ne se sont rien promis.

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
      "text": "pendant",
      "lemma": "pendant",
      "upos": "ADP",
      "head": 7,
      "deprel": "case",
      "start_char": 18,
      "end_char": 25
    },
    {
      "id": 6,
      "text": "des",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Number=Plur|PronType=Art",
      "head": 7,
      "deprel": "det",
      "start_char": 26,
      "end_char": 29
    },
    {
      "id": 7,
      "text": "heures",
      "lemma": "heure",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 4,
      "deprel": "obl:mod",
      "start_char": 30,
      "end_char": 36,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 8,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 15,
      "deprel": "punct",
      "start_char": 36,
      "end_char": 37
    },
    {
      "id": 9,
      "text": "mais",
      "lemma": "mais",
      "upos": "CCONJ",
      "head": 15,
      "deprel": "cc",
      "start_char": 38,
      "end_char": 42
    },
    {
      "id": 10,
      "text": "ils",
      "lemma": "eux",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs",
      "head": 15,
      "deprel": "nsubj",
      "start_char": 43,
      "end_char": 46
    },
    {
      "id": 11,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 15,
      "deprel": "advmod",
      "start_char": 47,
      "end_char": 49
    },
    {
      "id": 12,
      "text": "se",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 15,
      "deprel": "expl:pv",
      "start_char": 50,
      "end_char": 52
    },
    {
      "id": 13,
      "text": "sont",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 15,
      "deprel": "aux:tense",
      "start_char": 53,
      "end_char": 57
    },
    {
      "id": 14,
      "text": "rien",
      "lemma": "rien",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|PronType=Neg",
      "head": 15,
      "deprel": "obj",
      "start_char": 58,
      "end_char": 62
    },
    {
      "id": 15,
      "text": "promis",
      "lemma": "promettre",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 4,
      "deprel": "conj",
      "start_char": 63,
      "end_char": 69,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 16,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 69,
      "end_char": 70,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 87. Sentence

Sentence: Les maisons qu'ils se sont construites dominent la vallée.

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
      "text": "maisons",
      "lemma": "maison",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 4,
      "end_char": 11
    },
    {
      "id": 3,
      "text": "qu'",
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
      "text": "ils",
      "lemma": "eux",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 15,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "se",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 7,
      "deprel": "expl:pv",
      "start_char": 19,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "sont",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "aux:tense",
      "start_char": 22,
      "end_char": 26
    },
    {
      "id": 7,
      "text": "construites",
      "lemma": "construire",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 2,
      "deprel": "acl:relcl",
      "start_char": 27,
      "end_char": 38
    },
    {
      "id": 8,
      "text": "dominent",
      "lemma": "dominer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 39,
      "end_char": 47
    },
    {
      "id": 9,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 10,
      "deprel": "det",
      "start_char": 48,
      "end_char": 50
    },
    {
      "id": 10,
      "text": "vallée",
      "lemma": "vallée",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 8,
      "deprel": "obj",
      "start_char": 51,
      "end_char": 57,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 57,
      "end_char": 58,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 88. Sentence

Sentence: Combien de personnes avez-vous invitées exactement ?

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Combien",
      "lemma": "combien",
      "upos": "ADV",
      "feats": "ExtPos=PRON|PronType=Int",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 7
    },
    {
      "id": 2,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 3,
      "deprel": "case",
      "start_char": 8,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "personnes",
      "lemma": "personne",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 1,
      "deprel": "obl:arg",
      "start_char": 11,
      "end_char": 20
    },
    {
      "id": 4,
      "text": "avez",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 6,
      "deprel": "aux:tense",
      "start_char": 21,
      "end_char": 25,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": "-vous",
      "lemma": "vous",
      "upos": "PRON",
      "feats": "Emph=No|Number=Plur|Person=2|PronType=Prs",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 25,
      "end_char": 30
    },
    {
      "id": 6,
      "text": "invitées",
      "lemma": "inviter",
      "upos": "VERB",
      "feats": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass",
      "head": 0,
      "deprel": "root",
      "start_char": 31,
      "end_char": 39
    },
    {
      "id": 7,
      "text": "exactement",
      "lemma": "exactement",
      "upos": "ADV",
      "head": 6,
      "deprel": "advmod",
      "start_char": 40,
      "end_char": 50
    },
    {
      "id": 8,
      "text": "?",
      "lemma": "?",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 51,
      "end_char": 52,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 89. Sentence

Sentence: Quelqu'un aurait-il vu mes lunettes noires ?

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Quelqu'un",
      "lemma": "quelqu'un",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Ind",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 0,
      "end_char": 9
    },
    {
      "id": 2,
      "text": "aurait",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 4,
      "deprel": "aux:tense",
      "start_char": 10,
      "end_char": 16,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 3,
      "text": "-il",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
      "head": 4,
      "deprel": "expl:subj",
      "start_char": 16,
      "end_char": 19
    },
    {
      "id": 4,
      "text": "vu",
      "lemma": "voir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 20,
      "end_char": 22
    },
    {
      "id": 5,
      "text": "mes",
      "lemma": "son",
      "upos": "DET",
      "feats": "Number=Plur|Number[psor]=Sing|Person[psor]=1|Poss=Yes|PronType=Prs",
      "head": 6,
      "deprel": "det",
      "start_char": 23,
      "end_char": 26
    },
    {
      "id": 6,
      "text": "lunettes",
      "lemma": "lunette",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 4,
      "deprel": "obj",
      "start_char": 27,
      "end_char": 35
    },
    {
      "id": 7,
      "text": "noires",
      "lemma": "noir",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Plur",
      "head": 6,
      "deprel": "amod",
      "start_char": 36,
      "end_char": 42
    },
    {
      "id": 8,
      "text": "?",
      "lemma": "?",
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

## 90. Sentence

Sentence: Ni Pierre ni Leïla ne souhaitent commenter l'affaire.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Ni",
      "lemma": "ni",
      "upos": "CCONJ",
      "head": 6,
      "deprel": "cc",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "Pierre",
      "lemma": "Pierre",
      "upos": "PROPN",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "ni",
      "lemma": "ni",
      "upos": "CCONJ",
      "head": 4,
      "deprel": "cc",
      "start_char": 10,
      "end_char": 12
    },
    {
      "id": 4,
      "text": "Leïla",
      "lemma": "Leïla",
      "upos": "PROPN",
      "head": 2,
      "deprel": "conj",
      "start_char": 13,
      "end_char": 18
    },
    {
      "id": 5,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 6,
      "deprel": "advmod",
      "start_char": 19,
      "end_char": 21
    },
    {
      "id": 6,
      "text": "souhaitent",
      "lemma": "souhaiter",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 22,
      "end_char": 32
    },
    {
      "id": 7,
      "text": "commenter",
      "lemma": "commenter",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 6,
      "deprel": "xcomp",
      "start_char": 33,
      "end_char": 42
    },
    {
      "id": 8,
      "text": "l'",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Number=Sing|PronType=Art",
      "head": 9,
      "deprel": "det",
      "start_char": 43,
      "end_char": 45,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": "affaire",
      "lemma": "affaire",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 7,
      "deprel": "obj",
      "start_char": 45,
      "end_char": 52,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 52,
      "end_char": 53,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 91. Sentence

Sentence: Il arrive que des phrases sans verbe posent problème.

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
      "text": "arrive",
      "lemma": "arriver",
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
      "head": 8,
      "deprel": "mark",
      "start_char": 10,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "des",
      "lemma": "un",
      "upos": "DET",
      "feats": "Definite=Ind|Number=Plur|PronType=Art",
      "head": 5,
      "deprel": "det",
      "start_char": 14,
      "end_char": 17
    },
    {
      "id": 5,
      "text": "phrases",
      "lemma": "phrase",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Plur",
      "head": 8,
      "deprel": "nsubj",
      "start_char": 18,
      "end_char": 25
    },
    {
      "id": 6,
      "text": "sans",
      "lemma": "sans",
      "upos": "ADP",
      "head": 7,
      "deprel": "case",
      "start_char": 26,
      "end_char": 30
    },
    {
      "id": 7,
      "text": "verbe",
      "lemma": "verbe",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "nmod",
      "start_char": 31,
      "end_char": 36
    },
    {
      "id": 8,
      "text": "posent",
      "lemma": "poser",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 2,
      "deprel": "csubj",
      "start_char": 37,
      "end_char": 43
    },
    {
      "id": 9,
      "text": "problème",
      "lemma": "problème",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 8,
      "deprel": "obj:lvc",
      "start_char": 44,
      "end_char": 52,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 10,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 52,
      "end_char": 53,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 92. Sentence

Sentence: Silence dans la salle.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Silence",
      "lemma": "silence",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 0,
      "end_char": 7
    },
    {
      "id": 2,
      "text": "dans",
      "lemma": "dans",
      "upos": "ADP",
      "head": 4,
      "deprel": "case",
      "start_char": 8,
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
      "text": "salle",
      "lemma": "salle",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 1,
      "deprel": "nmod",
      "start_char": 16,
      "end_char": 21,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 21,
      "end_char": 22,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 93. Sentence

Sentence: Trois ans plus tard, retour à la case départ.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Trois",
      "lemma": "trois",
      "upos": "NUM",
      "feats": "Number=Plur",
      "head": 2,
      "deprel": "nummod",
      "start_char": 0,
      "end_char": 5
    },
    {
      "id": 2,
      "text": "ans",
      "lemma": "an",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 6,
      "deprel": "nmod",
      "start_char": 6,
      "end_char": 9
    },
    {
      "id": 3,
      "text": "plus",
      "lemma": "plus",
      "upos": "ADV",
      "head": 4,
      "deprel": "advmod",
      "start_char": 10,
      "end_char": 14
    },
    {
      "id": 4,
      "text": "tard",
      "lemma": "tard",
      "upos": "ADV",
      "head": 2,
      "deprel": "advmod",
      "start_char": 15,
      "end_char": 19,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 19,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "retour",
      "lemma": "retour",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 21,
      "end_char": 27
    },
    {
      "id": 7,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 9,
      "deprel": "case",
      "start_char": 28,
      "end_char": 29
    },
    {
      "id": 8,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 9,
      "deprel": "det",
      "start_char": 30,
      "end_char": 32
    },
    {
      "id": 9,
      "text": "case",
      "lemma": "case",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 6,
      "deprel": "nmod",
      "start_char": 33,
      "end_char": 37
    },
    {
      "id": 10,
      "text": "départ",
      "lemma": "départ",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "nmod",
      "start_char": 38,
      "end_char": 44,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 44,
      "end_char": 45,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 94. Sentence

Sentence: Le dossier "budget_final_v3.xlsx" n'était pas le bon.

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
      "head": 10,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 10
    },
    {
      "id": 3,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 11,
      "end_char": 12,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 4,
      "text": "budget_final_v3.xlsx",
      "lemma": "budget_final_v3.xlsx",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 2,
      "deprel": "appos",
      "start_char": 12,
      "end_char": 32,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 4,
      "deprel": "punct",
      "start_char": 32,
      "end_char": 33
    },
    {
      "id": 6,
      "text": "n'",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 10,
      "deprel": "advmod",
      "start_char": 34,
      "end_char": 36,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": "était",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 10,
      "deprel": "cop",
      "start_char": 36,
      "end_char": 41
    },
    {
      "id": 8,
      "text": "pas",
      "lemma": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 10,
      "deprel": "advmod",
      "start_char": 42,
      "end_char": 45
    },
    {
      "id": 9,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 10,
      "deprel": "det",
      "start_char": 46,
      "end_char": 48
    },
    {
      "id": 10,
      "text": "bon",
      "lemma": "bon",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 49,
      "end_char": 52,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 11,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 10,
      "deprel": "punct",
      "start_char": 52,
      "end_char": 53,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 95. Sentence

Sentence: Si le fichier s'appelle test.final.v2.txt, ne supprimez pas la mauvaise extension.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Si",
      "lemma": "si",
      "upos": "SCONJ",
      "head": 5,
      "deprel": "mark",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 3,
      "deprel": "det",
      "start_char": 3,
      "end_char": 5
    },
    {
      "id": 3,
      "text": "fichier",
      "lemma": "fichier",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 5,
      "deprel": "nsubj:pass",
      "start_char": 6,
      "end_char": 13
    },
    {
      "id": 4,
      "text": "s'",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 5,
      "deprel": "expl:pv",
      "start_char": 14,
      "end_char": 16,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": "appelle",
      "lemma": "appeler",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 9,
      "deprel": "advcl",
      "start_char": 16,
      "end_char": 23
    },
    {
      "id": 6,
      "text": "test.final.v2.txt",
      "lemma": "test.final.v2.txt",
      "upos": "X",
      "feats": "ExtPos=PROPN",
      "head": 5,
      "deprel": "xcomp",
      "start_char": 24,
      "end_char": 41,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 41,
      "end_char": 42
    },
    {
      "id": 8,
      "text": "ne",
      "lemma": "ne",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 9,
      "deprel": "advmod",
      "start_char": 43,
      "end_char": 45
    },
    {
      "id": 9,
      "text": "supprimez",
      "lemma": "supprimer",
      "upos": "VERB",
      "feats": "Mood=Imp|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 46,
      "end_char": 55
    },
    {
      "id": 10,
      "text": "pas",
      "lemma": "pas",
      "upos": "ADV",
      "feats": "Polarity=Neg",
      "head": 9,
      "deprel": "advmod",
      "start_char": 56,
      "end_char": 59
    },
    {
      "id": 11,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 13,
      "deprel": "det",
      "start_char": 60,
      "end_char": 62
    },
    {
      "id": 12,
      "text": "mauvaise",
      "lemma": "mauvais",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Sing",
      "head": 13,
      "deprel": "amod",
      "start_char": 63,
      "end_char": 71
    },
    {
      "id": 13,
      "text": "extension",
      "lemma": "extension",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 9,
      "deprel": "obj",
      "start_char": 72,
      "end_char": 81,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 9,
      "deprel": "punct",
      "start_char": 81,
      "end_char": 82,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 96. Sentence

Sentence: Elle a tapé "jtm" au lieu de "je t'aime", puis elle a rougi.

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
      "text": "tapé",
      "lemma": "taper",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act",
      "head": 0,
      "deprel": "root",
      "start_char": 7,
      "end_char": 11
    },
    {
      "id": 4,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 12,
      "end_char": 13,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": "jtm",
      "lemma": "jtm",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 3,
      "deprel": "obj",
      "start_char": 13,
      "end_char": 16,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 5,
      "deprel": "punct",
      "start_char": 16,
      "end_char": 17
    },
    {
      "id": [
        7,
        8
      ],
      "text": "au",
      "start_char": 18,
      "end_char": 20
    },
    {
      "id": 7,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "feats": "ExtPos=ADV",
      "head": 3,
      "deprel": "advmod"
    },
    {
      "id": 8,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 7,
      "deprel": "fixed"
    },
    {
      "id": 9,
      "text": "lieu",
      "lemma": "lieu",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 7,
      "deprel": "fixed",
      "start_char": 21,
      "end_char": 25
    },
    {
      "id": 10,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 14,
      "deprel": "mark",
      "start_char": 26,
      "end_char": 28
    },
    {
      "id": 11,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 14,
      "deprel": "punct",
      "start_char": 29,
      "end_char": 30,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 14,
      "deprel": "nsubj",
      "start_char": 30,
      "end_char": 32
    },
    {
      "id": 13,
      "text": "t'",
      "lemma": "toi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=2|PronType=Prs",
      "head": 14,
      "deprel": "obj",
      "start_char": 33,
      "end_char": 35,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 14,
      "text": "aime",
      "lemma": "aimer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "ccomp",
      "start_char": 35,
      "end_char": 39,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": "\"",
      "lemma": "\"",
      "upos": "PUNCT",
      "head": 14,
      "deprel": "punct",
      "start_char": 39,
      "end_char": 40,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 16,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 20,
      "deprel": "punct",
      "start_char": 40,
      "end_char": 41
    },
    {
      "id": 17,
      "text": "puis",
      "lemma": "puis",
      "upos": "CCONJ",
      "head": 20,
      "deprel": "cc",
      "start_char": 42,
      "end_char": 46
    },
    {
      "id": 18,
      "text": "elle",
      "lemma": "lui",
      "upos": "PRON",
      "feats": "Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
      "head": 20,
      "deprel": "nsubj",
      "start_char": 47,
      "end_char": 51
    },
    {
      "id": 19,
      "text": "a",
      "lemma": "avoir",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 20,
      "deprel": "aux:tense",
      "start_char": 52,
      "end_char": 53
    },
    {
      "id": 20,
      "text": "rougi",
      "lemma": "rougir",
      "upos": "VERB",
      "feats": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part",
      "head": 3,
      "deprel": "conj",
      "start_char": 54,
      "end_char": 59,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 21,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 3,
      "deprel": "punct",
      "start_char": 59,
      "end_char": 60,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 97. Sentence

Sentence: Les étudiants de L2, voire de M1, pourront s'inscrire dès lundi.

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
      "text": "étudiants",
      "lemma": "étudiant",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Plur",
      "head": 10,
      "deprel": "nsubj",
      "start_char": 4,
      "end_char": 13
    },
    {
      "id": 3,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 4,
      "deprel": "case",
      "start_char": 14,
      "end_char": 16
    },
    {
      "id": 4,
      "text": "L2",
      "lemma": "L2",
      "upos": "PROPN",
      "head": 2,
      "deprel": "nmod",
      "start_char": 17,
      "end_char": 19,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 19,
      "end_char": 20
    },
    {
      "id": 6,
      "text": "voire",
      "lemma": "voire",
      "upos": "CCONJ",
      "head": 8,
      "deprel": "cc",
      "start_char": 21,
      "end_char": 26
    },
    {
      "id": 7,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 8,
      "deprel": "case",
      "start_char": 27,
      "end_char": 29
    },
    {
      "id": 8,
      "text": "M1",
      "lemma": "M1",
      "upos": "PROPN",
      "head": 4,
      "deprel": "conj",
      "start_char": 30,
      "end_char": 32,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 9,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 8,
      "deprel": "punct",
      "start_char": 32,
      "end_char": 33
    },
    {
      "id": 10,
      "text": "pourront",
      "lemma": "pouvoir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 34,
      "end_char": 42
    },
    {
      "id": 11,
      "text": "s'",
      "lemma": "soi",
      "upos": "PRON",
      "feats": "Person=3|PronType=Prs|Reflex=Yes",
      "head": 12,
      "deprel": "expl:pv",
      "start_char": 43,
      "end_char": 45,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 12,
      "text": "inscrire",
      "lemma": "inscrire",
      "upos": "VERB",
      "feats": "VerbForm=Inf",
      "head": 10,
      "deprel": "xcomp",
      "start_char": 45,
      "end_char": 53
    },
    {
      "id": 13,
      "text": "dès",
      "lemma": "dès",
      "upos": "ADP",
      "head": 14,
      "deprel": "case",
      "start_char": 54,
      "end_char": 57
    },
    {
      "id": 14,
      "text": "lundi",
      "lemma": "lundi",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 12,
      "deprel": "obl:mod",
      "start_char": 58,
      "end_char": 63,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
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

## 98. Sentence

Sentence: Le voisin du dessus, celui qui joue du piano à minuit, déménage enfin.

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
      "text": "voisin",
      "lemma": "voisin",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 16,
      "deprel": "nsubj",
      "start_char": 3,
      "end_char": 9
    },
    {
      "id": [
        3,
        4
      ],
      "text": "du",
      "start_char": 10,
      "end_char": 12
    },
    {
      "id": 3,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 5,
      "deprel": "case"
    },
    {
      "id": 4,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 5,
      "deprel": "det"
    },
    {
      "id": 5,
      "text": "dessus",
      "lemma": "dessus",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 2,
      "deprel": "nmod",
      "start_char": 13,
      "end_char": 19,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 6,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 19,
      "end_char": 20
    },
    {
      "id": 7,
      "text": "celui",
      "lemma": "celui",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Dem",
      "head": 2,
      "deprel": "appos",
      "start_char": 21,
      "end_char": 26
    },
    {
      "id": 8,
      "text": "qui",
      "lemma": "qui",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 9,
      "deprel": "nsubj",
      "start_char": 27,
      "end_char": 30
    },
    {
      "id": 9,
      "text": "joue",
      "lemma": "jouer",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 7,
      "deprel": "acl:relcl",
      "start_char": 31,
      "end_char": 35
    },
    {
      "id": [
        10,
        11
      ],
      "text": "du",
      "start_char": 36,
      "end_char": 38
    },
    {
      "id": 10,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 12,
      "deprel": "case"
    },
    {
      "id": 11,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 12,
      "deprel": "det"
    },
    {
      "id": 12,
      "text": "piano",
      "lemma": "piano",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "obl:arg",
      "start_char": 39,
      "end_char": 44
    },
    {
      "id": 13,
      "text": "à",
      "lemma": "à",
      "upos": "ADP",
      "head": 14,
      "deprel": "case",
      "start_char": 45,
      "end_char": 46
    },
    {
      "id": 14,
      "text": "minuit",
      "lemma": "minuit",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 9,
      "deprel": "obl:mod",
      "start_char": 47,
      "end_char": 53,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 53,
      "end_char": 54
    },
    {
      "id": 16,
      "text": "déménage",
      "lemma": "déménager",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 55,
      "end_char": 63
    },
    {
      "id": 17,
      "text": "enfin",
      "lemma": "enfin",
      "upos": "ADV",
      "head": 16,
      "deprel": "advmod",
      "start_char": 64,
      "end_char": 69,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 18,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 16,
      "deprel": "punct",
      "start_char": 69,
      "end_char": 70,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 99. Sentence

Sentence: Ce que je veux, c'est que ça fonctionne du premier coup.

Raw Stanza output:

```json
[
  [
    {
      "id": 1,
      "text": "Ce",
      "lemma": "ce",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Dem",
      "head": 7,
      "deprel": "dislocated",
      "start_char": 0,
      "end_char": 2
    },
    {
      "id": 2,
      "text": "que",
      "lemma": "que",
      "upos": "PRON",
      "feats": "PronType=Rel",
      "head": 4,
      "deprel": "obj",
      "start_char": 3,
      "end_char": 6
    },
    {
      "id": 3,
      "text": "je",
      "lemma": "moi",
      "upos": "PRON",
      "feats": "Emph=No|Number=Sing|Person=1|PronType=Prs",
      "head": 4,
      "deprel": "nsubj",
      "start_char": 7,
      "end_char": 9
    },
    {
      "id": 4,
      "text": "veux",
      "lemma": "vouloir",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
      "head": 1,
      "deprel": "acl:relcl",
      "start_char": 10,
      "end_char": 14,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 5,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 14,
      "end_char": 15
    },
    {
      "id": 6,
      "text": "c'",
      "lemma": "ce",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Dem",
      "head": 7,
      "deprel": "nsubj",
      "start_char": 16,
      "end_char": 18,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": "est",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 10,
      "deprel": "cop",
      "start_char": 18,
      "end_char": 21
    },
    {
      "id": 8,
      "text": "que",
      "lemma": "que",
      "upos": "SCONJ",
      "head": 10,
      "deprel": "mark",
      "start_char": 22,
      "end_char": 25
    },
    {
      "id": 9,
      "text": "ça",
      "lemma": "ça",
      "upos": "PRON",
      "feats": "Gender=Masc|Number=Sing|Person=3|PronType=Dem",
      "head": 10,
      "deprel": "nsubj",
      "start_char": 26,
      "end_char": 28
    },
    {
      "id": 10,
      "text": "fonctionne",
      "lemma": "fonctionner",
      "upos": "VERB",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
      "head": 0,
      "deprel": "root",
      "start_char": 29,
      "end_char": 39
    },
    {
      "id": [
        11,
        12
      ],
      "text": "du",
      "start_char": 40,
      "end_char": 42
    },
    {
      "id": 11,
      "text": "de",
      "lemma": "de",
      "upos": "ADP",
      "head": 14,
      "deprel": "case"
    },
    {
      "id": 12,
      "text": "le",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
      "head": 14,
      "deprel": "det"
    },
    {
      "id": 13,
      "text": "premier",
      "lemma": "premier",
      "upos": "ADJ",
      "feats": "Gender=Masc|Number=Sing",
      "head": 14,
      "deprel": "amod",
      "start_char": 43,
      "end_char": 50
    },
    {
      "id": 14,
      "text": "coup",
      "lemma": "coup",
      "upos": "NOUN",
      "feats": "Gender=Masc|Number=Sing",
      "head": 10,
      "deprel": "obl:mod",
      "start_char": 51,
      "end_char": 55,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 15,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 7,
      "deprel": "punct",
      "start_char": 55,
      "end_char": 56,
      "misc": "SpaceAfter=No"
    }
  ]
]
```

## 100. Sentence

Sentence: Il pleuvait ; pourtant, la terrasse était pleine.

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
      "text": ";",
      "lemma": ";",
      "upos": "PUNCT",
      "head": 2,
      "deprel": "punct",
      "start_char": 12,
      "end_char": 13
    }
  ],
  [
    {
      "id": 1,
      "text": "pourtant",
      "lemma": "pourtant",
      "upos": "ADV",
      "head": 6,
      "deprel": "advmod",
      "start_char": 14,
      "end_char": 22,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 2,
      "text": ",",
      "lemma": ",",
      "upos": "PUNCT",
      "head": 1,
      "deprel": "punct",
      "start_char": 22,
      "end_char": 23
    },
    {
      "id": 3,
      "text": "la",
      "lemma": "le",
      "upos": "DET",
      "feats": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
      "head": 4,
      "deprel": "det",
      "start_char": 24,
      "end_char": 26
    },
    {
      "id": 4,
      "text": "terrasse",
      "lemma": "terrasse",
      "upos": "NOUN",
      "feats": "Gender=Fem|Number=Sing",
      "head": 6,
      "deprel": "nsubj",
      "start_char": 27,
      "end_char": 35
    },
    {
      "id": 5,
      "text": "était",
      "lemma": "être",
      "upos": "AUX",
      "feats": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
      "head": 6,
      "deprel": "cop",
      "start_char": 36,
      "end_char": 41
    },
    {
      "id": 6,
      "text": "pleine",
      "lemma": "plein",
      "upos": "ADJ",
      "feats": "Gender=Fem|Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 42,
      "end_char": 48,
      "misc": "SpaceAfter=No"
    },
    {
      "id": 7,
      "text": ".",
      "lemma": ".",
      "upos": "PUNCT",
      "head": 6,
      "deprel": "punct",
      "start_char": 48,
      "end_char": 49,
      "misc": "SpaceAfter=No"
    }
  ]
]
```
