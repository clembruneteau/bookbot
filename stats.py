    
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