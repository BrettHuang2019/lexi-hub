from __future__ import annotations

import csv
import math
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"
OUT_DIR = ROOT / "generated"
OUT_PATH = OUT_DIR / "phrase_dictionary_sample_100.tsv"

FLELEX_PATH = RESEARCH / "FleLex_CRF.csv"
DELA_PATH = RESEARCH / "dela-fr-public-u8.phrases.tsv"
IDIOM_PATH = RESEARCH / "idioms-runtime-dictionary.tsv"

CEFR_WEIGHTS = {
    "freq_a1": 0.05,
    "freq_a2": 0.20,
    "freq_b1": 0.40,
    "freq_b2": 0.60,
    "freq_c1": 0.80,
    "freq_c2": 0.95,
}

LEARNER_LEVEL_OVERRIDES = {
    "au lit": 0.05,
    "bien sûr": 0.05,
    "appareil photo": 0.40,
    "a priori": 0.80,
}

CONFIDENCE_IDIOM_STRENGTH_SCORES = {
    "free lexeme": 0.10,
    "weak idiom": 0.35,
    "semi-idiom": 0.60,
    "strong idiom": 0.90,
}

DIFFICULTY_IDIOM_STRENGTH_SCORES = {
    "free lexeme": 0.0,
    "weak idiom": 0.30,
    "semi-idiom": 0.60,
    "strong idiom": 0.90,
}

TYPE_SCORES = {
    "prepositional_phrase": 0.25,
    "fixed_expression": 0.45,
    "verbal_phrase": 0.50,
    "nominal_phrase": 0.40,
    "idiom": 0.75,
}

TOKEN_RE = re.compile(r"[a-zàâäçéèêëîïôöùûüÿñæœ'-]+", re.IGNORECASE)


@dataclass
class FleLexScore:
    lexical_score: float
    cefr_score: float
    rarity_score: float
    freq_total: float
    matched: bool


@dataclass
class PhraseEntry:
    phrase: str
    surface_forms: set[str] = field(default_factory=set)
    sources: set[str] = field(default_factory=set)
    types: set[str] = field(default_factory=set)
    pos: set[str] = field(default_factory=set)
    idiom_strengths: set[str] = field(default_factory=set)
    idiom_r1: set[str] = field(default_factory=set)
    idiom_source_ids: set[str] = field(default_factory=set)
    source_rows: int = 0


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).strip().lower()
    text = text.replace("’", "'").replace("`", "'")
    text = re.sub(r"\s+", " ", text)
    return text


def parse_float(value: str | None) -> float:
    if not value:
        return 0.0
    try:
        return float(value)
    except ValueError:
        return 0.0


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def length_score(phrase: str) -> float:
    token_count = len(tokenize(phrase))
    if token_count <= 1:
        return 0.0
    if token_count == 2:
        return 0.20
    if token_count == 3:
        return 0.40
    if token_count == 4:
        return 0.60
    return 0.80


def structural_complexity_score(phrase: str) -> float:
    normalized = normalize(phrase)
    tokens = tokenize(normalized)
    if "à ce que" in normalized or " que" in f" {normalized}" or " où" in f" {normalized}":
        return 0.80
    if len(tokens) <= 2:
        return 0.20
    if len(tokens) == 3:
        return 0.40
    return 0.60


def max_structural_complexity_score(entry: PhraseEntry) -> float:
    forms = [entry.phrase, *entry.surface_forms]
    return max(structural_complexity_score(form) for form in forms if form)


def scoring_form(entry: PhraseEntry) -> str:
    forms = [entry.phrase, *entry.surface_forms]
    return max(forms, key=lambda value: (structural_complexity_score(value), len(tokenize(value)), len(value)))


def tokenize(phrase: str) -> list[str]:
    return TOKEN_RE.findall(normalize(phrase))


def flelex_row_score(row: dict[str, str]) -> FleLexScore:
    level_freqs = {key: parse_float(row.get(key)) for key in CEFR_WEIGHTS}
    level_total = sum(level_freqs.values())
    freq_total = parse_float(row.get("freq_total"))

    if level_total:
        cefr_score = sum(level_freqs[key] * CEFR_WEIGHTS[key] for key in CEFR_WEIGHTS) / level_total
    else:
        cefr_score = 0.75

    common_threshold = 100.0
    rarity_score = 1.0 - min(1.0, math.log(freq_total + 1.0) / math.log(common_threshold + 1.0))
    lexical_score = clamp((0.7 * cefr_score) + (0.3 * rarity_score))
    return FleLexScore(lexical_score, cefr_score, rarity_score, freq_total, True)


def load_flelex() -> dict[str, FleLexScore]:
    scores: dict[str, FleLexScore] = {}
    with FLELEX_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            word = normalize(row["word"])
            score = flelex_row_score(row)
            previous = scores.get(word)
            if previous is None or score.freq_total > previous.freq_total:
                scores[word] = score
    return scores


def add_entry(entries: dict[str, PhraseEntry], phrase: str) -> PhraseEntry:
    key = normalize(phrase)
    if key not in entries:
        entries[key] = PhraseEntry(phrase=key)
    return entries[key]


def load_dela(entries: dict[str, PhraseEntry]) -> None:
    with DELA_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            base = normalize(row["base"])
            entry = add_entry(entries, base)
            entry.surface_forms.add(normalize(row["surface"]))
            entry.sources.add("dela")
            entry.types.add(row["type"])
            entry.pos.add(row["pos"])
            entry.source_rows += 1


def load_idioms(entries: dict[str, PhraseEntry]) -> None:
    with IDIOM_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            phrase = normalize(row["entry"])
            entry = add_entry(entries, phrase)
            entry.surface_forms.add(phrase)
            entry.sources.add("idiom")
            entry.types.add(row["type"])
            entry.pos.add(row["pos"])
            entry.idiom_strengths.add(row["strength"])
            entry.idiom_r1.add(row["r1"])
            entry.idiom_source_ids.add(row["source_id"])
            entry.source_rows += parse_float(row["source_rows"]) or 1


def score_phrase_with_flelex(phrase: str, flelex: dict[str, FleLexScore]) -> tuple[FleLexScore, str]:
    exact = flelex.get(normalize(phrase))
    if exact:
        return exact, "exact"

    token_flelex_scores = [flelex[token] for token in tokenize(phrase) if token in flelex]
    if not token_flelex_scores:
        return FleLexScore(0.75, 0.75, 0.75, 0.0, False), "none"

    token_scores = [score.lexical_score for score in token_flelex_scores]
    token_rarity_scores = [score.rarity_score for score in token_flelex_scores]
    token_cefr_scores = [score.cefr_score for score in token_flelex_scores]
    token_freqs = [score.freq_total for score in token_flelex_scores if score.freq_total > 0.0]
    avg_score = sum(token_scores) / len(token_scores)
    avg_rarity = sum(token_rarity_scores) / len(token_rarity_scores)
    avg_cefr = sum(token_cefr_scores) / len(token_cefr_scores)
    lexical_score = clamp((0.7 * max(token_scores)) + (0.3 * avg_score))
    rarity_score = clamp((0.7 * max(token_rarity_scores)) + (0.3 * avg_rarity))
    token_freq = min(token_freqs) if token_freqs else 0.0
    return FleLexScore(lexical_score, avg_cefr, rarity_score, token_freq, True), "tokens"


def best_idiom_strength(strengths: set[str]) -> str:
    if not strengths:
        return ""
    return max(strengths, key=lambda value: DIFFICULTY_IDIOM_STRENGTH_SCORES.get(value, 0.0))


def best_type(types: set[str]) -> str:
    if not types:
        return "unknown"
    return max(types, key=lambda value: TYPE_SCORES.get(value, 0.50))


def semantic_opacity_score(entry: PhraseEntry, strength: str, phrase_type: str) -> float:
    transparent_expressions = {
        "à cause de",
        "appareil photo",
        "au lit",
        "au lieu",
        "au lieu de",
        "avoir besoin",
        "bien sûr",
        "en public",
        "tout à fait",
    }
    opaque_expressions = {
        "a fortiori",
        "a posteriori",
        "a priori",
        "bouton-d'or",
        "pot-de-vin",
    }
    fixed_collocations = {
        "de peur",
        "de peur de",
        "dans l'hypothèse de",
        "de manière à ce que",
    }

    if entry.phrase in transparent_expressions:
        return 0.15
    if entry.phrase in opaque_expressions:
        return 0.85
    if entry.phrase in fixed_collocations:
        return 0.45
    if has_formal_marker(entry) and structural_complexity_score(scoring_form(entry)) >= 0.60:
        return 0.65
    if strength == "strong idiom":
        return 0.95
    if strength == "semi-idiom":
        return 0.60
    if strength == "weak idiom":
        return 0.35
    if phrase_type == "idiom":
        return 0.65
    if phrase_type == "fixed_expression":
        return 0.30
    if phrase_type == "verbal_phrase":
        return 0.25
    if phrase_type == "prepositional_phrase":
        return 0.15
    return 0.20


def has_formal_marker(entry: PhraseEntry) -> bool:
    phrase_text = " ".join([entry.phrase, " ".join(entry.surface_forms)])
    return any(term in phrase_text for term in FORMAL_TERMS)


LEGAL_TECHNICAL_LITERARY_TERMS = [
    "accus",
    "appel",
    "bail",
    "criminel",
    "essai",
    "juridique",
    "médical",
    "politique",
    "pot-de-vin",
    "pot de vin",
    "scientifique",
    "vasculaire",
]

FORMAL_TERMS = [
    "a fortiori",
    "a posteriori",
    "a priori",
    "afin",
    "condition",
    "conséquence",
    "en vue",
    "hypothèse",
    "intention",
    "manière à ce que",
    "mesure où",
    "moyen",
    "raison",
]

SPOKEN_TERMS = [
    "ah ",
    "bah",
    "ben",
    "bonjour",
    "merci",
    "ouais",
]


def difficulty_rarity_score(entry: PhraseEntry, flelex_score: FleLexScore, flelex_match: str) -> float:
    rarity = flelex_score.rarity_score
    if entry.phrase in LEARNER_LEVEL_OVERRIDES and LEARNER_LEVEL_OVERRIDES[entry.phrase] <= 0.05:
        rarity = min(rarity, 0.15)
    if has_formal_marker(entry):
        rarity = max(rarity, 0.75)
    elif "idiom" in entry.sources and flelex_match == "none":
        rarity = max(rarity, 0.75)
    elif flelex_match != "exact" and entry.types.intersection({"prepositional_phrase", "fixed_expression"}):
        rarity = max(rarity, 0.35)
    elif "prepositional_phrase" in entry.types:
        rarity = max(rarity, 0.25)
    return clamp(rarity)


def cefr_proxy_score(entry: PhraseEntry, flelex_score: FleLexScore, rarity_score: float, phrase_type: str) -> float:
    if entry.phrase in LEARNER_LEVEL_OVERRIDES:
        return LEARNER_LEVEL_OVERRIDES[entry.phrase]

    score = flelex_score.cefr_score if flelex_score.matched else 0.75
    if flelex_score.freq_total >= 50.0:
        score = min(score, 0.25)
    elif flelex_score.freq_total >= 10.0:
        score = min(score, 0.45)
    elif flelex_score.freq_total < 1.0:
        score = max(score, 0.60)

    if phrase_type in {"nominal_phrase", "prepositional_phrase"} and semantic_head_is_common(entry):
        score = min(score, 0.45)
    if has_formal_marker(entry):
        score = max(score, 0.75)
    return clamp((0.65 * score) + (0.35 * rarity_score))


def semantic_head_is_common(entry: PhraseEntry) -> bool:
    common_heads = {
        "appareil",
        "besoin",
        "cause",
        "lieu",
        "lit",
        "photo",
        "public",
    }
    return any(token in common_heads for token in tokenize(entry.phrase))


def construction_fixedness_score(entry: PhraseEntry, phrase_type: str) -> float:
    if entry.phrase in {"appareil photo", "au lit", "bien sûr", "à cause de", "au lieu de"}:
        return 0.10
    if entry.phrase in {"de peur de", "de peur", "dans l'hypothèse de", "de manière à ce que"}:
        return 0.45
    if phrase_type == "fixed_expression":
        return 0.35
    if phrase_type == "prepositional_phrase":
        return 0.25
    if phrase_type == "nominal_phrase":
        return 0.20
    if phrase_type == "idiom":
        return 0.55
    return 0.30


def register_score(entry: PhraseEntry) -> float:
    phrase_text = " ".join([entry.phrase, " ".join(entry.surface_forms)])
    if any(term in phrase_text for term in LEGAL_TECHNICAL_LITERARY_TERMS):
        return 0.90
    if any(term in phrase_text for term in FORMAL_TERMS):
        return 0.70
    if any(term in phrase_text for term in SPOKEN_TERMS):
        return 0.10
    return 0.30


def final_score(entry: PhraseEntry, flelex: dict[str, FleLexScore]) -> dict[str, str]:
    flelex_score, flelex_match = score_phrase_with_flelex(entry.phrase, flelex)
    strength = best_idiom_strength(entry.idiom_strengths)
    phrase_type = best_type(entry.types)
    confidence_idiom_score = CONFIDENCE_IDIOM_STRENGTH_SCORES.get(strength, 0.0)
    idiom_strength_score = DIFFICULTY_IDIOM_STRENGTH_SCORES.get(strength, 0.0)
    type_score = TYPE_SCORES.get(phrase_type, 0.50)
    phrase_length_score = length_score(entry.phrase)
    semantic_opacity = semantic_opacity_score(entry, strength, phrase_type)
    structural_complexity = max_structural_complexity_score(entry)
    phrase_register_score = register_score(entry)
    rarity_score = difficulty_rarity_score(entry, flelex_score, flelex_match)
    cefr_score = cefr_proxy_score(entry, flelex_score, rarity_score, phrase_type)
    construction_score = construction_fixedness_score(entry, phrase_type)

    confidence_score = clamp(
        (0.55 * flelex_score.lexical_score)
        + (0.25 * confidence_idiom_score)
        + (0.10 * type_score)
        + (0.10 * phrase_length_score)
    )
    difficulty_score = clamp(
        (0.45 * rarity_score)
        + (0.25 * cefr_score)
        + (0.15 * semantic_opacity)
        + (0.06 * phrase_register_score)
        + (0.05 * construction_score)
        + (0.02 * structural_complexity)
        + (0.02 * idiom_strength_score)
    )

    return {
        "phrase": entry.phrase,
        "scoring_form": scoring_form(entry),
        "surface_forms": "|".join(sorted(entry.surface_forms)[:5]),
        "sources": "|".join(sorted(entry.sources)),
        "types": "|".join(sorted(entry.types)),
        "pos": "|".join(sorted(entry.pos)),
        "idiom_strength": strength,
        "idiom_r1": "|".join(sorted(entry.idiom_r1)),
        "idiom_source_ids": "|".join(sorted(entry.idiom_source_ids)[:3]),
        "source_rows": str(int(entry.source_rows)),
        "flelex_match": flelex_match,
        "lexical_score": f"{flelex_score.lexical_score:.4f}",
        "frequency_total": f"{flelex_score.freq_total:.4f}",
        "flelex_rarity_score": f"{flelex_score.rarity_score:.4f}",
        "rarity_score": f"{rarity_score:.4f}",
        "cefr_proxy_score": f"{cefr_score:.4f}",
        "semantic_opacity": f"{semantic_opacity:.4f}",
        "structural_complexity": f"{structural_complexity:.4f}",
        "register_score": f"{phrase_register_score:.4f}",
        "construction_fixedness": f"{construction_score:.4f}",
        "idiom_strength_score": f"{idiom_strength_score:.4f}",
        "confidence_idiom_score": f"{confidence_idiom_score:.4f}",
        "type_score": f"{type_score:.4f}",
        "length_score": f"{phrase_length_score:.4f}",
        "confidence_score": f"{confidence_score:.4f}",
        "difficulty_score": f"{difficulty_score:.4f}",
    }


def find_entry(entries: dict[str, PhraseEntry], phrase: str) -> PhraseEntry | None:
    key = normalize(phrase)
    if key in entries:
        return entries[key]
    for entry in entries.values():
        if key in entry.surface_forms:
            return entry
    return None


def sample_entries(entries: dict[str, PhraseEntry]) -> list[PhraseEntry]:
    seed_phrases = [
        "avoir besoin",
        "avoir peur",
        "être en retard",
        "à cause de",
        "au lieu de",
        "en public",
        "bien sûr",
        "tout à fait",
        "a priori",
        "a posteriori",
        "dans l'hypothèse de",
        "de peur de",
        "de manière à ce que",
        "pot-de-vin",
        "bouton-d'or",
        "avoir le coup de foudre",
    ]

    selected: dict[str, PhraseEntry] = {}
    for phrase in seed_phrases:
        entry = find_entry(entries, phrase)
        if entry:
            selected[normalize(entry.phrase)] = entry

    groups = [
        (40, lambda item: item.sources == {"dela"} and "prepositional_phrase" in item.types),
        (40, lambda item: item.sources == {"dela"} and "fixed_expression" in item.types),
        (40, lambda item: item.sources == {"dela"} and "nominal_phrase" in item.types),
        (65, lambda item: item.sources == {"idiom"} and "strong idiom" in item.idiom_strengths),
        (80, lambda item: item.sources == {"idiom"} and "semi-idiom" in item.idiom_strengths),
        (90, lambda item: item.sources == {"idiom"} and "weak idiom" in item.idiom_strengths),
        (100, lambda item: item.sources == {"dela", "idiom"}),
    ]

    for target_count, predicate in groups:
        for entry in sorted(entries.values(), key=lambda item: (len(tokenize(item.phrase)), item.phrase)):
            if len(selected) >= target_count:
                break
            if normalize(entry.phrase) in selected:
                continue
            if predicate(entry):
                selected[normalize(entry.phrase)] = entry

    return list(selected.values())[:100]


def validate_difficulty_ranking(rows: list[dict[str, str]]) -> None:
    by_phrase = {row["phrase"]: float(row["difficulty_score"]) for row in rows}
    checks = [
        ("bien sûr", "appareil photo"),
        ("au lit", "a priori"),
        ("appareil photo", "a priori"),
        ("bien sûr", "bouton-d'or"),
    ]
    missing = sorted({phrase for pair in checks for phrase in pair if phrase not in by_phrase})
    if missing:
        raise RuntimeError(f"Missing difficulty calibration phrase(s): {', '.join(missing)}")
    failed = [
        f"{lower} ({by_phrase[lower]:.4f}) >= {higher} ({by_phrase[higher]:.4f})"
        for lower, higher in checks
        if by_phrase[lower] >= by_phrase[higher]
    ]
    if failed:
        raise RuntimeError("Difficulty calibration failed: " + "; ".join(failed))


def main() -> None:
    flelex = load_flelex()
    entries: dict[str, PhraseEntry] = {}
    load_dela(entries)
    load_idioms(entries)

    rows = [final_score(entry, flelex) for entry in sample_entries(entries)]
    rows.sort(key=lambda row: (float(row["difficulty_score"]), row["phrase"]))
    validate_difficulty_ranking(rows)

    OUT_DIR.mkdir(exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUT_PATH}")


if __name__ == "__main__":
    main()
