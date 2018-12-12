# https://raw.githubusercontent.com/dwiel/talon_community/master/apps/finder.py
from talon.voice import Key, Context, Str, press


def go_to_path(path):
    def path_function(m):
        press("cmd-shift-g")
        Str(path)(None)
        press("return")

    return path_function


ctx = Context("Finder", bundle="com.apple.finder")
ctx.keymap(
    {
        "go to desktop": Key("cmd-shift-d"),
        "go to recent": Key("cmd-shift-f"),
        "go to [over]": Key("cmd-shift-g"),
        "go to home": Key("cmd-shift-h"),
        "go to icloud": Key("cmd-shift-i"),
        "go to documents": Key("cmd-shift-o"),
        "go to air drop": Key("cmd-shift-r"),
        "go to utilities": Key("cmd-shift-u"),
        "go to downloads": Key("cmd-alt-l"), # TODO fixed
        "go to applications": Key("cmd-shift-a"),
        "go to source": go_to_path("~/src/"),
        "go to talon": go_to_path("~/.talon/user"),
        "go to dropbox": go_to_path("~/Dropbox/"),
        "go to DFO": go_to_path("~/Dropbox/dfo/"),
        "go to G F synopsis": go_to_path("~/src/gfsynopsis/"),
        "go to G F plot": go_to_path("~/src/gfplot/"),
    }
)
