from __future__ import annotations

import argparse
import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

from grammar_extract.trankit_report import DEFAULT_IDEA_PATH, parse_idea_sentences

DEFAULT_MODEL = "fr_dep_news_trf"
DEFAULT_REPORT_PATH = Path("reports/idea_md_spacy_report.md")


class SpacyUnavailableError(RuntimeError):
    """Raised when spaCy or the requested French model cannot be loaded."""


class FrenchSpacyAnalyzer:
    def __init__(
        self,
        *,
        pipeline: Callable[[str], Any] | None = None,
        model: str = DEFAULT_MODEL,
    ) -> None:
        self._pipeline = pipeline
        self._model = model

    def analyze(self, sentence: str) -> dict[str, Any]:
        sentence = sentence.strip()
        if not sentence:
            raise ValueError("sentence must not be empty")

        doc = self._get_pipeline()(sentence)
        return serialize_doc(doc, model=self._model)

    def _get_pipeline(self) -> Callable[[str], Any]:
        if self._pipeline is None:
            self._pipeline = build_french_spacy_pipeline(model=self._model)
        return self._pipeline


def build_french_spacy_pipeline(*, model: str = DEFAULT_MODEL) -> Callable[[str], Any]:
    try:
        import spacy
    except ImportError as exc:
        raise SpacyUnavailableError(
            "spaCy could not be imported. Install it with "
            '`python -m pip install -e ".[spacy]"`, then install the French transformer model with '
            f"`python -m spacy download {model}`. {exc}"
        ) from exc

    try:
        return spacy.load(model)
    except OSError as exc:
        raise SpacyUnavailableError(
            f"spaCy model `{model}` could not be loaded. Install it with "
            f"`python -m spacy download {model}`. {exc}"
        ) from exc


def generate_idea_spacy_report(
    *,
    analyzer: FrenchSpacyAnalyzer | None = None,
    samples: list[dict[str, str]] | None = None,
    idea_path: Path = DEFAULT_IDEA_PATH,
) -> str:
    analyzer = analyzer or FrenchSpacyAnalyzer()
    samples = samples or parse_idea_sentences(idea_path)

    sections = [
        "# French spaCy Report for idea.md Sentences",
        "",
        f"Generated from spaCy `{DEFAULT_MODEL}` output using the sentences listed in `idea.md`.",
        "",
    ]

    for index, sample in enumerate(samples, start=1):
        result = analyzer.analyze(sample["sentence"])
        tokens = flatten_tokens(result)
        verb_tokens = [token for token in tokens if token.get("pos_") in {"VERB", "AUX"}]

        sections.extend(
            [
                f"## {index}. {sample['label']}",
                "",
                f"Sentence: {sample['sentence']}",
                "",
                "Verb and auxiliary analysis:",
                "",
                "| Text | Lemma | POS | Tag | Morph | Head | Dependency |",
                "| --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        sections.extend(format_spacy_table_rows(verb_tokens))
        sections.extend(
            [
                "",
                "Full token analysis:",
                "",
                "| I | Character | Text | Lemma | POS | Tag | Morph | Head I | Head Text | Dependency | Entity |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        sections.extend(format_spacy_table_rows(tokens, include_position=True))
        sections.extend(
            [
                "",
                "Raw spaCy output:",
                "",
                "```json",
                json.dumps(result, ensure_ascii=False, indent=2),
                "```",
                "",
            ]
        )

    return "\n".join(sections)


def serialize_doc(doc: Any, *, model: str = DEFAULT_MODEL) -> dict[str, Any]:
    tokens = [serialize_token(token) for token in doc]
    return {
        "text": doc.text,
        "model": model,
        "lang_": getattr(doc, "lang_", None),
        "cats": getattr(doc, "cats", {}),
        "sentences": [sent.text for sent in getattr(doc, "sents", [])],
        "ents": [serialize_span(ent) for ent in getattr(doc, "ents", [])],
        "tokens": tokens,
    }


def serialize_token(token: Any) -> dict[str, Any]:
    feats = str(token.morph) if str(token.morph) else None
    head = token.head

    return {
        "i": token.i,
        "idx": token.idx,
        "text": token.text,
        "text_with_ws": token.text_with_ws,
        "whitespace_": token.whitespace_,
        "lemma_": token.lemma_,
        "pos_": token.pos_,
        "tag_": token.tag_,
        "morph": feats,
        "dep_": token.dep_,
        "head_i": head.i,
        "head_text": head.text,
        "is_sent_start": token.is_sent_start,
        "ent_iob_": token.ent_iob_,
        "ent_type_": token.ent_type_,
        "shape_": token.shape_,
        "is_alpha": token.is_alpha,
        "is_stop": token.is_stop,
    }


def serialize_span(span: Any) -> dict[str, Any]:
    return {
        "text": span.text,
        "label_": span.label_,
        "start": span.start,
        "end": span.end,
        "start_char": span.start_char,
        "end_char": span.end_char,
    }


def flatten_tokens(result: dict[str, Any]) -> list[dict[str, Any]]:
    return list(result.get("tokens", []))


def format_spacy_table_rows(
    tokens: list[dict[str, Any]],
    *,
    include_position: bool = False,
) -> list[str]:
    if not tokens:
        column_count = 11 if include_position else 7
        return ["| " + " | ".join(["_"] * column_count) + " |"]

    if include_position:
        return [
            (
                f"| {cell(token.get('i'))} | {cell(token.get('idx'))} | {cell(token.get('text'))} "
                f"| {cell(token.get('lemma_'))} | {cell(token.get('pos_'))} | {cell(token.get('tag_'))} "
                f"| {cell(token.get('morph'))} | {cell(token.get('head_i'))} | {cell(token.get('head_text'))} "
                f"| {cell(token.get('dep_'))} | {cell(entity_cell(token))} |"
            )
            for token in tokens
        ]

    return [
        (
            f"| {cell(token.get('text'))} | {cell(token.get('lemma_'))} | {cell(token.get('pos_'))} "
            f"| {cell(token.get('tag_'))} | {cell(token.get('morph'))} | {cell(token.get('head_text'))} "
            f"| {cell(token.get('dep_'))} |"
        )
        for token in tokens
    ]


def entity_cell(token: dict[str, Any]) -> str | None:
    ent_iob = token.get("ent_iob_")
    ent_type = token.get("ent_type_")
    if not ent_iob or ent_iob == "O":
        return None
    return f"{ent_iob}-{ent_type}" if ent_type else str(ent_iob)


def cell(value: Any) -> str:
    if value is None or value == "":
        return "_"
    return str(value).replace("|", "\\|")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=f"Analyze the French test sentences in idea.md with spaCy {DEFAULT_MODEL}.",
    )
    parser.add_argument(
        "--idea",
        default=str(DEFAULT_IDEA_PATH),
        help=f"Path to idea.md. Default: {DEFAULT_IDEA_PATH}",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_REPORT_PATH),
        help=f"Markdown report path. Default: {DEFAULT_REPORT_PATH}",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"spaCy model name. Default: {DEFAULT_MODEL}",
    )
    args = parser.parse_args(argv)

    analyzer = FrenchSpacyAnalyzer(model=args.model)
    try:
        report = generate_idea_spacy_report(
            analyzer=analyzer,
            idea_path=Path(args.idea),
        )
    except (SpacyUnavailableError, ValueError) as exc:
        parser.error(str(exc))

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"Wrote spaCy report to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
