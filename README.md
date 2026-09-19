# WorldDialogueSystem

A Python project for a world dialogue system.

## Project structure

```
WorldDialogueSystem/
├── main.py                          # Entry point
├── requirements.txt                 # Dependencies
├── pyproject.toml                   # Tooling config (ruff, mypy, pytest)
├── .env                             # Local secrets (gitignored)
├── world_dialogue_system/           # Main package
│   ├── __init__.py
│   ├── config.py                    # Typed settings (pydantic-settings)
│   ├── secrets.py                   # API key / secret access helpers
│   ├── logging_config.py            # Logging setup (loguru)
│   ├── models/                      # Domain models
│   ├── services/                    # Business logic & external integrations
│   └── utils/                       # Shared helpers
└── tests/                           # Test suite (pytest)
```

## Setup

1. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate

   pip install -r requirements.txt
   ```

2. Configure secrets in `.env` (gitignored — never commit it).

3. Run the application:

   ```bash
   python main.py
   ```

## Configuration & secrets

- All settings live in `world_dialogue_system/config.py` (`Settings` class) and
  are loaded from environment variables / `.env`.
- Access secrets through `world_dialogue_system/secrets.py`:
  `get_secret("name")` returns a secret or raises `MissingSecretError`.
- Add new settings by adding a field to `Settings` and a matching entry in
  `.env`.

## Testing & linting

```bash
pytest                 # run tests
ruff check .           # lint
ruff format .          # format
mypy world_dialogue_system  # type check
```
