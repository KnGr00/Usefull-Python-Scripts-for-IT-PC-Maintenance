from pyautogui import hotkey
from time import sleep
helplist = ['\\t', '\\n', '\\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']

cont1, cont2 = -1, -1

def stroke():
    global splitted_starter
    starter = input("Please type key combination you want to simulate in format of CTRL,V or CTRL V. \nYou can use /help to show keynames : ")

    if starter == "/help":
        for i in range(0, len(helplist), 10):
            print(helplist[i:i + 10])
        return -1
    else:
        splitted_starter = starter.split(",")

    for i in splitted_starter:
        if i not in helplist:
            print(str(i), " is not available. Please select keystroke from known keys")
            sleep(2)
            exit()
    return print("You have selected", splitted_starter, "as keystroke combination")




def sim():
    trigger = input("Please type key combination you want to trigger the keystroke. \nYou can use /help to show keynames : ")

    if trigger == "/help":
        for i in range(0, len(helplist), 10):
            print(helplist[i:i+10])
        return -1
    else:
        splitted_trigger = trigger.split(",")

    for i in splitted_trigger:
        if i not in helplist:
            print(str(i), " is not available. Please select keystroke from known keys")
            sleep(2)
            exit()
    return print("You have selected", splitted_trigger, "as keystroke trigger combination")


while cont1 == -1:
    cont1 = stroke()
while cont2 == -1:
    cont2 = sim()

