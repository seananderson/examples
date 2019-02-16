from talon.voice import Context, Key

apps = ("org.rstudio.RStudio", "com.googlecode.iterm2", "org.vim.MacVim", "com.sublimetext.3")
ctx = Context("R", func=lambda app, win: any(t in app.bundle for t in apps))

ctx.keymap({
  'word d-plier':                'dplyr',
  'word tidier':                 'tidyr',
  'word reshape 2':              'reshape2',
  'word G G plot':               'ggplot',

  'score (group | grouped) by':  'group_by(',
  'score inner (join | joint)':  'inner_join(',
  "score left (join | joint)":   'left_join(',
  'score bind (rows | rose)':    'bind_rows(',

  'geom point':                  'geom_point(',
  'geom line':                   'geom_line(',
  'geom point':                  'geom_point(',
  'geom segment':                'geom_segment(',
  'geom histogram':              'geom_histogram(',
  'geom bar':                    'geom_bar(',
  'geom area':                   'geom_area(',
  'geom violin':                 'geom_violin(',
  'geom boxplot':                'geom_boxplot(',
  'geom pointrange':             'geom_pointrange(',
  'geom polygon':                'geom_polygon(',
  'geom (ab|A B) line':          'geom_abline(',
  'geom horizontal line':        'geom_hline(',
  'geom vertical line':          'geom_vline(',
})
