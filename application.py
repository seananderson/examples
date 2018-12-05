# # https://github.com/lexjacobs/talon_user/blob/master/application.py
# from talon.voice import Context, ui
# 
# ctx = Context('application_launcher')
# 
# # will launch if not already open
# def open_application(application):
# 
#     def open_or_switch(m):
#         ui.launch(bundle=application)
#     return open_or_switch
# 
# # get bundle: osascript -e 'id of app "app-name"'
# keymap = {
#      # 'chrome app': open_application('com.google.Chrome'),
#      # 'mac mail': open_application('com.apple.Mail'),
#      'termite': open_application('com.googlecode.iterm2'),
# }
# 
# ctx.keymap(keymap)
