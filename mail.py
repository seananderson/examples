from talon.voice import Context, Key

ctx = Context('mail', bundle='com.apple.mail')

keymap =  {
    'message send that': Key('cmd-shift-d'),
    'message viewer new': Key('cmd-shift-n'),
    'message new': Key('cmd-n'),
    'message reply': Key('cmd-r'),
    'message reply all': Key('cmd-shift-r'),
    'message forward': Key('cmd-shift-f'),
    'message archive': Key('cmd-ctrl-a'),
    'toggle filter': Key('cmd-l'),
}

ctx.keymap(keymap)
