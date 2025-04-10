def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    print(f"{num_words} words found in the document")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def number_of_words(text):
    words = text.split()
    return len(words)

main()