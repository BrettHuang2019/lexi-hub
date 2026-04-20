from __future__ import annotations

from collections.abc import Callable
from typing import Any

DEFAULT_PROCESSORS = "tokenize,mwt,pos,lemma,depparse,ner"


class StanzaUnavailableError(RuntimeError):
    """Raised when Stanza is not installed but a real pipeline is requested."""


class FrenchAnalyzer:
    def __init__(
        self,
        *,
        pipeline: Callable[[str], Any] | None = None,
        processors: str = DEFAULT_PROCESSORS,
        download: bool = False,
    ) -> None:
        self._pipeline = pipeline
        self._processors = processors
        self._download = download

    def analyze(self, sentence: str) -> Any:
        sentence = sentence.strip()
        if not sentence:
            raise ValueError("sentence must not be empty")

        document = self._get_pipeline()(sentence)
        return serialize_document(document)

    def _get_pipeline(self) -> Callable[[str], Any]:
        if self._pipeline is None:
            self._pipeline = build_french_pipeline(
                processors=self._processors,
                download=self._download,
            )
        return self._pipeline


def analyze_sentence(
    sentence: str,
    *,
    pipeline: Callable[[str], Any] | None = None,
    processors: str = DEFAULT_PROCESSORS,
    download: bool = False,
) -> Any:
    analyzer = FrenchAnalyzer(
        pipeline=pipeline,
        processors=processors,
        download=download,
    )
    return analyzer.analyze(sentence)


def build_french_pipeline(
    *,
    processors: str = DEFAULT_PROCESSORS,
    download: bool = False,
) -> Callable[[str], Any]:
    try:
        import stanza
    except ImportError as exc:
        raise StanzaUnavailableError(
            "Stanza is required. Install this project with `python -m pip install -e .`."
        ) from exc

    if download:
        stanza.download("fr", processors=processors)

    return stanza.Pipeline(
        lang="fr",
        processors=processors,
        use_gpu=False,
        verbose=False,
    )


def serialize_document(document: Any) -> Any:
    if hasattr(document, "to_dict"):
        return document.to_dict()

    return {
        "text": getattr(document, "text", None),
        "sentences": [_serialize_sentence(sentence) for sentence in document.sentences],
        "entities": [_serialize_entity(entity) for entity in getattr(document, "ents", [])],
    }


def _serialize_sentence(sentence: Any) -> dict[str, Any]:
    return {
        "text": getattr(sentence, "text", None),
        "tokens": [_serialize_token(token) for token in getattr(sentence, "tokens", [])],
        "words": [_serialize_word(word) for word in getattr(sentence, "words", [])],
        "dependencies": [
            {
                "governor": _word_ref(governor),
                "relation": relation,
                "dependent": _word_ref(dependent),
            }
            for governor, relation, dependent in getattr(sentence, "dependencies", [])
        ],
    }


def _serialize_token(token: Any) -> dict[str, Any]:
    return {
        "id": getattr(token, "id", None),
        "text": getattr(token, "text", None),
        "misc": getattr(token, "misc", None),
        "start_char": getattr(token, "start_char", None),
        "end_char": getattr(token, "end_char", None),
        "ner": getattr(token, "ner", None),
    }


def _serialize_word(word: Any) -> dict[str, Any]:
    return {
        "id": getattr(word, "id", None),
        "text": getattr(word, "text", None),
        "lemma": getattr(word, "lemma", None),
        "upos": getattr(word, "upos", None),
        "xpos": getattr(word, "xpos", None),
        "feats": getattr(word, "feats", None),
        "head": getattr(word, "head", None),
        "deprel": getattr(word, "deprel", None),
        "start_char": getattr(word, "start_char", None),
        "end_char": getattr(word, "end_char", None),
    }


def _serialize_entity(entity: Any) -> dict[str, Any]:
    return {
        "text": getattr(entity, "text", None),
        "type": getattr(entity, "type", None),
        "start_char": getattr(entity, "start_char", None),
        "end_char": getattr(entity, "end_char", None),
    }


def _word_ref(word: Any) -> dict[str, Any]:
    return {
        "id": getattr(word, "id", None),
        "text": getattr(word, "text", None),
    }
