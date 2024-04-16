def main():
    book_contents = get_book_text("./books/frankenstein.txt")

    report(book_contents)
    
def get_word_count(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(book):
    book_as_list = list(book.lower())
    character_count = {}
    list_of_character_dicts = []

    for character in book_as_list:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1

    for key, value in character_count.items():
        character_dict = {}
        character_dict['character'] = key
        character_dict['count'] = value
        list_of_character_dicts.append(character_dict)

    return sorted(list_of_character_dicts, key=lambda i: i['count'])
        

def report(book):
    word_count = get_word_count(book)
    print(f"{word_count} words found inm the document\n")

    character_count = get_character_count(book)
    
    for character in character_count:
        print(f"the '{character['character']}' character was found {character['count']} times")

    

main()
