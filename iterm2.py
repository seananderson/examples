from talon.voice import Word, Context, Key, Rep, Str, press
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER

ctx = Context('vim', bundle='com.googlecode.iterm2')

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
    'run git': 'git ',
    'run git remove': 'git rm ',
    'run git add': 'git add ',
    # 'run git bisect': 'git bisect ',
    'run git branch': 'git branch ',
    'run git checkout': 'git checkout ',
    'run git clone': 'git clone ',
    'run git commit': 'git commit ',
    'run git diff': 'git diff ',
    'run git fetch': 'git fetch ',
    'run git grep': 'git grep ',
    'run git in it': 'git init ',
    'run git log': 'git log ',
    'run git merge': 'git merge ',
    'run git move': 'git mv ',
    'run git pull': 'git pull ',
    'run git push': 'git push ',
    'run git rebase': 'git rebase ',
    'run git reset': 'git reset ',
    'run git show': 'git show ',
    # 'run git tag': 'git tag ',
    'run git status': 'git status\n',
    'run git commit all': 'git commit -av\n',
    'run git word-diff': 'git diff --color-words\n',
    'run git pretty log': "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative\n",
})
