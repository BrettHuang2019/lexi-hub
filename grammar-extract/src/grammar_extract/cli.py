from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from grammar_extract.analyzer import DEFAULT_PROCESSORS, analyze_sentence
from grammar_extract.report import generate_sample_report


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.sample_report:
        report = generate_sample_report()
        report_path = Path(args.sample_report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8")
        print(f"Wrote report to {args.sample_report}")
        return 0

    sentence = args.sentence or sys.stdin.read()
    try:
        result = analyze_sentence(
            sentence,
            processors=args.processors,
            download=args.download,
        )
    except ValueError as exc:
        parser.error(str(exc))

    if args.format == "pretty":
        print(format_pretty(result))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analyze a French sentence with Stanza.",
    )
    parser.add_argument(
        "sentence",
        nargs="?",
        help="French sentence to analyze. Reads stdin when omitted.",
    )
    parser.add_argument(
        "--download",
        action="store_true",
        help="Download French Stanza resources before running the pipeline.",
    )
    parser.add_argument(
        "--processors",
        default=DEFAULT_PROCESSORS,
        help=f"Stanza processors to load. Default: {DEFAULT_PROCESSORS}",
    )
    parser.add_argument(
        "--format",
        choices=["json", "pretty"],
        default="json",
        help="Output format.",
    )
    parser.add_argument(
        "--sample-report",
        metavar="PATH",
        help="Write a Markdown report for built-in tense and mood sample sentences.",
    )
    return parser


def format_pretty(result: Any) -> str:
    if isinstance(result, list):
        return format_stanza_sentences(result)

    lines: list[str] = []
    for sentence_index, sentence in enumerate(result["sentences"], start=1):
        sentence_text = sentence.get("text") or result.get("text") or ""
        lines.append(f"Sentence {sentence_index}: {sentence_text}")
        lines.append("ID\tTEXT\tLEMMA\tUPOS\tFEATS\tHEAD\tDEPREL")
        for word in sentence["words"]:
            lines.append(
                "\t".join(
                    str(word.get(field) or "_")
                    for field in ("id", "text", "lemma", "upos", "feats", "head", "deprel")
                )
            )
    return "\n".join(lines)


def format_stanza_sentences(sentences: list[list[dict[str, Any]]]) -> str:
    lines: list[str] = []
    for sentence_index, words in enumerate(sentences, start=1):
        lines.append(f"Sentence {sentence_index}")
        lines.append("ID\tTEXT\tLEMMA\tUPOS\tFEATS\tHEAD\tDEPREL")
        for word in words:
            lines.append(
                "\t".join(
                    str(word.get(field) or "_")
                    for field in ("id", "text", "lemma", "upos", "feats", "head", "deprel")
                )
            )
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
