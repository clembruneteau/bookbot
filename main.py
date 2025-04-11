import sys
from stats import (
    get_num_words, 
    get_num_chars, 
    sort_chars_dict
)

def main():
    if len(sys.argv) < 2:
        print_usage()
    
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_chars = sort_chars_dict(num_chars)

    print_report(book_path, num_words, sorted_chars)


def print_usage():
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for item in sorted_chars:
        if item['char'].isalpha():
            print(item['char'] + ": " + str(item['num']))

    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()