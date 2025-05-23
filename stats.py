def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
        print(file_contents)

def get_word_count(path_to_file):
    with open(path_to_file) as file:
        return len(file.read().split())

def get_char_count(path_to_file):
    characters = {}
    with open(path_to_file) as file:
        file_contents = file.read()
        words = file_contents.lower().split()
        for word in words:
            chars = list(word)
            for char in chars:
                if char in characters:
                    characters[char] += 1
                else:
                    characters[char] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def dict_into_sorted_list(dict):
    sorted_list = []
    for key,value in dict.items():
        chars = {"char": key, "num": value}
        sorted_list.append(chars)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list