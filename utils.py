import string
import itertools
import collections
import json
from time import sleep
from talon import clip, resource
from talon.voice import Str, Key, press

# Useful for identifying app/window information for context selection
def context_func(app, win):
    print('---')
    print(app.bundle)
    print(win)
    print(win.title)
    print(win.doc)
    print('---')
    return True

numeral_map = dict((str(n), n) for n in range(0, 20))
for n in range(20, 101, 10):
    numeral_map[str(n)] = n
for n in range(100, 1001, 100):
    numeral_map[str(n)] = n
for n in range(1000, 10001, 1000):
    numeral_map[str(n)] = n
numeral_map["oh"] = 0  # synonym for zero
numeral_map["and"] = None  # drop me

numerals = " (" + " | ".join(sorted(numeral_map.keys())) + ")+"
optional_numerals = " (" + " | ".join(sorted(numeral_map.keys())) + ")*"

# mapping = {
#     "semicolon": ";",
#     "new-line": "\n",
#     "new-paragraph": "\n\n",
#     "yamel": "yaml",
# }

# mapping = json.load(open(os.path.join(os.path.dirname(__file__), "replace_words.json")))

with resource.open('replace_words.json') as f:
    mapping = json.load(f)

mappings = collections.defaultdict(dict)
for k, v in mapping.items():
    mappings[len(k.split(" "))][k] = v

punctuation = set(".,-!?")

# def parse_word(word):
#     word = str(word).lstrip("\\").split("\\", 1)[0].lower()
#     return word

# token_replace =  {   # <-- add this block in std.py
#     'i\\pronoun': 'I',
#     'i\'m': 'I\'m',
#     'i\'ve': 'I\'ve',
#     # 'i\'d': 'I\'d', # etc
# }

def parse_word(word, force_lowercase=True):
    word = str(word).lstrip("\\").split("\\", 1)[0]

    if force_lowercase:
        word = word.lower()
    word = mapping.get(word, word)

    return word

def replace_words(words, mapping, count):
    if len(words) < count:
        return words

    new_words = []
    i = 0
    while i < len(words) - count + 1:
        phrase = words[i : i + count]
        key = " ".join(phrase)
        if key in mapping:
            new_words.append(mapping[key])
            i = i + count
        else:
            new_words.append(phrase[0])
            i = i + 1

    new_words.extend(words[i:])
    return new_words


def parse_words(m, natural=False):
    if isinstance(m, list):
        words = m
    elif hasattr(m, "dgndictation"):
        words = m.dgndictation[0]
    else:
        return []

    # split compound words like "pro forma" into two words.
    words = sum([word.split(" ") for word in words], [])
    words = list(map(lambda current_word: parse_word(current_word, not natural), words))
    words = replace_words(words, mappings[2], 2)
    words = replace_words(words, mappings[3], 3)
    return words


def join_words(words, sep=" "):
    out = ""
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation:
            out += sep
        out += str(word)
    return out

def insert(s):
    Str(s)(None)

def text(m):
    insert(join_words(parse_words(m)).lower())

def spoken_text(m):
    insert(join_words(parse_words(m, True)))


def sentence_text(m):
    raw_sentence = join_words(parse_words(m, True))
    sentence = raw_sentence[0].upper() + raw_sentence[1:]
    insert(sentence)

def word(m):
    try:
        text = join_words(list(map(parse_word, m.dgnwords[0]._words)))
        insert(text.lower())
    except AttributeError:
        pass

def surround(by):
    def func(i, word, last):
        if i == 0:
            word = by + word
        if last:
            word += by
        return word

    return func


def m_to_number(m):
    tmp = [str(s).lower() for s in m._words]
    words = [parse_word(word) for word in tmp]

    result = 0
    factor = 1
    for word in reversed(words):
        if word not in numerals:
            # we consumed all the numbers and only the command name is left.
            break

        result = result + factor * int(numeral_map[word])
        factor = 10 * factor

    return result
