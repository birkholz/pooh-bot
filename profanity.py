import os
import re

profane_words = None


def get_profanity():
    if not profane_words:
        current_dir = os.path.abspath(os.path.dirname(__file__))
        f = open(os.path.join(current_dir, 'wordlist.txt'))
        global profane_words
        profane_words = [w.strip() for w in f.readlines() if w]
        profane_words.pop(0) # Remove header line
    return profane_words


def contains_profanity(input_text):
    words = get_profanity()
    for word in words:
        swear_word = re.compile(r'\b%s\b' % word, re.I)
        if swear_word.search(input_text):
            return True
    return False
