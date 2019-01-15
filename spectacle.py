# originally from https://github.com/tabrat/talon_user/blob/master/spectacle.py
from talon.voice import Key, Context

# Move and resize windows with Spectacle.app

ctx = Context('spectacle')

keymap = {
    'snap center':           Key('shift-cmd-alt-C'), # Note this is not the default shortcut
    'snap full screen':      Key('shift-cmd-alt-f'), # not default; conflicts with RStudio
  
    'snap left':             Key('cmd-alt-left'),
    'snap right':            Key('cmd-alt-right'),
    'snap top':              Key('cmd-alt-top'),
    'snap bottom':           Key('cmd-alt-bottom'),
  
    'snap top left':         Key('cmd-ctrl-left'),
    'snap bottom left':      Key('cmd-ctrl-shift-left'),
    'snap top right':        Key('cmd-ctrl-right'),
    'snap bottom right':     Key('cmd-ctrl-shift-right'),

    'snap next display':     Key('cmd-ctrl-alt-right'),
    'snap previous display': Key('cmd-ctrl-alt-left'),

    'snap next third':       Key('ctrl-alt-right'),
    'snap previous third':   Key('ctrl-alt-left'),
  
    'snap larger':           Key('shift-ctrl-alt-right'),
    'snap smaller':          Key('shift-ctrl-alt-left'),
  
    'snap undo':             Key('cmd-alt-z'),
    'snap redo':             Key('cmd-alt-shift-z'),
}

ctx.keymap(keymap)
