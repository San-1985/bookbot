def get_text(file):
    with open(file) as f:
        text = f.read()
    return text

def get_word_count(text):
    
    words = text.split()
    return len(words)

def get_char_count(text):
    
    char_count = {}
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

def sort_dict(d):
    char_list = []
    for k, v in d.items():
        char_d = {"char": k, "num": v}
        char_list.append(char_d)
    def sort_on(items):
        return items["num"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list