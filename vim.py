from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('vim', bundle='com.googlecode.iterm2',
        func=lambda app, win: 'vim' in win.title)

def search_forward(m):
    press('/')
    w = str(m.dgndictation[0]._words[0])
    w = w.lower()
    Str(w)(None)
    press('return')


def search_reverse(m):
    press('?')
    w = str(m.dgndictation[0]._words[0])
    w = w.lower()
    Str(w)(None)
    press('enter')

ctx.keymap({

        "(insert | sert)":          "i",
        "big (insert | sert)":      "I",
        "append":                   "a",
        "big append":               "A",

        "dosh line":                [Key('d')] * 2,
        "yank line":                [Key('y')] * 2,
        "go to top":                  [Key("g")] * 2,
        "go to bottom":               Key("esc G"),
        "open":                     Key("esc o"),
        "big open":                 Key("esc O"),
        "paste":                    Key("esc p"),
        "big open":                 Key("esc P"),

        'screen (center|middle)':   Key("esc z ."),
        'screen top':               Key("esc z t"),
        'screen bottom':            Key("esc z b"),

        "split screen":             Key("esc ctrl-w s"),
        "split screen vertically":  Key("esc ctrl-w v"),
        "screen left":              Key("ctrl-h"),
        "screen right":             Key("ctrl-l"),
        "screen up":                Key("ctrl-k"),
        "screen down":              Key("ctrl-j"),

        "comment line":             "gcc",
        "comment para":             "gcap",

        "duplicate line":           "yyp",
        "mort":                     Key("ctrl-d"),
        "lest":                     Key("ctrl-u"),

        "record macro":             "qq",
        "end macro":                "q",

        "format para":              "Q",

        "mark that":                "ma",
        "jump mark":                "`a",
        "copy mark":                "y`a",
        "dosh mark":                "d`a",
        "format mark":              "gq`a",
        "remove mark":              "m -",

        "pip":                      Key("ctrl-n"),
        "pop":                      Key("ctrl-p"),
        "(pop|pip) file":           Key("ctrl-x ctrl-f"),
        "(pop|pip) line":           Key("ctrl-x ctrl-l"),
        "(pop|pip) omni":           Key("ctrl-x ctrl-o"),
        "(pop|pip) arg":            Key("ctrl-x ctrl-a"),
        "(pop|pip) cancel":         Key("ctrl-e"),

        "edit file":                [Key("escape"), ':e '],
        "edit args":                ":args *.",
        "write file":               [Key("escape"), ':update', Key("enter")],
        "write and exit":           ":wq!",
        "close buffer":             ":q\n",
        "delete buffer":            ":bd\n",
        "write all files":          ":wall\n",

        "fuzzy buff":               [Key("escape"), ":Buffers", Key("enter")],
        "fuzzy close":              [Key("ctrl-c")],
#        "fuzzy files": esc + Key("colon,s-F,i,l,e,s,enter"),
#        "fuzzy lines all": esc + Key("colon,s-L,i,n,e,s,enter"),
#        "fuzzy lines": esc + Key("colon,s-B,s-L,i,n,e,s,enter"),
#        "fuzzy tags all": esc + Key("colon,s-T,a,g,s,enter"),
#        "fuzzy tags": esc + Key("colon,s-B,s-T,a,g,s,enter"),
#        "fuzzy git files": esc + Key("colon,s-G,i,t,s-F,i,l,e,s,enter"),
#        "fuzzy (history|recent)": esc + Key("colon,s-H,i,s,t,o,r,y,enter"),
#        "fuzzy commits": esc + Key("colon,s-C,o,m,m,i,t,s,enter"),
#        "fuzzy help": esc + Key("colon,s-H,e,l,p,enter"),
#        "fuzzy grep": esc + Key("colon,s-A,g,enter"),

        "vim theme solarize dark":  ":colo flattened_dark\n",
        "vim theme solarize light": ":colo flattened_light\n",
        "vim theme (soul|Seoul)":   ":colo seoul256\n",
        "vim toggle lights":        ":ToggleBG\n",
        "vim toggle spelling":      ":setlocal spell!\n",
        "vim toggle obsession":     ":Obsession!\n",
        "vim toggle numbers":       ":set relativenumber!\n",

        # R specific stuff
        "pipe that":                " %>% ",
        "assign that":              " <- ",

        "argument that":            ",ra",
        "help that":                ",rh",
        "print that":               ",rp",
        "structure that":           ",rt",
        "name that":                ",rn",

        "eval":                     Key("enter"),
        "eval chunk":                     Key(",cc"),

        # https://github.com/pimentel/talon_user/blob/master/vim.py
        'jump till <dgndictation>': search_forward,
        'jump back till <dgndictation>': search_reverse,

        'go back': 'g;',
})
