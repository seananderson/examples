from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import ctrl, clip
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string

# alpha_alt = 'air bat cap drum each fine gust harp sit jury crunch look made near odd pit quench red sun trap urge vest whale plex yank zip'.split()

alpha_alt = 'arch bravo char dilbert echo fox golf hotel ice juliet kilo lug mike nerb ork pooch queen romeo souk tango unk victor whiskey x-ray yankee zulu'.split()

###
alnum = list(zip(alpha_alt, string.ascii_lowercase)) + [(str(i), str(i)) for i in range(0, 10)]

alpha = {}
alpha.update(dict(alnum))
alpha.update({'sky %s' % word: letter for word, letter in zip(alpha_alt, string.ascii_uppercase)})

# modifier key mappings
fkeys = [(f'F {i}', f'f{i}') for i in range(1, 13)]
keys = [
    'left', 'right', 'up', 'down', 'shift', 'tab', 'escape', 'enter', 'space',
    'backspace', 'delete', 'home', 'pageup', 'pagedown', 'end',
]
keys = alnum + [(k, k) for k in keys]
keys += [
    ('tilde', '`'),
    ('comma', ','),
    ('dot', '.'),
    ('slash', '/'),
    ('(semi | semicolon)', ';'),
    ('quote', "'"),
    ('lack', '['),
    ('rack', ']'),
    ('backslash', '\\'),
    ('minus', '-'),
    ('equals', '='),
] + fkeys
alpha.update({word: Key(key) for word, key in fkeys})
alpha.update({'control %s' % k: Key('ctrl-%s' % v) for k, v in keys})
alpha.update({'control shift %s' % k: Key('ctrl-shift-%s' % v) for k, v in keys})
alpha.update({'control alt %s' % k: Key('ctrl-alt-%s' % v) for k, v in keys})
alpha.update({'(command | cod) %s' % k: Key('cmd-%s' % v) for k, v in keys})
alpha.update({'(command | cod) shift %s' % k: Key('cmd-shift-%s' % v) for k, v in keys})
alpha.update({'(command | cod) alt shift %s' % k: Key('cmd-alt-shift-%s' % v) for k, v in keys})
alpha.update({'alt %s' % k: Key('alt-%s' % v) for k, v in keys})
alpha.update({'alt shift %s' % k: Key('alt-%s' % v) for k, v in keys})

numerals = {
    'ten': '10',
    'eleven': '11',
    'twelve': '12',
    'thirteen': '13',
    'fourteen': '14',
    'fifteen': '15',
    'sixteen': '16',
    'seventeen': '17',
    'eighteen': '18',
    'nineteen': '19',
    'twenty': '20',
    'thirty': '30',
    'forty': '40',
    'fifty': '50',
    'sixty': '60',
    'seventy': '70',
    'eighty': '80',
    'ninety': '90',
}

alpha.update(numerals)

# cleans up some Dragon output from <dgndictation>
mapping = {
    'semicolon': ';',
    'new-line': '\n',
    'new-paragraph': '\n\n',
}
# used for auto-spacing
punctuation = set('.,-!?')

def CursorText(s):
  left, right = s.split('{.}', 1)
  return [left + right, Key(' '.join(['left'] * len(right)))]

def parse_word(word):
    word = str(word).lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word

def join_words(words, sep=' '):
    out = ''
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation:
            out += sep
        out += word
    return out

def parse_words(m):
    return list(map(parse_word, m.dgndictation[0]._words))

def insert(s):
    Str(s)(None)

def text(m):
    insert(join_words(parse_words(m)).lower())

def sentence_text(m):
    text = join_words(parse_words(m)).lower()
    insert(text.capitalize())

def word(m):
    text = join_words(list(map(parse_word, m.dgnwords[0]._words)))
    insert(text.lower())

def surround(by):
    def func(i, word, last):
        if i == 0: word = by + word
        if last: word += by
        return word
    return func

formatters = {
    'camel':  (True,  lambda i, word, _: word if i == 0 else word.capitalize()),
    'score':  (True,  lambda i, word, _: word if i == 0 else '_'+word),
    'jumble':  (True,  lambda i, word, _: word),
    'shash':  (True,  lambda i, word, _: word),
    'hyphenate':  (True,  lambda i, word, _: word if i == 0 else '-'+word),
    'titlecase':  (False, lambda i, word, _: word.capitalize()),
    'uppercase': (False, lambda i, word, _: word.upper()),
    'string': (False, surround('"')),
    'single-string': (False, surround("'")),
    'padded': (False, surround(" ")),
    # https://github.com/lexjacobs/talon_user/blob/master/std.py for the next set:
    'pathway':  (True, lambda i, word, _: word if i == 0 else '/'+word),
    'dot-case':  (True, lambda i, word, _: word if i == 0 else '.'+word),
    'thrack': (True, lambda i, word, _: word[0:3]), # first 3 letters of word
    'quattro': (True, lambda i, word, _: word[0:4]), # first 4 letters of word
}

def FormatText(m):
    fmt = []
    for w in m._words:
        if isinstance(w, Word):
            fmt.append(w.word)
    try:
        words = parse_words(m)
    except AttributeError:
        with clip.capture() as s:
            press('cmd-c')
        words = s.get().split(' ')
        if not words:
            return

    tmp = []
    spaces = True
    for i, word in enumerate(words):
        word = parse_word(word)
        for name in reversed(fmt):
            smash, func = formatters[name]
            word = func(i, word, i == len(words)-1)
            spaces = spaces and not smash
        tmp.append(word)
    words = tmp

    sep = ' '
    if not spaces:
        sep = ''
    Str(sep.join(words))(None)

ctx = Context('input')

keymap = {}
keymap.update(alpha)
keymap.update({
    'say <dgndictation> [over]': text,

    'cap <dgndictation> [over]': sentence_text,
    'comma <dgndictation> [over]': [', ', text],
    'period <dgndictation> [over]': ['. ', sentence_text],
    'more <dgndictation> [over]': [' ', text],
    'word <dgnwords>': word,

    '(%s)+ [<dgndictation>]' % (' | '.join(formatters)): FormatText,

    'tab':   Key('tab'),
    'left':  Key('left'),
    'right': Key('right'),
    'up':    Key('up'),
    'down':  Key('down'),

    'chuck': Key('backspace'),

    'slap': [Key('cmd-right enter')],
    'enter': Key('enter'),
    'escape | scape': Key('esc'),
    'quest mark': '?',
    'tilde': '~',
    '(bang | exclamation [mark])': '!',
    'dollar': '$',
    'underscore': '_',
    '(semi | semicolon)': ';',
    'colon': ':',
    'lack': '[',
    'rack': ']',
    'lap': '(',
    'rap': ')',
    'lace': '{',
    'race': '}',
    'langle': '<',
    'rangle': '>',

    'asterisk': '*',
    'hash': '#',
    'percent [sign]': '%',
    'caret': '^',
    'at sign': '@',
    'ampersand': '&',
    '(vertical bar | or sign | pipe)': '|',

    '(dubquote | double quote)': '"',
    'quote': "'",
    # 'triple quote': "'''",
    '(dot | period)': '.',
    'comma': ',',
    'space': ' ',
    'slash': '/',
    'backslash': '\\',

    '(dot dot | dotdot)': '..',
    '(dot dot dot | dotdotdot)': '...',
    'cd': 'cd ',
    'cd talon home': 'cd {}'.format(TALON_HOME),
    'cd talon user': 'cd {}'.format(TALON_USER),
    'cd talon plugins': 'cd {}'.format(TALON_PLUGINS),

    'run make (durr | dear)': 'mkdir ',
    'run get': 'git ',
    'run get (R M | remove)': 'git rm ',
    'run get add': 'git add ',
    'run get bisect': 'git bisect ',
    'run get branch': 'git branch ',
    'run get checkout': 'git checkout ',
    'run get clone': 'git clone ',
    'run get commit': 'git commit ',
    'run get diff': 'git diff ',
    'run get fetch': 'git fetch ',
    'run get grep': 'git grep ',
    'run get in it': 'git init ',
    'run get log': 'git log ',
    'run get merge': 'git merge ',
    'run get move': 'git mv ',
    'run get pull': 'git pull ',
    'run get push': 'git push ',
    'run get rebase': 'git rebase ',
    'run get reset': 'git reset ',
    'run get show': 'git show ',
    'run get status': 'git status \n',
    'run get tag': 'git tag ',
    'run (them | vim)': 'vim ',
    'run (L S | ellis)': 'ls\n',
    'dot pie': '.py',
    'dot R': '.R',
    'dot C P P': '.cpp',
    'dot Stan': '.stan',
    'run make': 'make\n',
    # 'run jobs': 'jobs\n',

#    'const': 'const ',
#    'static': 'static ',
#    'tip pent': 'int ',
#    'tip char': 'char ',
#    'tip byte': 'byte ',
#    'tip pent 64': 'int64_t ',
#    'tip you went 64': 'uint64_t ',
#    'tip pent 32': 'int32_t ',
#    'tip you went 32': 'uint32_t ',
#    'tip pent 16': 'int16_t ',
#    'tip you went 16': 'uint16_t ',
#    'tip pent 8': 'int8_t ',
#    'tip you went 8': 'uint8_t ',
#    'tip size': 'size_t',
#    'tip float': 'float ',
#    'tip double': 'double ',

    'args': ['()', Key('left')],
    'index': ['[]', Key('left')],
    # 'block': [' {}', Key('left enter enter up tab')],
    # 'empty array': '[]',
    # 'empty dict': '{}',

    # 'state (def | deaf | deft)': 'def ',
    # 'state else if': 'elif ',
    'state if': 'if ',
    'state else if': [' else if ()', Key('left')],
    'state while': ['while ()', Key('left')],
    'state for': ['for ()', Key('left')],
    # 'state for': 'for ',
    'state switch': ['switch ()', Key('left')],
    # 'state case': ['case \nbreak;', Key('up')],
    # 'state goto': 'goto ',
    # 'state import': 'import ',
    # 'state class': 'class ',

    # 'state include': '#include ',
    # 'state include system': ['#include <>', Key('left')],
    # 'state include local': ['#include ""', Key('left')],
    # 'state type deaf': 'typedef ',
    # 'state type deaf struct': ['typedef struct {\n\n};', Key('up'), '\t'],

    'comment see': '// ',
    'comment are': '# ',

    'word queue': 'queue',
    'word eye': 'eye',
    # 'word bson': 'bson',
    # 'word iter': 'iter',
    'word no': 'NULL',
    'word cmd': 'cmd',
    # 'word dup': 'dup',
    # 'word streak': ['streq()', Key('left')],
    # 'word printf': 'printf',
    # 'word (dickt | dictionary)': 'dict',
    # 'word shell': 'shell',

    # 'word lunixbochs': 'lunixbochs',
    'word talon': 'talon',
    # 'word Point2d': 'Point2d',
    # 'word Point3d': 'Point3d',
    # 'title Point': 'Point',
    'word angle': 'angle',

    # 'dunder in it': '__init__',
    # 'self taught': 'self.',
    # 'dickt in it': ['{}', Key('left')], # FIXME redefine
    # 'list in it': ['[]', Key('left')], # FIXME redefine
    # 'string utf8': "'utf8'",
    # 'state past': 'pass',

    'equals': '=',
    '(minus | dash)': '-',
    'plus': '+',
    'arrow': '->',
    'call': '()',
    'indirect': '&',
    'dereference': '*',
    '(op equals | assign)': ' = ',
    'op (minus | subtract)': ' - ',
    'op (plus | add)': ' + ',
    'op (times | multiply | asterisk)': ' * ',
    'op divide': ' / ',
    'op mod': ' % ',
    '[op] (minus | subtract) equals': ' -= ',
    '[op] (plus | add) equals': ' += ',
    '[op] (times | multiply) equals': ' *= ',
    '[op] divide equals': ' /= ',
    '[op] mod equals': ' %= ',

    '(op | is) greater [than]': ' > ',
    '(op | is) less [than]': ' < ',
    '(op | is) equal': ' == ',
    '(op | is) not equal': ' != ',
    '(op | is) greater [than] or equal': ' >= ',
    '(op | is) less [than] or equal': ' <= ',
    '(op (power | exponent) | to the power [of])': ' ** ',
    'op and': ' && ',
    'op or': ' || ',
    '[op] (logical | bitwise) and': ' & ',
    '[op] (logical | bitwise) or': ' | ',
    '(op | logical | bitwise) (ex | exclusive) or': ' ^ ',
    '[(op | logical | bitwise)] (left shift | shift left)': ' << ',
    '[(op | logical | bitwise)] (right shift | shift right)': ' >> ',
    '(op | logical | bitwise) and equals': ' &= ',
    '(op | logical | bitwise) or equals': ' |= ',
    '(op | logical | bitwise) (ex | exclusive) or equals': ' ^= ',
    '[(op | logical | bitwise)] (left shift | shift left) equals': ' <<= ',
    '[(op | logical | bitwise)] (right shift | shift right) equals': ' >>= ',

    'shebang bash': '#!/bin/bash -u\n',

    'new window': Key('cmd-n'),
    'next window': Key('cmd-`'),
    'last window': Key('cmd-shift-`'),
    'next app': Key('cmd-tab'),
    'last app': Key('cmd-shift-tab'),
    'next tab': Key('ctrl-tab'),
    'new tab': Key('cmd-t'),
    'last tab': Key('ctrl-shift-tab'),

    'next space': Key('cmd-alt-ctrl-right'),
    'last space': Key('cmd-alt-ctrl-left'),

    'scroll down': [Key('down')] * 30,
    'scroll up': [Key('up')] * 30,

})

ctx.keymap(keymap)
