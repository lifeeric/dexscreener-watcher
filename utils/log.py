import logging
from typing import Optional


class Logger:
    """Singleton the logger Wrapper."""

    @staticmethod
    def init(name: str) -> "Logger":
        """
        Initialize the logger instance.

        Args:
            name: Name of the logger class

        Returns:
            An instance of Logger class

        Examples:
            >>> logger = Logger.init('MyApp')
            >>> logger.info('Hello world!')
        """

        # Create a logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # Create a file handler
        fh = logging.FileHandler("error.log")
        fh.setLevel(logging.DEBUG)

        # Create a console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # Create a formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)

        return logger
