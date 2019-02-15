from talon.voice import Word, Context, Key, Rep, Str, press

apps = ("com.googlecode.iterm2", "org.vim.MacVim")
ctx = Context("vim", func=lambda app, win: any(t in app.bundle for t in apps))

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

        # "(insert | sert)":          "i",
        # "big (insert | sert)":      "I",
        # "append":                   "a",
        # "big append":               "A",

        # "dosh line":                [Key('d')] * 2,
        # "yank line":                [Key('y')] * 2,
        # "go to top":                  [Key("g")] * 2,
        # "go to bottom":               Key("esc G"),
        "open":                     Key("esc o"),
        "big open":                 Key("esc O"),
        # "paste":                    Key("esc p"),
        # "big open":                 Key("esc P"),

        # 'screen (center|middle)':   Key("esc z ."),
        # 'screen top':               Key("esc z t"),
        # 'screen bottom':            Key("esc z b"),

        "split screen":             Key("esc ctrl-w s"),
        "split screen vertically":  Key("esc ctrl-w v"),
        "screen left":              Key("ctrl-h"),
        "screen right":             Key("ctrl-l"),
        "screen up":                Key("ctrl-k"),
        "screen down":              Key("ctrl-j"),
        "screen close":             Key("esc ctrl-w c"),
        "close other splits":       [Key("escape"), ':only', Key('enter')],

        # 'buff-switch': Key(':')

        "comment line":             "gcc",
        "comment para":             "gcap",

        "duplicate line":           "yyp",
        "mort":                     Key("ctrl-d"),
        "lest":                     Key("ctrl-u"),

        'join': Key('esc shift-J'),

        "record macro":             "esc qq",
        "end macro":                "esc q",

        "format para":              "esc Q",

        "mark that":                "esc ma",
        "jump mark":                "esc `a",
        "copy mark":                "esc y`a",
        "dosh mark":                "esc d`a",
        "format mark":              "esc gq`a",
        "remove mark":              "esc m -",

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
        "write and exit":           "esc :wq!",
        
        "buff quit":                "esc :q\n",
        'buff delete':              "esc :bd\n",
        'buff next':                "esc :bn\n",
        'buff preeve':              "esc :bp\n",
        'buff list':                "esc :ls\n",
        "write all files":          "esc :wall\n",

        "fugitive status": "esc Gstatus\n",
        "fugitive push": "esc Gpush\n",
        "fugitive pull": "esc Gpull\n",
        "fugitive diff": "esc Gdiff\n",
        "fugitive commit": "esc Gcommit\n i",
        "fugitive (add|write)": "esc Gwrite\n",
        # "fugitive blame": esc + Key("colon,s-G,b,l,a,m,e,enter"),
        # "fugitive remove": esc + Key("colon,s-G,r,e,m,o,v,e,enter"),
        # "fugitive grep": esc + Key("colon,s-G,g,r,e,p,space"),
        "fugitive browse": "esc Gbrowse\n",
        # "fugitive move": esc + Key("colon,s-G,m,o,v,e,space"),
        "fugitive log": "esc Glog\n",
        # "fugitive commit all": esc + Key("colon,s-G,i,t,space,c,o,m,m,i,t,space,hyphen,a,v,enter"),

        "fuzzy buf":               [Key("escape"), ":Buffers", Key("enter")],
        # "fuzzy files": esc + Key("colon,s-F,i,l,e,s,enter"),
        # "fuzzy lines all": esc + Key("colon,s-L,i,n,e,s,enter"),
        # "fuzzy lines": esc + Key("colon,s-B,s-L,i,n,e,s,enter"),
        # "fuzzy tags all": esc + Key("colon,s-T,a,g,s,enter"),
        # "fuzzy tags": esc + Key("colon,s-B,s-T,a,g,s,enter"),
        # "fuzzy git files": esc + Key("colon,s-G,i,t,s-F,i,l,e,s,enter"),
        # "fuzzy (history|recent)": esc + Key("colon,s-H,i,s,t,o,r,y,enter"),
        # "fuzzy commits": esc + Key("colon,s-C,o,m,m,i,t,s,enter"),
        # "fuzzy help": esc + Key("colon,s-H,e,l,p,enter"),
        # "fuzzy grep": esc + Key("colon,s-A,g,enter"),

        "vim theme solarize dark":  "esc :colo flattened_dark\n",
        "vim theme solarize light": "esc :colo flattened_light\n",
        "vim theme (soul|Seoul)":   "esc :colo seoul256\n",
        "vim toggle lights":        "esc :ToggleBG\n",
        "vim toggle spelling":      "esc :setlocal spell!\n",
        "vim toggle obsession":     "esc :Obsession!\n",
        "vim toggle numbers":       "esc :set relativenumber!\n",

        # R specific stuff
        "pipe that":                " %>% ",
        "assign that":              " <- ",

        "argument that":            "esc ,ra",
        "help that":                "esc ,rh",
        "print that":               "esc ,rp",
        "structure that":           "esc ,rt",
        "name that":                "esc ,rn",

        "eval":                     Key("esc enter"),
        "eval chunk":               Key("esc ,cc"),

        # https://github.com/pimentel/talon_user/blob/master/vim.py
        'jump till <dgndictation>': search_forward,
        'jump back till <dgndictation>': search_reverse,

        'go back': 'esc g;',
})
