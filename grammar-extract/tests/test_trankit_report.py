from __future__ import annotations

from pathlib import Path

import pytest

from grammar_extract.trankit_report import (
    FrenchTrankitAnalyzer,
    TrankitUnavailableError,
    generate_idea_trankit_report,
    main,
    parse_idea_sentences,
)


class FakeTrankitAnalyzer:
    def analyze(self, sentence: str):
        return {
            "text": sentence,
            "tokens": [
                {
                    "id": 1,
                    "text": sentence.split()[0],
                    "lemma": "chanter",
                    "upos": "VERB",
                    "feats": "Mood=Ind|Tense=Pres|VerbForm=Fin",
                    "head": 0,
                    "deprel": "root",
                }
            ],
        }


def test_parse_idea_sentences_reads_labels(tmp_path: Path) -> None:
    idea_path = tmp_path / "idea.md"
    idea_path.write_text(
        "\n".join(
            [
                "Notes before the samples.",
                "",
                "Test sentences:",
                "",
                "Il chante tous les jours. （直陈现在）",
                "Il faut qu'il chante. （虚拟现在，与上句同形）",
            ]
        ),
        encoding="utf-8",
    )

    samples = parse_idea_sentences(idea_path)

    assert samples == [
        {"sentence": "Il chante tous les jours.", "label": "直陈现在"},
        {"sentence": "Il faut qu'il chante.", "label": "虚拟现在，与上句同形"},
    ]


def test_generate_idea_trankit_report_contains_tables_and_raw_output() -> None:
    report = generate_idea_trankit_report(
        analyzer=FakeTrankitAnalyzer(),
        samples=[{"sentence": "Il chante.", "label": "直陈现在"}],
    )

    assert "# French Trankit Report for idea.md Sentences" in report
    assert "## 1. 直陈现在" in report
    assert "Verb and auxiliary analysis" in report
    assert "Mood=Ind\\|Tense=Pres\\|VerbForm=Fin" in report
    assert "Raw Trankit output" in report
    assert '"lemma": "chanter"' in report


def test_french_trankit_analyzer_passes_sentence_mode_to_pipeline() -> None:
    calls = []

    def fake_pipeline(sentence: str, *, is_sent: bool):
        calls.append((sentence, is_sent))
        return {"text": sentence, "tokens": []}

    analyzer = FrenchTrankitAnalyzer(pipeline=fake_pipeline)
    analyzer.analyze("Bonjour.")

    assert calls == [("Bonjour.", True)]


def test_empty_trankit_sentence_is_rejected() -> None:
    analyzer = FrenchTrankitAnalyzer(pipeline=lambda sentence, *, is_sent: {})

    with pytest.raises(ValueError, match="sentence must not be empty"):
        analyzer.analyze("   ")


def test_main_reports_missing_trankit_without_traceback(monkeypatch, tmp_path: Path) -> None:
    idea_path = tmp_path / "idea.md"
    idea_path.write_text("Test sentences:\nBonjour. （test）\n", encoding="utf-8")

    def fake_build(*, language: str, gpu: bool, cache_dir: str | None):
        raise TrankitUnavailableError("Trankit missing")

    monkeypatch.setattr("grammar_extract.trankit_report.build_french_trankit_pipeline", fake_build)

    with pytest.raises(SystemExit) as exc_info:
        main(["--idea", str(idea_path), "--output", str(tmp_path / "report.md")])

    assert exc_info.value.code == 2
