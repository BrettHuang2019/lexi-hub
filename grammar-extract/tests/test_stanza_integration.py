from __future__ import annotations

import pytest

from grammar_extract.analyzer import analyze_sentence
from grammar_extract.report import generate_sample_report


@pytest.mark.integration
def test_real_stanza_french_pipeline_outputs_expected_word_fields() -> None:
    result = analyze_sentence(
        "Je mange une pomme.",
        processors="tokenize,mwt,pos,lemma,depparse",
        download=True,
    )

    assert isinstance(result, list)
    assert len(result) == 1

    words = result[0]
    assert [word["text"] for word in words] == ["Je", "mange", "une", "pomme", "."]

    mange = words[1]
    assert mange["lemma"] == "manger"
    assert mange["upos"] == "VERB"
    assert mange["head"] == 0
    assert mange["deprel"] == "root"

    pomme = words[3]
    assert pomme["lemma"] == "pomme"
    assert pomme["upos"] == "NOUN"
    assert pomme["deprel"] == "obj"


@pytest.mark.integration
def test_real_stanza_sample_report_contains_mood_and_tense_features() -> None:
    report = generate_sample_report()

    assert "Present indicative" in report
    assert "Subjunctive" in report
    assert "Imperative" in report
    assert "Mood=Ind" in report
    assert "Mood=Cnd" in report
    assert "Tense=Fut" in report
    assert "Tense=Past" in report
    assert "Raw Stanza output" in report
    assert '"lemma": "manger"' in report
