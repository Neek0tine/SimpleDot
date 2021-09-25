from PySimpleGUI import Window, theme
from psgtray import SystemTray
import pystray._win32

theme('HotDogStand')  # Keep things interesting for your users
layout = [[]]
menu = ['', ['Exit']]
tooltip = 'SimpleDot'

window = Window('Window that stays open',
                layout,
                grab_anywhere=False,
                auto_size_buttons=False,
                border_depth=0,
                return_keyboard_events=False,
                use_default_focus=False,
                no_titlebar=True,
                keep_on_top=True,
                size=(8, 8),
                resizable=False,
                finalize=True)
tray = SystemTray(menu, single_click_events=False, window=window, tooltip=tooltip, icon='logo.ico')

while True:
    event, values = window.read()
    if event == tray.key:
        break

window.close()
