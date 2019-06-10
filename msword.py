from talon.voice import Context, Key

ctx = Context('msword', bundle='com.microsoft.Word')

ctx.keymap({
    "new comment": Key("cmd-alt-a"),
    "toggle track changes": Key("cmd-shift-E"),

    # Move to the previous insertion point: Shift + F5
    # Look up selected text on the Internet: COMMAND + Shift + L
    # Move one paragraph up COMMAND + Up arrow

# Move one paragraph down COMMAND + Down arrow

# Move to the top of the next page COMMAND + Page Down

# Move to the top of the previous page COMMAND + Page Up

# To the end of a document COMMAND + End
# To the beginning of a document COMMAND + Home

# Paste special COMMAND + Control + V

# Paste and match the formatting of the surrounding text COMMAND + Option + Shift + V

# Apply the Normal style COMMAND + Shift + N

# Apply the Heading 1 style COMMAND + Option + 1

# Apply the Heading 2 style COMMAND + Option + 2

# Apply the Heading 3 style COMMAND + Option + 3

# Apply subscript formatting (automatic spacing) COMMAND + Equal sign

# Apply superscript formatting (automatic spacing) COMMAND + Shift + Plus sign

# Insert a line break Shift + Return

# Insert a page break COMMAND + Enter
# Insert a footnote COMMAND + Option + F

# Choose the Go To command (Edit menu) Option +  COMMAND + G

# Open the Spelling and Grammar dialog box Option +  COMMAND + L

# Extend a selection F8
# Shrink a selection Shift+ F8
# Open the Thesaurus pane Shift+ F7


# Control+H for Find and Replace

# Cut the selection to the Spike COMMAND + F3
# Paste Spike COMMAND +shift  F3
})
