from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import app, ctrl, clip, ui
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string
import time

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

def join_words(words, sep=' ', cap_first=False):
    out = ''
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation:
            out += sep
        if i == 0 and cap_first:
            out += word.capitalize()
        else:
            out += word
    return out

def parse_words(m):
   return list(map(parse_word, m.dgndictation[0]._words))

def insert(s):
    Str(s)(None)

def text(m):
    insert(join_words(parse_words(m)))

def sentence_text(m):
    insert(join_words(parse_words(m), cap_first=True))

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
    'camel':     (True,  lambda i, word, _: word if i == 0 else word.capitalize()),
    'score':     (True,  lambda i, word, _: word if i == 0 else '_'+word.lower()),
    'smash':     (True,  lambda i, word, _: word.lower()),
    'jumble':    (True,  lambda i, word, _: word.lower()),
    'jive':      (True,  lambda i, word, _: word.lower() if i == 0 else '-'+word.lower()),
    'titlecase': (False, lambda i, word, _: word.capitalize()),
    'uppercase': (False, lambda i, word, _: word.upper()),
    'double-string':    (False, surround('"')),
    'single-string': (False, surround("'")),
    'padded':    (False, surround(" ")),
    'pathify':   (True,  lambda i, word, _: word.lower() if i == 0 else '/'+word.lower()),
    'dotify':    (True,  lambda i, word, _: word.lower() if i == 0 else '.'+word.lower()),

    'thrack':    (True,  lambda i, word, _: word.lower()[0:3]), # first 3 letters of word
    'quattro':   (True,  lambda i, word, _: word.lower()[0:4]), # first 4 ...
    'quintro':   (True,  lambda i, word, _: word.lower()[0:5]), # first 5 ...
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

def copy_bundle(m):
    bundle = ui.active_app().bundle
    clip.set(bundle)
    app.notify('Copied app bundle', body='{}'.format(bundle))

ctx = Context('input')

ctx.keymap({
    'say <dgndictation> [over]': text,
    'cap <dgndictation> [over]': sentence_text,
    'comma <dgndictation> [over]': [', ', text],
    'period <dgndictation> [over]': ['. ', sentence_text],
    # 'more <dgndictation> [over]': [' ', text],
    'word <dgnwords>': word,
    '(%s)+ [<dgndictation>]' % (' | '.join(formatters)): FormatText,

    'kill': Key('delete'),
    '(chuck|delete)': Key('backspace'),

    'slap': Key('enter'),
    'slap that': [Key('cmd-right'), lambda m: time.sleep(0.05), Key('enter')],
    '(escape | scape)': Key('esc'),
    'quest mark': '?',
    'tilde': '~',
    'backtick': '`',
    '(bang | exclamation [mark])': '!',
    'dollar': '$',
    'underscore': '_',
    'colon': ':',
    'paren': '(',
    'R paren': ')',
    'lace': '{',
    'race': '}',
    'langle': '<',
    'rangle': '>',

    'asterisk': '*',
    'hash': '#',
    'percent': '%',
    'caret': '^',
    'at symbol': '@',
    'ampersand': '&',
    'vertical bar': '|',

    'double quote': '"',
    'quote': "'",
    'calm': ',',
    'calmer': ', ',
    '(dot dot dot | dotdotdot)': '...',
    '(dot dot | dotdot)': '..',

    #'extension python': '.py',
    #'extension R': '.R',
    #'extension see plus plus': '.cpp',
    #'extension Stan': '.stan',
    #'extension markdown': '.md',
    #'extension R markdown': '.Rmd',

    'args': ['()', Key('left')],
    # 'index': ['[]', Key('left')],
    #'block': [' {}', Key('left enter enter up tab')],

    'state if': ['if ()', Key('left')],
    'state else if': [' else if ()', Key('left')],
    'state while': ['while ()', Key('left')],
    'state for': ['for ()', Key('left')],
    'state switch': ['switch ()', Key('left')],

    #'state include': '#include ',
    #'state include system': ['#include <>', Key('left')],
    #'state include local': ['#include ""', Key('left')],
    #'state type deaf': 'typedef ',
    #'state type deaf struct': ['typedef struct {\n\n};', Key('up'), '\t'],

    #'comment see': '// ',
    #'comment are': '# ',

    #'word queue': 'queue',
    #'word eye': 'eye',
    #'word iter': 'iter',
    #'word no': 'NULL',

    'word talon': 'talon',
    'word D-plier': 'dplyr',
    'word G G plot 2': 'ggplot2',
    'word reshape 2': 'reshape2',
    'word G L M M': 'GLMM',
    'word G L M': 'GLM',
    'word area': 'area',
    'word axis': 'axis',
    'word paste': 'paste',
    'word to do': 'TODO: ',
    'word ref': 'REF',
    # 'word down': 'down',
    # 'word up': 'up',
    # 'word left': 'left',
    # 'word right': 'right',

    #'dickt in it': ['{}', Key('left')],
    #FIXME redefine# 'list in it': ['[]', Key('left')],
    #FIXME redefine# 'string utf8': "'utf8'",
    #'state past': 'pass',

    'plus': '+',
    'op (equal | equals)': ' = ',
    'equals': '=',
    'op (minus | hyphen)': ' - ',
    'op (plus | add)': ' + ',
    'op (times | asterisk | star)': ' * ',
    'op divide': ' / ',
    #'op comma': ', ',
    #'op mod': ' % ',
    #'[op] (minus | subtract) equals': ' -= ',
    #'[op] (plus | add) equals': ' += ',
    #'[op] (times | multiply) equals': ' *= ',
    #'[op] divide equals': ' /= ',
    #'[op] mod equals': ' %= ',

    '(op | is) tilde': ' ~ ',
    '(op | is) greater than': ' > ',
    '(op | is) less than': ' < ',
    '(op | is) an element of': ' %in% ',
    '(op | is) equal to': ' == ',
    '(op | is) not equal': ' != ',
    '(op | is) greater than or equal': ' >= ',
    '(op | is) less than or equal': ' <= ',
    #'(op (power | exponent) | to the power [of])': ' ** ',
    'op double and': ' && ',
    'op double or': ' || ',
    'op and': ' & ',
    'op or': ' | ',
    #'(op | logical | bitwise) (ex | exclusive) or': ' ^ ',
    #'[(op | logical | bitwise)] (left shift | shift left)': ' << ',
    #'[(op | logical | bitwise)] (right shift | shift right)': ' >> ',
    #'(op | logical | bitwise) and equals': ' &= ',
    #'(op | logical | bitwise) or equals': ' |= ',
    #'(op | logical | bitwise) (ex | exclusive) or equals': ' ^= ',
    #'[(op | logical | bitwise)] (left shift | shift left) equals': ' <<= ',
    #'[(op | logical | bitwise)] (right shift | shift right) equals': ' >>= ',

    #'shebang bash': '#!/bin/bash -u\n',

    'window new': Key('cmd-n'),
    'window next': Key('cmd-`'),
    'window close': Key('cmd-w'),
    'window last': Key('cmd-shift-`'),
    'window hide': Key('cmd-h'),
    'window hide others': Key('cmd-alt-h'),
    #'quit that': Key('cmd-q'),
    #'save that': Key('cmd-s'),
    'app next': Key('cmd-tab'),
    'app last': Key('cmd-shift-tab'),
    'tab next': Key('ctrl-tab'),
    'tab preev': Key('ctrl-shift-tab'),
    'tab new': Key('cmd-t'),

    'scroll down': [Key('down')] * 30,
    'scroll up': [Key('up')] * 30,

    # 'copy that': Key('cmd-c'),
    # 'cut that': Key('cmd-x'),
    # 'paste that': Key('cmd-v'),
    'Alfred paste': Key('cmd-shift-v'),
    'Alfred paste that': [Key('cmd-shift-v'), lambda m: time.sleep(0.1), Key('enter')],
    'Alfred go to': [Key('cmd-space'), lambda m: time.sleep(0.1), Key('space')],
    'Alfred launch': Key('cmd-space'),
    # 'undo that': Key('cmd-z'),
    'redo that': Key('cmd-shift-z'),
    'insert dfo signature': '---=', # keyboard shortcut for my e-mail signature

     # Selecting text
    'select line': Key('cmd-right cmd-shift-left'),
    'select start': Key('cmd-shift-left'),
    'select end': Key('cmd-shift-right'),
    'select word': [Key('alt-left'), Key('alt-shift-right')],
    # 'select right': Key('shift-right'),
    # 'select left': Key('shift-left'),

    # 'jump word [right]': Key('alt-right'),
    # 'jump word left': Key('alt-left'),

    # 'go top': Key('cmd-up'),
    # 'go bottom': Key('cmd-down'),
    # 'go end': Key('cmd-right'),
    # 'go start': Key('cmd-left'),
    'page up': Key('pageup'),
    'page down': Key('pagedown'),

    "mac toggle dock": Key("cmd-alt-d"),

    'copy active bundle': copy_bundle,

     # The following gives you 1 second to hover your mouse over your application
     # of choice; adjust timing as desired or abort early with 'choose app'.
    'switch apps': lambda m: (
        ctrl.key_press('cmd', cmd=True, down=True),
        press('tab'),
        time.sleep(1.0),
        ctrl.key_press('cmd', cmd=True, up=True),
    ),
    '(choose app|release app switcher|release command)': lambda m: (
        ctrl.key_press('cmd', cmd=True, up=True),
    ),
    'hold app switcher': lambda m: (
        ctrl.key_press('cmd', cmd=True, down=True),
        press('tab'),
    ),
    'hold command': lambda m: (
        ctrl.key_press('cmd', cmd=True, down=True),
    ),
    # Multiple cursors via mouse in Sublime Text and RStudio:
    'hold option command': lambda m: (
        ctrl.key_press('cmd', cmd=True, alt=True, down=True),
    ),
    'release option command': lambda m: (
        ctrl.key_press('cmd', cmd=True, alt=True, up=True),
    ),

})
