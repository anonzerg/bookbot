import logging
import sys

from pathlib import Path

from librarian import (
    number_of_words,
)

def get_book_text(book_path):
    with open(book_path) as book:
        book_text = book.read()

    return book_text

def main() -> None:
    
    book_path = Path("./books/frankenstein_or_the_modern_prometheus.txt")
    book_text = get_book_text(book_path)
    num_of_words = number_of_words(book_text)

    logger.info(f"found {num_of_words} words in {book_path.stem}")

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
