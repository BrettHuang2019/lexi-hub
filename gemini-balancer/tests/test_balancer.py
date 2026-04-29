from gemini_balancer import GeminiBalancer, ModelLimit, NoModelAvailable


class FakeModels:
    def __init__(self) -> None:
        self.calls = []

    def generate_content(self, *, model: str, contents: str):
        self.calls.append((model, contents))
        return type("Response", (), {"text": f"{model}: {contents}"})()


class FakeClient:
    def __init__(self) -> None:
        self.models = FakeModels()


def test_uses_first_model_until_limit_then_next_model():
    now = 0.0
    client = FakeClient()
    balancer = GeminiBalancer(
        [
            ModelLimit("first", rpm=1),
            ModelLimit("second", rpm=1),
        ],
        client=client,
        clock=lambda: now,
    )

    assert balancer.generate_content("one").text == "first: one"
    assert balancer.generate_content("two").text == "second: two"
    assert client.models.calls == [("first", "one"), ("second", "two")]


def test_reuses_model_after_window_expires():
    now = 0.0
    balancer = GeminiBalancer(
        [ModelLimit("first", rpm=1)],
        client=FakeClient(),
        clock=lambda: now,
    )

    assert balancer.next_model() == "first"
    now = 60.0

    assert balancer.next_model() == "first"


def test_raises_when_all_models_are_limited():
    now = 10.0
    balancer = GeminiBalancer(
        [ModelLimit("first", rpm=1)],
        client=FakeClient(),
        clock=lambda: now,
    )

    assert balancer.next_model() == "first"

    try:
        balancer.next_model()
    except NoModelAvailable as exc:
        assert "retry after 60.00 seconds" in str(exc)
    else:
        raise AssertionError("expected NoModelAvailable")
