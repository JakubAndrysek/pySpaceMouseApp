import pySpaceMouseApp
import pySpaceMouse
import pyautogui
import time

config = pySpaceMouseApp.Config(
    {
        "Opera": pySpaceMouse.Config(
            button_callback_arr=[
                pySpaceMouse.ButtonCallback(4, lambda state, buttons: pyautogui.hotkey('ctrl', '1')),  # Messenger
                pySpaceMouse.ButtonCallback(9, lambda state, buttons: pyautogui.hotkey('ctrl', 'shift', 'tab')), # Reopen tab
                pySpaceMouse.ButtonCallback(10, lambda state, buttons: pyautogui.hotkey('ctrl', 'tab')),  # Next tab
                pySpaceMouse.ButtonCallback(11, lambda state, buttons: pyautogui.hotkey('ctrl', 't')),  # New tab
                pySpaceMouse.ButtonCallback(12, lambda state, buttons: pyautogui.hotkey('ctrl', 'shift', 't')), # Previous tab
                pySpaceMouse.ButtonCallback(13, lambda state, buttons: pyautogui.hotkey('ctrl', 'w')),  # Close tab

                pySpaceMouse.ButtonCallback(3, lambda state, buttons: pyautogui.hotkey('alt', 'left')),  # Close tab
                pySpaceMouse.ButtonCallback(2, lambda state, buttons: pyautogui.hotkey('alt', 'right')),  # Close tab

                pySpaceMouse.ButtonCallback(5, lambda state, buttons: pyautogui.hotkey('ctrl', '[')),  # Workspace 1
                pySpaceMouse.ButtonCallback(6, lambda state, buttons: pyautogui.hotkey('ctrl', ']')),  # Workspace 2
                pySpaceMouse.ButtonCallback(7, lambda state, buttons: pyautogui.hotkey('ctrl', ';')),  # Workspace 3
                pySpaceMouse.ButtonCallback(8, lambda state, buttons: pyautogui.hotkey('ctrl', "'")),  # Workspace 4
                pySpaceMouse.ButtonCallback(14, lambda state, buttons: pyautogui.hotkey('pause')),  # Pause music
                pySpaceMouse.ButtonCallback(0, lambda state, buttons: pyautogui.scroll(1)),  # Test
            ]
        ),

        "Chrome": pySpaceMouse.Config(
            button_callback=lambda state, buttons: print(state, buttons)
        ),

        "Inkscape": pySpaceMouse.Config(
        )
    }
)

if __name__ == '__main__':
    app = pySpaceMouseApp.App(config)

    while True:
        app.run()
        time.sleep(0.001)
