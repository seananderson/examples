from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('RStudio', bundle='org.rstudio.RStudio')

ctx.keymap({
  "expand select":            Key("shift-alt-cmd-up"),
  "reduce select":            Key("shift-alt-cmd-down"),
  # "duplicate line": Key("alt-cmd-down"),

  "jump matching":            Key("ctrl-p"),

  "pip":                      Key("tab"),

  # Console

  'Move cursor to Console':   Key('ctrl-2'),
  # 'Clear console': Key('ctrl-L'),
  # 'Move cursor to beginning of line': Key('cmd-left'),
  # 'Move cursor to end of line': Key('cmd-right'),
  # 'Popup history': Key('cmd-Up'),
  # 'Change working directory': Key('ctrl-shift-H'),

  # Source

  'go to omni':               Key('ctrl-.'),

  'go to source':             Key('ctrl-1'),
  # 'New document': Key('cmd-shift-N'),
  # 'New document (Chrome only)': Key('cmd-shift-Alt-N'),
  # 'Open document': Key('cmd-O'),
  # 'Save active document': Key('cmd-S'),
  # 'Close active document (except on Chrome)': Key('cmd-W'),
  # 'Close active document (Chrome only)': Key('cmd-alt-W'),
  'Close all tabs':           Key('cmd-shift-W'),
  'run knitter':              Key('cmd-shift-K'),
  'Insert chunk':             Key('cmd-alt-I'),
  # 'Insert code section': Key('cmd-shift-R'),

  'Rip':                      Key('cmd-enter'),
  # 'Run current line/selection (retain cursor position)': Key('alt-enter'),
  'Run previous':             Key('cmd-shift-P'),
  # 'Run current document': Key('cmd-alt-R'),
  'Run from top':             Key('cmd-alt-B'),
  'Run to end':               Key('cmd-alt-E'),
  'Run function':             Key('cmd-alt-F'),
  'Run section':              Key('cmd-alt-T'),
  'Run previous chunks':      Key('cmd-alt-P'),
  'Run chunk':                Key('cmd-alt-C'),
  'Run next chunk':           Key('cmd-alt-N'),
  # 'Source a file': Key('cmd-shift-O'),
  'Run all ':                 Key('cmd-shift-S'),
  # 'Run and echo all':         Key('cmd-shift-enter'),

  # 'Fold Selected': Key('cmd-alt-L'),
  # 'Unfold Selected': Key('cmd-shift-alt-L'),
  # 'Fold All': Key('cmd-alt-O'),
  # 'Unfold All': Key('cmd-shift-alt-O'),

  'go to line':               Key('cmd-shift-alt-G'),
  'go to section':            Key('cmd-shift-alt-J'),

  'go to tab':                Key('ctrl-shift-.'),
  'Previous tab':             Key('ctrl-F11'),
  'Next tab':                 Key('ctrl-F12'),
  'First tab':                Key('ctrl-shift-F11'),
  'Last tab':                 Key('ctrl-shift-F12'),

  '(jump | go) back':         Key('cmd-F9'),
  '(jump | go) forward':      Key('cmd-F10'),

  # 'Extract function from selection': Key('cmd-alt-X'),
  # 'Extract variable from selection': Key('cmd-alt-V'),

  'indent lines':             Key('cmd-I'),
  'toggle comment':           Key('cmd-shift-C'),
  'Reflow Comment':           Key('cmd-shift-/'),
  'Reformat that':            Key('cmd-shift-A'),
  # 'Show Diagnostics': Key('cmd-shift-Alt-P'),
  # 'Transpose Letters': Key('ctrl-T'),

  'Move Up':                  Key('alt-Up'),
  'Move Down':                Key('alt-Down'),
  # 'Copy Up':                  Key('cmd-alt-Up'),
  'duplicate line':           Key('cmd-alt-Down'),

  'Jump to Matching Paren':   Key('ctrl-P'),
  'select to Matching Paren': Key('ctrl-shift-E'),
  # 'Select to Matching Paren': Key('ctrl-shift-Alt-E'),

  'Add Cursor up':            Key('ctrl-Alt-Up'),
  'Add Cursor down':          Key('ctrl-Alt-Down'),

  # 'Move Active Cursor Up': Key('ctrl-Alt-shift-Up'),
  # 'Move Active Cursor Down': Key('ctrl-Alt-shift-Down'),

  'Find and Replace':         Key('cmd-F'),
  'Find Next':                Key('cmd-G'),
  'Find Previous':            Key('cmd-shift-G'),
  'Use Selection for Find':   Key('cmd-E'),
  'Replace and Find':         Key('cmd-shift-J'),
  'Find in Files':            Key('cmd-shift-F'),

  'Check Spelling':           Key('F7'),

  # Editing (Console and Source)

  # 'Undo': Key('cmd-Z'),
  # 'Redo': Key('cmd-shift-Z'),
  # 'Cut': Key('cmd-X'),
  # 'Copy': Key('cmd-C'),
  # 'Paste': Key('cmd-V'),
  # 'Select All': Key('cmd-A'),
  # 'Jump to Word': Key('alt-left/right'),
  # 'Jump to Start/End': Key('cmd-home/End or cmd-Up/Down'),
  'dosh Line':                Key('cmd-D'),
  # 'Select': Key('shift-[Arrow]'),
  # 'Select Word': Key('alt-shift-left/right'),
  # 'Select to Line Start': Key('cmd-shift-left'),
  # 'Select to Line End': Key('cmd-shift-right'),
  # 'Select Page Up/Down': Key('shift-pageup/Down'),
  # 'Select to Start/End': Key('cmd-shift-Up/Down'),
  'dosh Word left':           Key('alt-backspace'),
  'dosh Word right':          Key('alt-delete'),
  # 'Delete to Line End': Key('ctrl-K'),
  # 'Delete to Line Start': Key('alt-backspace'),
  # 'Indent': Key('Tab (at beginning of line)'),
  # 'Outdent': Key('shift-Tab'),
  # 'Yank line up to cursor': Key('ctrl-U'),
  # 'Yank line after cursor': Key('ctrl-K'),
  # 'Insert currently yanked text': Key('ctrl-Y'),
  'assign that':              Key('alt--'),
  'pipe that':                Key('cmd-shift-M'),
  "help that":                Key("F1"),
  "define that":              Key("F2"),
  # 'Find usages for symbol at cursor (C--)': Key('cmd-alt-U'),

  # Views

  'go to Source':             Key('ctrl-1'),
  'go to Console':            Key('ctrl-2'),
  'go to Help':               Key('ctrl-3'),
  'go to History':            Key('ctrl-4'),
  'go to Files':              Key('ctrl-5'),
  'go to Plots':              Key('ctrl-6'),
  'go to Packages':           Key('ctrl-7'),
  'go to Environment':        Key('ctrl-8'),
  'go to Git':                Key('ctrl-9'),
  'go to Build':              Key('ctrl-0'),
  # 'Sync Editor & PDF Preview': Key('cmd-F8'),
  # 'Show Keyboard Shortcut Reference': Key('alt-shift-K'),

  # Build

  'devtools Build':           Key('cmd-shift-B'),
  'devtools Load All':        Key('cmd-shift-L'),
  'devtools Test':            Key('cmd-shift-T'),
  'devtools Check':           Key('cmd-shift-E'),
  'devtools Document':        Key('cmd-shift-D'),

  # Debug

  'toggle breakpoint':        Key('shift-F9'),
  'debug Next':               Key('F10'),
  # 'Step Into Function': Key('shift-F4'),
  'debug finish Function':    Key('shift-F6'),
  'debug Continue':           Key('shift-F5'),
  'debug Stop':               Key('shift-F8'),

  # Plots

  'Previous plot':            Key('cmd-alt-F11'),
  'Next plot':                Key('cmd-alt-F12'),

  # Git/SVN

  'Git Diff':                 Key('ctrl-alt-D'),
  'Git Commit':               Key('ctrl-alt-M'),
  # 'Scroll diff view': Key('ctrl-Up/Down'),
  'Git Stage':                Key('space'), # toggles
  # 'Stage/Unstage and move to next (Git)': Key('enter'),

  # Session

  'Restart R':                Key('cmd-shift-F10'),

  # Terminal

  # 'New Terminal': Key('shift-alt-T'),
  # 'Rename Current Terminal': Key('shift-alt-R'),
  # 'Clear Current Terminal': Key('ctrl-shift-L'),
  # 'Move Focus to Terminal': Key('ctrl-shift-T'),
  # 'Previous Terminal': Key('ctrl-alt-F11'),
  # 'Next Terminal': Key('ctrl-alt-F12'),

  'dee-ply-er select':        'select(',
  'dee-ply-er mutate':        'mutate(',
  'dee-ply-er summarize':     'summarize(',
  'dee-ply-er filter':        'filter(',
  'dee-ply-er rename':        'rename(',
  'dee-ply-er group by':      'group_by(',

  'G G plot 2':               'ggplot2',
  'G G plot funk':            'ggplot(',
  'G G aesthetic':            'aes(',
  'geom point':               'geom_point(',
  'geom line':                'geom_line(',
  'geom point':               'geom_point(',
  'geom segment':             'geom_segment(',
  'geom bar':                 'geom_bar(',
  'geom area':                'geom_area(',
  'geom violin':              'geom_violin(',
  'geom boxplot':             'geom_boxplot(',
  'geom pointrange':          'geom_pointrange(',
  'geom polygon':             'geom_polygon(',
  'geom ab line':             'geom_abline(',
  'geom H line':              'geom_hbline(',
  'geom V line':              'geom_vbline(',
  'G G X lab':                'xlab(',
  'G G y lab':                'ylab(',

})
