
input: FR sentence,
output: extract phrases used in sentenc. 

example: 

input: J’ai besoin de ton aide à cause de la pluie.

output:
{
  "sentence": "J’ai besoin de ton aide à cause de la pluie.",
  "phrases": [
    {
      "base_form": "avoir besoin de",
      "surface_form": "ai besoin de",
      "type": "verbal_phrase"
    },
    {
      "base_form": "à cause de",
      "surface_form": "à cause de",
      "type": "prepositional_phrase"
    }
  ]
}


Note:
1. candidate types: 
- verbal_phrase
avoir besoin de
avoir peur de
- idiom
pleuvoir des cordes
avoir le coup de foudre
- prepositional_phrase
à cause de
grâce à
- fixed_expression
bien sûr
tout à fait

2. one sentence can contain 0-many phrases. 


Test example: 

Sentences: 
Sentences (1 → 10)
Le chien dort.
Marie mange une pomme.
J’ai besoin d’eau.
Il a peur du noir.
Nous sommes en retard.
Elle part à cause de la pluie.
J’ai besoin de ton aide aujourd’hui.
Il a peur de parler en public.
J’ai besoin de ton aide à cause du problème.
Il a peur de parler en public à cause du stress.

Expected Phrase Extraction Answers
1.
✅ No phrase

2.
✅ No phrase

3.
avoir besoin de (verbal_phrase)


4.
avoir peur de (verbal_phrase)


5.
être en retard (verbal_phrase)


6.
à cause de (prepositional_phrase)


7.
avoir besoin de (verbal_phrase)


8.
avoir peur de (verbal_phrase)
en public (prepositional_phrase)


9.
avoir besoin de (verbal_phrase)
à cause de (prepositional_phrase)


10.
avoir peur de (verbal_phrase)
en public (prepositional_phrase)
à cause de (prepositional_phrase)