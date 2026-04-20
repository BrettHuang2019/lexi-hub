from __future__ import annotations

from pathlib import Path
import pytest

from grammar_extract.spacy_report import (
    FrenchSpacyAnalyzer,
    SpacyUnavailableError,
    generate_idea_spacy_report,
    main,
)


class FakeSpacyAnalyzer:
    def analyze(self, sentence: str):
        return {
            "text": sentence,
            "model": "fr_dep_news_trf",
            "tokens": [
                {
                    "i": 0,
                    "idx": 0,
                    "text": sentence.split()[0],
                    "lemma_": "chanter",
                    "pos_": "VERB",
                    "tag_": "VERB",
                    "morph": "Mood=Ind|Tense=Pres|VerbForm=Fin",
                    "head_i": 0,
                    "head_text": sentence.split()[0],
                    "dep_": "ROOT",
                }
            ],
        }


class FakeToken:
    def __init__(
        self,
        *,
        index: int,
        text: str,
        lemma: str,
        pos: str,
        tag: str,
        morph: str,
        dep: str,
    ) -> None:
        self.i = index
        self.idx = 0
        self.text = text
        self.text_with_ws = text
        self.whitespace_ = ""
        self.lemma_ = lemma
        self.pos_ = pos
        self.tag_ = tag
        self.morph = morph
        self.dep_ = dep
        self.head = self
        self.is_sent_start = True
        self.ent_iob_ = "O"
        self.ent_type_ = ""
        self.shape_ = "Xxxxx"
        self.is_alpha = True
        self.is_stop = False


def test_generate_idea_spacy_report_contains_tables_and_raw_output() -> None:
    report = generate_idea_spacy_report(
        analyzer=FakeSpacyAnalyzer(),
        samples=[{"sentence": "Il chante.", "label": "直陈现在"}],
    )

    assert "# French spaCy Report for idea.md Sentences" in report
    assert "## 1. 直陈现在" in report
    assert "Verb and auxiliary analysis" in report
    assert "Mood=Ind\\|Tense=Pres\\|VerbForm=Fin" in report
    assert "Raw spaCy output" in report
    assert '"lemma_": "chanter"' in report


def test_french_spacy_analyzer_serializes_pipeline_doc() -> None:
    class FakeDoc:
        text = "Chante."

        def __iter__(self):
            return iter(
                [
                    FakeToken(
                        index=0,
                        text="Chante",
                        lemma="chanter",
                        pos="VERB",
                        tag="VERB",
                        morph="Mood=Imp|VerbForm=Fin",
                        dep="ROOT",
                    )
                ]
            )

    analyzer = FrenchSpacyAnalyzer(pipeline=lambda sentence: FakeDoc())
    result = analyzer.analyze("Chante.")

    assert result["text"] == "Chante."
    assert result["tokens"] == [
        {
            "i": 0,
            "idx": 0,
            "text": "Chante",
            "text_with_ws": "Chante",
            "whitespace_": "",
            "lemma_": "chanter",
            "pos_": "VERB",
            "tag_": "VERB",
            "morph": "Mood=Imp|VerbForm=Fin",
            "dep_": "ROOT",
            "head_i": 0,
            "head_text": "Chante",
            "is_sent_start": True,
            "ent_iob_": "O",
            "ent_type_": "",
            "shape_": "Xxxxx",
            "is_alpha": True,
            "is_stop": False,
        }
    ]


def test_empty_spacy_sentence_is_rejected() -> None:
    analyzer = FrenchSpacyAnalyzer(pipeline=lambda sentence: {})

    with pytest.raises(ValueError, match="sentence must not be empty"):
        analyzer.analyze("   ")


def test_main_reports_missing_spacy_without_traceback(monkeypatch, tmp_path: Path) -> None:
    idea_path = tmp_path / "idea.md"
    idea_path.write_text("Test sentences:\nBonjour. （test）\n", encoding="utf-8")

    def fake_build(*, model: str):
        raise SpacyUnavailableError("spaCy missing")

    monkeypatch.setattr("grammar_extract.spacy_report.build_french_spacy_pipeline", fake_build)

    with pytest.raises(SystemExit) as exc_info:
        main(["--idea", str(idea_path), "--output", str(tmp_path / "report.md")])

    assert exc_info.value.code == 2
