def number_of_words(text):
    words = text.split()
    return len(words)


def char_count(text):
    chars = list(text)
    char_lib = {}

    for char in chars:
        char = char.lower()
        if char in char_lib:
            char_lib[char] += 1
        else:
            char_lib[char] = 1

    return char_lib

def sort_helper(items):
    return items["num"]

def sorted_libs(char_count_lib):
    char_list = []
    
    for char, count in char_count_lib.items():
        char_list.append({"char": char, "num": count})
        char_list.sort(reverse=True, key=sort_helper)
    
    return char_list