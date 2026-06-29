"""
OPG Core Logger.

Official logging foundation for OPG.

Rules:
- No Blender dependency.
- No external dependency.
- No duplicated handlers.
- Stable log format.
"""

import logging
from typing import Optional


DEFAULT_LOGGER_NAME = "opg"
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = "[%(levelname)s] %(name)s: %(message)s"


class LoggerFactory:
    """
    Creates and configures OPG loggers.

    This factory centralizes logger creation and prevents duplicated handlers.
    """

    _configured = False
    _level = DEFAULT_LOG_LEVEL
    _format = DEFAULT_LOG_FORMAT

    @classmethod
    def configure(
        cls,
        level: int = DEFAULT_LOG_LEVEL,
        log_format: str = DEFAULT_LOG_FORMAT,
    ) -> None:
        """
        Configure the root OPG logger.

        Args:
            level: Standard logging level.
            log_format: Logging format string.
        """
        cls._level = level
        cls._format = log_format

        logger = logging.getLogger(DEFAULT_LOGGER_NAME)
        logger.setLevel(level)
        logger.propagate = False

        if not logger.handlers:
            handler = logging.StreamHandler()
            logger.addHandler(handler)

        for handler in logger.handlers:
            handler.setLevel(level)
            handler.setFormatter(logging.Formatter(log_format))

        cls._configured = True

    @classmethod
    def get_logger(cls, name: Optional[str] = None) -> logging.Logger:
        """
        Return an OPG logger.

        Args:
            name: Optional namespace suffix.
                  Example: "core" returns logger "opg.core".

        Returns:
            Configured logging.Logger instance.
        """
        if not cls._configured:
            cls.configure()

        if name is None or not name.strip():
            return logging.getLogger(DEFAULT_LOGGER_NAME)

        if name.startswith(DEFAULT_LOGGER_NAME):
            logger_name = name
        else:
            logger_name = f"{DEFAULT_LOGGER_NAME}.{name}"

        logger = logging.getLogger(logger_name)
        logger.setLevel(cls._level)
        logger.propagate = True

        return logger


def configure_logging(
    level: int = DEFAULT_LOG_LEVEL,
    log_format: str = DEFAULT_LOG_FORMAT,
) -> None:
    """
    Configure OPG logging.
    """
    LoggerFactory.configure(level=level, log_format=log_format)


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Return an OPG logger.
    """
    return LoggerFactory.get_logger(name)