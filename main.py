import logging
import sys

from pathlib import Path

from librarian import (
    number_of_words,
    number_of_each_char,
    sort_dict,
)

def get_book_text(book_path):
    with open(book_path) as book:
        book_text = book.read()

    return book_text

def usage():
    logger.error(f"python3 {sys.argv[0]} <book>.")
    sys.exit(1)

def main() -> None:
    if len(sys.argv) != 2:
        usage()
    
    book_path = Path(sys.argv[1])
    book_text = get_book_text(book_path)
    num_of_words = number_of_words(book_text)
    num_each_char = number_of_each_char(book_text)
    
    logger.info(f"found {num_of_words} words in {book_path.stem}")
    for e in sort_dict(num_each_char):
        print(f"{e["char"]}: {e["num"]}")

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
