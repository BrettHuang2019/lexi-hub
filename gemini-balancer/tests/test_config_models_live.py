import json
import time
from datetime import datetime, timezone
from pathlib import Path

from gemini_balancer.balancer import ModelLimit, load_dotenv


PROMPT = "tell me a joke"
CONFIG_PATH = Path("config.json")
REPORT_PATH = Path("model_report.json")


def test_every_configured_model_responds_once():
    load_dotenv()

    from google import genai

    raw_config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    raw_models = raw_config["models"] if isinstance(raw_config, dict) else raw_config
    models = [ModelLimit.from_dict(item) for item in raw_models]
    client = genai.Client()
    results = []

    for model in models:
        started = time.perf_counter()
        result = {
            "model": model.model,
            "prompt": PROMPT,
            "ok": False,
            "duration_seconds": None,
            "reply": None,
            "error": None,
        }

        try:
            response = client.models.generate_content(
                model=model.model,
                contents=PROMPT,
            )
            result["ok"] = True
            result["reply"] = getattr(response, "text", None)
        except Exception as exc:
            result["error"] = f"{type(exc).__name__}: {exc}"
        finally:
            result["duration_seconds"] = round(time.perf_counter() - started, 3)
            results.append(result)

    report = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "config": str(CONFIG_PATH),
        "prompt": PROMPT,
        "results": results,
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2), encoding="utf-8")

    failures = [result for result in results if not result["ok"]]
    assert not failures, f"{len(failures)} configured model(s) failed; see {REPORT_PATH}"
