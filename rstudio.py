from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('RStudio', bundle='org.rstudio.RStudio')

ctx.keymap({
  #'expand selection':              Key('shift-alt-cmd-up'),
  #'reduce selection':              Key('shift-alt-cmd-down'),
  # 'duplicate line': Key('alt-cmd-down'),

  'go to matching':                Key('ctrl-p'),

  'pip':                           Key('tab'),

  # Console

  # 'Clear console': Key('ctrl-L'),
  # 'Move cursor to beginning of line': Key('cmd-left'),
  # 'Move cursor to end of line': Key('cmd-right'),
  # 'Popup history': Key('cmd-Up'),
  # 'Change working directory': Key('ctrl-shift-H'),

  # Source

  'go to omni':                   Key('ctrl-.'),

  # 'New document': Key('cmd-shift-N'),
  # 'New document (Chrome only)': Key('cmd-shift-Alt-N'),
  # 'Open document': Key('cmd-O'),
  # 'Save active document': Key('cmd-S'),
  # 'Close active document (except on Chrome)': Key('cmd-W'),
  # 'Close active document (Chrome only)': Key('cmd-alt-W'),
  'close all tabs':               Key('cmd-shift-w'),
  'run knitter':                  Key('cmd-shift-k'),
  'insert knitter chunk':         Key('cmd-alt-i'),
  # 'Insert code section': Key('cmd-shift-R'),

  'run that':                     Key('cmd-enter'),
  # 'run current line/selection (retain cursor position)': Key('alt-enter'),
  'run previous':                 Key('cmd-shift-P'),
  # 'eval current document': Key('cmd-alt-R'),
  'run from top':                 Key('cmd-alt-b'),
  'run to end':                   Key('cmd-alt-e'),
  'run (function|funk)':          Key('cmd-alt-f'),
  # 'eval section':               Key('cmd-alt-t'),
  'run previous chunks':          Key('cmd-alt-p'),
  'run chunk':                    Key('cmd-alt-c'),
  'run next chunk':               Key('cmd-alt-n'),
  # 'Source a file': Key('cmd-shift-O'),
  'run all':                      Key('cmd-shift-S'),
  # 'eval and echo all':         Key('cmd-shift-enter'),

  # 'Fold Selected': Key('cmd-alt-L'),
  # 'Unfold Selected': Key('cmd-shift-alt-L'),
  # 'Fold All': Key('cmd-alt-O'),
  # 'Unfold All': Key('cmd-shift-alt-O'),

  'go to line':                   Key('cmd-shift-alt-g'),
  'go to section':                Key('cmd-shift-alt-j'),

  'go to tab':                    Key('ctrl-shift-.'),
  'go to previous tab':           Key('ctrl-f11'),
  'go to next tab':               Key('ctrl-f12'),
  #'go to first tab':              Key('ctrl-shift-f11'),
  #'go to last tab':               Key('ctrl-shift-f12'),

  'jump back':                    Key('cmd-F9'),
  'jump forward':                 Key('cmd-F10'),

  # 'Extract function from selection': Key('cmd-alt-X'),
  # 'Extract variable from selection': Key('cmd-alt-V'),

  'indent lines':                 Key('cmd-I'),
  'toggle comment':               Key('cmd-shift-C'),
  'reformat comment':             Key('cmd-shift-/'),
  'reformat are code':            Key('cmd-shift-A'),
  # 'Show Diagnostics': Key('cmd-shift-Alt-P'),
  # 'Transpose Letters': Key('ctrl-T'),

  'move up':                      Key('alt-up'),
  'move down':                    Key('alt-down'),
  # 'duplicate line up':        Key('cmd-alt-up'),
  'duplicate line':               Key('cmd-alt-down'),

  'jump to paren':                Key('ctrl-p'),
  'select to paren':              Key('ctrl-shift-E'),
  # 'Select to Matching Paren': Key('ctrl-shift-Alt-E'),

  'add cursor up':                Key('ctrl-alt-up'),
  'add cursor down':              Key('ctrl-alt-down'),

  # 'Move Active Cursor Up': Key('ctrl-Alt-shift-Up'),
  # 'Move Active Cursor Down': Key('ctrl-Alt-shift-Down'),

  'find and replace':             Key('cmd-f'),
  'find next':                    Key('cmd-g'),
  'find previous':                Key('cmd-shift-G'),
  'find with selection':          Key('cmd-e'),
  # 'Replace and Find':         Key('cmd-shift-J'),
  'find in files':                Key('cmd-shift-F'),

  'run spell check':              Key('f7'),

  # Editing (Console and Source)

  # 'Undo': Key('cmd-Z'),
  # 'Redo': Key('cmd-shift-Z'),
  # 'Cut': Key('cmd-X'),
  # 'Copy': Key('cmd-C'),
  # 'Paste': Key('cmd-V'),
  # 'Select All': Key('cmd-A'),
  # 'Jump to Word': Key('alt-left/right'),
  # 'Jump to Start/End': Key('cmd-home/End or cmd-Up/Down'),
  'dosh line':                    Key('cmd-d'),
  # 'Select': Key('shift-[Arrow]'),
  # 'Select Word': Key('alt-shift-left/right'),
  # 'Select to Line Start': Key('cmd-shift-left'),
  # 'Select to Line End': Key('cmd-shift-right'),
  # 'Select Page Up/Down': Key('shift-pageup/Down'),
  # 'Select to Start/End': Key('cmd-shift-Up/Down'),
  'dosh word left':               Key('alt-backspace'),
  'dosh word right':              Key('alt-delete'),
  # 'Delete to Line End': Key('ctrl-K'),
  # 'Delete to Line Start': Key('alt-backspace'),
  # 'Indent': Key('Tab (at beginning of line)'),
  # 'Outdent': Key('shift-Tab'),
  # 'Yank line up to cursor': Key('ctrl-U'),
  # 'Yank line after cursor': Key('ctrl-K'),
  # 'Insert currently yanked text': Key('ctrl-Y'),
  'assign that':                  Key('alt--'),
  'pipe that':                    Key('cmd-shift-M'),
  'help that':                    Key('f1'),
  'define that':                  Key('f2'),
  # 'Find usages for symbol at cursor (C--)': Key('cmd-alt-U'),

  # Views

  'go to source':                 Key('ctrl-1'),
  'go to console':                Key('ctrl-2'),
  'go to help':                   Key('ctrl-3'),
  'go to history':                Key('ctrl-4'),
  'go to files':                  Key('ctrl-5'),
  'go to (plots|plot)':           Key('ctrl-6'),
  'go to packages':               Key('ctrl-7'),
  'go to environment':            Key('ctrl-8'),
  'go to git':                    Key('ctrl-9'),
  'go to build':                  Key('ctrl-0'),
  'go to terminal':                  Key('alt-shift-T'),
  # 'Sync Editor & PDF Preview': Key('cmd-F8'),
  # 'Show Keyboard Shortcut Reference': Key('alt-shift-K'),

  # Build

  'dev tools Build':              Key('cmd-shift-B'),
  'dev tools Load All':           Key('cmd-shift-L'),
  'dev tools Test':               Key('cmd-shift-T'),
  'dev tools Check':              Key('cmd-shift-E'),
  'dev tools Document':           Key('cmd-shift-D'),

  # Debug

  'toggle breakpoint':            Key('shift-f9'),
  'debug Next':                   Key('f10'),
  # 'Step Into Function': Key('shift-f4'),
  'debug finish Function':        Key('shift-f6'),
  'debug Continue':               Key('shift-f5'),
  'debug Stop':                   Key('shift-f8'),

  # Plots

  'go to Previous plot':          Key('cmd-alt-f11'),
  'go to Next plot':              Key('cmd-alt-f12'),

  # Git/SVN

  'run git diff':                 Key('ctrl-alt-d'),
  'run git commit':               Key('ctrl-alt-m'),
  # 'Scroll diff view': Key('ctrl-Up/Down'),
  'run git stage':                Key('space'), # toggles
  # 'Stage/Unstage and move to next (Git)': Key('enter'),

  # Session

  'restart R session':                Key('cmd-shift-f10'),

  # Terminal

  # 'New Terminal': Key('shift-alt-T'),
  # 'Rename Current Terminal': Key('shift-alt-R'),
  # 'Clear Current Terminal': Key('ctrl-shift-L'),
  # 'Move Focus to Terminal': Key('ctrl-shift-T'),
  # 'Previous Terminal': Key('ctrl-alt-F11'),
  # 'Next Terminal': Key('ctrl-alt-F12'),

  'D-plier select':               'select(',
  'D-plier mutate':               'mutate(',
  'D-plier summarize':            'summarize(',
  'D-plier filter':               'filter(',
  'D-plier rename':               'rename(',
  'D-plier group by':             'group_by(',
  'D-plier inner join': 'inner_join(',
  'D-plier left join': 'left_join(',
  'D-plier bind rows': 'bind_rows(',

  'word G G plot':                'ggplot(',
  'G G aesthetic':                'aes(',
  'geom point':                   'geom_point(',
  'geom line':                    'geom_line(',
  'geom point':                   'geom_point(',
  'geom segment':                 'geom_segment(',
  'geom bar':                     'geom_bar(',
  'geom area':                    'geom_area(',
  'geom violin':                  'geom_violin(',
  'geom boxplot':                 'geom_boxplot(',
  'geom pointrange':              'geom_pointrange(',
  'geom polygon':                 'geom_polygon(',
  'geom (ab|A B) line':           'geom_abline(',
  'geom horizontal line':         'geom_hbline(',
  'geom vertical line':           'geom_vbline(',
  'G G ex label':                 'xlab(',
  'G G why label':                'ylab(',

  'R function':                   'function(',
  'R data frame':                 'data.frame(',
  'R is N A':                     'is.na(',

  'nerb (smash|jumble) row': 'nrow',
})
