# Gemini Balancer

A small Python CLI and library that spreads Gemini API calls across configured models based on per-model request limits.

## Setup

Install dependencies:

```powershell
pip install -e .
```

Create `.env` with your API key:

```env
GEMINI_API_KEY=your_key_here
```

Edit `config.json` to change the model limits. The balancer uses `rpm` as the
number of requests allowed per model per minute. TPM and RPD are included as
config metadata.

```json
[
  {
    "model": "gemini-3.1-flash-lite-preview",
    "category": "Text-out",
    "rpm": 15,
    "tpm": 250000,
    "rpd": 500
  }
]
```

## Usage

Send one prompt:

```powershell
gemini-balancer "Explain how AI works in a few words"
```

Use a custom config:

```powershell
gemini-balancer --config config.json "Write a short haiku"
```

From Python:

```python
from gemini_balancer import GeminiBalancer

balancer = GeminiBalancer.from_config_file("config.json")
response = balancer.generate_content("Explain how AI works in a few words")
print(response.text)
```

The balancer keeps rate-limit state in memory. Restarting the process resets local counters.
