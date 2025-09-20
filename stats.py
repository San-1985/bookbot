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