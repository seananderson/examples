# originally from https://github.com/tabrat/talon_user/blob/master/spectacle.py
from talon.voice import Key, Context

# Move and resize windows with Spectacle.app

ctx = Context('spectacle')

keymap = {
    'window center':         Key('cmd-alt-c'),
    'window max':            Key('cmd-alt-f'),

    'window left':           Key('cmd-alt-left'),
    'window right':          Key('cmd-alt-right'),
    'window top':            Key('cmd-alt-top'),
    'window bottom':         Key('cmd-alt-bottom'),

    'window upper left':     Key('cmd-ctrl-left'),
    'window lower left':     Key('cmd-ctrl-shift-left'),
    'window upper right':    Key('cmd-ctrl-right'),
    'window lower right':    Key('cmd-ctrl-shift-right'),

    # 'window next display':     Key('cmd-ctrl-alt-right'),
    # 'window previous display': Key('cmd-ctrl-alt-left'),

    'window next third':     Key('ctrl-alt-right'),
    'window previous third': Key('ctrl-alt-left'),

    'window larger':         Key('shift-ctrl-alt-right'),
    'window smaller':        Key('shift-ctrl-alt-left'),

    'window undo':           Key('cmd-alt-z'),
    'window redo':           Key('cmd-alt-shift-z'),
}

ctx.keymap(keymap)
