from talon.voice import Word, Context, Key, Rep, Str, press
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER

ctx = Context("terminal", bundle="com.googlecode.iterm2")

ctx.keymap(
    {
        "cd": "cd ",
        "cd talon user": "cd {}".format(TALON_USER),
        # 'cd talon home': 'cd {}'.format(TALON_HOME),
        # 'cd talon plugins': 'cd {}'.format(TALON_PLUGINS),
        "cd source": "cd ~/src/",
        "cd home": "cd ~/",
        "run make": "make\n",
        "run make directory": "mkdir ",

        "run get": "git ",
        "run get remove": "git rm ",
        "run get status": "git status\n",
        "run get add": "git add ",
        "run get bisect": "git bisect ",
        "run get branch": "git branch ",
        "run get checkout": "git checkout ",
        "run get cherry pick": "git cherry-pick ",
        "run get clone": "git clone ",
        "run get commit": "git commit ",
        "run get commit message": ['git commit -m ""', Key("left")],
        "run get diff": "git diff/n",
        "run get fetch": "git fetch\n",
        "run get grep": "git grep ",
        "run get in it": "git init\n",
        "run get log": "git lg\n",
        "run get merge": "git merge ",
        "run get move": "git mv ",
        "run get pull [rebase]": "git pull --rebase\n",
        "run get pull merge": "git pull\n",
        "run get push": "git push\n",
        "run get rebase": "git rebase\n",
        "run get reset": "git reset ",
        "run get show": "git show ",
        "run get tag": "git tag ",
        "run get stash": "git stash ",
        "run get commit all": "git commit -av\n",
        "run get word-diff": "git diff --color-words\n",
    }
)
