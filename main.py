import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(get_usage(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_usage(text):
    alphabet = list(string.ascii_lowercase)
    usage = {}
    for letter in text:
        letter = letter.lower()
        if letter in alphabet:
            if letter in usage:
                usage[letter] += 1
            else:
                usage[letter] = 1
    return usage


main()