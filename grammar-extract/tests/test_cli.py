from __future__ import annotations

import json

from grammar_extract import cli


def test_cli_prints_json(monkeypatch, capsys) -> None:
    def fake_analyze_sentence(sentence: str, *, processors: str, download: bool):
        return [[{"id": 1, "text": sentence, "processors": processors, "download": download}]]

    monkeypatch.setattr(cli, "analyze_sentence", fake_analyze_sentence)

    exit_code = cli.main(["--download", "Bonjour."])

    assert exit_code == 0
    output = json.loads(capsys.readouterr().out)
    assert output[0][0]["text"] == "Bonjour."
    assert output[0][0]["download"] is True


def test_pretty_format() -> None:
    result = {
        "text": "Je mange.",
        "sentences": [
            {
                "text": "Je mange.",
                "words": [
                    {
                        "id": 1,
                        "text": "Je",
                        "lemma": "je",
                        "upos": "PRON",
                        "feats": "Number=Sing",
                        "head": 2,
                        "deprel": "nsubj",
                    }
                ],
            }
        ],
        "entities": [],
    }

    assert "ID\tTEXT\tLEMMA\tUPOS\tFEATS\tHEAD\tDEPREL" in cli.format_pretty(result)
