def main():
    print_report("frankenstein.txt")
    
def read_file(file):
    with open("./books/" + file) as f:
        file_contents = f.read()

    return file_contents

def count_words(text):
    word_list = text.split(" ")
    return len(word_list)

def count_characters(text):
    character_count = {}

    for character in text.lower():
        if character in character_count.keys():
            character_count[character] += 1
        else:
            character_count[character] = 0

    return character_count

def print_report(book):
    book_text = read_file(book)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)

    print(f"--- Begin Report of { book } ---\n")
    for character, count in character_count.items():
        print(f"The { character } character was found { count } times")
    print("--- End Report ---")
    

main()

