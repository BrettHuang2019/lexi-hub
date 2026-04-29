from __future__ import annotations

import json
import os
import time
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Deque, Iterable


Clock = Callable[[], float]


class NoModelAvailable(RuntimeError):
    """Raised when every configured model has reached its current limit."""


@dataclass(frozen=True)
class ModelLimit:
    model: str
    rpm: int
    category: str | None = None
    tpm: int | str | None = None
    rpd: int | None = None

    window_seconds: float = 60.0

    @classmethod
    def from_dict(cls, value: dict[str, object]) -> "ModelLimit":
        model = str(value["model"])
        rpm = int(value["rpm"])
        category = value.get("category")
        tpm = value.get("tpm")
        rpd_value = value.get("rpd")
        rpd = int(rpd_value) if rpd_value is not None else None

        if not model:
            raise ValueError("model name must not be empty")
        if rpm <= 0:
            raise ValueError(f"{model}: rpm must be greater than zero")

        return cls(
            model=model,
            rpm=rpm,
            category=str(category) if category is not None else None,
            tpm=tpm,
            rpd=rpd,
        )


class GeminiBalancer:
    def __init__(
        self,
        models: Iterable[ModelLimit],
        *,
        client: Any | None = None,
        clock: Clock = time.monotonic,
    ) -> None:
        self.models = list(models)
        if not self.models:
            raise ValueError("at least one model must be configured")

        self.client = client or _build_client()
        self.clock = clock
        self._calls: dict[str, Deque[float]] = {
            model.model: deque() for model in self.models
        }

    @classmethod
    def from_config_file(
        cls,
        path: str | Path = "config.json",
        *,
        client: Any | None = None,
        clock: Clock = time.monotonic,
    ) -> "GeminiBalancer":
        config_path = Path(path)
        data = json.loads(config_path.read_text(encoding="utf-8"))
        raw_models = data["models"] if isinstance(data, dict) else data
        models = [ModelLimit.from_dict(item) for item in raw_models]
        return cls(models, client=client, clock=clock)

    def next_model(self) -> str:
        now = self.clock()

        for model in self.models:
            calls = self._calls[model.model]
            self._drop_expired(calls, now, model.window_seconds)
            if len(calls) < model.rpm:
                calls.append(now)
                return model.model

        retry_after = self.retry_after()
        raise NoModelAvailable(
            f"all models are rate limited; retry after {retry_after:.2f} seconds"
        )

    def retry_after(self) -> float:
        now = self.clock()
        waits: list[float] = []

        for model in self.models:
            calls = self._calls[model.model]
            self._drop_expired(calls, now, model.window_seconds)
            if len(calls) < model.rpm:
                return 0.0
            waits.append(model.window_seconds - (now - calls[0]))

        return max(0.0, min(waits))

    def generate_content(self, contents: str):
        model = self.next_model()
        return self.client.models.generate_content(model=model, contents=contents)

    @staticmethod
    def _drop_expired(
        calls: Deque[float], now: float, window_seconds: float
    ) -> None:
        while calls and now - calls[0] >= window_seconds:
            calls.popleft()


def load_dotenv(path: str | Path = ".env") -> None:
    env_path = Path(path)
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def _build_client() -> Any:
    try:
        from google import genai
    except ImportError as exc:
        raise RuntimeError(
            "google-genai is not installed. Run `pip install -e .` first."
        ) from exc

    return genai.Client()
