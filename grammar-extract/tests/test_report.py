from __future__ import annotations

from grammar_extract.report import generate_sample_report


class FakeAnalyzer:
    def analyze(self, sentence: str):
        return [
            [
                {
                    "id": 1,
                    "text": sentence.split()[0],
                    "lemma": "manger",
                    "upos": "VERB",
                    "feats": "Mood=Ind|Tense=Pres|VerbForm=Fin",
                    "head": 0,
                    "deprel": "root",
                }
            ]
        ]


def test_generate_sample_report_contains_target_and_full_analysis() -> None:
    report = generate_sample_report(
        analyzer=FakeAnalyzer(),
        samples=[
            {
                "label": "Present indicative",
                "sentence": "Mange.",
                "target_lemma": "manger",
            }
        ],
    )

    assert "# French Stanza Tense and Mood Report" in report
    assert "## Present indicative" in report
    assert "Mood=Ind\\|Tense=Pres\\|VerbForm=Fin" in report
    assert "Full token analysis" in report
    assert "Raw Stanza output" in report
    assert '"feats": "Mood=Ind|Tense=Pres|VerbForm=Fin"' in report
