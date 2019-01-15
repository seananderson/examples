from talon.voice import Context, Key

ctx = Context('RStudio', bundle='org.rstudio.RStudio')

ctx.keymap({

  # Console

  # 'Clear console':                       Key('ctrl-L'),
  # 'Popup history':                       Key('cmd-Up'),
  # 'Change working directory':            Key('ctrl-shift-H'),

  # 'New document':                        Key('cmd-shift-N'),
  # 'New document (Chrome only)':          Key('cmd-shift-Alt-N'),
  # 'Insert code section':                 Key('cmd-shift-R'),

  'close all tabs':                        Key('cmd-shift-w'),
  'run knitter':                           Key('cmd-shift-k'),
  'insert knitter chunk':                  Key('cmd-alt-i'),

  'run that':                              Key('cmd-enter'),
  'run line and stay':                     Key('alt-enter'),
  'run previous':                          Key('cmd-shift-P'),
  'run document':                          Key('cmd-alt-R'),
  'run from top':                          Key('cmd-alt-b'),
  'run to end':                            Key('cmd-alt-e'),
  'run (function|funk)':                   Key('cmd-alt-f'),
  'run section':                           Key('cmd-alt-t'),
  'run previous chunks':                   Key('cmd-alt-p'),
  'run chunk':                             Key('cmd-alt-c'),
  'run next chunk':                        Key('cmd-alt-n'),
  'run all':                               Key('cmd-shift-S'),
  'run and echo all':                      Key('cmd-shift-enter'),

  # 'Fold Selected':                       Key('cmd-alt-L'),
  # 'Unfold Selected':                     Key('cmd-shift-alt-L'),
  # 'Fold All':                            Key('cmd-alt-O'),
  # 'Unfold All':                          Key('cmd-shift-alt-O'),

  'go to omni':                            Key('ctrl-.'),
  'go to line':                            Key('cmd-shift-alt-g'),
  'go to section':                         Key('cmd-shift-alt-j'),
  'go to tab':                             Key('ctrl-shift-.'),
  'go to previous tab':                    Key('ctrl-f11'),
  'go to next tab':                        Key('ctrl-f12'),
  'go to first tab':                       Key('ctrl-shift-f11'),
  'go to last tab':                        Key('ctrl-shift-f12'),

  'jump back':                             Key('cmd-F9'),
  'jump forward':                          Key('cmd-F10'),

  'extract function from selection':       Key('cmd-alt-X'),
  'extract variable from selection':       Key('cmd-alt-V'),

  'indent lines':                          Key('cmd-I'),
  'toggle comment':                        Key('cmd-shift-C'),
  'reformat comment':                      Key('cmd-shift-/'),
  'reformat are code':                     Key('cmd-shift-A'),
  'show diagnostics':                      Key('cmd-shift-Alt-P'),

  'move up':                               Key('alt-up'),
  'move down':                             Key('alt-down'),
  'duplicate line up':                     Key('cmd-alt-up'),
  'duplicate line (down)':                 Key('cmd-alt-down'),

  'select to paren':                       Key('ctrl-shift-E'),
  'select to matching paren':              Key('ctrl-shift-Alt-E'),
  'jump to matching':                      Key('ctrl-p'),
  'expand selection':                      Key('shift-alt-cmd-up'),
  'reduce selection':                      Key('shift-alt-cmd-down'),

  'add cursor up':                         Key('ctrl-alt-up'),
  'add cursor down':                       Key('ctrl-alt-down'),
  'move active cursor up':                 Key('ctrl-alt-shift-up'),
  'move active cursor down':               Key('ctrl-alt-shift-down'),

  'find and replace':                      Key('cmd-f'),
  'find next':                             Key('cmd-g'),
  'find previous':                         Key('cmd-shift-G'),
  'find with selection':                   Key('cmd-e'),
  'run replace':                           Key('cmd-shift-J'),
  'find in files':                         Key('cmd-shift-F'),

  'run spell check':                       Key('f7'),

  # Editing (Console and Source)

  'delete line':                           Key('cmd-d'),
  'delete word left':                      Key('alt-backspace'),
  'delete word right':                     Key('alt-delete'),
  'assign that':                           Key('alt--'),
  'pipe that':                             Key('cmd-shift-M'),
  'help that':                             Key('f1'),
  'define that':                           Key('f2'),

  # 'Delete to Line End':                  Key('ctrl-K'),
  # 'Delete to Line Start':                Key('alt-backspace'),
  # 'Yank line up to cursor':              Key('ctrl-U'),
  # 'Yank line after cursor':              Key('ctrl-K'),
  # 'Insert currently yanked text':        Key('ctrl-Y'),

  # Views

  'go to source':                          Key('ctrl-1'),
  'go to console':                         Key('ctrl-2'),
  'go to help':                            Key('ctrl-3'),
  'go to history':                         Key('ctrl-4'),
  'go to files':                           Key('ctrl-5'),
  'go to (plots|plot)':                    Key('ctrl-6'),
  'go to packages':                        Key('ctrl-7'),
  'go to environment':                     Key('ctrl-8'),
  'go to git':                             Key('ctrl-9'),
  'go to build':                           Key('ctrl-0'),
  'go to terminal':                        Key('alt-shift-T'),
  # 'sync editor & PDF preview':           Key('cmd-F8'),
  'show keyboard shortcuts':               Key('alt-shift-K'),

  # Build

  'dev tools Build':                       Key('cmd-shift-B'),
  'dev tools Load All':                    Key('cmd-shift-L'),
  'dev tools Test':                        Key('cmd-shift-T'),
  'dev tools Check':                       Key('cmd-shift-E'),
  'dev tools Document':                    Key('cmd-shift-D'),

  # Debug

  'toggle breakpoint':                     Key('shift-f9'),
  'debug next':                            Key('f10'),
  'debug step into function':              Key('shift-f4'),
  'debug finish function':                 Key('shift-f6'),
  'debug continue':                        Key('shift-f5'),
  'debug stop':                            Key('shift-f8'),

  # Plots

  'previous plot':                         Key('cmd-alt-f11'),
  'next plot':                             Key('cmd-alt-f12'),

  # Git/SVN

  'run git diff':                          Key('ctrl-alt-d'),
  'run git commit':                        Key('ctrl-alt-m'),
  # 'scroll diff view':                    Key('ctrl-Up/Down'),
  'run git stage':                         Key('space'), # toggles
  'stage/unstage and next (Git)':          Key('enter'),

  # Session

  'restart R session':                     Key('cmd-shift-f10'),

  # Terminal

  # 'New Terminal':                        Key('shift-alt-T'),
  # 'Rename Current Terminal':             Key('shift-alt-R'),
  # 'Clear Current Terminal':              Key('ctrl-shift-L'),
  # 'Move Focus to Terminal':              Key('ctrl-shift-T'),
  # 'Previous Terminal':                   Key('ctrl-alt-F11'),
  # 'Next Terminal':                       Key('ctrl-alt-F12'),

  'd-plier select':                        'select(',
  'd-plier mutate':                        'mutate(',
  'd-plier summarize':                     'summarize(',
  'd-plier filter':                        'filter(',
  'd-plier rename':                        'rename(',
  'd-plier group by':                      'group_by(',
  'd-plier inner join':                    'inner_join(',
  'd-plier left join':                     'left_join(',
  'd-plier bind rows':                     'bind_rows(',

  'word G G plot':                         'ggplot',
  'geom point':                            'geom_point(',
  'geom line':                             'geom_line(',
  'geom point':                            'geom_point(',
  'geom segment':                          'geom_segment(',
  'geom histogram':                        'geom_histogram(',
  'geom bar':                              'geom_bar(',
  'geom area':                             'geom_area(',
  'geom violin':                           'geom_violin(',
  'geom boxplot':                          'geom_boxplot(',
  'geom pointrange':                       'geom_pointrange(',
  'geom polygon':                          'geom_polygon(',
  'geom (ab|A B) line':                    'geom_abline(',
  'geom horizontal line':                  'geom_hbline(',
  'geom vertical line':                    'geom_vbline(',
  'G G aesthetic':                         'aes(',
  'G G ex label':                          'xlab(',
  'G G why label':                         'ylab(',
})
