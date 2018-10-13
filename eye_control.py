import eye_mouse
from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('eye_control')
ctx.keymap({
    '(toggle|run) Tobi debug':   lambda m: eye_mouse.on_menu('Eye Tracking >> Show Debug Overlay'),
    'Tobi':   lambda m: eye_mouse.on_menu('Eye Tracking >> Control Mouse'),
    '(toggle|run) Tobi overlay':  lambda m: eye_mouse.on_menu('Eye Tracking >> Show Camera Overlay'),
    'run Tobi calibration': lambda m: eye_mouse.on_menu('Eye Tracking >> Calibrate'),
})
