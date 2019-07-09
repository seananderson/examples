from talon.voice import Context, Key

ctx = Context('mail', bundle='com.microsoft.Outlook')

keymap =  {
    'new message': Key('cmd-n'),
    'reply that': Key('cmd-r'),
    'forward that': Key('cmd-j'),
    'reply all that': Key('cmd-r'),
    'send that please': Key('cmd-return'),
    # set via Keyboard Shortcuts in System Preferences:
    # https://apple.stackexchange.com/questions/211610/outlook-for-mac-archive-single-email-with-a-keyboard-shortcut
    'archive that': Key('cmd-e'),
    'search contacts': Key('cmd-0'),
    'go to mail': Key('cmd-1'),
    'go to calendar': Key('cmd-2'),
    'go to contacts': Key('cmd-3'),
    'go to search': Key('alt-cmd-f'),
    'go to advanced search': Key('cmd-shift-f'),
    'move that': Key('cmd-shift-m'),
    'refresh': Key('cmd-k'),
}

ctx.keymap(keymap)
