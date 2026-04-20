from __future__ import annotations

from types import SimpleNamespace

import pytest

from grammar_extract.analyzer import FrenchAnalyzer, analyze_sentence


def test_analyze_sentence_serializes_stanza_like_document() -> None:
    result = analyze_sentence("Je mange une pomme.", pipeline=fake_pipeline)

    assert result[0][1] == {
        "id": 2,
        "text": "mange",
        "lemma": "manger",
        "upos": "VERB",
        "feats": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
        "head": 0,
        "deprel": "root",
        "start_char": 3,
        "end_char": 8,
    }


def test_analyzer_reuses_pipeline_instance() -> None:
    calls: list[str] = []

    def pipeline(sentence: str) -> SimpleNamespace:
        calls.append(sentence)
        return fake_document(sentence)

    analyzer = FrenchAnalyzer(pipeline=pipeline)

    analyzer.analyze("Bonjour.")
    analyzer.analyze("Salut.")

    assert calls == ["Bonjour.", "Salut."]


def test_empty_sentence_is_rejected() -> None:
    with pytest.raises(ValueError, match="sentence must not be empty"):
        analyze_sentence("   ", pipeline=fake_pipeline)


def fake_pipeline(sentence: str) -> SimpleNamespace:
    return fake_document(sentence)


def fake_document(text: str) -> SimpleNamespace:
    stanza_output = [
        [
            {
                "id": 1,
                "text": "Je",
                "lemma": "je",
                "upos": "PRON",
                "feats": "Number=Sing|Person=1",
                "head": 2,
                "deprel": "nsubj",
                "start_char": 0,
                "end_char": 2,
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
                "end_char": 8,
            },
        ]
    ]
    return SimpleNamespace(text=text, to_dict=lambda: stanza_output)
