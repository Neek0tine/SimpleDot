from PySimpleGUI import Window, theme
from psgtray import SystemTray
import pystray._win32

theme('HotDogStand')  # Keep things interesting for your users
layout = [[]]
menu = ['', ['Exit']]
tooltip = 'SimpleDot'

window = Window('Window that stays open',
                layout,
                border_depth=0,
                no_titlebar=True,
                keep_on_top=True,
                size=(8, 8),
                resizable=False)
tray = SystemTray(menu, single_click_events=False, window=window, tooltip=tooltip, icon='logo.ico')

while True:
    event, values = window.read()
    if event == tray.key:
        break

window.close()
