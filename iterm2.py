from talon.voice import Word, Context, Key, Rep, Str, press
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER

ctx = Context('terminal', bundle='com.googlecode.iterm2')

ctx.keymap({
    'cd': 'cd ',
    'cd talon user': 'cd {}'.format(TALON_USER),
    # 'cd talon home': 'cd {}'.format(TALON_HOME),
    # 'cd talon plugins': 'cd {}'.format(TALON_PLUGINS),
    'cd source': 'cd ~/src/',
    'cd home': 'cd ~/',

    'run (them | vim)': 'nvim ',
    'run (L S | ellis)': 'ls\n',
    'run make': 'make\n',
    'run make (durr | dear)': 'mkdir ',

    'run (git|get)': 'git ',
    'run (git|get) remove': 'git rm ',
    'run (git|get) add': 'git add ',
    'run (git|get) bisect': 'git bisect ',
    'run (git|get) branch': 'git branch ',
    'run (git|get) checkout': 'git checkout ',
    'run (git|get) clone': 'git clone ',
    'run (git|get) commit': 'git commit ',
    'run (git|get) commit all': 'git commit -av\n',
    'run (git|get) commit message': ['git commit -am ""', Key('left')],
    'run (git|get) diff': 'git diff ',
    'run (git|get) fetch': 'git fetch\n',
    'run (git|get) fetch wait': 'git fetch ',
    'run (git|get) grep': 'git grep ',
    'run (git|get) in it': 'git init ',
    'run (git|get) standard log': 'git log\n',
    'run (git|get) merge': 'git merge ',
    'run (git|get) move': 'git mv ',
    'run (git|get) pull': 'git pull\n',
    'run (git|get) pull wait': 'git pull ',
    'run (git|get) push': 'git push\n',
    'run (git|get) push wait': 'git push ',
    'run (git|get) rebase': 'git rebase\n',
    'run (git|get) rebase wait': 'git rebase ',
    'run (git|get) reset': 'git reset ',
    'run (git|get) show': 'git show ',
    'run (git|get) tag': 'git tag ',
    'run (git|get) status': 'git status\n',
    'run (git|get) stash': 'git stash',
    'run (git|get) commit all': 'git commit -av\n',
    'run (git|get) word-diff': 'git diff --color-words\n',
    'run (git|get) log': "git lg\n",
    # git lg = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
})
