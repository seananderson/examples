# Original draft script posted to Slack by aegis under a BSD 0 license.
# This version contains some modifications such as placing the webview
# in the top left corner and writing a `phrase.log` text file in
# ~/.talon/phrase.log

import os
from atomicwrites import atomic_write

from talon import app, webview, ui
from talon.engine import engine
from talon_init import TALON_HOME

path = os.path.join(TALON_HOME, 'last_phrase')
path_log = os.path.join(TALON_HOME, 'phrase.log')
WEBVIEW = True
NOTIFY = False

if WEBVIEW: 
    webview = webview.Webview()
    webview.move(0, ui.main_screen().height)
    webview.body = '<i>[waiting&nbsp;for&nbsp;phrase]</i>'
    webview.show()
    
def parse_phrase(phrase):
    return ' '.join(word.split('\\')[0] for word in phrase)
    
def on_phrase(j):
    phrase = parse_phrase(j.get('phrase', []))
    cmd = j['cmd']
    if cmd == 'p.end' and phrase:
        with atomic_write(path, overwrite=True) as f:
            f.write(phrase)
        with open(path_log, 'a') as f:
            f.write(phrase + '\n')
            
    if WEBVIEW and cmd in ('p.end', 'p.hypothesis') and phrase:
        body = phrase.replace(' ', '&nbsp;')
        if cmd == 'p.hypothesis':
            webview.render("<i>{{ phrase }}</i>", phrase=body)
        else:
            webview.render("{{ phrase }}", phrase=body)
            
    if NOTIFY and cmd == 'p.end' and phrase:
        app.notify(body=phrase)
        
engine.register('phrase', on_phrase)