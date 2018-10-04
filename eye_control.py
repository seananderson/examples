import eye_mouse
from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('eye_control')
ctx.keymap({
    'toggle debug overlay':   lambda m: eye_mouse.on_menu('Eye Tracking >> Show Debug Overlay'),
    'toggle Tobi':   lambda m: eye_mouse.on_menu('Eye Tracking >> Control Mouse'),
    'toggle camera overlay':  lambda m: eye_mouse.on_menu('Eye Tracking >> Show Camera Overlay'),
    'run calibration': lambda m: eye_mouse.on_menu('Eye Tracking >> Calibrate'),
})
