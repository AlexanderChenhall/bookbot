import re
import string
def main():
    path_to_file = "books/frankenstein.txt"
    generate_report(path_to_file)


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

def get_sorted_list_from_dict(letter_occurances):
    sorted_list = sorted(letter_occurances.items(), key=lambda item: item[1], reverse=True)
    return sorted_list

def generate_report(path_to_file):
    book_name = get_book_name(path_to_file)
    sorted_list = get_sorted_list_from_dict(get_letter_count(path_to_file))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"There are {get_number_of_words_in_book(path_to_file)} in the book {book_name}.")
    print(list_letter_occurances(sorted_list))

def list_letter_occurances(letter_occurances):
    report_list = ("\nLetters in order of occurance:\n")
    for elem in letter_occurances:
        report_list += (f"The '{elem[0]}' character occurs {elem[1]} times\n")
    return report_list

if __name__ == "__main__":
    main()