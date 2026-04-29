from __future__ import annotations

import argparse
import sys
import time

from .balancer import GeminiBalancer, NoModelAvailable, load_dotenv


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Call Gemini using the first configured model with capacity."
    )
    parser.add_argument("prompt", help="Prompt to send to Gemini.")
    parser.add_argument(
        "--config",
        default="config.json",
        help="Path to JSON config file. Defaults to config.json.",
    )
    parser.add_argument(
        "--wait",
        action="store_true",
        help="Wait until a model has capacity instead of failing fast.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    load_dotenv()
    balancer = GeminiBalancer.from_config_file(args.config)

    while True:
        try:
            response = balancer.generate_content(args.prompt)
            print(response.text)
            return 0
        except NoModelAvailable as exc:
            if not args.wait:
                print(str(exc), file=sys.stderr)
                return 2
            time.sleep(balancer.retry_after())


if __name__ == "__main__":
    raise SystemExit(main())
