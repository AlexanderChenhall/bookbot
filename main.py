import re
import string
def main():
    path_to_file = "books/frankenstein.txt"
    book_name = get_book_name(path_to_file)
    print(f"There are {get_number_of_words_in_book(path_to_file)} in the book {book_name}.")
    print(get_letter_count(path_to_file))

def get_book_name(path_to_file):
    separated_text = re.split(r'\W+', path_to_file)
    for x, elem in enumerate(separated_text):
        if elem == "books" or elem == "txt":
            separated_text.pop(x)
    separated_text = ' '.join(separated_text)
    capitalized_book_name = string.capwords(separated_text)
    return capitalized_book_name

def print_book(path_to_file):
    with open(path_to_file) as file:
        book_text = file.read()
        return(book_text)

def get_letter_count(path_to_file):
    letter_occurances = {letter: 0 for letter in string.ascii_lowercase}
    book_text = print_book(path_to_file)
    split_text = re.split(r'\W*', book_text)
    split_text_lowercase = [letter.lower() for letter in split_text if letter]
    alphabet = list(string.ascii_lowercase)
    for x, elem in enumerate(split_text_lowercase):
        if elem not in alphabet:
            pass
        else:
            letter_occurances[elem] += 1
    return letter_occurances

def get_number_of_words_in_book(path_to_file):
    book_text = print_book(path_to_file)
    separated_text = book_text.split()
    return len(separated_text)

if __name__ == "__main__":
    main()