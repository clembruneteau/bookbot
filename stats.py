   
def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars = dict()
    for char in text.lower():
        if char not in chars.keys():
            chars[char] = 1
        else:
            chars.update({char: chars[char]+1})
    
    return chars

def sort_on(dict):
    return dict["num"]

def sort_chars_dict(chars_dict):
    dict_list = []

    for char, num in chars_dict.items():
        dict_list.append({"char": char, "num": num})
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
