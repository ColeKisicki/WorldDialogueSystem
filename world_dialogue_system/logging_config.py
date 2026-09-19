"""Logging configuration.

Sets up a single, consistent logging configuration for the whole application
using `loguru`. Call `setup_logging()` once at startup (e.g. from `main.py`).
"""

from __future__ import annotations

import sys

from loguru import logger

from world_dialogue_system.config import settings


def setup_logging() -> None:
    """Configure application-wide logging."""
    logger.remove()  # Remove the default handler.

    logger.add(
        sys.stderr,
        level=settings.log_level,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan> | "
            "<level>{message}</level>"
        ),
        colorize=True,
    )

    logger.debug("Logging configured (level={})", settings.log_level)
