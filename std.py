from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import app, ctrl, clip, ui
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string
import time

from .utils import parse_word, surround, text, sentence_text, word, parse_words, spoken_text, select_last_insert, insert

punctuation = set('.,-!?')

def CursorText(s):
  left, right = s.split('{.}', 1)
  return [left + right, Key(' '.join(['left'] * len(right)))]

formatters = {
    'camel':     (True,  lambda i, word, _: word if i == 0 else word.capitalize()),
    'score':     (True,  lambda i, word, _: word if i == 0 else '_'+word.lower()),
    'smash':     (True,  lambda i, word, _: word.lower()),
    'jumble':    (True,  lambda i, word, _: word.lower()),
    'jive':      (True,  lambda i, word, _: word.lower() if i == 0 else '-'+word.lower()),
    'titlecase': (False, lambda i, word, _: word.capitalize()),
    'uppercase': (False, lambda i, word, _: word.upper()),
    'quote': (False, surround('"')),
    # 'single-quote': (False, surround("'")),
    'padded':    (False,     surround(" ")),
    'dotify':    (True,  lambda i, word, _: word.lower() if i == 0 else '.'+word.lower()),
    'thrack':    (True,  lambda i, word, _: word.lower()[0:3]), # first 3 letters of word
    'quattro':   (True,  lambda i, word, _: word.lower()[0:4]), # first 4 ...
    'acronym':   (True,  lambda i, word, _: word[0:1].upper()),
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
    insert(sep.join(words))

def copy_bundle(m):
    bundle = ui.active_app().bundle
    clip.set(bundle)
    app.notify('Copied app bundle', body='{}'.format(bundle))

ctx = Context('input')

ctx.keymap({
    'say <dgndictation> [over]': text,
    'cap <dgndictation> [over]': sentence_text,
    # 'say <dgndictation> [over]': [text, ' '],
    # 'cap <dgndictation> [over]': [sentence_text, ' '],
    'calmer <dgndictation> [over]': [', ', text],
    # 'period <dgndictation> [over]': ['. ', sentence_text],
    'and say <dgndictation> [over]': [' ', text],
    'and cap <dgndictation> [over]': [' ', sentence_text],
    'word <dgnwords>': word,
    '(%s)+ [<dgndictation>]' % (' | '.join(formatters)): FormatText,

    'select last': select_last_insert,

    "cut that": Key("cmd-x"),
    "copy that": Key("cmd-c"),
    "paste that": Key("cmd-v"),
    "undo that": Key("cmd-z"),
    "redo that": Key("cmd-shift-z"),

    'kill': Key('delete'),
    'chuck': Key('backspace'),

    'slap': Key('enter'),
    'slap that': [Key('cmd-right'), lambda m: time.sleep(0.05), Key('enter')],
    '(escape | scape | cape)': Key('esc'),
    'quest mark': '?',
    'tilde': '~',
    'backtick': '`',
    '(bang | exclamation mark)': '!',
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
    'bar': '|',

    'quote [double]': '"',
    'apostrophe': "'",
    'quote single': "'",
    # 'calm': ',',
    'calmer': ', ',
    '(dot dot dot | dotdotdot)': '...',
    '(dot dot | dotdot)': '..',

    'args': ['()', Key('left')],

    'state if': ['if ()', Key('left')],
    'state else if': [' else if ()', Key('left')],
    'state while': ['while ()', Key('left')],
    'state for': ['for ()', Key('left')],
    'state switch': ['switch ()', Key('left')],

    'word to do': 'TODO: ',
    'word fix me': 'FIXME: ',
    'word ref': 'REF',

    'word talon': 'talon',
    'word G L M M': 'GLMM',
    'word deeplier': 'dplyr',
    'word G L M': 'GLM',

    'cap filina': 'Philina',
    'word filina': 'Philina',
    'word sacha': 'Sacha',

    'plus': '+',
    'op (equal | equals)': ' = ',
    'equals': '=',
    'op (minus | hyphen)': ' - ',
    'op (plus | add)': ' + ',
    'op (times | asterisk | star)': ' * ',
    'op (divide | slash)': ' / ',
    'op comma': ', ',
    #'op mod': ' % ',
    'op (minus | subtract) equals': ' -= ',
    'op (plus | add) equals': ' += ',
    'op (times | multiply) equals': ' *= ',
    'op divide equals': ' /= ',
    'op mod equals': ' %= ',

    '(op | is) tilde': ' ~ ',
    '(op | is) greater than': ' > ',
    '(op | is) less than': ' < ',
    '(op | is) an element of': ' %in% ',
    '(op | is) equal [to]': ' == ',
    '(op | is) not equal [to]': ' != ',
    '(op | is) greater than or equal [to]': ' >= ',
    '(op | is) less than or equal [to]': ' <= ',
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
    'tab last': Key('ctrl-shift-tab'),
    'tab new': Key('cmd-t'),

    'scroll down': [Key('down')] * 30,
    'scroll up': [Key('up')] * 30,

    'Alfred paste': Key('cmd-shift-v'),
    'Alfred paste that': [Key('cmd-shift-v'), lambda m: time.sleep(0.1), Key('enter')],
    'Alfred go to': [Key('cmd-space'), lambda m: time.sleep(0.1), Key('space')],
    'Alfred launch': Key('cmd-space'),
    # 'undo that': Key('cmd-z'),
    'redo that': Key('cmd-shift-z'),
    'save that': Key('cmd-s'),
    'insert dfo signature': '---=', # keyboard shortcut for my e-mail signature

     # Selecting text
    'select line': Key('cmd-right cmd-shift-left'),
    'select start': Key('cmd-shift-left'),
    'select end': Key('cmd-shift-right'),
    'select word': [Key('alt-left'), Key('alt-shift-right')],

    'delete line': [Key('cmd-right cmd-shift-left'), Key('delete')],
    'delete start': [Key('cmd-shift-left'), Key('delete')],
    'delete end': [Key('cmd-shift-right'), Key('delete')],
    'delete word': [Key('alt-left'), Key('alt-shift-right'), Key('delete')],

    # 'jump word [right]': Key('alt-right'),
    # 'jump word left': Key('alt-left'),

    # 'go top': Key('cmd-up'),
    # 'go bottom': Key('cmd-down'),
    # 'go end': Key('cmd-right'),
    # 'go start': Key('cmd-left'),
    'page up': Key('pageup'),
    'page down': Key('pagedown'),

    "mac toggle dock": Key("cmd-alt-d"),
    "cap (jenny|chani)": "Chani",
    "cap for lena": "Philina",
    "cap elise": "Elise",
    "cap sasha": "Sacha",
    "cap robin": "Robyn",

    "reference figure": ["Figure \@ref(fig:)", Key("left")],
    "reference table": ["Table \@ref(tab:)", Key("left")],
    "reference equation": ["Equation \@ref(eq:)", Key("left")],
    "reference section": ["Section \@ref(sec:)", Key("left")],
    "reference appendix": ["Appendix \@ref(app:)", Key("left")],

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
