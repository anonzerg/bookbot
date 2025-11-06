import logging
import sys


def main() -> None:
    return None


if __name__ == "__main__":
    logging.basicConfig(
        format="[%(levelname)s] %(message)s",
        level=logging.INFO
    )
    logger = logging.getLogger(__name__)

    try:
        main()
    except Exception as e:
        logger.error(e)
        sys.exit(1)
