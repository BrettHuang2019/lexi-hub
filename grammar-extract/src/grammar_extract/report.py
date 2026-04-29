from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

from grammar_extract.analyzer import FrenchAnalyzer

SAMPLE_SENTENCES = [
    {
        "label": "Present indicative",
        "sentence": "Je mange une pomme.",
        "target_lemma": "manger",
    },
    {
        "label": "Past participle in passe compose",
        "sentence": "J'ai mangé une pomme.",
        "target_lemma": "manger",
    },
    {
        "label": "Imperfect indicative",
        "sentence": "Je mangeais une pomme.",
        "target_lemma": "manger",
    },
    {
        "label": "Future indicative",
        "sentence": "Je mangerai une pomme.",
        "target_lemma": "manger",
    },
    {
        "label": "Conditional",
        "sentence": "Je voudrais une pomme.",
        "target_lemma": "vouloir",
    },
    {
        "label": "Subjunctive",
        "sentence": "Il faut que je mange une pomme.",
        "target_lemma": "manger",
    },
    {
        "label": "Imperative",
        "sentence": "Mange la pomme.",
        "target_lemma": "manger",
    },
]


def generate_sample_report(
    *,
    analyzer: FrenchAnalyzer | None = None,
    samples: list[dict[str, str]] | None = None,
) -> str:
    analyzer = analyzer or FrenchAnalyzer(processors="tokenize,mwt,pos,lemma,depparse", download=True)
    samples = samples or SAMPLE_SENTENCES

    sections = [
        "# French Stanza Tense and Mood Report",
        "",
        "Generated from real Stanza `Document.to_dict()` output.",
        "",
    ]

    for sample in samples:
        result = analyzer.analyze(sample["sentence"])
        words = flatten_words(result)
        target_words = [
            word
            for word in words
            if word.get("lemma") == sample["target_lemma"] and word.get("upos") in {"VERB", "AUX"}
        ]

        sections.extend(
            [
                f"## {sample['label']}",
                "",
                f"Sentence: {sample['sentence']}",
                "",
                "Target verb analysis:",
                "",
                "| Text | Lemma | UPOS | Features | Head | Dependency |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        sections.extend(format_word_table_rows(target_words))
        sections.extend(
            [
                "",
                "Full token analysis:",
                "",
                "| ID | Text | Lemma | UPOS | Features | Head | Dependency |",
                "| --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        sections.extend(format_word_table_rows(words, include_id=True))
        sections.extend(
            [
                "",
                "Raw Stanza output:",
                "",
                "```json",
                json.dumps(result, ensure_ascii=False, indent=2),
                "```",
                "",
            ]
        )

    return "\n".join(sections)


def generate_sentence_file_raw_report(
    sentence_path: Path,
    *,
    analyzer: FrenchAnalyzer | None = None,
    title: str | None = None,
) -> str:
    analyzer = analyzer or FrenchAnalyzer(processors="tokenize,mwt,pos,lemma,depparse", download=True)
    sentences = read_sentence_file(sentence_path)
    display_path = sentence_path.as_posix()

    sections = [
        f"# {title or 'French Stanza Raw JSON Report'}",
        "",
        f"Generated from real Stanza `Document.to_dict()` output using `{display_path}`.",
        "",
    ]

    for index, sentence in enumerate(sentences, start=1):
        result = analyzer.analyze(sentence)
        sections.extend(
            [
                f"## {index}. Sentence",
                "",
                f"Sentence: {sentence}",
                "",
                "Raw Stanza output:",
                "",
                "```json",
                json.dumps(result, ensure_ascii=False, indent=2),
                "```",
                "",
            ]
        )

    return "\n".join(sections)


def read_sentence_file(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def flatten_words(stanza_result: Any) -> list[dict[str, Any]]:
    if isinstance(stanza_result, list):
        return [word for sentence in stanza_result for word in sentence]

    sentences = stanza_result.get("sentences", [])
    return [word for sentence in sentences for word in sentence.get("words", [])]


def format_word_table_rows(
    words: list[dict[str, Any]],
    *,
    include_id: bool = False,
) -> list[str]:
    if not words:
        column_count = 7 if include_id else 6
        return ["| " + " | ".join(["_"] * column_count) + " |"]

    row_formatter: Callable[[dict[str, Any]], str]
    if include_id:
        row_formatter = lambda word: (
            f"| {cell(word.get('id'))} | {cell(word.get('text'))} | {cell(word.get('lemma'))} "
            f"| {cell(word.get('upos'))} | {cell(word.get('feats'))} | {cell(word.get('head'))} "
            f"| {cell(word.get('deprel'))} |"
        )
    else:
        row_formatter = lambda word: (
            f"| {cell(word.get('text'))} | {cell(word.get('lemma'))} | {cell(word.get('upos'))} "
            f"| {cell(word.get('feats'))} | {cell(word.get('head'))} | {cell(word.get('deprel'))} |"
        )

    return [row_formatter(word) for word in words]


def cell(value: Any) -> str:
    if value is None or value == "":
        return "_"
    return str(value).replace("|", "\\|")
