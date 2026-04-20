# French Trankit Report for idea.md Sentences

Trankit output was not generated for the current `idea.md` sentences.

## Attempted command

```powershell
$env:PYTHONPATH='src'
python -m grammar_extract.trankit_report --idea idea.md --output reports/idea_md_trankit_new_sentences_report.md
```

## Result

The Trankit report command started after installing Trankit runtime dependencies, but Trankit could not download its French model package from the upstream host:

```text
http://nlp.uoregon.edu/download/trankit/v1.0.0/xlm-roberta-base/french.zip
```

Direct download attempts over both HTTP and HTTPS also failed to connect to `nlp.uoregon.edu`.

## Current idea.md Sentences

1. Qu’il vienne immédiatement !
2. Sois prudent, même si tu crois avoir raison.
3. Ayant terminé son travail, elle serait déjà partie.
4. Les lettres qu’elle s’est écrites ont disparu.
5. Ils se sont parlé, puis ils se sont revus.
6. Il faut qu’elles soient revenues avant minuit.
7. Si elle avait su, elle ne serait pas venue.
8. Quand il aura fini, nous commencerons sans lui.
9. Eussiez-vous accepté, tout aurait été différent.
10. Leurs décisions ont été contestées puis annulées.
11. Cette maison s’est vendue très vite.
12. Il paraît qu’elle l’aurait vu hier.
13. Le livre que j’ai laissé tomber est abîmé.
14. Encore faut-il qu’on puisse le prouver.
15. Rentré trop tard, il s’est fait gronder par sa mère.

## Environment Notes

The normal install command failed because Trankit 1.1.2 declares `torch<=2.0.1`, while this Python 3.12 environment has Torch 2.10.0 installed. Trankit was installed with direct runtime dependencies to proceed as far as model loading, but model loading is blocked by the unavailable upstream download host.
