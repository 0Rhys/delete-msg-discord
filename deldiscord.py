from time import sleep
from keyboard import press_and_release
from pyautogui import hotkey


n = 0
a = int(input('How many messages do you want to delete :'))

sleep(5)

while n < a:
    press_and_release('up arrow')
    hotkey('ctrl', 'a')
    sleep(0.1)
    press_and_release('backspace')
    press_and_release('enter')
    press_and_release('enter')
    n += 1