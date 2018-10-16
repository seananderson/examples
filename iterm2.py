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

    'run git': 'git ',
    'run git remove': 'git rm ',
    'run git add': 'git add ',
    'run git bisect': 'git bisect ',
    'run git branch': 'git branch ',
    'run git checkout': 'git checkout ',
    'run git cherry pick': 'git cherry-pick ',
    'run git clone': 'git clone ',
    'run git commit': 'git commit ',
    'run git commit all': 'git commit -av\n',
    'run git commit message': ['git commit -am ""', Key('left')],
    'run git diff': 'git diff ',
    'run git fetch': 'git fetch\n',
    'run git fetch wait': 'git fetch ',
    'run git grep': 'git grep ',
    'run git in it': 'git init ',
    'run git standard log': 'git log\n',
    'run git merge': 'git merge ',
    'run git move': 'git mv ',
    'run git pull': 'git pull\n',
    'run git pull wait': 'git pull ',
    'run git push': 'git push\n',
    'run git push wait': 'git push ',
    'run git rebase': 'git rebase\n',
    'run git rebase wait': 'git rebase ',
    'run git reset': 'git reset ',
    'run git show': 'git show ',
    'run git tag': 'git tag ',
    'run git status': 'git status\n',
    'run git stash': 'git stash',
    'run git commit all': 'git commit -av\n',
    'run git word-diff': 'git diff --color-words\n',
    'run git log': "git lg\n",
    # git lg = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
})
