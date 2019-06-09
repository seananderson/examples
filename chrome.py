from talon.voice import Word, Context, Key, Rep, Str, press
ctx = Context('chrome', bundle='com.google.Chrome')

# from .vim import common_to_bash

chromemap = {}

# chromemap.update(common_to_bash)

# chromemap.update({'%d ruff' % k: [Key('J')]*k for k in range(1, 10)})
# chromemap.update({'%d buff' % k: [Key('K')]*k for k in range(1, 10)})


chromemap.update({
    "go to amazon" : [Key("escape escape cmd-l"), "amazon.ca", Key("enter")],
    "go to wikipedia" : [Key("escape escape cmd-l"), "wikipedia.com", Key("enter")],
    "go to github" : [Key("escape escape cmd-l"), "github.com", Key("enter")],
    "go to gmail" : [Key("escape escape cmd-l"), "gmail.com", Key("enter")],
    "go to DFO e-mail" : [Key("escape escape cmd-l"), "https://webmail.dfo-mpo.gc.ca/OWA", Key("enter")],
    "go to google" : [Key("escape escape cmd-l"), "google.com", Key("enter")],
    "go to red it" : [Key("escape escape cmd-l"), "reddit.com", Key("enter")],
    "go to google drive" : [Key("escape escape cmd-l"), "drive.google.com", Key("enter")],
    "go to netflix" : [Key("escape escape cmd-l"), "netflix.com", Key("enter")],
    "go to my github" : [Key("escape escape cmd-l"), "https://github.com/seananderson", Key("enter")],
    })

# chromemap.update({
    # 'mort' : 'd',
    # 'lest' : 'u',
    # 'tab close' : Key('cmd-w'),
    # 'run 1 password' : Key('cmd-\\'),
    # 'goto address': Key('escape escape cmd-l'),
    # 'mortar' : Key('alt-down'),
    # 'lesser' : Key('alt-up'),
    # 'out' : [Key('tab')]*25,
    # 'links': Key('f'),
    # 'new links': Key('F'), # Open link in new tab
    # 'zoom in' : Key('cmd-='),
    # 'zoom out' : Key('cmd+-'),
    # 'pan left' : 'h'*4,
    # 'pan right' : 'l'*4,
    # 'nex' : 'n',
    # 'bex' : 'N',
    # 'tab search' : 'T',
    # 'tab restore' : 'X',
    # 'ruff' : Key("escape J"),
    # 'buff' : Key("escape K"),
    # 'back' : 'H',
    # 'forward' : 'L',
    # 'refresh' : 'cmd-r',
    # 'toggle bookmarks' : Key('cmd-shift-B'),
    # 'show history' : Key('cmd-alt-b'),
   # })

ctx.keymap(chromemap)

