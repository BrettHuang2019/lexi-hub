# README

This is the README file from the PARSEME verbal multiword expressions (VMWEs) corpus for French, version 1.3.

The raw corpus is not released in the present directory, but can be downloaded from a [dedicated page](https://gitlab.com/parseme/corpora/-/wikis/Raw-corpora-for-the-PARSEME-1.2-shared-task)

## Data annotated for verbal MWEs

The current data contains the same VWME annotations as in the release 1.2 (with a small number of corrections), but with the underlying morphosyntactic annotation updated following UD 2.11.

The verbal MWE-annotated data for edition 1.2 (corresponding to edition 1.1, except that the morpho-syntactic annotations have been upgraded to UD 2.5 release) can be found on the tag [st1.2-release-training-v1](https://gitlab.com/parseme/parseme_corpus_fr/-/tree/st1.2-release-training-v1).

### Corpora

The verbal MWEs have been annotated in the following corpora:

#### Sequoia

All the 3099 sentences of the [Sequoia Treebank](https://www.rocq.inria.fr/alpage-wiki/tiki-index.php?page=CorpusSequoia).

Genres: sentences from a regional newspaper, medical reports, Europarl, and wikipedia historical frauds.

#### fr_gsd-ud
The French UD "GSD" corpus (for Google Stanford Dependencies").

Genres: the precise source and genre of each sentence was lost when the data was reshuffled from https://github.com/ryanmcd/uni-dep-tb to universal dependencies.
It seems the sentences come from very diverse web sites, as can be seen when searching on the web some GSD sentences.

#### fr_partut-ud

The French part of the ParTUT UD corpus.

Genres: from the fr_partut-ud README: "UD_French-ParTUT is a conversion of a multilingual parallel treebank developed at the University of Turin, and consisting of a variety of text genres, including talks, legal texts and Wikipedia articles, among others."


#### fr_pud-ud

The first 500 sentences of the French part of the Parallel Universal Dependencies (PUD) treebanks created for the [CoNLL 2017 shared task on Multilingual Parsing from Raw Text to Universal Dependencies](http://universaldependencies.org/conll17/).

Genres: from the fr_pud-ud README: "The sentences are taken from the news domain (sentence id starts in ‘n’) and from Wikipedia (sentence id starts with ‘w’)."

### Provided annotations

The data are in the [.cupt](http://multiword.sourceforge.net/cupt-format) format. Here is detailed information about some columns:

* LEMMA (column 3): Available.
* UPOS (column 4): Available. Manually annotated.
* XPOS (column 5): Inconsistent across subcorpora (Absent in the fr_gsd and fr_sequoia subcorpora; present but with two different tagsets in fr_partut and fr_pud subcorpora)
* HEAD and DEPREL (columns 7 and 8): Available. Manually annotated. The inventory is [Universal Dependency Relations](http://universaldependencies.org/u/dep)
* MISC (column 10): No-space information available. Automatically annotated.
* PARSEME:MWE (column 11): Manually annotated. The following [VMWE categories](http://parsemefr.lif.univ-mrs.fr/parseme-st-guidelines/1.1/?page=030_Categories_of_VMWEs) are annotated: VID, LVC.full, LVC.cause, IRV, MVC.

For all the subcorpora, the CoNLL-U columns are those found in the UD 2.11 release.

The annotation scheme for POS tags and syntactic dependencies are thus relatively homogeneous
(although there remain some differences across the various French UD corpora).

The annotation scheme for the parsed raw corpus (see above) is UD 2.5, more precisely,
it is that of fr_gsd-ud-2.5 (cf. the UDPIPE model used to parse the corpus was trained on fr_gsd-ud-2.5).

### Statistics
To know the number of annotated VMWEs of different types and with different properties (length, continuity, etc.), use these scripts: [mwe-stats.py](https://gitlab.com/parseme/utilities/-/blob/master/st-organizers/corpus-statistics/mwe-stats.py) and [mwe-stats-simple.py](https://gitlab.com/parseme/utilities/-/blob/master/st-organizers/corpus-statistics/mwe-stats-simple.py). 


### Tokenization

* The tokenization is that of the French UD treebanks, in which the following contractions appear as multi-word tokens (e.g. 1-2 au), split into words:
E.g. : Au soleil
```
1-2 Au
1 à
2 le
3 soleil
```

The list of contractions is:
```
au
auquel
aux
auxquelles
auxquels
des
desquelles
du
duquel
```

Note that the only ambiguous case are "des" / "du". Depending on the context, these tokens are either a plain determiner, or are split into preposition "de" + determiner "le" / "les".

## Raw corpora (UD-parsed) for the 1.2 edition

The raw corpus for the PARSEME 1.2 shared task contains about two thirds of the French wikipedia (dumped on Dec 12, 2016).

More precisely, the corpus contains 34 million sentences (out of a total of 46.7 million sentences),
minus 20919 sentences (corresponding to 5911 unique sentences), which have been removed because they were found in the VMWE annotated corpus.
So the precise number of sentences is 33 979 081 sentences,
and contains none of the sentences appearing in the VMWE annotated corpus.

The raw corpus is tokenized into a little less than 1 billion tokens (914 824 075 tokens),
and parsed with UDPIPE (http://ufal.mff.cuni.cz/udpipe),
using the french-gsd-ud-2.5-191206.udpipe model
(https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3131).

Each file contains around 1 million sentences and 27 million tokens.

The corpus processing was performed by Benoît Crabbé, Vincent Segonne and Marie Candito.

NB: the text in the "# text" lines of the CONLLU files is NOT the original text but a bare space-separated concatenation of the tokens.

### Authors

The VMWEs annotations were performed by Marie Candito, Mathieu Constant, Caroline Pasquer, Yannick Parmentier, Carlos Ramisch, Jean-Yves Antoine.
The annotations for the new test set for the 1.1 shared task were performed by Marie Candito.


### Licence

The VMEs annotations are distributed under the terms of the [CC-BY v4 license](https://creativecommons.org/licenses/by/4.0/). As far as the CONLL-U files are concerned, the UD part of the corpus is under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) and the Sequoia part is under [LGPL-LR](http://infolingu.univ-mlv.fr/DonneesLinguistiques/Lexiques-Grammaires/lgpllr.html). UD sentences can be identified by their `sent_id` prefixed with `fr-ud`.

The raw corpus is under CC BY-NC-SA 4.0 licence (the licence of the UDPipe model used to parse it).

## Contact

`marie.candito@gmail.com`


## Change log
- **2023-04-15**:
  - Version 1.3 of the corpus was released on LINDAT.
  - updating of morphosyntactic annotations to [UD 2.11](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-4923) by Bruno Guillaume
- **2020-07-09**:
  - [Version 1.2](http://hdl.handle.net/11234/1-3367) of the corpus was released on LINDAT.
  - Changes with respect to the 1.1 version are the following:
    - updating the morphosyntactic annotation (UPOS and FEATS columns) to make them compatible with the [Universal Dependencies version 2.5](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3105)
- **2018-04-30**:
  - [Version 1.1](http://hdl.handle.net/11372/LRT-2842) of the corpus was released on LINDAT.
  - Changes with respect to the 1.0 version are the following:
    - updating the existing VMWE annotations to comply with PARSEME [guidelines edition 1.1](http://parsemefr.lif.univ-mrs.fr/parseme-st-guidelines/1.1/).
    - addition of VWME annotations on other UD French corpora, to serve as new test for the 1.1 edition of the PARSEME shared task:
      - `fr_partut-ud`: 2.1 UD version of the French part of the ParTUT
      - `fr_pud-ud`: 2.1 UD version of the French part of the Parallel Universal Dependencies (PUD) treebanks created for the [CoNLL 2017 shared task on Multilingual Parsing from Raw Text to Universal Dependencies](http://universaldependencies.org/conll17/

- **2017-01-20**:
  - [Version 1.0](http://hdl.handle.net/11372/LRT-2282) of the corpus was released on LINDAT.
