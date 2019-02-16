# originally from https://github.com/JonathanNickerson/talon_voice_user_scripts
# and https://github.com/pimentel/talon_user/blob/master/repeat.py

from talon.voice import Context, Rep, RepPhrase, talon
from user.utils import m_to_number, numerals

ctx = Context('repeater')

def repeat(m):
    repeat_count = m_to_number(m)

    if repeat_count != None and repeat_count >= 2:
        repeater = Rep(repeat_count - 1)
        repeater.ctx = talon
        return repeater(None)


ctx.keymap({
    'twice': Rep(1),
    'thrice': Rep(2),
    "(rep|repeat)" + numerals: repeat,
    })
