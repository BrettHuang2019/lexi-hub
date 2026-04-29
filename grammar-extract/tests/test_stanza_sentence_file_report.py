from __future__ import annotations

from pathlib import Path

from grammar_extract.report import generate_sentence_file_raw_report, read_sentence_file


class FakeAnalyzer:
    def analyze(self, sentence: str):
        return [
            [
                {
                    "id": 1,
                    "text": sentence.split()[0],
                    "lemma": "manger",
                    "upos": "VERB",
                    "feats": "Mood=Ind|Tense=Pres|VerbForm=Fin|Voice=Act",
                    "head": 0,
                    "deprel": "root",
                }
            ]
        ]


def test_generate_sentence_file_raw_report_for_tense_mood_voice_sentences() -> None:
    sentence_path = Path("Stanza-test/fr_stanza_tense_mood_voice_test_sentences.txt")
    report = generate_sentence_file_raw_report(
        sentence_path,
        analyzer=FakeAnalyzer(),
        title="French Stanza Raw JSON Report for Tense, Mood, and Voice Test Sentences",
    )

    sentences = read_sentence_file(sentence_path)

    assert len(sentences) == 100
    assert "# French Stanza Raw JSON Report for Tense, Mood, and Voice Test Sentences" in report
    assert "Generated from real Stanza `Document.to_dict()` output using" in report
    assert "Sentence: Je mange une pomme pendant que tu lis le journal." in report
    assert "Sentence: La clé que tu croyais avoir perdue se trouvait dans le manteau que tu portais." in report
    assert report.count("Raw Stanza output:") == 100
    assert '"feats": "Mood=Ind|Tense=Pres|VerbForm=Fin|Voice=Act"' in report
