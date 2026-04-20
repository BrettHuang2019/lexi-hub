from __future__ import annotations

import argparse
import json
import re
from collections.abc import Callable
from pathlib import Path
from typing import Any

from grammar_extract.report import format_word_table_rows

DEFAULT_IDEA_PATH = Path("idea.md")
DEFAULT_REPORT_PATH = Path("reports/idea_md_trankit_report.md")
DEFAULT_LANGUAGE = "french"


class TrankitUnavailableError(RuntimeError):
    """Raised when Trankit is not installed but a real pipeline is requested."""


class FrenchTrankitAnalyzer:
    def __init__(
        self,
        *,
        pipeline: Callable[..., dict[str, Any]] | None = None,
        language: str = DEFAULT_LANGUAGE,
        gpu: bool = False,
        cache_dir: str | None = None,
    ) -> None:
        self._pipeline = pipeline
        self._language = language
        self._gpu = gpu
        self._cache_dir = cache_dir

    def analyze(self, sentence: str) -> dict[str, Any]:
        sentence = sentence.strip()
        if not sentence:
            raise ValueError("sentence must not be empty")

        return self._get_pipeline()(sentence, is_sent=True)

    def _get_pipeline(self) -> Callable[..., dict[str, Any]]:
        if self._pipeline is None:
            self._pipeline = build_french_trankit_pipeline(
                language=self._language,
                gpu=self._gpu,
                cache_dir=self._cache_dir,
            )
        return self._pipeline


def build_french_trankit_pipeline(
    *,
    language: str = DEFAULT_LANGUAGE,
    gpu: bool = False,
    cache_dir: str | None = None,
) -> Callable[..., dict[str, Any]]:
    try:
        from trankit import Pipeline
    except ImportError as exc:
        raise TrankitUnavailableError(
            "Trankit could not be imported. Install it with "
            f"`python -m pip install -e \".[trankit]\"`, then check dependency compatibility. {exc}"
        ) from exc

    options: dict[str, Any] = {"gpu": gpu}
    if cache_dir:
        options["cache_dir"] = cache_dir

    return Pipeline(language, **options)


def parse_idea_sentences(idea_path: Path = DEFAULT_IDEA_PATH) -> list[dict[str, str]]:
    text = idea_path.read_text(encoding="utf-8")
    samples: list[dict[str, str]] = []
    in_test_sentences = False

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.lower().startswith("test sentences"):
            in_test_sentences = True
            continue
        if not in_test_sentences:
            continue

        match = re.match(r"^(?P<sentence>.+?)\s*[（(](?P<label>.+?)[）)]\s*$", line)
        if match:
            samples.append(
                {
                    "sentence": match.group("sentence").strip(),
                    "label": match.group("label").strip(),
                }
            )
        else:
            samples.append({"sentence": line, "label": "Unlabeled"})

    if not samples:
        raise ValueError(f"no test sentences found in {idea_path}")

    return samples


def generate_idea_trankit_report(
    *,
    analyzer: FrenchTrankitAnalyzer | None = None,
    samples: list[dict[str, str]] | None = None,
    idea_path: Path = DEFAULT_IDEA_PATH,
) -> str:
    analyzer = analyzer or FrenchTrankitAnalyzer()
    samples = samples or parse_idea_sentences(idea_path)

    sections = [
        "# French Trankit Report for idea.md Sentences",
        "",
        "Generated from real Trankit output using the sentences listed in `idea.md`.",
        "",
    ]

    for index, sample in enumerate(samples, start=1):
        result = analyzer.analyze(sample["sentence"])
        tokens = flatten_tokens(result)
        verb_tokens = [token for token in tokens if token.get("upos") in {"VERB", "AUX"}]

        sections.extend(
            [
                f"## {index}. {sample['label']}",
                "",
                f"Sentence: {sample['sentence']}",
                "",
                "Verb and auxiliary analysis:",
                "",
                "| Text | Lemma | UPOS | Features | Head | Dependency |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        sections.extend(format_word_table_rows(verb_tokens))
        sections.extend(
            [
                "",
                "Full token analysis:",
                "",
                "| ID | Text | Lemma | UPOS | Features | Head | Dependency |",
                "| --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        sections.extend(format_word_table_rows(tokens, include_id=True))
        sections.extend(
            [
                "",
                "Raw Trankit output:",
                "",
                "```json",
                json.dumps(result, ensure_ascii=False, indent=2),
                "```",
                "",
            ]
        )

    return "\n".join(sections)


def flatten_tokens(result: dict[str, Any]) -> list[dict[str, Any]]:
    if "tokens" in result:
        return [normalize_token(token) for token in result["tokens"]]

    tokens: list[dict[str, Any]] = []
    for sentence in result.get("sentences", []):
        tokens.extend(normalize_token(token) for token in sentence.get("tokens", []))
    return tokens


def normalize_token(token: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(token)
    if "feats" not in normalized and "expanded" in normalized:
        expanded = normalized["expanded"]
        if expanded:
            normalized.update(
                {
                    key: expanded[0].get(key)
                    for key in ("lemma", "upos", "xpos", "feats", "head", "deprel")
                    if expanded[0].get(key) is not None
                }
            )
    return normalized


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Analyze the French test sentences in idea.md with Trankit.",
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
        "--language",
        default=DEFAULT_LANGUAGE,
        help=f"Trankit language package. Default: {DEFAULT_LANGUAGE}",
    )
    parser.add_argument(
        "--gpu",
        action="store_true",
        help="Allow Trankit to use GPU instead of forcing CPU.",
    )
    parser.add_argument(
        "--cache-dir",
        help="Optional Trankit model cache directory.",
    )
    args = parser.parse_args(argv)

    analyzer = FrenchTrankitAnalyzer(
        language=args.language,
        gpu=args.gpu,
        cache_dir=args.cache_dir,
    )
    try:
        report = generate_idea_trankit_report(
            analyzer=analyzer,
            idea_path=Path(args.idea),
        )
    except (TrankitUnavailableError, ValueError) as exc:
        parser.error(str(exc))

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"Wrote Trankit report to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
