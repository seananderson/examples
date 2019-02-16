# Original draft script posted to Slack by aegis under a BSD 0 license.
# This version contains some modifications such as placing the webview
# in the top left corner, writing a log text file in
# ~/.talon/phrase_log.csv and not printing or logging input to 1Password.

import os
import re
from atomicwrites import atomic_write
from datetime import datetime

from talon import app, webview, ui
from talon.engine import engine
from talon_init import TALON_HOME

path = os.path.join(TALON_HOME, 'last_phrase')
path_log = os.path.join(TALON_HOME, 'phrase_log.csv')
WEBVIEW = True
NOTIFY = False

# if WEBVIEW:
#     webview = webview.Webview()
#     webview.move(0, ui.main_screen().height)
#     webview.body = '<i>[waiting&nbsp;for&nbsp;phrase]</i>'
#     webview.show()

def parse_phrase(phrase):
    return ' '.join(word.split('\\')[0] for word in phrase)

def on_phrase(j):
    phrase = parse_phrase(j.get('phrase', []))
    cmd = j['cmd']
    app = ui.active_app().bundle
    private = bool(re.search('onepassword', app))
    if cmd == 'p.end' and phrase and not private:
        with atomic_write(path, overwrite=True) as f:
            f.write(phrase)
        with open(path_log, 'a') as f:
            f.write(phrase + ', ' + str(datetime.now()) + ', ' + app + '\n')

    #if WEBVIEW and cmd in ('p.end', 'p.hypothesis') and phrase and not private:
    #    body = phrase.replace(' ', '&nbsp;')
    #    if cmd == 'p.hypothesis':
    #        webview.render("<i>{{ phrase }}</i>", phrase=body)
    #    else:
    #        webview.render("{{ phrase }}", phrase=body)
    #
    if NOTIFY and cmd == 'p.end' and phrase:
        app.notify(body=phrase)

engine.register('phrase', on_phrase)
