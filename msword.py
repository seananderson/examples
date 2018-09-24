from talon.voice import Context, Key

ctx = Context('msword', bundle='com.microsoft.Word')

ctx.keymap({
    "new comment": Key("cmd-alt-a"),
    "toggle track changes": Key("cmd-shift-E"),
})
