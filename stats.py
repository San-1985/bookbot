def get_word_count(file):
    with open(file) as f:
        text = f.read()
    words = text.split()
    return len(words)
