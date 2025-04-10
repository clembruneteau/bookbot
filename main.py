from stats import (
    get_num_words, 
    get_num_chars, 
    sort_chars_dict
)

def main():
    book_path = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)
    num_words = get_num_words(text)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    num_chars = get_num_chars(text)
    sorted_chars = sort_chars_dict(num_chars)

    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(item["char"] + ": " + str(item["num"]))

    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()