# grammar-extract

Small test project based on `idea.md`: use Stanza to analyze a French sentence and output Stanza's parsed data.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

Download the French Stanza models once:

```powershell
grammar-extract --download "Je mange une pomme."
```

## Usage

Analyze a sentence passed as an argument. JSON output is Stanza's native `Document.to_dict()` data:

```powershell
grammar-extract "Je mange une pomme."
```

Analyze text from stdin:

```powershell
"Je mange une pomme." | grammar-extract
```

Generate a Markdown report from built-in sample sentences covering tense and mood:

```powershell
grammar-extract --sample-report reports/french_stanza_tense_mood_report.md
```

Generate a Trankit Markdown report from the test sentences in `idea.md`:

```powershell
python -m pip install -e ".[trankit]"
trankit-idea-report --output reports/idea_md_trankit_report.md
```

Trankit 1.1.2 pins `torch<=2.0.1`; use a Python/Torch environment compatible
with that pin if your current environment has a newer Torch build.

Generate a spaCy Markdown report from the test sentences in `idea.md` using
`fr_dep_news_trf`:

```powershell
python -m pip install -e ".[spacy]"
python -m spacy download fr_dep_news_trf
spacy-idea-report --output reports/idea_md_spacy_report.md
```

Pretty-print token-level fields:

```powershell
grammar-extract --format pretty "Je mange une pomme."
```

## Tests

```powershell
pytest
```

The test suite includes a real Stanza integration test. Its first run downloads French models:

```powershell
pytest -m integration
```

Run everything:

```powershell
pytest
```
