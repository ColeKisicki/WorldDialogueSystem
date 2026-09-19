"""Secrets management helpers.

Centralizes access to API keys and other sensitive values so that:
  * Secrets are read from a single place (the `Settings` object).
  * Missing secrets raise a clear, actionable error.
  * Secret values are never accidentally logged.
"""

from __future__ import annotations

from world_dialogue_system.config import settings


class MissingSecretError(RuntimeError):
    """Raised when a required secret is not configured."""


def get_secret(name: str, *, required: bool = True) -> str | None:
    """Return a secret by its settings attribute name.

    Args:
        name: The attribute name on `Settings` (e.g. ``"openai_api_key"``).
        required: If True, raise `MissingSecretError` when the value is unset.

    Returns:
        The secret value, or ``None`` if unset and `required` is False.
    """
    value = getattr(settings, name, None)
    if required and not value:
        raise MissingSecretError(
            f"Secret '{name}' is not set. Add it to your `.env` file."
        )
    return value
