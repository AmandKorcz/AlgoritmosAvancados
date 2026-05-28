import logging
import sys


def configure_logging() -> None:
    """Configura logs estruturados simples para a aplicação."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
